# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/misc/texilikecover.sty
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-texilikecover
Version:	0.1
Release:	3
Summary:	A cover-page package, like TeXinfo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc/texilikecover.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texilikecover.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package creates document cover pages, like those that
TeXinfo produces.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texilikecover/texilikecover.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 756625
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719688
- texlive-texilikecover
- texlive-texilikecover
- texlive-texilikecover

