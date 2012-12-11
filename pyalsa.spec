Name:           pyalsa
Version:        1.0.25
Release:        1
License:        LGPL
Group:          Development/Python
Summary:        Python ALSA binding
Source0:        pyalsa-%{version}.tar.bz2
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


%changelog
* Thu Feb 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.25-1
+ Revision: 772242
- egg-info fix again
- removed egg-info
- imported package pyalsa

