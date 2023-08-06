# MenuTitle: Delete Kerning Groups for Selected Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
• Delete all Kerning Groups for the selected Glyphs
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

Font = Glyphs.font
selectedLayers = Font.selectedLayers
listOfGlyphNames = [thisLayer.parent.name for thisLayer in selectedLayers]

print("Removed kerning groups for:")
for layer in selectedLayers:
    glyph = layer.parent
    print(
        "%s\t\t\t[%s]\t\t\t%s"
        % (glyph.leftKerningGroup, glyph.name, glyph.rightKerningGroup)
    )
    glyph.setLeftKerningGroup_(None)
    glyph.setRightKerningGroup_(None)
