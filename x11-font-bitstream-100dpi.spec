Name: x11-font-bitstream-100dpi
Version: 1.0.4
Release: 2
Summary: Xorg X11 font bitstream-100dpi
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-bitstream-100dpi-%{version}.tar.xz
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font bitstream-100dpi.

%prep
%autosetup -p1 -n font-bitstream-100dpi-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/100dpi

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/100dpi/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/100dpi/fonts.scale

%post
mkfontscale %{_datadir}/fonts/100dpi
mkfontdir %{_datadir}/fonts/100dpi

%postun
mkfontscale %{_datadir}/fonts/100dpi
mkfontdir %{_datadir}/fonts/100dpi

%files
%doc COPYING
%{_datadir}/fonts/100dpi/char*.pcf.gz
%{_datadir}/fonts/100dpi/tech*.pcf.gz
%{_datadir}/fonts/100dpi/term*.pcf.gz
