#MenuTitle: Report Missing Anchors
# -*- coding: utf-8 -*-
__doc__ = """
• Report all glyphs that have no anchors at all.
• Selected Master
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

Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font
selection = Font.selectedLayers
thisMaster = Font.selectedFontMaster

allGlyphsToReport = []

for layer in selection:
	glyphName = layer.parent.name
	anchors = layer.anchors
	if len(anchors) == 0:
		allGlyphsToReport.append(glyphName)

print "\n".join(allGlyphsToReport)