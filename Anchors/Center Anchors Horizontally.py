#MenuTitle: Center Anchors Horizontally
# -*- coding: utf-8 -*-
__doc__ = """
• Center Anchors horizontally for selected Glyphs (only current Layer)
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

import math

Font = Glyphs.font
selection = Font.selectedLayers


def angle(angle, xHeight, yPos):
	'''
	Italic Angle
	'''
	# rotation point is half of x-height
	offset = math.tan(math.radians(angle)) * xHeight / 2
	shift = math.tan(math.radians(angle)) * yPos - offset
	return shift


for l in selection:
	print l.anchors
	# print "__glyphMetrics(): ", l.glyphMetrics()
	charWidth = l.glyphMetrics()[0]
	thisMasterAngle = l.glyphMetrics()[5]
	thisMasterXHeight = l.glyphMetrics()[4]
	for anchor in l.anchors:
		anchor.x = charWidth / 2 + angle(thisMasterAngle, thisMasterXHeight, anchor.y)
