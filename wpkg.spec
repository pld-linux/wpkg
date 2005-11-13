Summary:	WPKG - a Windows Packager
Summary(pl):	WPKG - a Windows Packager - instalator pakietów dla Windows
Name:		wpkg
Version:	0.9.1
Release:	1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://wpkg.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	79f3819ed43840fb67e3ef741234dd5e
Source1:	%{name}-samba.conf
Source2:	%{name}-install-service.js
Source3:	%{name}-install.bat
Source4:	%{name}-install-service.bat
Source5:	%{name}-start.bat
URL:		http://wpkg.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WPKG is an automated software deployment, upgrade and removal script
for Windows. It can be used to push/pull software packages, such as
Service Packs, hotfixes, or program installations from a central
server (for example, Samba) to a number of workstations. It can run as
a service to install software in the background, without user
interaction. It can install MSI, InstallShield, PackagefortheWeb etc.
packages, and all other packages using repackaging or AutoIt.

%description -l pl
WPKG to skrypt dla Windows do zautomatyzowanego rozprowadzania,
uaktualniania i usuwania oprogramowania. Mo¿e byæ u¿ywany do
upychania/¶ci±gania pakietów z oprogramowaniem, takich jak Service
Packi, hotfiksy albo programy instalacyjne z centralnego serwera (np.
Samby) na wiele stacji roboczych. Mo¿e dzia³aæ jako us³uga do
instalowania oprogramowania w tle, bez interakcji u¿ytkownika. Potrafi
instalowaæ pakiety MSI, InstallShield, PackagefortheWeb itp. oraz
wszystkie inne pakiety poprzez przepakowanie albo AutoIt.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/files,%{_sysconfdir}/{%{name},samba}}

install wpkg.js		$RPM_BUILD_ROOT%{_datadir}/%{name}/wpkg.js
install hosts.xml 	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hosts.xml
install packages.xml	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/packages.xml
install profiles.xml	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/profiles.xml
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/samba
install %{SOURCE2}	$RPM_BUILD_ROOT%{_datadir}/%{name}/files
install %{SOURCE3}	$RPM_BUILD_ROOT%{_datadir}/%{name}/files
install %{SOURCE4}	$RPM_BUILD_ROOT%{_datadir}/%{name}/files
install %{SOURCE5}	$RPM_BUILD_ROOT%{_datadir}/%{name}

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s %{_sysconfdir}/%{name}/hosts.xml hosts.xml
ln -s %{_sysconfdir}/%{name}/packages.xml packages.xml
ln -s %{_sysconfdir}/%{name}/profiles.xml profiles.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/%{name}
