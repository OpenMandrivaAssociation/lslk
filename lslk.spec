Summary:	A lock file lister
Name:		lslk
Version:	1.29
Release:	17
License:	GPL style
Group:		Monitoring
Url:		ftp://vic.cc.purdue.edu:/pub/tools/unix/lslk/
Source0:	ftp://vic.cc.purdue.edu/pub/tools/unix/lslk/lslk_%{version}_W.tar.bz2

%description
Lslk is a lock file lister.  Lslk attempts to list all of the locks on
the executing system's local files (i.e., on the active inodes).

Install lslk if you need a utility for listing file locks.

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(0755,root,kmem) %{_sbindir}/lslk
%{_mandir}/man8/lslk.8*

#----------------------------------------------------------------------------

%prep
%setup -q -c -n lslk
tar xf lslk_%{version}.tar

%build
[ -d lslk_%{version} ] && cd lslk_%{version}
./Configure -n linux
%make DEBUG="%{optflags}" CFGF=-DLINUXV=228

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8

install lslk_%{version}/lslk %{buildroot}%{_sbindir}
install lslk_%{version}/lslk.8 %{buildroot}%{_mandir}/man8/

