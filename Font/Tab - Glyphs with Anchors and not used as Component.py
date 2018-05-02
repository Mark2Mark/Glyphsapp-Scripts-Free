#MenuTitle: Tab: Glyphs with Anchors and not used as Component (and remove Anchors)
# -*- coding: utf-8 -*-
__doc__="""
• New Tab with all Glyphs that are have Anchors but are not used anywhere else as Components.
• Option to Remove the anchors alongside

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

#+++++++++++++++++++++++++++++
removeAnchors = False
#+++++++++++++++++++++++++++++

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers
thisFontMaster = thisFont.selectedFontMaster # active master


candidates = []
listOfAllComponents = []
allGlyphs = [glyph.name for glyph in thisFont.glyphs]

for glyph in thisFont.glyphs:
	thisLayer = glyph.layers[thisFont.selectedFontMaster.id]
	if len(thisLayer.components) > 0:
		for component in thisLayer.componentNames():
			listOfAllComponents.append(component)
	if len(thisLayer.paths) > 0:
		if len(thisLayer.components) == 0 and len(thisLayer.anchors) > 0:
			candidates.append(glyph.name)


glyphNamesNotUsedAsComponents = [x for x in candidates if x not in listOfAllComponents]

output = "/"
output += "/".join(glyphNamesNotUsedAsComponents)
thisFont.newTab(output) ### Open Tab with all Characters

for g in glyphNamesNotUsedAsComponents:
	glyphToRemoveAnchor = thisFont.glyphs[g]
	if removeAnchors:
		layer = glyphToRemoveAnchor.layers[thisFont.selectedFontMaster.id]
		layer.setAnchors_( None )

