#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parse-EDID
Version  : 1.0.7
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/G/GR/GROUSSE/Parse-EDID-1.0.7.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GROUSSE/Parse-EDID-1.0.7.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libparse-edid-perl/libparse-edid-perl_1.0.6-2.debian.tar.xz
Summary  : 'Extended display identification data (EDID) parser'
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-Parse-EDID-license = %{version}-%{release}
Requires: perl-Parse-EDID-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Warn)

%description
Parse::EDID
===========
DESCRIPTION
-----------
This module provides some function to parse Extended Display Identification
Data binary data structures.

%package dev
Summary: dev components for the perl-Parse-EDID package.
Group: Development
Provides: perl-Parse-EDID-devel = %{version}-%{release}
Requires: perl-Parse-EDID = %{version}-%{release}

%description dev
dev components for the perl-Parse-EDID package.


%package license
Summary: license components for the perl-Parse-EDID package.
Group: Default

%description license
license components for the perl-Parse-EDID package.


%package perl
Summary: perl components for the perl-Parse-EDID package.
Group: Default
Requires: perl-Parse-EDID = %{version}-%{release}

%description perl
perl components for the perl-Parse-EDID package.


%prep
%setup -q -n Parse-EDID-1.0.7
cd %{_builddir}
tar xf %{_sourcedir}/libparse-edid-perl_1.0.6-2.debian.tar.xz
cd %{_builddir}/Parse-EDID-1.0.7
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Parse-EDID-1.0.7/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Parse-EDID
cp %{_builddir}/Parse-EDID-1.0.7/LICENSE %{buildroot}/usr/share/package-licenses/perl-Parse-EDID/d37922f09c009bd59d32ebe0d11c632b24213731
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parse::EDID.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Parse-EDID/d37922f09c009bd59d32ebe0d11c632b24213731

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
