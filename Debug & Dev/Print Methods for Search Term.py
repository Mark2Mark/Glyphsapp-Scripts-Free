#MenuTitle: Print Methods for Search Term ...
# -*- coding: utf-8 -*-
__doc__ = """
• Print Methods for Search Term
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


from vanilla import *

'''
Thanks @mekkablue for the script snippet:
https://forum.glyphsapp.com/t/some-sdk-related-questions/3473/5
'''

class dialog( object ):
	def __init__(self):
		L = 10
		objectOptions = [
		"GSFont",
		"GSFontMaster",
		"GSInstance",
		"GSCustomParameter",
		"GSGlyph",
		"GSLayer",
		"GSPath",
		"GSNode",
		"GSGlyphsInfo",
		"GSComponent",
		"GSEditViewController",
		"GSWindowController",
		"thisLayer.color()",
		"smartComp",
		"NSClassFromString(\"GlyphsFilterRoundCorner\")",
		"GSApplication",
		]
		self.w = Window((420, 100), "Methods for Term:")
		self.w.Text1 = TextBox((10, L, -L, 22), "for:")
		self.w.editText1 = EditText((50, L, -L, 22), placeholder="'tool' or 'path' or 'layer' or ...", callback=self.SavePreferences)
		self.w.Text2 = TextBox((L, 40, -L, 22), "in:")
		self.w.editText2 = ComboBox((50, 40, -L, 22), objectOptions, "GSWindowController", callback=self.SavePreferences)
		self.w.myButton = Button((L, 70, -L, 20), "Show me!", callback=self.buttonCallback)
		self.w.center()
		self.w.open()
		self.w.setDefaultButton( self.w.myButton )

		if not self.LoadPreferences():
			print "Could not load preferences. Will resort to defaults."

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.markfromberg.methodsearcher.editText1"] = self.w.editText1.get()
			Glyphs.defaults["com.markfromberg.methodsearcher.editText2"] = self.w.editText2.get()
		except:
			return False
			
		return True

	def LoadPreferences( self ):
		try:
			NSUserDefaults.standardUserDefaults().registerDefaults_(
				{
					"com.markfromberg.methodsearcher.editText1": "",
					"com.markfromberg.methodsearcher.editText2": "GSWindowController",
				}
			)
			self.w.editText1.set( Glyphs.defaults["com.markfromberg.methodsearcher.editText1"] )
			self.w.editText2.set( Glyphs.defaults["com.markfromberg.methodsearcher.editText2"] )

		except:
			return False
			
		return True


	def methods(self, term, thisObject):
		myObj = NSClassFromString( str(thisObject) )
		for x in dir(myObj):
			if term.lower() in x.lower():
				print x


	def buttonCallback(self, sender):
		Glyphs.clearLog()
		inputString = self.w.editText1.get()
		GSObject = self.w.editText2.get()
		print "----", GSObject
		print "__Methods for %s:\n" % inputString
		print self.methods(inputString, GSObject)
		Glyphs.showMacroWindow()
		self.w.close()

dialog()
