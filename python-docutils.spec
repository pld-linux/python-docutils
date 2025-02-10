%bcond_without	tests	# unit tests

Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		python-docutils
Version:	0.18.1
Release:	7
License:	Public Domain, BSD, GPL v3 (see COPYING.txt)
Group:		Development/Tools
# original URL, but only with major releases: http://downloads.sourceforge.net/docutils/%{name}-%{version}.tar.gz
#Source0Download: https://pypi.org/simple/docutils/
Source0:	https://files.pythonhosted.org/packages/source/d/docutils/docutils-%{version}.tar.gz
# Source0-md5:	ca5827e2432fd58f4c8d74a6591135de
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
# py3 patch assumes python3 lexer is the default, as it is since pygments 2.5.0
BuildRequires:	python-pygments >= 2.5.0
# a few tests fail with _xmlplus implementation of xml
BuildConflicts:	python-PyXML
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Docutils are utilities for general- and special-purpose documentation,
including autodocumentation of Python modules. Includes
reStructuredText, the easy to read, easy to use,
what-you-see-is-what-you-get plaintext markup language.

This package provides the Docutils modules for Python 2.

%description -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

Ten pakiet dostarcza moduły Docutils dla Pythona 2.

%package -n docutils-2
Summary:	Documentation Utilities for Python 2.x
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji dla Pythona 2.x
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description -n docutils-2
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

This package provides the Docutils for Python 2.

%description -n docutils-2 -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

Ten pakiet zawiera Docutils dla Pythona 2.

%prep
%setup -q -n docutils-%{version}

%build
%{__python} setup.py config build -b build-2

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} test/alltests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	%{__mv} "${f}" "${f%.py}-2"
done

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.txt COPYING.txt README.txt RELEASE-NOTES.txt THANKS.txt docs
%{py_sitescriptdir}/docutils
%{py_sitescriptdir}/docutils-%{version}-py*.egg-info

%files -n docutils-2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rst*-2
