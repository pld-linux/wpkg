Summary:	WPKG - a Windows Packager
Summary(pl):	WPKG - a Windows Packager - instalator pakietów dla Windows
Name:		wpkg
Version:	0.9
Release:	0.1
Epoch:		0
License:	GPL v.2
Group:		Applications
Source0:	http://dl.sourceforge.net/wpkg/%{name}-%{version}.tar.gz
# Source0-md5:	1f9fbeeb07525ba2182880ef28a041c4
Source1:	%{name}-samba.conf
#Source2:	%{name}-
URL:		http://wpkg.sourceforge.net/
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
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/{%{name},samba}}

install wpkg.js		$RPM_BUILD_ROOT%{_datadir}/%{name}/wpkg.js
install hosts.xml 	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hosts.xml
install packages.xml	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/packages.xml
install profiles.xml	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/profiles.xml
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/samba

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s %{_sysconfdir}/%{name}/hosts.xml	hosts.xml
ln -s %{_sysconfdir}/%{name}/packages.xml packages.xml 
ln -s %{_sysconfdir}/%{name}/profiles.xml profiles.xml 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO GPL-2 LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/wpkg.js
%{_datadir}/%{name}/*.xml
