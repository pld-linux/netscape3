Summary:	Netscape 3.04 - good, old web browser
Summary(pl):	Netscape 3.04 - stara, dobra przegl±darka WWW
Name:		netscape
Version:	3.04
Release:	4
License:	non-profit
Group:		X11/Applications/Networking
Source0:	ftp://archive.netscape.com/archive/navigator/3.04/shipping/english/unix/linux12/navigator_complete/%{name}-v304-export.x86-unknown-linux-elf.tar.gz
# Source0-md5:	c530b25d3442a05741d34f884b2128f1
Source1:	%{name}3.desktop
Source2:	%{name}3.xpm
URL:		http://www.netscape.com/
Provides:	wwwbrowser
Obsoletes:	netscape < 4
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
An old version of Netscape WWW browser.

%description -l pl
Stara wersja przegl±darki WWW Netscape'a

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/netscape3/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT%{_applnkdir}/Networking/WWW \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps

install netscape $RPM_BUILD_ROOT%{_bindir}/netscape3
install Netscape.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Netscape
install java_301 $RPM_BUILD_ROOT%{_libdir}/netscape3

mv -f movemail-src/README README-movemail

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LICENSE movemail-src/movemail.c
%attr(755,root,root) %{_bindir}/netscape3
%dir %{_libdir}/netscape3
%dir %{_libdir}/netscape3/plugins
%{_libdir}/netscape3/java_301
%{_libdir}/X11/app-defaults/*
%{_applnkdir}/Networking/WWW/*
%{_pixmapsdir}/*
