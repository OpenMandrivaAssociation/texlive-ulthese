Name:		texlive-ulthese
Version:	4.4
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
%{_texmfdistdir}/tex/latex/ulthese
%doc %{_texmfdistdir}/doc/latex/ulthese
#- source
%doc %{_texmfdistdir}/source/latex/ulthese

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
