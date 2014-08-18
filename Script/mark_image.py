#!/usr/bin/env python

from __future__ import division
import sys
import cairo


if len(sys.argv) < 8:
	print "Usage: mark_image.py <file>.png <text> <color> <X1> <Y1> <X2> <Y2>  (000000 < color < ffffff) (0 < X/Y < 100)"
	sys.exit (0)


file = str(sys.argv[1])
text = str(sys.argv[2])
c_red   = (int(sys.argv[3], 16) >> 16) & 0xff;
c_green = (int(sys.argv[3], 16) >> 8) & 0xff;
c_blue  = int(sys.argv[3], 16) & 0xff;
x1 = int(sys.argv[4])
y1 = int(sys.argv[5])
x2 = int(sys.argv[6])
y2 = int(sys.argv[7])

if x1 >= x2:
	print "<X2> has to be bigger than <X1> !"
	sys.exit (1)

if y1 >= y2:
	print "<Y2> has to be bigger than <Y1> !"
	sys.exit (1)


surface = cairo.ImageSurface.create_from_png (file)
context = cairo.Context (surface)


width = surface.get_width ()
height = surface.get_height ()

size = 6
context.set_font_size (size)
xext,yext,wext,hext,xaext,yaext = context.text_extents (text)

while ((x2-x1)*width)/100 > wext:
	size += 1
	context.set_font_size (size)
	xext,yext,wext,hext,xaext,yaext = context.text_extents (text)


context.move_to ((x1*width)/100, (y1*height)/100)
context.set_source_rgb (c_red/255, c_green/255, c_blue/255)
context.show_text (text)

surface.write_to_png (file)
