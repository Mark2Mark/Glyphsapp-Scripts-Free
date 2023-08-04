# MenuTitle: Swap Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
• Swap 2 selected characters
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

Doc = Glyphs.currentDocument
Font = Glyphs.font
Selection = Font.selectedLayers

listOfGlyphNames = [x.parent.name for x in Selection]

if len(listOfGlyphNames) == 2:
    Selection[1].parent.name = "Temp"

    print(listOfGlyphNames)
    Selection[0].parent.name = listOfGlyphNames[1]
    Selection[1].parent.name = listOfGlyphNames[0]
else:
    # pass
    # from robofab.interface.all.dialogs import Message
    Message("Select only TWO glyphs", "", OKButton="OK")
