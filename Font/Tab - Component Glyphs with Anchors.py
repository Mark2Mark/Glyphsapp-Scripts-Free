#MenuTitle: Tab: Component Glyphs with Anchors
# -*- coding: utf-8 -*-
__doc__="""
• New Tab with all Glyphs that are only made of Components and have Anchors.
• Anchors are usually not needed in these Glyphs.
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

import GlyphsApp


thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers
thisFontMaster = thisFont.selectedFontMaster # active master


candidates = []

for glyph in thisFont.glyphs:
	thisLayer = glyph.layers[thisFont.selectedFontMaster.id]
	if len(thisLayer.paths) == 0:
		if len(thisLayer.components) > 0 and len(thisLayer.anchors) > 0:
			candidates.append(glyph.name)


output = "/"
output += "/".join(candidates)
thisFont.newTab(output) ### Open Tab with all Characters
