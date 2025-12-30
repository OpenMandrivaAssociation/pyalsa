Name:           pyalsa
Version:	1.2.14
Release:	3
License:        LGPL
Group:          Development/Python
Summary:        Python ALSA binding
Source0:        ftp://ftp.alsa-project.org/pub/pyalsa/pyalsa-%{version}.tar.bz2
BuildRequires:  python-devel
BuildRequires:  pkgconfig(alsa)

%description
This package provides the Python binding to ALSA.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%{__python} setup.py build

%install
%{__python} setup.py install \
    --root=%{buildroot} \
    --prefix=%{_prefix}

%files
%py_platsitedir/%{name}
%py_platsitedir/*.egg-info
