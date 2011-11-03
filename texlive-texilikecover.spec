# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/misc/texilikecover.sty
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-texilikecover
Version:	0.1
Release:	1
Summary:	A cover-page package, like TeXinfo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc/texilikecover.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texilikecover.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package creates document cover pages, like those that
TeXinfo produces.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texilikecover/texilikecover.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
