# MenuTitle: Color Label for Selection to All Open Fonts ...
# -*- coding: utf-8 -*-
__doc__ = """
• Same value for all Layers (!)
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

import GlyphsApp
import vanilla
import traceback

colors = [
    ["Red", 0],
    ["Orange", 1],
    ["Brown", 2],
    ["Yellow", 3],
    ["Light Green", 4],
    ["Dark Green", 5],
    ["Light Blue", 6],
    ["Dark Blue", 7],
    ["Purple", 8],
    ["Magenta", 9],
    ["Light gray", 10],
    ["Charcoal", 11],
    ["White", 9223372036854775807],
]


class Window(object):
    def __init__(self):
        self.w = vanilla.FloatingWindow((380, 45), "Set Color Label")

        self.w.editText = vanilla.PopUpButton(
            (10, 10, 100, 20), [c[0] for c in colors], sizeStyle="small"
        )
        self.w.make_button = vanilla.Button(
            (170, 12, -15, 17),
            "Set for all Fonts",
            sizeStyle="small",
            callback=self.setColor,
        )

        self.w.center()
        self.w.open()
        self.w.setDefaultButton(self.w.make_button)
        self.w.makeKey()  ### Focus on Window and Button

    def setColor(self, sender):
        try:
            sourceFont = Glyphs.fonts[0]
            sourceGlyphs = [g.parent.name for g in sourceFont.selectedLayers]

            userInput = self.w.editText.getTitle()
            for thisGlyph in sourceGlyphs:
                for targetFont in Glyphs.fonts:
                    for g in targetFont.glyphs:
                        if g.name == thisGlyph:
                            ### access colors list, and take only the first item (hack to avoid it being a list)
                            g.color = int(
                                [c[1] for c in colors if c[0] == str(userInput)][0]
                            )

        except:
            print(traceback.format_exc())

        self.w.close()


Window()
