#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter_server
Version  : 1.1.4
Release  : 2
URL      : https://files.pythonhosted.org/packages/aa/d3/6779ca0da27e861696032eaf7a7dcc2d1be8fe332448ff69a2b1b321faaf/jupyter_server-1.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/d3/6779ca0da27e861696032eaf7a7dcc2d1be8fe332448ff69a2b1b321faaf/jupyter_server-1.1.4.tar.gz
Summary  : The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: jupyter_server-bin = %{version}-%{release}
Requires: jupyter_server-license = %{version}-%{release}
Requires: jupyter_server-python = %{version}-%{release}
Requires: jupyter_server-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Send2Trash
Requires: anyio
Requires: ipython_genutils
Requires: jupyter_client
Requires: jupyter_core
Requires: nbconvert
Requires: nbformat
Requires: prometheus_client
Requires: pyzmq
Requires: terminado
Requires: tornado
Requires: traitlets
BuildRequires : Jinja2
BuildRequires : Send2Trash
BuildRequires : anyio
BuildRequires : buildreq-distutils3
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : nbconvert
BuildRequires : nbformat
BuildRequires : prometheus_client
BuildRequires : pyzmq
BuildRequires : terminado
BuildRequires : tornado
BuildRequires : traitlets
Patch1: deps.patch

%description
# Jupyter Server
[![Build Status](https://github.com/jupyter/jupyter_server/workflows/CI/badge.svg)](https://github.com/jupyter/jupyter_server/actions)
[![Documentation Status](https://readthedocs.org/projects/jupyter-server/badge/?version=latest)](http://jupyter-server.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the jupyter_server package.
Group: Binaries
Requires: jupyter_server-license = %{version}-%{release}

%description bin
bin components for the jupyter_server package.


%package license
Summary: license components for the jupyter_server package.
Group: Default

%description license
license components for the jupyter_server package.


%package python
Summary: python components for the jupyter_server package.
Group: Default
Requires: jupyter_server-python3 = %{version}-%{release}

%description python
python components for the jupyter_server package.


%package python3
Summary: python3 components for the jupyter_server package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_server)
Requires: pypi(anyio)
Requires: pypi(ipython_genutils)
Requires: pypi(jinja2)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(prometheus_client)
Requires: pypi(pyzmq)
Requires: pypi(send2trash)
Requires: pypi(terminado)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the jupyter_server package.


%prep
%setup -q -n jupyter_server-1.1.4
cd %{_builddir}/jupyter_server-1.1.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609956801
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter_server
cp %{_builddir}/jupyter_server-1.1.4/COPYING.md %{buildroot}/usr/share/package-licenses/jupyter_server/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-server

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter_server/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
