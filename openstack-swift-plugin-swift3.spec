Name:		openstack-swift-plugin-swift3
Version:	1.10
Release:	1%{?dist}
Summary:	The swift3 plugin for Openstack Swift

License:	ASL 2.0
URL:		https://github.com/openstack/swift3

# Do this once per builder:
# git config --global tar.tar.xz.command "xz -c"

# TODO change to tarballs.openstack.org once
# https://bugs.launchpad.net/swift3/+bug/1561790 is solved
Source0:	https://github.com/openstack/swift3/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
BuildRequires:	git

Requires:	openstack-swift >= 2.1.0

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
%autosetup -n swift3-%{version} -S git
# XXX fake git is to help PBR until proper sdist tarball is available
git tag %{version}.0

%build
%{__python} setup.py build
sed -i 's/\r//' LICENSE

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
%{python_sitelib}/swift3-*.egg-info/
%{python_sitelib}/swift3/
%doc AUTHORS README.md

%changelog
* Fri Mar 25 2016 Alan Pevec <apevec@redhat.com> 1.10-1
- Update to 1.10

* Mon Dec 14 2015 Pete Zaitcev <zaitcev@redhat.com> 1.9-1
- Update to upstream 1.9: CVE-2015-8466

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6.20150601git69f94393
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Pete Zaitcev <zaitcev@redhat.com> 1.7-5.20150601git69f94393
- Far too long without an update, go back to snapshots (#1117012)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Pete Zaitcev <zaitcev@redhat.com> - 1.7-1
- Update to upstream 1.7; keep git style as comments in the spec
- Upstream update fixes Cyberduck

* Mon Sep 17 2012 Alan Pevec <apevec@redhat.com> - 1.0.0-0.20120711git
- Pull bugfixes from upstream git.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.20120613git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.0.0-0.20120612git
- Rename once again to match guidelines for pre-releases
- Drop Group: per review bz#831871 c#3

* Wed Jun 13 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.0.0-20120612.1
- Move the datestr to release per Packaging:NamingGuidelines#Release_Tag

* Wed Jun 13 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.0.0.20120612-1
- Use a reproducible tarball with a specific commit id (5c74ba04)

* Tue Jun 12 2012 Pete Zaitcev <zaitcev@redhat.com>
- 1.0.0.20120601-1
- Initial revision
