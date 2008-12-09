
%define realname   POE-Component-Client-Keepalive
%define version    0.24
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
Epoch:      1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Manage connections, with keep-alive
Source:     http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(POE)
BuildRequires: perl(POE::Component::Client::DNS)

BuildArch: noarch

%description
POE::Component::Client::Keepalive creates and manages connections for
other components. It maintains a cache of kept-alive connections for
quick reuse. It is written specifically for clients that can benefit
from kept-alive connections, such as HTTP clients. Using it for one-shot
connections would probably be silly.


%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*



