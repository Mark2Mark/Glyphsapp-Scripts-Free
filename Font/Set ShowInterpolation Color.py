#MenuTitle: Set ShowInterpolation Color.py
# -*- coding: utf-8 -*-
__doc__="""
• Set the interpolation color for all instances. Visible when Show Interpolations filter is active.
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   >> Mark Froemberg << aka `Mark2Mark` @ GitHub
#   >> www.markfromberg.com <<
#
#   _NOTES:
#       - 
#
#   _TODO:
#       - 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp
from AppKit import NSColor
from vanilla import *

thisFont = Glyphs.font # frontmost font
Glyphs.clearLog()
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

class ColorWellWindow(object):

    def __init__(self):
        self.w = Window((150, 50), "set color")
        self.w.colorWell = ColorWell((10, 10, -10, -10),
                            callback=self.colorWellEdit,
                            color=NSColor.colorWithCalibratedRed_green_blue_alpha_( 0, 0.2, 1, .25))
        self.w.open()

    def colorWellEdit(self, sender):
        color = str(sender.get())
        color2 = color.split(" ")
        color3 = ";".join(color2[1:])

        ## CP Handling
        cpName = "ShowInterpolation"
        cpValue = color3

        ### OVERWRITING existing CP
        for instance in thisFont.instances:
            instance.customParameters[cpName] = cpValue

ColorWellWindow()

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
