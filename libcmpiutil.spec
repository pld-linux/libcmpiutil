#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	CMPI toolkit library for writing providers
Summary(pl.UTF-8):	Biblioteka narzędziowa CMPI do pisania dostarczycieli
Name:		libcmpiutil
Version:	0.5.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://libvirt.org/libvirt-cim/%{name}-%{version}.tar.bz2
# Source0-md5:	c5813eb39f5e3157048b8b6c9904d237
URL:		http://libvirt.org/
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRequires:	sblim-cmpi-devel >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# symbols defined by referer (libcmpiutil library circularly)
%define		skip_post_check_so	libcueoparser\.so.*

%description
Libcmpiutil is a library of utility functions for CMPI providers. The
goal is to reduce the amount of repetitive work done in most CMPI
providers by encapsulating common procedures with more "normal" APIs.
This extends from operations like getting typed instance properties
to standardizing method dispatch and argument checking.

%description -l pl.UTF-8
Libcmpiutil to biblioteka funkcji narzędziowych dla dostarczycieli
CMPI. Jej celem jest zmniejszenie ilości pracy powtarzanej przy
większości dostarczycieli CMPI poprzez obudowanie wspólnych procedur w
bardziej "normalne" API. Obejmuje to operacje od pobierania
właściwości zadanych typów do standaryzacji wywoływania metod i
sprawdzania argumentów.

%package devel
Summary:	Header files for libcmpiutil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcmpiutil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2-devel >= 2
Requires:	sblim-cmpi-devel >= 2

%description devel
Header files for libcmpiutil library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcmpiutil.

%package static
Summary:	Static libcmpiutil library
Summary(pl.UTF-8):	Statyczna biblioteka libcmpiutil
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcmpiutil library.

%description static -l pl.UTF-8
Statyczna biblioteka libcmpiutil.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libcmpiutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmpiutil.so.0
%attr(755,root,root) %{_libdir}/libcueoparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcueoparser.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpiutil.so
%attr(755,root,root) %{_libdir}/libcueoparser.so
%{_libdir}/libcmpiutil.la
%{_libdir}/libcueoparser.la
%{_includedir}/libcmpiutil
%{_pkgconfigdir}/libcmpiutil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcmpiutil.a
%{_libdir}/libcueoparser.a
