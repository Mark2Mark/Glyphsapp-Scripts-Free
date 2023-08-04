# MenuTitle: Print Glyphs User Defaults
# -*- coding: utf-8 -*-
__doc__ = """
• Print Glyphs User Defaults & Examples for related objects
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# 	>> Mark Froemberg << aka `Mark2Mark` @ GitHub
# 	>> www.markfromberg.com <<
#
# 	_NOTES:
# 		-
#
# 	_TODO:
# 		-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Glyphs.clearLog()  # clear macro window log
Glyphs.showMacroWindow()


"""
see:
https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSUserDefaults_Class/#//apple_ref/occ/instm/NSUserDefaults/dictionaryRepresentation
"""
print(NSUserDefaults.standardUserDefaults().dictionaryRepresentation())


## Example: Bool for preview is black or white:
print()
print(NSUserDefaults.standardUserDefaults().boolForKey_("GSPreview_Black"))

"""
OFFICIAL SOLUTION:
Example
"""
print(Glyphs.defaults["TransformRotate"])
