%global dotname backports.functools_lru_cache
%global srcname backports-functools_lru_cache
%global sum A backport of functools.lru_cache from Python 3.3 as published at ActiveState

Name:           python-%{srcname}
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
#BuildRequires:  python2-setuptools_scm
#BuildRequires:  python2-pytest-runner

%description
%{sum}.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Requires:	python2-backports
Group:          Development/Python

%description -n python2-%{srcname}
%{sum}.


%prep
%autosetup -n %{dotname}-%{version}


%build
%py2_build


%install
%py2_install


%check
%{__python2} setup.py test

%files -n python2-%{srcname}
%doc CHANGES.rst README.rst
%{python2_sitelib}/*
%exclude %{python2_sitelib}/backports/__init__.py*

