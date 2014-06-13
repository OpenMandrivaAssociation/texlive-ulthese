# revision 27951
# category Package
# catalog-ctan /macros/latex/contrib/ulthese
# catalog-date 2012-10-10 18:33:50 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-ulthese
Version:	1.0
Release:	2
Summary:	Thesis class and templates for Universite Laval
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ulthese
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulthese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulthese.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulthese.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a class based on memoir to prepare theses
and memoirs compliant with the presentation rules set forth by
the Faculty of Graduate Studies of Universite Laval, Quebec,
Canada. The class also comes with an extensive set of templates
for the various types of theses and memoirs offered at Laval.
Please note that the documentation for the class and the
comments in the templates are all written in French, the
language of the target audience.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ulthese/ul_p.eps
%{_texmfdistdir}/tex/latex/ulthese/ul_p.pdf
%{_texmfdistdir}/tex/latex/ulthese/ulthese.cls
%doc %{_texmfdistdir}/doc/latex/ulthese/README
%doc %{_texmfdistdir}/doc/latex/ulthese/abstract.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/annexe.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/avantpropos.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/chapitre1.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/chapitre2.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-doctorat-cotutelle.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-doctorat-extension-UQO.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-doctorat-extension-UdeS.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-doctorat-mesure.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-doctorat-multifacultaire.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-doctorat.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-maitrise-extension-UQAC.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-maitrise-mesure.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/gabarit-maitrise.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/introduction.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/remerciements.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/resume.tex
%doc %{_texmfdistdir}/doc/latex/ulthese/ulthese.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ulthese/ulthese.dtx
%doc %{_texmfdistdir}/source/latex/ulthese/ulthese.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
