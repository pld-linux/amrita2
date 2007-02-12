Summary:	An HTML/XHTML template library for Ruby
Summary(pl.UTF-8):	Biblioteka szablonów HTML/XHTML dla języka Ruby
Name:		amrita2
Version:	1.9.6
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/7554/%{name}-%{version}.tar.gz
# Source0-md5:	e4004b105bd6cc1ee4226905a5469830
Source1:	setup.rb
URL:		http://amrita2.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby.

%description -l pl.UTF-8
Biblioteka szablonów HTML/XHTML dla języka Ruby.

%prep
%setup -q -n %{name}
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README lib

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog sample rdoc/* docs/*
%dir %{ruby_rubylibdir}/%{name}
%{ruby_rubylibdir}/%{name}/*.rb
%{ruby_rubylibdir}/%{name}.rb
