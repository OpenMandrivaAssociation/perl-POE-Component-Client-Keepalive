%define upstream_name    POE-Component-Client-Keepalive
Name:		perl-%{upstream_name}
Version:	0.272
Release:	2
Epoch:		1

Summary:	Manage connections, with keep-alive
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rcaputo/poe-component-client-keepalive
Source0:	https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-Keepalive-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Net::IP)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Component::Client::DNS)
BuildRequires:	perl(POE::Component::Resolver)
BuildArch:	noarch

%description
POE::Component::Client::Keepalive creates and manages connections for
other components. It maintains a cache of kept-alive connections for
quick reuse. It is written specifically for clients that can benefit
from kept-alive connections, such as HTTP clients. Using it for one-shot
connections would probably be silly.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun May 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.266.0-1mdv2011.0
+ Revision: 661391
- new version

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1:0.263.0-2
+ Revision: 658541
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.263.0-1mdv2011.0
+ Revision: 552482
- update to 0.263

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.262.0-1mdv2010.1
+ Revision: 461345
- update to 0.262

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.260.0-1mdv2010.0
+ Revision: 410722
- adding missing buildrequires:
- update to 0.260

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.250.0-1mdv2010.0
+ Revision: 401614
- rebuild using %0.272 fixed license field

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.25-1mdv2009.1
+ Revision: 314257
- update to new version 0.25

* Tue Dec 09 2008 Jérôme Quelin <jquelin@mandriva.org> 1:0.24-1mdv2009.1
+ Revision: 312167
- update to 0.24

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1001-2mdv2009.0
+ Revision: 268701
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1001-1mdv2009.0
+ Revision: 193923
- update to new version 0.1001

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.1000-4mdv2008.1
+ Revision: 168505
- rebuild
- fix summary

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.1000-3mdv2008.1
+ Revision: 152238
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.1000-2mdv2008.1
+ Revision: 152237
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 14 2007 Jérôme Quelin <jquelin@mandriva.org> 0.1000-1mdv2008.1
+ Revision: 108701
- import perl-POE-Component-Client-Keepalive


