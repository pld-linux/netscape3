Summary:	Netscape 3.04 - good, old web browser
Summary(pl):	Netscape 3.04 - stara, dobra przeglądarka WWW
Name:		netscape
Version:	3.04
Release:	1
Copyright:	non-profit
Group:		Applications/Network
Group(pl):	Aplikacje/Sieciowe
Group(pl):	Aplikacje/Sieciowe
URL:		http://www.netscape.com
Source0:	ftp://archive:oldies@archive.netscape.com/archive/navigator/3.04/shipping/english/unix/linux12/navigator_complete/%{name}-v304-export.x86-unknown-linux-elf.tar.gz
Source1:	netscape3.desktop
Source2:	netscape3.xpm
ExclusiveArch:	i386 i586 i686
Buildroot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6
%define _applnkdir %{_datadir}/applnk

%description
An old version of Netscape WWW browser.

%description -l pl
Stara wersja przeglądarki WWW Netscape'a

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/netscape/plugins,%{_bindir}} \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT%{_applnkdir}/Networking/WWW \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps
	
install netscape $RPM_BUILD_ROOT%{_bindir}/netscape3
install Netscape.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Netscape
install java_301 $RPM_BUILD_ROOT%{_libdir}/netscape

mv movemail-src/README README-movemail

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Networking/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf README README-movemail LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netscape3

%dir %{_libdir}/netscape/plugins
%{_libdir}/netscape/java_301
%{_applnkdir}/Networking/WWW/*
%{_datadir}/pixmaps/*

%doc README.gz LICENSE.gz
%doc movemail-src/movemail.c README-movemail.gz
