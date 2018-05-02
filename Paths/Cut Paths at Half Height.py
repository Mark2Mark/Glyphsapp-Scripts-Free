#MenuTitle: ✂ Cut Paths at Half Height
# -*- coding: utf-8 -*-
__doc__="""
• Cut all Paths in the selected Layer into half of its height.
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
#		- Make one script from both versions with Options: height/width
#		- Cannot nicely deal with overlapping paths, which is due to the fact
#		that the cutting function is a layer method, instead of a path method
#		But for the majority of cases this script is needed, this might not
#		be too much of an issue.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Glyphs.clearLog()
font = Glyphs.font
selLayer = font.selectedLayers[0]

listOfPathsToCut = []
if len(selLayer.paths) > 0:
	selLayer.beginChanges()
	for path in selLayer.paths:
		(x, y), (width, height) = path.bounds
		halfHeightOfBounds = height/2
		positionY = y + halfHeightOfBounds
		listOfPathsToCut.append( [positionY, x, width] )

	for value in listOfPathsToCut:
		selLayer.cutBetweenPoints((value[1], value[0]), (value[2]+value[1], value[0]))
	selLayer.endChanges()
else:
	pass
