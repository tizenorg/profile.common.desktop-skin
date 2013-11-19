%define USERHOME	/home/app

Name:		desktop-skin
Summary:	Provides desktop-skin.
Version: 	2.0
Group: 		Applications
License:        GPL-2.0+
Release: 	1



Source0:        %{name}-%{version}.tar.gz

%description
Provides desktop-skin.


%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_libdir}/alsa
install -m 644 Sound/asound.state %{buildroot}%{_libdir}/alsa

mkdir -p %{buildroot}%{_bindir}
install -m 755 Sound/alsamixer %{buildroot}%{_bindir}

install -m 755 Script/launch_cam.sh %{buildroot}%{_bindir}
install -m 755 Script/launch_video.sh %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{USERHOME}
install -m 644 Video/AmazingNature_480p.mp4 %{buildroot}%{USERHOME}


mkdir -p %{buildroot}%{USERHOME}/Photos
install -m 644 Photos/* %{buildroot}%{USERHOME}/Photos

mkdir -p %{buildroot}%{_datadir}/icons/tizen/32x32
install -m 644 icons/tizen/32x32/* %{buildroot}%{_datadir}/icons/tizen/32x32

mkdir -p %{buildroot}%{_datadir}/backgrounds/tizen
install -m 644  backgrounds/tizen/golfe-morbihan.jpg %{buildroot}%{_datadir}/backgrounds/tizen/golfe-morbihan.jpg

mkdir -p %{buildroot}%{_sysconfdir}/xdg/weston
install -m 644 weston/weston.ini %{buildroot}%{_sysconfdir}/xdg/weston

%post
chown -R app:app %{USERHOME}

%files
%{_libdir}/alsa/asound.state
%{_bindir}/alsamixer

%{_bindir}/launch_cam.sh
%{_bindir}/launch_video.sh

%{USERHOME}/AmazingNature_480p.mp4

%{USERHOME}/Photos/*

%{_datadir}/icons/tizen/32x32/*

%{_datadir}/backgrounds/tizen/golfe-morbihan.jpg

%{_sysconfdir}/xdg/weston/weston.ini
