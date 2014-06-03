Name:		desktop-skin
Summary:	Desktop skin for Tizen:Common
Version: 	2.0
Group: 		Applications/Multimedia
License:    GPL-2.0+
Release: 	1
Source0:        %{name}-%{version}.tar.gz

%description
Provides desktop visuals and test programs
- desktop background
- sample media
- icons
- test programs

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 Script/launch_cam.sh %{buildroot}%{_bindir}
install -m 755 Script/launch_video.sh %{buildroot}%{_bindir}
install -m 755 Script/wifi %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/media/videos
install -m 644 Video/AmazingNature_480p.mp4 %{buildroot}%{_datadir}/media/videos

mkdir -p %{buildroot}%{_datadir}/media/photos
install -m 644 Photos/* %{buildroot}%{_datadir}/media/photos

mkdir -p %{buildroot}%{_datadir}/icons/tizen/32x32
install -m 644 icons/tizen/32x32/* %{buildroot}%{_datadir}/icons/tizen/32x32

mkdir -p %{buildroot}%{_datadir}/applications/tizen
install -m 644 applications/tizen/* %{buildroot}%{_datadir}/applications/tizen

mkdir -p %{buildroot}%{_datadir}/backgrounds/tizen
install -m 644  backgrounds/tizen/golfe-morbihan.jpg %{buildroot}%{_datadir}/backgrounds/tizen/golfe-morbihan.jpg
install -m 644  backgrounds/tizen/tizen_common.png %{buildroot}%{_datadir}/backgrounds/tizen/tizen_common.png

%post
ln -s tizen_common.png %{_datadir}/backgrounds/tizen/current

%files
%{_bindir}/*
%{_datadir}/media/videos/AmazingNature_480p.mp4
%{_datadir}/media/photos/*
%{_datadir}/icons/tizen/32x32/*
%{_datadir}/applications/tizen/*
%{_datadir}/backgrounds/tizen/*
