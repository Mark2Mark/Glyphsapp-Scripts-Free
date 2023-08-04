#MenuTitle: Convert Open Fonts To Instances And Save
# -*- coding: utf-8 -*-
__doc__="""
• Closes the base fonts after generating their instances.
• Takes care that the new file's master weight name matches the prior instance weight name.
• Do save your base fonts beforehand, Script will close them without asking.
• Saves the Instances as .glyphs files to your Desktop into a folder called 'TEMP_FONT_INSTANCES'
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

# Version 0.1

# from Foundation import *
import os
import traceback

# GetSaveFile()

OpenFonts = list(Glyphs.fonts) ### Do not iterate over Glyphs.fonts itself, otherwise the loop will be endless

try:
	for thisFont in OpenFonts:
		for instance in thisFont.instances:
			if instance.active:
				transferedWeightName = instance.weight
				newFont = thisFont.interpolateInstance_error_( instance, None )
				Glyphs.fonts.append( newFont )
				newFont.masters[0].weight = transferedWeightName ## New font will have one master anyway
		thisFont.close(True) # parameter: ignoreChanges True/False
except:
	print(traceback.format_exc())


filePath = '~/Desktop/TEMP_FONT_INSTANCES'
filePathRelative = os.path.expanduser(filePath) # Will expand ~ to being the users home directory if it is defined
if not os.path.exists(filePathRelative):
    os.makedirs(filePathRelative)

for newInstance in Glyphs.fonts:
	thisName = "%s - %s" % ( newInstance.familyName, newInstance.masters[0].name )
	thisPath = "%s/%s.glyphs" % (filePathRelative, thisName)
	print thisPath
	newInstance.save(thisPath)
	newInstance.close(True)

