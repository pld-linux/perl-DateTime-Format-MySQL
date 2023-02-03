#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	DateTime
%define	pnam	Format-MySQL
Summary:	DateTime::Format::MySQL - Parse and format MySQL dates and times
Summary(pl.UTF-8):	DateTime::Format::MySQL - analizowanie i formatowanie dat MySQL-a
Name:		perl-DateTime-Format-MySQL
Version:	0.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	60b84516b5f29e0c639cd1a0f12333d2
URL:		https://metacpan.org/release/DateTime-Format-MySQL
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Format-Builder >= 0.60
%endif
Requires:	perl-DateTime-Format-Builder >= 0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module understands the formats used by MySQL for its DATE,
DATETIME, TIME and TIMESTAMP data types. It can be used to parse
these formats in order to create DateTime objects, and it can take a
DateTime object and produce a string representing it in the MySQL
format.

%description -l pl.UTF-8
Ten moduł rozumie formaty używane przez MySQL-a dla typów danych DATE,
DATETIME, TIME i TIMESTAMP. Może być używany do analizy tych formatów
w celu utworzenia obiektów DateTime; może także przyjąć obiekt
DateTime i utworzyć łańcuch z jego reprezentacją w formacie MySQL-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Format/MySQL.pm
%{_mandir}/man3/DateTime::Format::MySQL.3pm*
