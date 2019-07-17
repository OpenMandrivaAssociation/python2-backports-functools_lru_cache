%global dotname backports.functools_lru_cache
%global srcname backports-functools_lru_cache
%global sum A backport of functools.lru_cache from Python 3.3 as published at ActiveState

Name:           python2-%{srcname}
Version:	1.5
Release:	1
Summary:        %{sum}
Group:          Development/Python

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/57/d4/156eb5fbb08d2e85ab0a632e2bebdad355798dece07d4752f66a8d02d1ea/backports.functools_lru_cache-1.5.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:	python2-setuptools_scm

%description
%{sum}.

%prep
%autosetup -n %{dotname}-%{version}


%build
%py2_build


%install
%py2_install


%files
%doc CHANGES.rst README.rst
%{python2_sitelib}/*
%exclude %{python2_sitelib}/backports/__init__.py*

