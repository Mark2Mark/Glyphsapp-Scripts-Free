#MenuTitle: Fontmetrics-Glyph
# -*- coding: utf-8 -*-
__doc__="""
• Generate a Glyph with lines at vertical metrics
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	>> Mark Froemberg << aka `Mark2Mark` @ GitHub
#	>> www.markfromberg.com <<
#
#	_NOTES:
#		- Take care to have the GSPen.py and objectsGS.py on first level of the glyphs
#		scripts folder for RoboFab to work
#
#	_TODO:
#		- 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from robofab.world import CurrentFont
import math
f = CurrentFont()

baseline = 0
descender = f.info.descender
xHeight = f.info.xHeight
capHeight = f.info.capHeight
ascender = f.info.ascender
angle = f.info.italicAngle

metrics = [baseline, descender, xHeight, capHeight, ascender]

g = f.newGlyph("fontmetrics", True)

p = g.getPen()
print dir(p)
w = 600

u = 1
gap = 10

# rotation point is half of x-height
offset = math.tan(math.radians(angle)) * xHeight/2
    
for m in metrics:
    # offset for italic angle
    shift = math.tan(math.radians(angle)) * m - offset
	
    p.moveTo((shift+gap, m))
    p.lineTo((shift+gap, m+u))
    p.lineTo((w+shift, m+u))
    p.lineTo((w+shift, m))
    p.closePath()
