Summary:	WPKG - a Windows Packager
Summary(pl.UTF-8):	WPKG - a Windows Packager - instalator pakietów dla Windows
Name:		wpkg
Version:	1.0
Release:	beta.1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://wpkg.org/files/beta/%{name}-%{version}-rc2.tar.bz2
# Source0-md5:	0570cbdd552570f708ec795aaf955b66
Source1:	%{name}-samba.conf
Source2:	%{name}-install-service.js
Source3:	%{name}-install.bat
Source4:	%{name}-install-service.bat
Source5:	%{name}-start.bat
URL:		http://wpkg.org/
Requires:	samba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/%{name}

%description
WPKG is an automated software deployment, upgrade and removal script
for Windows. It can be used to push/pull software packages, such as
Service Packs, hotfixes, or program installations from a central
server (for example, Samba) to a number of workstations. It can run as
a service to install software in the background, without user
interaction. It can install MSI, InstallShield, PackagefortheWeb etc.
packages, and all other packages using repackaging or AutoIt.

%description -l pl.UTF-8
WPKG to skrypt dla Windows do zautomatyzowanego rozprowadzania,
uaktualniania i usuwania oprogramowania. Może być używany do
upychania/ściągania pakietów z oprogramowaniem, takich jak Service
Packi, hotfiksy albo programy instalacyjne z centralnego serwera (np.
Samby) na wiele stacji roboczych. Może działać jako usługa do
instalowania oprogramowania w tle, bez interakcji użytkownika. Potrafi
instalować pakiety MSI, InstallShield, PackagefortheWeb itp. oraz
wszystkie inne pakiety poprzez przepakowanie albo AutoIt.

%prep
%setup -q -n %{name}-%{version}-rc2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/samba,%{_sysconfdir}/{files,hosts,packages,profiles,tools}}

install wpkg.js		$RPM_BUILD_ROOT%{_sysconfdir}/wpkg.js
install hosts.xml 	$RPM_BUILD_ROOT%{_sysconfdir}/hosts.xml
install packages.xml	$RPM_BUILD_ROOT%{_sysconfdir}/packages.xml
install profiles.xml	$RPM_BUILD_ROOT%{_sysconfdir}/profiles.xml
install %{SOURCE1}	$RPM_BUILD_ROOT/etc/samba
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/files
install %{SOURCE3}	$RPM_BUILD_ROOT%{_sysconfdir}/files
install %{SOURCE4}	$RPM_BUILD_ROOT%{_sysconfdir}/files
install %{SOURCE5}	$RPM_BUILD_ROOT%{_sysconfdir}
cp -rf {hosts,packages,profiles,tools} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE CHANGES Changelog USAGE CONTRIBUTORS 
%dir %{_sysconfdir}
%{_sysconfdir}/*.js
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.bat
%dir %{_sysconfdir}/files
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/files/*
%dir %{_sysconfdir}/hosts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hosts/*
%dir %{_sysconfdir}/packages
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/packages/*
%dir %{_sysconfdir}/profiles
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/profiles/*
%dir %{_sysconfdir}/tools
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tools/*
%config(noreplace) %verify(not md5 mtime size) /etc/samba/*
