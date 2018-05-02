#MenuTitle: Disable Automatic Alignment
# -*- coding: utf-8 -*-
__doc__="""
• Disables Automatic Alignment for first Component only.
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

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers
thisFontMaster = thisFont.selectedFontMaster # active master
masters = thisFont.masters
activeMasterIndex = masters.index(thisFontMaster)

try:
	for glyph in selectedLayers:
		# thisLayer = glyph.parent.layers[thisFont.selectedFontMaster.id]
		for layer in glyph.parent.layers:
			associatedMaster = layer.parent.layers[layer.associatedMasterId]
			try:
				# firstComponent = thisLayer.components[0]
				firstComponent = associatedMaster.components[0]
				firstComponent.setDisableAlignment_( True )
			except:
				print "No components in this layer."

except Exception, e:
	Message("Ooops", e, OKButton="OK")
