%global git_rev f216f1b4

Name:		openstack-swift-plugin-swift3
Version:	1.0.0
Release:	0.20120711git%{?dist}
Summary:	The swift3 plugin for Openstack Swift

License:	ASL 2.0
URL:		https://github.com/fujita/swift3
# git config --global tar.tar.xz.command "xz -c"
# git archive --format=tar.xz --prefix=swift3-1.0.0-%{git_rev}/ %{git_rev}
Source0:	swift3-1.0.0-%{git_rev}.tar.xz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools

Requires:	openstack-swift >= 1.5.0

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
%setup -q -n swift3-1.0.0-%{git_rev}

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
%{python_sitelib}/swift3-%{version}-*.egg-info/
%{python_sitelib}/swift3/
%doc AUTHORS LICENSE README.md

%changelog
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
