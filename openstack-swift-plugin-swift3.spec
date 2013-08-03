#global git_rev f216f1b4

Name:		openstack-swift-plugin-swift3
Version:	1.7
#Release:	0.20120711git%{?dist}
Release:	3%{?dist}
Summary:	The swift3 plugin for Openstack Swift

License:	ASL 2.0
URL:		https://github.com/fujita/swift3
# git config --global tar.tar.xz.command "xz -c"
# git archive --format=tar.xz --prefix=swift3-1.0.0-#{git_rev}/ #{git_rev}
#Source0:	swift3-1.0.0-#{git_rev}.tar.xz
# URL: https://github.com/fujita/swift3/archive/v1.7.tar.gz
# However, github returns 302 for it. When follow redirect, it returns
# Content-Disposition: attachment; filename=swift3-1.7.tar.gz
Source0:	swift3-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools

Requires:	openstack-swift >= 1.5.0

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
#setup -q -n swift3-1.0.0-#{git_rev}
%setup -q -n swift3-1.7

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
#{python_sitelib}/#{name}-#{version}-*.egg-info/
# Tomo posted official release 1.7 but setup.py creating 1.7.0, way to go.
%{python_sitelib}/swift3-1.7.0-*.egg-info/
%{python_sitelib}/swift3/
%doc AUTHORS LICENSE README.md

%changelog
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
