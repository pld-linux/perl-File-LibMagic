#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	LibMagic
Summary:	File::LibMagic - Perlwrapper for libmagic
#Summary(pl.UTF-8):	
Name:		perl-File-LibMagic
Version:	0.84
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FI/FITZNER/File-LibMagic-0.84.tgz
# Source0-md5:	39aa7fd522e41475b6291dd8bc4e2c9a
URL:		http://search.cpan.org/dist/File-LibMagic/
BuildRequires:	libmagic-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File::LibMagic is a simple perl interface to libmagic from
the file-4.x package from Christos Zoulas (ftp://ftp.astron.com/pub/file/).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/File/*.pm
%dir %{perl_vendorarch}/auto/File/LibMagic
%attr(755,root,root) %{perl_vendorarch}/auto/File/LibMagic/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/File/LibMagic/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
