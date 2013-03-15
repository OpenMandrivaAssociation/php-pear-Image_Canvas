%define _class          Image
%define _subclass       Canvas
%define upstream_name       %{_class}_%{_subclass}

Name:           php-pear-%{upstream_name}
Version:        0.3.1
Release:        9
Summary:        Common interface to image drawing
License:        PHP License
Group:          Development/PHP
URL:            http://pear.php.net/package/Image_Canvas/
Source0:        http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-gd
Requires:       php-pear-Image_Color >= 1.0.0
Requires:       php-pear
BuildArch:      noarch
BuildRequires:  php-pear

%description
A package providing a common interface to image drawing,
making image source code independent on the library used.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-8mdv2012.0
+ Revision: 742018
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-7
+ Revision: 679370
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-6mdv2011.0
+ Revision: 613690
- the mass rebuild of 2010.1 packages

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-5mdv2010.1
+ Revision: 473541
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-4mdv2010.0
+ Revision: 441195
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-3mdv2009.1
+ Revision: 322136
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-2mdv2009.0
+ Revision: 236895
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2008.0
+ Revision: 54563
- 0.3.1


* Mon Oct 16 2006 David Walluck <walluck@mandriva.org> 0.3.0-2mdv2006.0
+ Revision: 65352
+ Status: not released
- $2

* Sun Oct 15 2006 David Walluck <walluck@mandriva.org> 0.3.0-1mdv2007.1
+ Revision: 64942
- Import php-pear-Image_Canvas

* Sat Sep 23 2006 David Walluck <walluck@mandriva.org> 0.3.0-1mdv2007.1
- release

