# MenuTitle: Select All Anchors
# -*- coding: utf-8 -*-
__doc__ = """
• Select All Anchors in current Glyph.
• Worsk with selection of multiple glyphs as well.
• Adds selection to existing selection.
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

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers

for layer in selectedLayers:
    ### select all anchors
    for anchor in layer.anchors:
        layer.addSelection_(anchor)

    ### select all components
    # for component in layer.components:
    # 	layer.addSelection_(component)

    ### select all paths
    # for path in layer.paths:
    # 	for node in path.nodes:
    # 		layer.addSelection_(node)
