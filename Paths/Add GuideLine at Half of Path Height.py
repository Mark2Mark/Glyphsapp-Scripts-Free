#MenuTitle: Add GuideLine at Half of PathHeight
# -*- coding: utf-8 -*-
__doc__="""
• One GuideLine for each Path in selected Layer
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

import traceback


Glyphs.clearLog()
font = Glyphs.font
selLayer = font.selectedLayers[0]

try:
	for path in selLayer.paths:
		x, y, width, height = path.bounds[0].x, path.bounds[0].y, path.bounds[1].width, path.bounds[1].height
		# print x, y, width, height
		
		halfHeightOfBounds = height/2
		guidePositionY = y+halfHeightOfBounds
		# print guidePositionY

		guideLine = GSGuideLine()
		print guideLine
		guideLine.x = 50
		guideLine.y = guidePositionY
		guideLine.angle = 0
		selLayer.guideLines.append( guideLine )

except:
	print traceback.format_exc()