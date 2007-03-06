Summary:	The Typesafe Signal Framework for C++ - Mingw32 cross version
Summary(pl.UTF-8):	Środowisko sygnałów z kontrolą typów dla C++ - wersja skrośna dla Mingw32
%define		_realname	libsigc++
Name:		crossmingw32-%{_realname}
Version:	2.0.17
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libsigc++/2.0/%{_realname}-%{version}.tar.bz2
# Source0-md5:	fde0ee69e3125e982746d9fe005763e1
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9
BuildRequires:	crossmingw32-gcc-c++
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	perl-base
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_pkgconfigdir		%{_libdir}/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

This package contains cross Mingw32 version.

%description -l pl.UTF-8
Ta biblioteka jest implementacją pełnego systemu callbacków do
używania w bibliotekach widgetów, interfejsach abstrakcyjnych i
ogólnym programowaniu. Oryginalnie była to część zestawu widgetów
Gtk--, ale jest teraz oddzielną biblioteką ogólniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z możliwością
łączenia abstrakcyjnych callbacków z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapterów do łączenia różnych
callbacków.

Ten pakiet zawiera wersję skrośną Mingw32.

%package static
Summary:	Static libsigc++ library (cross mingw32 version)
Summary(pl.UTF-8):	Statyczna biblioteka libsigc++ (wersja skrośna mingw32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libsigc++ library (cross mingw32 version).

%description static -l pl.UTF-8
Statyczna biblioteka libsigc++ (wersja skrośna mingw32).

%package dll
Summary:	DLL libsigc++ library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libsigc++ dla Windows
Group:		Applications/Emulators
Requires:	wine

%description dll
DLL libsigc++ library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL libsigc++ dla Windows.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--target=%{target} \
	--host=%{target} \
	--enable-shared \
	--enable-static

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libsigc-2.0.dll.a
%{_libdir}/libsigc-2.0.la
%{_libdir}/sigc++-2.0
%{_includedir}/sigc++-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsigc-2.0.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libsigc-2.0-*.dll
