%define upstream_name    POE-Component-Client-Keepalive
%define upstream_version 0.271

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Manage connections, with keep-alive

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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



