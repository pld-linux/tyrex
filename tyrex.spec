Summary:	Tyrex - Java Transaction Service implementation
Summary(pl):	Tyrex - implementacja Java Transation Service
Name:		tyrex
Version:	1.0
Release:	1
License:	BSD-like (see LICENSE)
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	cd999a03a78e70a5a8ef380f1917ce93
URL:		http://tyrex.sourceforge.net/
Requires:	jre >= 1.3
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
install ots-jts_%{version}.jar %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}.jar
ln -sf ots-jts_%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/jts.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
