#
# Conditional build:
%bcond_without	latex	# LaTeX fonts
#
Summary:	Thai Arundina scalable fonts
Summary(pl.UTF-8):	Tajskie fonty skalowalne Arundina
Name:		fonts-thai-arundina
Version:	0.2.1
Release:	2
License:	MIT-like
Group:		Fonts
Source0:	http://linux.thai.net/pub/thailinux/software/thaifonts-arundina/fonts-sipa-arundina-%{version}.tar.xz
# Source0-md5:	e3701365e007c0fb271de6d7778cea99
URL:		http://linux.thai.net/projects/thaifonts-arundina
BuildRequires:	fontforge >= 20080110
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with latex}
BuildRequires:	texlive
BuildRequires:	thailatex >= 0.4.6
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arundina fonts were created under SIPA's initiation, aiming at
Bitstream Vera / Dejavu compatibility. They were then further modified
by TLWG for certain aspects:
 - Latin glyph size compatiblity,
 - OpenType conformance.

%description -l pl.UTF-8
Fonty Arundina powstały z inicjatywy SIPA, gdzie celem była zgodność z
fontami Bitstream Vera / Dejavu. Następnie zostały zmodyfikowane przez
TLWG pod następującym kątem:
 - zgodność rozmiaru z glifami łacińskimi,
 - zgodność z OpenType.

%package -n fonts-TTF-thai-arundina
Summary:	TrueType Thai Arundina fonts
Summary(pl.UTF-8):	Tajskie fonty Arundina w formacie TrueType
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-TTF-thai-arundina
Arundina fonts were created under SIPA's initiation, aiming at
Bitstream Vera / Dejavu compatibility. They were then further modified
by TLWG for certain aspects:
 - Latin glyph size compatiblity,
 - OpenType conformance.

This package contains fonts in TrueType format.

%description -n fonts-TTF-thai-arundina -l pl.UTF-8
Fonty Arundina powstały z inicjatywy SIPA, gdzie celem była zgodność z
fontami Bitstream Vera / Dejavu. Następnie zostały zmodyfikowane przez
TLWG pod następującym kątem:
 - zgodność rozmiaru z glifami łacińskimi,
 - zgodność z OpenType.

Ten pakiet zawiera fonty w formacie TrueType.

%package -n fonts-Type1-thai-arundina
Summary:	Type1 Thai Arundina fonts
Summary(pl.UTF-8):	Tajskie fonty Arundina w formacie Type1
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-Type1-thai-arundina
Arundina fonts were created under SIPA's initiation, aiming at
Bitstream Vera / Dejavu compatibility. They were then further modified
by TLWG for certain aspects:
 - Latin glyph size compatiblity,
 - OpenType conformance.

This package contains fonts in Type1 format.

%description -n fonts-Type1-thai-arundina -l pl.UTF-8
Fonty Arundina powstały z inicjatywy SIPA, gdzie celem była zgodność z
fontami Bitstream Vera / Dejavu. Następnie zostały zmodyfikowane przez
TLWG pod następującym kątem:
 - zgodność rozmiaru z glifami łacińskimi,
 - zgodność z OpenType.

Ten pakiet zawiera fonty w formacie Type1.

%package -n thailatex-fonts-arundina
Summary:	Thai Arundina fonts for LaTeX
Summary(pl.UTF-8):	Tajskie fonty Arundina dla LaTeXa
Group:		Fonts
Requires(post,postun):	texlive
Requires:	texlive
Requires:	thailatex >= 0.4.7

%description -n thailatex-fonts-arundina
Arundina fonts were created under SIPA's initiation, aiming at
Bitstream Vera / Dejavu compatibility. They were then further modified
by TLWG for certain aspects:
 - Latin glyph size compatiblity,
 - OpenType conformance.

This package contains LaTeX fonts for use with thailatex.

%description -n thailatex-fonts-arundina -l pl.UTF-8
Fonty Arundina powstały z inicjatywy SIPA, gdzie celem była zgodność z
fontami Bitstream Vera / Dejavu. Następnie zostały zmodyfikowane przez
TLWG pod następującym kątem:
 - zgodność rozmiaru z glifami łacińskimi,
 - zgodność z OpenType.

Ten pakiet zawiera fonty LaTeXowe do używania z pakietem thailatex.

%prep
%setup -q -n fonts-sipa-arundina-%{version}

%build
%configure \
	%{?with_latex:--enable-latex} \
	--enable-pfb \
	--with-ttfdir=%{_fontsdir}/TTF \
	--with-type1dir=%{_fontsdir}/Type1
%{__make} %{?with_latex:-j1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	fontconfigdir=%{_datadir}/fontconfig/conf.avail

install -d $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
%{__mv} $RPM_BUILD_ROOT%{_fontsdir}/Type1/*.afm $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
mkfontscale -o $RPM_BUILD_ROOT%{_fontsdir}/Type1/fonts.scale.thai-arundina $RPM_BUILD_ROOT%{_fontsdir}/Type1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n fonts-TTF-thai-arundina
fontpostinst TTF

%postun	-n fonts-TTF-thai-arundina
fontpostinst TTF

%post	-n fonts-Type1-thai-arundina
fontpostinst Type1

%postun	-n fonts-Type1-thai-arundina
fontpostinst Type1

%post	-n thailatex-fonts-arundina
umask 022
%{_bindir}/texhash

%postun	-n thailatex-fonts-arundina
umask 022
%{_bindir}/texhash

%files -n fonts-TTF-thai-arundina
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/TTF/Arundina*.ttf
%{_datadir}/fontconfig/conf.avail/65-sipa-arundina.conf

%files -n fonts-Type1-thai-arundina
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/Type1/Arundina*.pfb
%{_fontsdir}/Type1/fonts.scale.thai-arundina
%{_fontsdir}/Type1/afm/Arundina*.afm

%files -n thailatex-fonts-arundina
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_datadir}/texmf/fonts/afm/public/fonts-arundina
%{_datadir}/texmf/fonts/enc/dvips/fonts-arundina
%{_datadir}/texmf/fonts/map/dvips/fonts-arundina
%{_datadir}/texmf/fonts/tfm/public/fonts-arundina
%{_datadir}/texmf/fonts/type1/public/fonts-arundina
%{_datadir}/texmf/fonts/vf/public/fonts-arundina
%{_datadir}/texmf/tex/latex/fonts-arundina
