%global dotname backports.functools_lru_cache
%global srcname backports-functools_lru_cache
%global sum A backport of functools.lru_cache from Python 3.3 as published at ActiveState

Name:           python2-%{srcname}
Version:        1.4
Release:        1
Summary:        %{sum}
Group:          Development/Python

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/b/%{dotname}/%{dotname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

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

