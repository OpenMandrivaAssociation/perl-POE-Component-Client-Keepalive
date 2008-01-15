
%define realname   POE-Component-Client-Keepalive
%define version    0.1000
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    a wheel wrapper around a
Source:     http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(POE)
BuildRequires: perl(POE::Component::Client::DNS)

BuildArch: noarch

%description
POE::Component::Connection::Keepalive is a helper class for
POE::Component::Client::Keepalive.  It wraps managed sockets,
providing a few extra features.

Connection objects free their underlying sockets when they are
DESTROYed.  This eliminates the need to explicitly free sockets when
you are done with them.

Connection objects manage POE::Wheel::ReadWrite objects internally,
saving a bit of effort.



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



