Summary: 	Tyrex
Name:		tyrex
Version:	0.9.7.0
Release:	1
License:	BSD-like license - see LICENSE file for more details
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	ftp://ftp.exolab.org/pub/%{name}/%{name}-%{version}/%{name}-%{version}.tgz
URL:		http://www.exolab.org
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Tyrex

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	tyrex documentation

%description doc
tyrex documentation

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp jts.jar %{name}-%{version}.jar $RPM_BUILD_ROOT/%{_javalibdir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT/%{_javalibdir}/%{name}.jar

gzip -9nf CHANGELOG LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
