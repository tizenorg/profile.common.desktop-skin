#!/bin/sh

#
#  Launch web cam 
#

pidfile=$HOME/.gstvid2-pid

touch $pidfile
alreadyrunning=`cat $pidfile`

video=/usr/share/media/videos/Caminandes_1080p.mp4

if [ $(echo $alreadyrunning | wc -w) -lt 1  ] ; then
    echo "create new"
	if gst-inspect-1.0  | grep ^vaapi &>/dev/null; then
		gst-launch-1.0  filesrc location=$video ! qtdemux name=demux  \
			demux.audio_0 ! queue ! decodebin ! audioconvert ! audioresample ! autoaudiosink  \
			demux.video_0 ! queue ! vaapidecode ! vaapisink fullscreen=1 &
	else
		echo "Playing without VA-API"
		gst-launch-1.0 playbin uri=file://$video video-sink=waylandsink &
	fi
    echo $!  >> $pidfile
else echo "already running"
    for x in $alreadyrunning; do kill -9 $x; done
    rm -rf $pidfile
fi


