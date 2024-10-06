Summary:	Qt API to store passwords and other secret data securely
Summary(pl.UTF-8):	API Qt do bezpiecznego przechowywania haseł i innych tajnych danych
Name:		Qt5Keychain
Version:	0.14.3
Release:	1
License:	Modified BSD License
Group:		Libraries
#Source0Download: https://github.com/frankosterfeld/qtkeychain/releases
Source0:	https://github.com/frankosterfeld/qtkeychain/archive/%{version}/qtkeychain-%{version}.tar.gz
# Source0-md5:	269fe04b6d9d3a22841695a25f1d70e6
URL:		https://github.com/frankosterfeld/qtkeychain
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	cmake >= 3.16
BuildRequires:	libsecret-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-linguist >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.605
Obsoletes:	QtKeychain-common < 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtKeychain a Qt API to store passwords and other secret data securely.

How the data is stored depends on the platform:
- Mac OS X: Passwords are stored in the OS X Keychain.
- Linux/Unix: If running, GNOME Keyring is used, otherwise qtkeychain
  tries to use KWallet (via D-Bus), if available.
- Windows: Windows does not provide a service for secure storage.
  QtKeychain uses the Windows API function

%description -l pl.UTF-8
API Qt do bezpiecznego przechowywania haseł i innych tajnych danych.

Sposób przechowywania danych zależy od platformy:
- Mac OS X: hasła są przechowywanie poprzez usługę OS X Keychain
- Linux/Unix: używany jest GNOME Keyring jeśli jest uruchomiony,
  w przeciwnym wypadku używany jest KWallet (przez DBus), o ile jest
  dostępny
- Windows: system nie udostępnia usługi do bezpiecznego przechowywania
  danych; QtKeychain używa funkcji Windows API

%package devel
Summary:	Development files for Qt5Keychain
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Qt5Keychain
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= 5

%description devel
This package contains the header files for developing applications
that use Qt5Keychain.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę Qt5Keychain.

%prep
%setup -q -n qtkeychain-%{version}

%build
%cmake -B build-qt5 \
	-DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules
%{__make} -C build-qt5

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang qtkeychain --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f qtkeychain.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog ReadMe.md
%attr(755,root,root) %{_libdir}/libqt5keychain.so.*.*.*
%ghost %{_libdir}/libqt5keychain.so.1
%dir %{_datadir}/qt5keychain
%dir %{_datadir}/qt5keychain/translations

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqt5keychain.so
%{_includedir}/qt5keychain
%{_libdir}/cmake/Qt5Keychain
%{_libdir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri
