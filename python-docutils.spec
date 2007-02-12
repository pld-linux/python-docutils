# TODO:
# - consider renaming the spec to distutils.spec and separate
#   python-docutils subpackage (this package includes utilities in
#   %{_bindir} and python-* packages should contain Python modules only)

%define		module	docutils
Summary:	Text documents processing for Python
Summary(pl.UTF-8):   Moduły Pythona do przetwarzania dokumentów tekstowych
Name:		python-%{module}
Version:	0.4
Release:	2
License:	Public Domain
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	0fe7b42bb3c2aa3680fe30f9a5fbf712
URL:		http://docutils.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of the Docutils project is to create a set of tools for
processing plaintext documentation into useful formats, such as HTML,
XML, and TeX. Support for the following sources has been implemented:
- Standalone files.
- PEPs (Python Enhancement Proposals)

Support for the following sources is planned:
- Inline documentation from Python modules and packages
- Email
- Wikis
- Compound documents
- And others as discovered.

%description -l pl.UTF-8
Celem projektu Docutils jest stworzenie zestawu narzędzi do
przetwarzania dokumentacji z czystego tekstu na użyteczne formaty,
takie jak HTML, XML czy TeX. Jak na razie obsługiwane są formaty:
- niezależne pliki tekstowe
- PEPy (proponowane rozszerzenia Pythona)

Planowane jest stworzenie obsługi formatów:
- dokumentacji inline dla modułów i pakietów Pythona
- Emaili
- Wiki
- dokumentów złożonych
- innych, w miarę potrzeb.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -r test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

cd $RPM_BUILD_ROOT%{_bindir}
for f in *.py; do
	mv $f ${f%%.py} 
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt HISTORY.txt COPYING.txt FAQ.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/roman.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
