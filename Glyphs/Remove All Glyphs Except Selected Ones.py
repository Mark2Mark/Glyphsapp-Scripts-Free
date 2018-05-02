#MenuTitle: Remove All Glyphs Except the Selected Ones
# -*- coding: utf-8 -*-
__doc__="""
• Usefull for Quick Test Fonts that need focus on just the selected Glyphs (e.g. accent handling)
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#	>> Mark Froemberg << aka `Mark2Mark` @ GitHub
#	>> www.markfromberg.com <<
#
#	_NOTES:
#		- 
#
#	_TODO:
#		- 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Font = Glyphs.font
selectedLayers = Font.selectedLayers

glyphsToKeep = []
for glyph in  selectedLayers:
	print glyph.parent
	glyphsToKeep.append(glyph.parent)
	
glyphsToRemove = []	
for g in Font.glyphs:
	if g not in glyphsToKeep:
		glyphsToRemove.append(g)

Font.removeGlyphs_(glyphsToRemove)
