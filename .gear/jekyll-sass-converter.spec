Name:    gem-jekyll-sass-converter
Version: 2.1.0
Release: alt1

Summary: A basic Sass converter for Jekyll.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/jekyll/jekyll-sass-converter

Packager:  Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch: noarch

Source:  %name-v%version.tar

BuildRequires(pre): rpm-build-ruby

%description
A basic Sass converter for Jekyll.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -n %name-v%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.1.0-alt1
- initial build
