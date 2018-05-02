#MenuTitle: Tab: Selected Glyphs Each on new line & Show All Glyphs
# -*- coding: utf-8 -*-
__doc__="""
• New Tab with each of the selected glyphs on a new line
• Show all Glyphs that are using this as component
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
#		- Avoid the NewLine(?)
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp

Doc = Glyphs.currentDocument
thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

lineBreak = "\n"
editString = ""
namesOfSelectedGlyphs = ["/" + l.parent.name for l in selectedLayers]


for GlyphName in namesOfSelectedGlyphs:
	### get the component use of this glyph:
	reusedGlyphs = []	
	for glyph in thisFont.glyphs:
		checkedLayer = glyph.layers[thisFont.selectedFontMaster.id]
		if len(checkedLayer.components) > 0:
			try:
				for component in checkedLayer.componentNames():
					if "/" + component == GlyphName:
						reusedGlyphs.append(glyph.name)
			except:
				pass

	# editString += ( GlyphName + lineBreak )
	if reusedGlyphs != []:
		reusedGlyphsAsString = "/"
		reusedGlyphsAsString += "/".join(reusedGlyphs)
	else:
		reusedGlyphsAsString = ""

	print "-----", editString
	editString += ( GlyphName + reusedGlyphsAsString + lineBreak )

print "output:", editString
thisFont.newTab(editString)
