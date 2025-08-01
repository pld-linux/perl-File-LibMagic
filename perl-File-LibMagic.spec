#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	File
%define	pnam	LibMagic
#
Summary:	File::LibMagic - Perlwrapper for libmagic
Summary(pl.UTF-8):	File::Libmagic - Moduł języka Perl opakowujący bibliotekę libmagic
Name:		perl-File-LibMagic
Version:	1.23
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7782e6f80a67c931a2682145eca6e832
URL:		http://search.cpan.org/dist/File-LibMagic/
BuildRequires:	libmagic-devel
BuildRequires:	perl-Config-AutoConf
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File::LibMagic is a simple perl interface to libmagic library.

%description -l pl.UTF-8
Moduł języka Perl File::LibMagic jest prostym interfejsem do
biblioteki libmagic.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__sed} -i 's/ -lz//' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/File/*.pm
%dir %{perl_vendorarch}/File/LibMagic
%{perl_vendorarch}/File/LibMagic/Constants.pm
%dir %{perl_vendorarch}/auto/File/LibMagic
%attr(755,root,root) %{perl_vendorarch}/auto/File/LibMagic/*.so
%{_mandir}/man3/*
