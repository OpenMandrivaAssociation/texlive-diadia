Name:		texlive-diadia
Version:	37656
Release:	2
Summary:	Package to keep a diabetes diary
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diadia
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diadia.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diadia.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The diadia package allows you to keep a diabetes diary.
Usually, this means keeping record of certain medical values
like blood sugar, blood pressure, pulse or weight. It might
also include other medical, pharmaceutical or nutritional data
(HbA1c, insulin doses, carbohydrate units). The diadia package
supports all of this plus more - simply by adding more columns
to the data file! It is able to evaluate the data file and
typesets formatted tables and derived plots. Furthermore, it
supports medication charts and info boxes. Supported languages:
English, German. Feel free to provide other translation files!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/tex/latex/diadia
%{_texmfdistdir}/scripts/diadia
%doc %{_texmfdistdir}/doc/latex/diadia

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
