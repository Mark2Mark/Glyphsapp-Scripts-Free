#MenuTitle: Select all Glyphs That Are Not Used As Components
# -*- coding: utf-8 -*-
__doc__="""
• Selects all glyphs that are not reused as Components
• Slow with large Fonts, quicker if used with list filters.
• Option to only select glyphs without color label is in this script.
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Version 1.2
#
# GEORG VERSION: Improved to be quick as hell
#
# --> let me know if you have ideas for improving
# --> Mark Froemberg aka Mark2Mark @ GitHub
# --> www.markfromberg.com
#
# It seems to not work perfectly, check with Meta Science, preselect category 'Mark'
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp


#++++++++++++++++++++++++++++++
# O P T I O N
checkIfColorLabel = False ## True: Only selects the ones, that have NO color Label / False: select everything
#++++++++++++++++++++++++++++++

import time

start = time.time()


thisFont = Glyphs.font # frontmost font
# selectedLayers = thisFont.selectedLayers
thisFontMasterID = thisFont.selectedFontMaster.id # active master


listOfAllComponents = []
allGlyphs = [glyph.name for glyph in thisFont.glyphs]

for glyph in thisFont.glyphs:
	thisLayer = glyph.layers[thisFontMasterID]
	#print thisLayer.components
	#print thisLayer.componentNames()
	if len(thisLayer.components) > 0:
		#print thisLayer.parent.name, "--------"
		for component in thisLayer.componentNames():
			listOfAllComponents.append(component)

#print set(listOfAllComponents) ### drops duplicates

print "List of all Componetns ", time.time() - start
### ( 1 )
### OPTION to open a Tab with all the Glyphs:
### But cmd+T will open this same tab after making the selection anyway
# output = "/".join(glyphNamesNotUsedAsComponents)
# thisFont.newTab(output) ### Open Tab with all Characters

glyphNamesNotUsedAsComponents = [x for x in allGlyphs if x not in listOfAllComponents]


#print glyphNamesNotUsedAsComponents

print "glyphNamesNotUsedAsComponents ", time.time() - start

### ( 2 a )
### OPTION to select all the Glyphs:
thisDoc = Glyphs.currentDocument
thisController = thisDoc.windowController().glyphsController()
displayedGlyphs = thisController.arrangedObjects()
print "__displayedGlyphs", displayedGlyphs

'''
	https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSMutableIndexSet_Class/
'''
Selection = NSMutableIndexSet.alloc().init()
for i in range(len( displayedGlyphs )):
	thisGlyph = displayedGlyphs[i]
	if thisGlyph.name in glyphNamesNotUsedAsComponents:
		if checkIfColorLabel:
			if thisGlyph.color > 20:
				Selection.addIndex_(i)
		else:
			Selection.addIndex_(i)
thisController.setSelectionIndexes_(Selection)
print "glyphNamesNotUsedAsComponents ", time.time() - start
