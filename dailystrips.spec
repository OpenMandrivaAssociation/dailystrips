%define	name	dailystrips
%define	version	1.0.28
%define release	7

Name:		%{name}
Summary:	A program to automatically download your favorite online comic strips 
Version:	%{version}
Release:	%{release}
# (misc) Don't really know where to put it...
Group:		Toys
Source:		%{name}-%{version}.tar.bz2 
# (misc) Use Date::Manip instead of Date::Parse
Patch0:		%{name}-1.0.28-module_date.patch.bz2
Url:		https://dailystrips.sf.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildArch:	noarch
Requires:	perl > 5.6
Requires:	perl-libwww-perl perl-DateManip

%description
dailystrips is a perl script to automatically download your favorite online
comics from the web. It currently supports over 300 comics and offers a
'local' mode in which strips are downloaded and saved locally to speed
access time.

%prep
%setup -q
%patch -p1 

cat <<EOF > README.mandrake
The main executable is patched to use the module Date::Manip
instead of Date::Parse, since only the first is packaged for Mandrake.
Date::Manip can parse more date format, see perldoc Date::Manip.
EOF

%install
rm -rf $RPM_BUILD_ROOT

install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 %{name}-clean -D $RPM_BUILD_ROOT%{_bindir}/%{name}-clean
install -m755 %{name}-update -D $RPM_BUILD_ROOT%{_bindir}/%{name}-update

mkdir -p  $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp strips.def archive.def  $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README BUGS CHANGELOG COPYING INSTALL README.LOCAL TODO README.dailystrips-clean README.DEFS README.mandrake
%{_bindir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*



%changelog
* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.28-6mdv2009.0
+ Revision: 243888
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.28-4mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import dailystrips


* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 1.0.28-4mdv2007.0
- rebuild

* Fri Mar 11 2005 Eskild Hustvedt <eskild@mandrake.org> 1.0.28-3mdk
- Include dailystrips-update

* Thu Feb 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.0.28-2mdk
- rebuild

* Sun Dec 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.28-1mdk
- 1.0.28
- spec cosmetics
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- remove perl dependencies, rpm will figure out these by itself now:)
- regenerate P0
- fix generation of README.mandrake

* Thu Apr 03 2003  Lenny Cartier <lenny@mandrakesoft.com> 1.0.27-1mdk
- 1.0.27

* Tue Apr 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.25-1mdk
- from Michael Scherer <scherer.michael@free.fr> :
	- initial Mandrake package
	- patch to use the module Date::Manip instead of Date::Parse
