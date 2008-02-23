#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	LibMagic
#
Summary:	File::LibMagic - Perlwrapper for libmagic
Summary(pl.UTF-8):	File::Libmagic - Moduł języka Perl opakowujący bibliotekę libmagic
Name:		perl-File-LibMagic
Version:	0.85
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FI/FITZNER/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	037150b3131a566b518a7042f9a8d527
URL:		http://search.cpan.org/dist/File-LibMagic/
BuildRequires:	libmagic-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File::LibMagic is a simple perl interface to libmagic library.

%description -l pl.UTF-8
Moduł języka Perl File::LibMagic jest prostym interfejsem do
biblioteki libmagic.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/File/*.pm
%dir %{perl_vendorarch}/auto/File/LibMagic
%{perl_vendorarch}/auto/File/LibMagic/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/File/LibMagic/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
