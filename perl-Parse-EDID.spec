#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parse-EDID
Version  : 1.0.7
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/G/GR/GROUSSE/Parse-EDID-1.0.7.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GROUSSE/Parse-EDID-1.0.7.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libparse-edid-perl/libparse-edid-perl_1.0.6-2.debian.tar.xz
Summary  : 'Extended display identification data (EDID) parser'
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-Parse-EDID-license = %{version}-%{release}
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

%description dev
dev components for the perl-Parse-EDID package.


%package license
Summary: license components for the perl-Parse-EDID package.
Group: Default

%description license
license components for the perl-Parse-EDID package.


%prep
%setup -q -n Parse-EDID-1.0.7
cd ..
%setup -q -T -D -n Parse-EDID-1.0.7 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Parse-EDID-1.0.7/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Parse-EDID
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Parse-EDID/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1Parse/EDID.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parse::EDID.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Parse-EDID/LICENSE
