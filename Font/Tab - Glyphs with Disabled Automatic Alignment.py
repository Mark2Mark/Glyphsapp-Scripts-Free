#MenuTitle: Tab: Glyphs with Disabled Automatic Alignment
# -*- coding: utf-8 -*-
__doc__="""
• New Tab with all Glyphs that have Components and Automatic Alignemt is disabled for at least one of them.
• Searches for each master separately.
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

candidates = []
for glyph in thisFont.glyphs:
	thisLayer = glyph.layers[thisFont.selectedFontMaster.id]
	# print thisLayer
	if len(thisLayer.paths) == 0:
		if len(thisLayer.components) > 0:
			for component in thisLayer.components:
				# print component, component.disableAlignment
				if component.disableAlignment == True:
					print "___found: %s in %s" % ( component.componentName, glyph.name)
					candidates.append(glyph.name)

output = "/"
output += "/".join(candidates)
if len(candidates) > 0:
	thisFont.newTab(output) ### Open Tab with all Characters
else:
	Message("Nice! All Components are automatically aligned.", "", OKButton="Cool")
