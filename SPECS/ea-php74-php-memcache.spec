%global scl_version ea-php74
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcache
Version: 4.0.3
Summary: memcache extension for %{scl_version}
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4576 for more details
%define release_prefix 2
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://github.com/websupport-sk/pecl-memcache/
Source: https://github.com/websupport-sk/pecl-memcache/archive/NON_BLOCKING_IO_php7.tar.gz?/pecl-memcache-NON_BLOCKING_IO_php7.tar.gz
Source1: memcache.ini

# should be no requires for building this package
#Requires: memcached
#BuildRequires: libyaml-devel
BuildRequires: %{scl_version} %{scl_version}-php-cli

%description
Memcached is a caching daemon designed especially for  dynamic web applications
to decrease database load by storing objects in memory. This extension allows
you to work with memcached through handy OO and procedural interfaces.


%prep
%setup -n pecl-memcache-NON_BLOCKING_IO_php7

%build
scl enable %{scl_version} phpize
scl enable %{scl_version} ./configure
make

%install
#scl enable %{scl_version} 'make install DESTDIR=$RPM_BUILD_ROOT'
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcache.so
%config /%{ext_prefix}/%{conf_dir}/memcache.ini

%changelog
* Tue Apr  7 2020 Dan Muey <dan@cpanel.net> - 4.0.3-2
- ZC-6277: Add support for php 7.4

* Thu Apr 25 2019 Tim Mullin <tim@cpanel.net> - 4.0.3-1
- EA-8302: Add support for php 7.3 and update to 4.0.3

* Wed Jan 01 2018 Dan Muey <dan@cpanel.net> - 3.0.9-1
- EA-6097: Correct version to 3.0.9

* Mon Mar  6 2017 Jack Hayhurst <jack@deleteos.com> - 0.2
- added ea-php71-php-memcahe branched off of php54

- Fixed package name, entire RPM is now working.
* Fri Mar  5 2017 Jack Hayhurst <jack@deleteos.com> - 0.2
- Fixed package name, entire RPM is now working.

* Wed Mar  1 2017 Jack Hayhurst <jack@deleteos.com> - 0.1
- Initial spec file creation.
