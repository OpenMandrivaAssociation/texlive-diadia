%global tl_name diadia
%global tl_revision 79618
%global tl_bin_links diadia:%{_texmfdistdir}/scripts/diadia/diadia.lua

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Package to keep a diabetes diary
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/diadia
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diadia.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/diadia.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(diadia.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The diadia package allows you to keep a diabetes diary. Usually, this
means keeping record of certain medical values like blood sugar, blood
pressure, pulse or weight. It might also include other medical,
pharmaceutical or nutritional data (HbA1c, insulin doses, carbohydrate
units). The diadia package supports all of this plus more - simply by
adding more columns to the data file! It is able to evaluate the data
file and typesets formatted tables and derived plots. Furthermore, it
supports medication charts and info boxes. Supported languages: English,
German. Feel free to provide other translation files!

