Summary:	Tyrex - Java Transaction Service implementation
Summary(pl):	Tyrex - implementacja Java Transation Service
Name:		tyrex
Version:	0.9.7.0
Release:	1
License:	BSD-like (see LICENSE)
Group:		Development/Languages/Java
Source0:	ftp://ftp.exolab.org/pub/%{name}/%{name}-%{version}/%{name}-%{version}.tgz
URL:		http://www.exolab.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Tyrex is an Open Source implementation of the Java Transaction Service
specification defined by Sun Microsystems, Inc.

%description -l pl
Tyrex jest implementacj± Open Source specyfikacji Java Transaction
Service zdefiniowanej przez Sun Microsystems, Inc.

%package doc
Summary:	Tyrex documentation
Summary(pl):	Dokumentacja Tyreksa
Group:		Development/Languages/Java

%description doc
Tyrex documentation.

%description doc -l pl
Dokumentacja Tyreksa.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install jts.jar %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}.jar

gzip -9nf CHANGELOG LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
