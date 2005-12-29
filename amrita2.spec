Summary:	An HTML/XHTML template library for Ruby
Summary(pl):	Biblioteka szablonów HTML/XHTML dla jêzyka Ruby
Name:		amrita2
Version:	1.9.5
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/4491/%{name}_050518.tar.gz
# Source0-md5:	2cc56bd862b97cd05744945b8072b0c1
Source1:	setup.rb
URL:		http://amrita2.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby.

%description -l pl
Biblioteka szablonów HTML/XHTML dla jêzyka Ruby.

%prep
%setup -q -n %{name}
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README docs/*

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog sample rdoc/*
%attr(755,root,root) %{_bindir}/amrita_r
%dir %{ruby_rubylibdir}/%{name}
%{ruby_rubylibdir}/%{name}/*.rb
%{ruby_rubylibdir}/%{name}.rb
