%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	An HTML/XHTML template library for Ruby
Summary(pl):	Biblioteka szablonów HTML/XHTML dla jêzyka Ruby
Name:		amrita2
Version:	1.9.3
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/3417/amrita2_050311.tar.gz
# Source0-md5:	4caf0c25001fc8b0979382abf3364df2
Source1:	setup.rb
URL:		http://amrita2.rubyforge.org/
BuildRequires:	ruby
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
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

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
