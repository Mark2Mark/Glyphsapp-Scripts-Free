#MenuTitle: Tab: Selected Letters HH*HHOO*OO ...
# -*- coding: utf-8 -*-
__doc__="""
• New Tab with selected characters as placeholders between HH*HHOO*OO (UI)
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
#		- Redesign UI
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
listOfGlyphNames = [ thisLayer.parent.name for thisLayer in selectedLayers ]
print listOfGlyphNames
#Unicode = [ x.parent.unicode for x in Font.selectedLayers ]
#print Unicode

# add the slash to call the actual glyph:
ListJoined = "/" + "/ ".join(listOfGlyphNames).replace(' ', '')

class OpenTab(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((500, 100), "Open Tab:")
		self.w.myTextBox = vanilla.TextBox((10, 10, -10, 40), "Open Tab wit these guys:")
		self.w.editText = vanilla.EditText((10, 30, -100, 50), ListJoined  + "\n/H/H/Placeholder/H/H/O/O/Placeholder/O/O\n/n/n/Placeholder/n/n/o/o/Placeholder/o/o", sizeStyle='small', callback=self.editTextCallback)
		self.w.myButton = vanilla.Button((410, 30, -10, 20), "Do it!", sizeStyle='small', callback=self.buttonCallback) 
		self.w.setDefaultButton( self.w.myButton )
		self.w.open()

	def editTextCallback(self, sender):
		print("text entry:", sender.get())
		
	def buttonCallback(self, sender):
		characters = self.w.editText.get()
		print(characters)
		Glyphs.currentDocument.windowController().addTabWithString_( characters )
		self.w.close()
		
OpenTab()
