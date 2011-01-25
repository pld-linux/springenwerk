Summary:	Cross Site Scripting (XSS) security scanner, written in Python
Name:		springenwerk
Version:	0.4.5
Release:	0.2
License:	BSD-like
Group:		Applications/WWW
Source0:	http://www.hacktoolrepository.com/files/Web%20applications/Springenwerk/%{name}-%{version}.tar.gz
# Source0-md5:	ca1d8236ff7701f7a2732002c22b6b1e
URL:		http://www.springenwerk.com/
BuildRequires:	sed >= 4.0
Requires:	python >= 1:2.4.0
Requires:	python-BeautifulSoup
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Springenwerk is a Cross Site Scripting (XSS) security scanner, written
in Python.

Features:
- Finds the most common XSS vulnerabilites
- Extracts forms and input elements from given webpages and checks
  them for vulnerabilites
- Follows the form action targets (1 level)
- Can check custom HTTP GET and POST data arguments
- Can use Springenwerk, Firefox or IE in the requests' user agent
  string
- Optionally generates an HTML report file with exploits to
  demonstrate the vulnerabilites
- Comes with an easy to use GUI

%package gui
Summary:	Cross Site Scripting (XSS) security scanner - GUI
Group:		X11/Applications
Requires:	%{name}-%{version}
Requires:	python-tkinter

%description gui
Cross Site Scripting (XSS) security scanner - GUI.

%prep
%setup -q

# add python shebang
%{__sed} -i -e '1i#!%{__python}' *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p springenwerk.py $RPM_BUILD_ROOT%{_bindir}/springenwerk
install -p springenwerkgui.py $RPM_BUILD_ROOT%{_bindir}/springenwerkgui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENCE README
%attr(755,root,root) %{_bindir}/springenwerk

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/springenwerkgui
