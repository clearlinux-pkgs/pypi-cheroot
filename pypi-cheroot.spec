#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cheroot
Version  : 8.6.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/99/c4/9b5ca09208047f2689c24ee63e195aa01ceffb7857d715cabc046559ddd6/cheroot-8.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/99/c4/9b5ca09208047f2689c24ee63e195aa01ceffb7857d715cabc046559ddd6/cheroot-8.6.0.tar.gz
Summary  : Highly-optimized, pure-python HTTP server
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cheroot-bin = %{version}-%{release}
Requires: pypi-cheroot-license = %{version}-%{release}
Requires: pypi-cheroot-python = %{version}-%{release}
Requires: pypi-cheroot-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jaraco.functools)
BuildRequires : pypi(more_itertools)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(six)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/cheroot.svg
:target: https://pypi.org/project/cheroot

%package bin
Summary: bin components for the pypi-cheroot package.
Group: Binaries
Requires: pypi-cheroot-license = %{version}-%{release}

%description bin
bin components for the pypi-cheroot package.


%package license
Summary: license components for the pypi-cheroot package.
Group: Default

%description license
license components for the pypi-cheroot package.


%package python
Summary: python components for the pypi-cheroot package.
Group: Default
Requires: pypi-cheroot-python3 = %{version}-%{release}

%description python
python components for the pypi-cheroot package.


%package python3
Summary: python3 components for the pypi-cheroot package.
Group: Default
Requires: python3-core
Provides: pypi(cheroot)
Requires: pypi(jaraco.functools)
Requires: pypi(more_itertools)
Requires: pypi(six)

%description python3
python3 components for the pypi-cheroot package.


%prep
%setup -q -n cheroot-8.6.0
cd %{_builddir}/cheroot-8.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649727041
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cheroot
cp %{_builddir}/cheroot-8.6.0/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cheroot/14ee588696fc67576de579f6094ab0e33a61125d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cheroot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cheroot/14ee588696fc67576de579f6094ab0e33a61125d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
