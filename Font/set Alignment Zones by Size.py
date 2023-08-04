# MenuTitle: Set Size for Alignment Zones
# -*- coding: utf-8 -*-
__doc__ = """
• Add ALignment Zones for all Masters according to input size (UI)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
Selection = Font.selectedLayers


class Window(object):
    def __init__(self):
        InputPosX = 90
        InputWidth = 50
        textHeight = 40
        self.w = vanilla.FloatingWindow((250, 45), "Set Alignment Zones")

        self.w.zonesText = vanilla.TextBox((10, 10, -10, textHeight), "AZ Size:")
        self.w.zonesValue = vanilla.EditText(
            (InputPosX, 10, InputWidth, 20), "15", sizeStyle="small"
        )
        self.w.make_button = vanilla.Button(
            (-80, 12, -15, 17), "Create", sizeStyle="small", callback=self.makeZones
        )

        self.w.setDefaultButton(self.w.make_button)
        self.w.open()
        self.w.makeKey()  ### Focus on window and Button

    def makeZones(self, sender):
        inputSize = int(self.w.zonesValue.get())
        self.w.close()

        ### the untouchable code:
        ### get the dimensions of the font
        for master in Font.masters:
            print(master)
            posA = master.ascender
            posC = master.capHeight
            posX = master.xHeight
            posB = 0
            posD = master.descender

            dimensions = [
                (posA, inputSize),
                (posC, inputSize),
                (posX, inputSize),
                (posB, -inputSize),
                (posD, -inputSize),
            ]

            print(dimensions)
            newZones = []
            for d in dimensions:
                pos, size = d
                a = GSAlignmentZone.alloc().init()
                a.setSize_(size)
                a.setPosition_(pos)
                newZones.append(a)

            master.setAlignmentZones_(newZones)
            # print( master.alignmentZones)


Font.disableUpdateInterface()
Window()
Font.enableUpdateInterface()
