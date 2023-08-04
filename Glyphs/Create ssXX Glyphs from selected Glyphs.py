# MenuTitle: Create empty .ssXX-Copies from selected Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
• Generate x copies of selected characters and add .ssXX
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
#       - Make new version that creates non-empty glyphs
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
Selection = Font.selectedLayers

listOfGlyphNames = [x.parent.name for x in Selection]


class Window(object):
    def __init__(self):
        self.w = vanilla.FloatingWindow((150, 45), ".ssXX")

        self.w.popUpButton = vanilla.PopUpButton(
            (10, 10, -90, 20), [str(i + 1) for i in range(20)]
        )
        self.w.make_button = vanilla.Button(
            (-80, 12, -15, 17), "Create", sizeStyle="small", callback=self.addSuffix
        )

        self.w.open()

    def buttonCheck(self, sender):
        myClassName = sender.get()
        # listOfGlyphNames # TODO: shouldn't that button do sth?

    def addSuffix(self, sender):
        # print listOfGlyphNames

        index = self.w.popUpButton.get()
        value = self.w.popUpButton.getItems()[index]

        amount = int(value)
        print(amount)

        suffix = ".ss"

        for i in range(amount):
            for letter in listOfGlyphNames:
                ### best version: add .zfill(2) after the suffx:
                glyph = letter + suffix + str(i + 1).zfill(2)
                print(glyph)

                newglyph = GSGlyph(glyph)
                newglyph.setLeftMetricsKey_(letter)
                newglyph.setRightMetricsKey_(letter)
                Font.addGlyph_(newglyph)

        self.w.close()


Window()
