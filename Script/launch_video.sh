#!/bin/sh

#
#  Launch web cam 
#

touch $HOME/gstvid-pid
alreadyrunning=`cat $HOME/gstvid-pid`

#URL=http://intel07.vannes/~sdx/Downloads/Amazing%20Nature%20full%20HD%20720p.mp4
#URL=http://intel07.vannes/~sdx/Videos/big_buck_bunny_480p_surround-fix.avi
#URL=http://intel07.vannes/~sdx/Videos/caminandes_480p.avi
URL=file:///usr/share/media/videos/AmazingNature_480p.mp4

if [ $(echo $alreadyrunning | wc -w) -lt 8  ] ; then
    echo "create new"
    gst-launch-1.0 playbin uri=$URL &
    echo $!  >> $HOME/gstvid-pid
else echo "already running"
    for x in $alreadyrunning; do kill -9 $x; done
    rm -rf $HOME/gstvid-pid
fi


