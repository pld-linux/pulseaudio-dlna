#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module		pulseaudio_dlna
%define		egg_name	pulseaudio_dlna
Summary:	A small DLNA server which brings DLNA / UPNP supportto PulseAudio and Linux
Name:		pulseaudio-dlna
Version:	0.5.2
Release:	1
License:	GPL v3
Group:		Applications/Sound
Source0:	https://github.com/masmu/pulseaudio-dlna/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3773d0333b9fc722878462e550a06a24
URL:		https://github.com/masmu/pulseaudio-dlna
BuildRequires:	python-chardet >= 2.0.1
BuildRequires:	python-docopt >= 0.6.1
BuildRequires:	python-futures >= 2.1.6
BuildRequires:	python-lxml >= 3
BuildRequires:	python-modules
BuildRequires:	python-netifaces >= 0.8
BuildRequires:	python-notify2 >= 0.3
BuildRequires:	python-protobuf >= 2.5.0
BuildRequires:	python-psutil >= 1.2.1
BuildRequires:	python-requests >= 2.2.1
BuildRequires:	python-setproctitle >= 1.0.1
BuildRequires:	python-setuptools
BuildRequires:	python-zeroconf >= 0.17
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	sox
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small DLNA server which brings DLNA / UPNP support to PulseAudio and
Linux.

It can stream your current PulseAudio playback to different UPNP
devices (UPNP Media Renderers) in your network. It's main goals are:
easy to use, no configuration hassle, no big dependencies. Renderers
in your network will show up as pulseaudio sinks.

By default this only pulls sox for basic transcoding. Optionally you
can install vorbis-tools, faac, flac, lame, opus-tools, ffmpeg for
better performance or quality. Check the man page for instructions and
how to use different encoders.

%prep
%setup -q

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/pulseaudio-dlna
%{_mandir}/man1/pulseaudio-dlna.1*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
