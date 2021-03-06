Name:           desktop-skin
Summary:        Desktop skin for Tizen:Common
Version:        2.0
Group:          Applications/Multimedia
License:        GPL-2.0+
Release:        0
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest

Requires:       python-cairo

BuildArchitectures: noarch

%description
Provides desktop visuals and test programs
- desktop background
- sample media
- icons
- test programs

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 Script/launch_cam.sh %{buildroot}%{_bindir}
install -m 755 Script/launch_video.sh %{buildroot}%{_bindir}
install -m 755 Script/launch_video2.sh %{buildroot}%{_bindir}
install -m 755 Script/mark_image.py %{buildroot}%{_bindir}
install -m 755 Script/wifi %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/media/videos
install -m 644 Video/AmazingNature_480p.mp4 %{buildroot}%{_datadir}/media/videos
install -m 644 Video/Caminandes_1080p.mp4 %{buildroot}%{_datadir}/media/videos

mkdir -p %{buildroot}%{_datadir}/media/photos
install -m 644 Photos/* %{buildroot}%{_datadir}/media/photos

mkdir -p %{buildroot}%{_datadir}/icons/tizen/32x32
install -m 644 icons/tizen/32x32/* %{buildroot}%{_datadir}/icons/tizen/32x32

mkdir -p %{buildroot}%{_datadir}/applications/tizen
install -m 644 applications/tizen/* %{buildroot}%{_datadir}/applications/tizen

mkdir -p %{buildroot}%{_datadir}/backgrounds/tizen
install -m 644  backgrounds/tizen/tizen_common_3.0.png %{buildroot}%{_datadir}/backgrounds/tizen/tizen_common_3.0.png

%post
ln -sf tizen_common_3.0.png %{_datadir}/backgrounds/tizen/current

%files
%manifest %{name}.manifest
%{_bindir}/*
%{_datadir}/media/videos/*
%{_datadir}/media/photos/*
%{_datadir}/icons/tizen/32x32/*
%{_datadir}/applications/tizen/*
%{_datadir}/backgrounds/tizen/*
