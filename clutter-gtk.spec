Summary:	Library integrating clutter with GTK+
Name:		clutter-gtk
Version:	1.6.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://download.gnome.org/sources/clutter-gtk/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	08e5d7c249733d4d96bbbd2dc970a06c
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel >= 1.20.0
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with GTK+.

%package devel
Summary:	Header files for clutter-gtk library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for clutter-gtk library.

%package apidocs
Summary:	clutter-gtk API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter-gtk API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-introspection	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %ghost %{_libdir}/libclutter-gtk-1.0.so.?
%attr(755,root,root) %{_libdir}/libclutter-gtk-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gtk-1.0.so
%{_includedir}/clutter-gtk-1.0
%{_pkgconfigdir}/clutter-gtk-1.0.pc
%{_datadir}/gir-1.0/GtkClutter-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-1.0

