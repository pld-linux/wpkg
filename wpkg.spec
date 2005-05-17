Summary:	WPKG - a Windows Packager
Summary(pl):	WPKG - a Windows Packager
Name:		wpkg
Version:	r433
Release:	0.1
Epoch:		0
License:	GPL v.2
Group:		Applications
Source0:	http://dl.sourceforge.net/sourceforge/wpkg/%{name}-%{version}.tar.gz
# Source0-md5:	ada1f9b4b9b22dc8a1d258d1714f513c
#Patch0:		%{name}-what.patch
URL:		http://wpkg.sourceforge.net/
#BuildRequires:	automake
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WPKG is an automated software deployment, upgrade and removal script
for Windows.It can be used to push/pull software packages, such as
Service Packs, hotfixes, or program installations from a central
server (for example, Samba) to a number of workstations.It can run
as a service to install software in the background, without user
interaction.It can install MSI, InstallShield, PackagefortheWeb etc.
packages, and all other packages using repackaging or AutoIt

%description -l pl
WPKG is an automated software deployment, upgrade and removal script
for Windows.It can be used to push/pull software packages, such as
Service Packs, hotfixes, or program installations from a central
server (for example, Samba) to a number of workstations.It can run
as a service to install software in the background, without user
interaction.It can install MSI, InstallShield, PackagefortheWeb etc.
packages, and all other packages using repackaging or AutoIt

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sysconfdir}/%{name}}
install wpkg.js		$RPM_BUILD_ROOT/%{_datadir}/%{name}/wpkg.js
install hosts.xml 	$RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/hosts.xml
install packages.xml	$RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/packages.xml
install profiles.xml	$RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/profiles.xml

cd $RPM_BUILD_ROOT/%{_datadir}/%{name}
ln -s %{_sysconfdir}/%{name}/hosts.xml	hosts.xml
ln -s %{_sysconfdir}/%{name}/packages.xml packages.xml 
ln -s %{_sysconfdir}/%{name}/profiles.xml profiles.xml 

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc README TODO GPL-2 LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_datadir}/%{name}/wpkg.js
%{_datadir}/%{name}/*.xml
