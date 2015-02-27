#!/bin/sh

#
#  Launch web cam 
#

pidfile=$HOME/.gstvid-pid

touch $pidfile
alreadyrunning=`cat $pidfile`

video=/usr/share/media/videos/AmazingNature_480p.mp4

if [ $(echo $alreadyrunning | wc -w) -lt 3  ] ; then
    echo "create new"
    #gst-launch-1.0 playbin uri=$URL &
	gst-launch-1.0  filesrc location=$video ! qtdemux name=demux  \
		demux.audio_0 ! queue ! decodebin ! audioconvert ! audioresample ! autoaudiosink  \
		demux.video_0 ! queue ! vaapidecode ! vaapisink &
    echo $!  >> $pidfile
else echo "already running"
    for x in $alreadyrunning; do kill -9 $x; done
    rm -rf $pidfile
fi


