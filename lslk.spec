%define name lslk
%define version 1.29
%define release %mkrel 15

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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.29-14mdv2011.0
+ Revision: 666100
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.29-13mdv2011.0
+ Revision: 606424
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.29-12mdv2010.1
+ Revision: 523213
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.29-11mdv2010.0
+ Revision: 426012
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.29-10mdv2009.1
+ Revision: 351542
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.29-9mdv2009.0
+ Revision: 223131
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.29-8mdv2008.1
+ Revision: 129501
- kill re-definition of %%buildroot on Pixel's request


* Wed Nov 22 2006 Lenny Cartier <lenny@mandriva.com> 1.29-8mdv2007.0
+ Revision: 86205
- Rebuild & mkrel
- Import lslk

