#!/bin/sh

#
#  Launch web cam 
#

touch /home/app/gst-pid
alreadyrunning=`cat /home/app/gst-pid`

cnt=$(echo $alreadyrunning | wc -w)
if [ $cnt -lt 2  ] ; then
    echo "create new $cnt"
    gst-launch-1.0 v4l2src device=/dev/video$cnt ! video/x-raw, width=640, height=480 ! videoconvert ! waylandsink &
    echo $!  >> /home/app/gst-pid
else echo "already running"
    for x in $alreadyrunning; do kill -9 $x; done
    rm -rf /home/app/gst-pid
fi


