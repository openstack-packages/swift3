# With the 1.9 release, the machinery of git_rev became unused, but we
# keep it around given the history of the long gap after 1.7.
%global with_git_rev 0

%if 0%{?with_git_rev}
# echo $(git rev-parse HEAD | dd bs=8 count=1 2>/dev/null)
%global git_rev 69f94393
# See: Fedora Packaging, Naming Guidelines, Snapshot Packages clause.
%global checkout .20150601git%{git_rev}
%endif

Name:		openstack-swift-plugin-swift3
Version:	1.9
Release:	1%{?checkout}%{?dist}
Summary:	The swift3 plugin for Openstack Swift

License:	ASL 2.0
URL:		https://github.com/fujita/swift3

# Do this once per builder:
# git config --global tar.tar.xz.command "xz -c"

%if 0%{?with_git_rev}
# git archive --format=tar.xz -o ../swift3-#{version}-#{git_rev}.tar.xz --prefix=swift3-#{version}-#{git_rev}/ #{git_rev}
Source0:	swift3-%{version}-%{git_rev}.tar.xz
%else
# git archive --format=tar.xz -o ../swift3-#{version}.tar.xz --prefix=swift3-#{version}/ v#{version}
Source0:	swift3-%{version}.tar.xz
%endif

# If we simply archive a tarball and let setup to do its job, this happens:
#  File "/usr/lib/python2.7/site-packages/pbr/hooks/metadata.py", line 28, in hook
#    self.config['name'], self.config.get('version', None))
#  File "/usr/lib/python2.7/site-packages/pbr/packaging.py", line 567, in get_version
#    raise Exception("Versioning for this project requires either an sdist"
# Our solution is to use a fake PKG-INFO that fools pbr into behaving.
Source1:	swift3-1.7.PKG-INFO

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools

Requires:	openstack-swift >= 2.1.0

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
%if 0%{?with_git_rev}
%setup -q -n swift3-%{version}-%{git_rev}
cp %{SOURCE1} %{_builddir}/swift3-%{version}-%{git_rev}/PKG-INFO
%else
%setup -q -n swift3-%{version}
cp %{SOURCE1} %{_builddir}/swift3-%{version}/PKG-INFO
%endif

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
#{python_sitelib}/#{name}-#{version}-*.egg-info/
# Tomo posted official release 1.7 but setup.py creating 1.7.0, way to go.
%{python_sitelib}/swift3-%{version}.0-*.egg-info/
%{python_sitelib}/swift3/
%doc AUTHORS README.md

%changelog
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
