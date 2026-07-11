%global tl_name texilikecover
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A cover-page package, like TeXinfo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/misc/texilikecover.sty
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texilikecover.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package creates document cover pages, like those that TeXinfo
produces.

