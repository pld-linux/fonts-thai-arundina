#
# Conditional build:
%bcond_without	latex	# LaTeX fonts
#
Summary:	Collection of Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich
Name:		fonts-thai-arundina
Version:	0.1.3
Release:	1
License:	MIT-like
Group:		Fonts
Source0:	http://linux.thai.net/pub/thailinux/software/thaifonts-arundina/thaifonts-arundina-%{version}.tar.gz
# Source0-md5:	ff64b01e060891277ae8a4f7093c4f60
URL:		http://linux.thai.net/projects/thaifonts-arundina
BuildRequires:	fontforge >= 20080110
BuildRequires:	xorg-app-mkfontscale
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
Summary:	Collection of TrueType Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich w formacie TrueType
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
Summary:	Collection of Type1 Thai scalable fonts
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich w formacie Type1
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
Summary:	Collection of Thai scalable fonts for LaTeX
Summary(pl.UTF-8):	Kolekcja skalowalnych fontów tajskich dla LaTeXa
Group:		Fonts
Requires(post,postun):	texlive
Requires:	texlive
Requires:	thailatex >= 0.4.6

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
%setup -q -n thaifonts-arundina-%{version}

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
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
mv $RPM_BUILD_ROOT%{_fontsdir}/Type1/*.afm $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
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

%files -n fonts-Type1-thai-arundina
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/Type1/Arundina*.pfb
%{_fontsdir}/Type1/fonts.scale.thai-arundina
%{_fontsdir}/Type1/afm/Arundina*.afm

%files -n thailatex-fonts-arundina
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
# shouldn't it be %{_datadir}/texmf/fonts/afm/public/arundina?
%{_datadir}/texmf/fonts/afm/public/tlwg/arun*.afm
%{_datadir}/texmf/fonts/map/dvips/arundina
%{_datadir}/texmf/fonts/tfm/public/arundina
%{_datadir}/texmf/fonts/type1/public/arundina
%{_datadir}/texmf/fonts/vf/public/arundina
%{_datadir}/texmf/tex/latex/fonts-arundina
