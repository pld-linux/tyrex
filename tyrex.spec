Summary:	Tyrex - Java Transaction Service implementation
Summary(pl.UTF-8):	Tyrex - implementacja Java Transation Service
Name:		tyrex
Version:	1.0.3
Release:	1
License:	BSD-like (see LICENSE)
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/tyrex/%{name}-%{version}.tgz
# Source0-md5:	f1c9b178bd1840094a6ba80310bfbcdd
URL:		http://tyrex.sourceforge.net/
Requires:	jre >= 1.3
BuildArch:	noarch
# same as java-sun
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tyrex is an Open Source implementation of the Java Transaction Service
specification defined by Sun Microsystems, Inc.

%description -l pl.UTF-8
Tyrex jest implementacją Open Source specyfikacji Java Transaction
Service zdefiniowanej przez Sun Microsystems, Inc.

%package doc
Summary:	Tyrex documentation
Summary(pl.UTF-8):	Dokumentacja Tyreksa
Group:		Development/Languages/Java

%description doc
Tyrex documentation.

%description doc -l pl.UTF-8
Dokumentacja Tyreksa.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install ots-jts_1.0.jar %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf ots-jts_1.0.jar $RPM_BUILD_ROOT%{_javadir}/jts.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
