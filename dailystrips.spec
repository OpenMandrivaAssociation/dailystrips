%define	name	dailystrips
%define	version	1.0.28
%define	release	%mkrel 4

Name:		%{name}
Summary:	A program to automatically download your favorite online comic strips 
Version:	%{version}
Release:	%{release}
# (misc) Don't really know where to put it...
Group:		Toys
Source:		%{name}-%{version}.tar.bz2 
# (misc) Use Date::Manip instead of Date::Parse
Patch0:		%{name}-1.0.28-module_date.patch.bz2
Url:		http://dailystrips.sf.net/
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

