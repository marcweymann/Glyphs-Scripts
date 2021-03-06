#MenuTitle: Move acute, grave and hook to top_viet position in all layers
"""Where applicable, puts acute, grave, hookabove on 'top_viet' in all selected glyphs. Assumes that you have a 'top_viet' anchor in circumflex. Useful for Vietnamese glyphs."""

accents_to_be_moved = [ "acute", "grave", "hookabovecomb", "acute.case", "grave.case", "hookabovecomb.case", "acute.sc", "grave.sc", "hookabovecomb.sc" ]
new_anchor = "top_viet"

import GlyphsApp

Doc  = Glyphs.currentDocument
Font = Glyphs.font
selectedGlyphs = [ x.parent for x in Doc.selectedLayers() ]

def process( thisGlyph ):
	for thisMaster in Font.masters:
		
		print "__Master", thisMaster
		
		thisLayerID = thisMaster.id
		thisLayer = thisGlyph.layers[ thisLayerID ]
		
		for thisComponentIndex in range( len( thisLayer.components )):
			for accent_name in accents_to_be_moved:
				if thisLayer.components[ thisComponentIndex ].componentName == accent_name:
					try:
						thisLayer.components[ thisComponentIndex ].setAnchor_( new_anchor )
					except Exception, e:
						print e

Font.disableUpdateInterface()

for thisGlyph in selectedGlyphs:
	print "Processing", thisGlyph.name
	thisGlyph.undoManager().beginUndoGrouping()
	process( thisGlyph )
	thisGlyph.undoManager().endUndoGrouping()

Font.enableUpdateInterface()
