#MenuTitle: Vertical Proportions as Ratio
# -*- coding: utf-8 -*-
__doc__="""
• Resize vertical Metrics according to Ratio (e.g. 5:10:4)
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
#		- Update AZ
#		- Include Cap Height
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GlyphsApp
import vanilla

font = Glyphs.font
Layer = font.selectedLayers[0]
masters = font.masters
upm = font.upm


class dialog(object):
	def __init__(self):
		InputPosX = 90
		InputWidth = 30
		textHeight = 40

		self.w = vanilla.FloatingWindow((250, 130), "Proportions as Ratio")

		# ascender
		self.w.ascenderText = vanilla.TextBox((10, 10, -10, textHeight), "ascender")
		self.w.ascenderValue = vanilla.EditText((InputPosX, 10, InputWidth, 20), "5.5", sizeStyle='small')

		# xHeight		
		self.w.xHeightText = vanilla.TextBox((10, 35, -10, textHeight), "xHeight")
		self.w.xHeightValue = vanilla.EditText((InputPosX, 35, InputWidth, 20), "10", sizeStyle='small')

		# descender
		self.w.descenderText = vanilla.TextBox((10, 60, -10, textHeight), "descender")
		self.w.descenderValue = vanilla.EditText((InputPosX, 60, InputWidth, 20), "5", sizeStyle='small')

		self.w.myTextBox1b = vanilla.TextBox((130, 10, 10, textHeight), unichr(int('23AB', 16)))
		# bracket extension
		self.w.myTextBox2 = vanilla.TextBox((130, 22, 10, textHeight), unichr(int('23AA', 16)))
		self.w.myTextBox3b = vanilla.TextBox((130, 35, 10, textHeight), unichr(int('23AC', 16)))
		# bracket extension
		self.w.myTextBox4 = vanilla.TextBox((130, 47, 10, textHeight), unichr(int('23AA', 16)))
		self.w.myTextBox5b = vanilla.TextBox((130, 60, 10, textHeight), unichr(int('23AD', 16)))
		self.w.myTextBox3c = vanilla.TextBox((150, 35, -10, textHeight), str(upm) + " upm")


		# Button
		self.w.myButton = vanilla.Button((10, 100, -10, 20), "Do it!", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.myButton )
		self.w.open()
		self.w.makeKey() ### Focus on window and Button

	def buttonCallback(self, sender):
		ascender = self.w.ascenderValue.get()
		xHeight = self.w.xHeightValue.get()
		descender = self.w.descenderValue.get()

		### function for calculating
		a = float(ascender)
		b = float(xHeight)
		c = float(descender)
		sumAll = a + b + c
		#print "sum:", sumAll
		a = round(a / sumAll * upm)
		b = round(b / sumAll * upm)
		c = round(c / sumAll * upm)

		total = a + b + c
		print "unrounded total upm:", total
		difference = total - upm
		roundedA = a - difference

		print "ascender:", roundedA, "above the xHeight"
		print "xHeight:", b
		print "descender:", -c

		for master in masters:
			master.ascender = roundedA + b
			master.xHeight = b
			master.descender = -c

		self.w.close()

dialog()
