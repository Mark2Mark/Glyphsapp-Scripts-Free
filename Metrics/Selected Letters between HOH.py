# MenuTitle: Tab: Selected Letters HH*HHOO*OO (Placeholders)
# -*- coding: utf-8 -*-
__doc__ = """
• New Tab with selected characters as placeholders between HH*HHOO*OO
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

import GlyphsApp

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

keyChars = "/H/O/H"

namesOfSelectedGlyphs = ["/" + l.parent.name for l in selectedLayers]
editString = ""

editString += keyChars
for GlyphName in namesOfSelectedGlyphs:
    editString += GlyphName + keyChars

print("output:", editString)
thisFont.newTab(editString)
