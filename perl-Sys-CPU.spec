Name:           perl-Sys-CPU
Version:        0.51
Release:        7%{?dist}
Summary:        Getting CPU information

Group:          Development/Libraries
License:        (GPL+ or Artistic) and (LGPLv3 or Artistic 2.0)
URL:            http://search.cpan.org/~mkoderer/Sys-CPU/CPU.pm
Source0:        http://search.cpan.org/CPAN/authors/id/M/MK/MKODERER/Sys-CPU-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(IO::Handle)

BuildRequires:  perl(ExtUtils::MakeMaker)

# For test suite
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(IO::Handle)

%{?perl_default_filter}

%description
Perl extension for getting CPU information. 
Currently only number of CPU's supported.

%prep
%setup -q -n Sys-CPU-%{version}


%{__sed} -i 's/\r//' README
%{__sed} -i 's/\r//' Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test TEST_VERBOSE=1

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'


find %{buildroot} -type f -name CPU.bs -exec rm -f {} ';'


%{_fixperms} %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys/*
%{_mandir}/man3/*.3*


%changelog
* Tue Oct 05 2011 Shakthi Kannan <shakthimaan@fedoraproject.org> - 0.51-7
- Used perl_vendorarch/auto, perl_vendorarch/Sys in files section.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.51-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.51-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jun 27 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.51-3
- Rebuild for perl-5.12.1.

* Mon May 03 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> 0.51-2
- Updated license to (GPL+ or Artistic) and (LGPLv3 or Artistic 2.0)

* Fri Apr 23 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> 0.51-1
- Initial Fedora RPM version
