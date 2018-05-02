#MenuTitle: Report Anchors That Are Not on KeyHeights
# -*- coding: utf-8 -*-
__doc__ = """
• Ignores ogonek and center (Option in this script).
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

# Version 0.3

Glyphs.clearLog()
Glyphs.showMacroWindow()


#+++++++++++++++++++++++++++++++
#
exclude = ["ogonek", "center"]
#
#+++++++++++++++++++++++++++++++

Font = Glyphs.font
selection = Font.selectedLayers
thisMaster = Font.selectedFontMaster

allGlyphsToReport = []

for layer in selection:
	glyphName = layer.parent.name
	anchors = layer.anchors
	glyphWithReportedAnchors = []
	glyphWithReportedAnchors.append(glyphName)
	anchorsList = []
	metrics = list(layer.glyphMetrics())
	metrics.append(0)
	for anchor in anchors:
		if anchor.name not in exclude:
			if anchor.position.y not in metrics:
				try:
					anchorsList.append( u'{0:{5}} → {1:20} {3:5}      {4:40}'.format("", anchor.name, int(anchor.position.x), int(anchor.position.y), [int(y) for y in metrics][1:-3], 40) )
				except Exception, e:
				 	print e

	glyphWithReportedAnchors.append( anchorsList )
	allGlyphsToReport.append(glyphWithReportedAnchors)

for glyph in allGlyphsToReport:
 	if glyph[1]:
 		print "-"*100
 		print glyph[0]
 		for anch in glyph[1]:
 			print anch
