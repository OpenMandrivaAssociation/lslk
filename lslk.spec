%define name lslk
%define version 1.29
%define release %mkrel 9

Summary: A lock file lister
Name: %name
Version: %version
Release: %release
License: GPL style
Group: Monitoring
URL: ftp://vic.cc.purdue.edu:/pub/tools/unix/lslk/
Source: ftp://vic.cc.purdue.edu/pub/tools/unix/lslk/lslk_%{version}_W.tar.bz2
Buildroot: %_tmppath/%name-buildroot

%description
Lslk is a lock file lister.  Lslk attempts to list all of the locks on
the executing system's local files (i.e., on the active inodes).

Install lslk if you need a utility for listing file locks.

%prep
%setup -q -c -n lslk
tar xf lslk_%version.tar
[ -d lslk_%version ] && cd lslk_%version

%build
[ -d lslk_%version ] && cd lslk_%version
./Configure -n linux
%make DEBUG="$RPM_OPT_FLAGS" CFGF=-DLINUXV=228

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_sbindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man8

[ -d lslk_%version ] && cd lslk_%version
install -s lslk $RPM_BUILD_ROOT%_sbindir
install lslk.8 $RPM_BUILD_ROOT%_mandir/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(0755,root,kmem) %_sbindir/lslk
%_mandir/man8/lslk.8*


