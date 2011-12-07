Name: hunspell-ga
Summary: Irish hunspell dictionaries
Version: 4.4
Release: 3.1%{?dist}
Source0: http://borel.slu.edu/ispell/ispell-gaeilge-%{version}.tar.gz
Source1: myspell-header
Source2: hunspell-header
Group: Applications/Text
URL: http://borel.slu.edu/ispell/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
Patch1: ispell-gaeilge-4.2-buildhunspell.patch

Requires: hunspell

%description
Irish hunspell dictionaries.

%prep
%setup -q -n ispell-gaeilge-%{version}
%patch1 -p1 -b .buildhunspell.patch

%build
make
cat %{SOURCE1} %{SOURCE2} > header
export LANG=en_IE.UTF-8
ispellaff2myspell gaeilge.aff --myheader header | sed -e "s/\"\"/0/g" | sed -e "s/\"//g" > ga_IE.aff
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ga_IE.dic ga_IE.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 4.4-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 05 2008 Caolán McNamara <caolanm@redhat.com> - 4.4-1
- latest version

* Wed Mar 05 2008 Caolan McNamara <caolanm@redhat.com> - 4.3-3
- build the .aff from gaeilge.aff and ispellaff2myspell

* Tue Mar 04 2008 Caolan McNamara <caolanm@redhat.com> - 4.3-2
- update to latest .aff

* Mon Nov 05 2007 Caolan McNamara <caolanm@redhat.com> - 4.3-1
- latest version

* Mon Aug 20 2007 Caolan McNamara <caolanm@redhat.com> - 4.2-1
- bump to latest upstream

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060731-2
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20060731-1
- initial version
