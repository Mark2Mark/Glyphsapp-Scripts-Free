# MenuTitle: Tab: Glyph  For All Open Fonts ...
# -*- coding: utf-8 -*-
__doc__ = """
• New Tab in all open Fonts with the desired String
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# 	>> Mark Froemberg << aka `Mark2Mark` @ GitHub
# 	>> www.markfromberg.com <<
#
# 	_NOTES:
# 		-
#
# 	_TODO:
# 		-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from vanilla import *

fonts = Glyphs.fonts


class dialog(object):
    def __init__(self):
        self.w = Window((200, 70), "Tabs in all open Fonts")
        self.w.editText = EditText((10, 10, -10, 22), placeholder="/epsilon/parenleft")
        self.w.myButton = Button((10, 40, -10, 20), "Open Tabs", callback=self.output)
        self.w.center()
        self.w.open()
        self.w.makeKey()

    def output(self, sender):
        output = ""
        inputString = self.w.editText.get()
        outputList = [str(y) for y in inputString.split("/")]
        for glyphName in outputList:
            output += str(glyphName) + "/"

        print(output)
        for font in fonts:
            font.newTab("".join(x for x in output))
        self.w.close()


dialog()
