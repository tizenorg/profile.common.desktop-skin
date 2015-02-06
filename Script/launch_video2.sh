#!/bin/sh

#
#  Launch web cam 
#

touch $HOME/gstvid-pid
alreadyrunning=`cat $HOME/gstvid-pid`

URL=file:///usr/share/media/videos/Caminandes_1080p.mp4

if [ $(echo $alreadyrunning | wc -w) -lt 1  ] ; then
    echo "create new"
    gst-launch-1.0 playbin uri=$URL &
    echo $!  >> $HOME/gstvid-pid
else echo "already running"
    for x in $alreadyrunning; do kill -9 $x; done
    rm -rf $HOME/gstvid-pid
fi


