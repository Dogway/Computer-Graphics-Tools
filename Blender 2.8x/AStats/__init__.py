'''
Copyright (C) 2019
yuriy.andropov@live.com

Created by Yurii Andropov

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
	"name": "A* Statistics",
	"description": "Show Stats in Viewport",
	"author": "A*, Zuorion, Dogway",
	"version": (1, 0, 0),
	"blender": (2, 83, 3),
	"location": "View3D",
	"wiki_url": "https://youtu.be/6Ra_2eng3XE",
	"category": "3D View"
}

# For Selected Count, it heats CPU (10% load) and GPU, because the draw is running constantly (for Tris and Material)

import os.path
import bpy
import blf
import bmesh

StatsText = {
	"font_id": 0,
	"handler": None,
}

font_id = 0
objectName = ""
totalComponents = [0, 0, 0, 0]
totalSelected = [0, 0, 0, 0]
names = ["Verts : ", "Edges : ", "Faces : ", "Tris : ", "Subd : ", "Dim : "]
globalnames = ["Verts :", "Edges :", "Tris :", "Faces :", "Objects :", "Memory :", "Version :", "Engine :", "Subdivisions : ", "Dimensions : "]
globalValues = [0, 0, 0, 0]
globalStates = []


class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__
	#TODO Add UV Channel Name check, snapping state
	#Location properties
	sLocX: bpy.props.IntProperty(name="X", description="Relative X position", default=14, min=0, max=1000)
	sLocY: bpy.props.IntProperty(name="Y", description="Relative Y position", default=870, min=0, max=1000)
	gLocX: bpy.props.IntProperty(name="X", description="Global X position", default=880, min=0, max=1000)
	gLocY: bpy.props.IntProperty(name="Y", description="Global Y position", default=0, min=0, max=1000)
	shOffsetX: bpy.props.IntProperty(name="X", description="X shadow offset ", default=1, min=-1000, max=1000)
	shOffsetY: bpy.props.IntProperty(name="Y", description="Y shadow offset ", default=-1, min=-1000, max=1000)
	#sFontSize Properties
	sFontSize: bpy.props.IntProperty(name="Size", description="Font size", default=12)
	gFontSize: bpy.props.IntProperty(name="Size", description="Font size", default=12)
	mFontSize: bpy.props.IntProperty(name="Size", description="Font size", default=12)
	fFontSize: bpy.props.IntProperty(name="Size", description="Font size", default=12)
	#Color Properties
	gStatColor: bpy.props.FloatVectorProperty(name="Stats", description="Global Color", default=(1.0, 1.0, 1.0), subtype='COLOR')
	sStatColor: bpy.props.FloatVectorProperty(name="Stats", description="Selected Color", default=(1.0, 1.0, 1.0), subtype='COLOR')
	highlightColor: bpy.props.FloatVectorProperty(name="Highlight", description="Highlight color", default=(0.0, 1.0, 0.0), subtype='COLOR')
	shadowColor: bpy.props.FloatVectorProperty(name="Shadow", description="Shadow Color", default=(0.0, 0.0, 0.0), subtype='COLOR')
	matColor: bpy.props.FloatVectorProperty(name="Material", description="Material Color", default=(0.5, 0.5, 0.5), subtype='COLOR')
	nameColor: bpy.props.FloatVectorProperty(name="Filename", description="Filename Color", default=(1.0, 1.0, 1.0), subtype='COLOR')
	globalStatesColor: bpy.props.FloatVectorProperty(name="States", description="State Color", default=(0.5, 0.5, 0.5), subtype='COLOR')
	#Switches
	bDispGlobal: bpy.props.BoolProperty(name="On/Off", description="On/Off switch", default=True)
	bDrawGlobalVer: bpy.props.BoolProperty(name="Version", description="Switch for drawing Version", default=True)
	bDrawGlobalEng: bpy.props.BoolProperty(name="Engine", description="Switch for drawing Engine", default=True)
	bDrawGlobalMem: bpy.props.BoolProperty(name="Memory", description="Switch for drawing Memory", default=True)
	bDrawGlobalFlname: bpy.props.BoolProperty(name="Filename", description="Switch for drawing FileName", default=True)
	bDrawGlobalVerts: bpy.props.BoolProperty(name="Verts", description="Switch for calculating vertices", default=True)
	bDrawGlobalEdges: bpy.props.BoolProperty(name="Edges", description="Switch for calculating edges", default=True)
	bDrawGlobalFaces: bpy.props.BoolProperty(name="Faces", description="Switch for calculating faces", default=True)
	bDrawGlobalObjects: bpy.props.BoolProperty(name="Objects Number", description="Switch for calculating total objects", default=True)
	bDrawGlobalOrient: bpy.props.BoolProperty(name="Axis", description="Switch for calculating axis orientation", default=True)
	bDrawGlobalPivot: bpy.props.BoolProperty(name="Pivot", description="Switch for calculating pivot", default=True)
	bDispShadow: bpy.props.BoolProperty(name="On/Off", description="On/Off switch", default=True)
	bDispSelected: bpy.props.BoolProperty(name="On/Off", description="On/Off switch", default=True)
	bDispActive: bpy.props.BoolProperty(name="SelectionMode", description="Switch for showing stats based on selection type(ie only verts)", default=False)
	bShowMats: bpy.props.BoolProperty(name="Materials", description="Switch for showing names of selected materials", default=True)
	bNameGrouping: bpy.props.BoolProperty(name="Group Names", description="Switch for name grouping", default=True)
	bFontScaling: bpy.props.BoolProperty(name="Font Scaling", description="Switch for font scaling", default=False)
	bDrawFaces: bpy.props.BoolProperty(name="Faces", description="Switch for drawing faces", default=True)
	bDrawEdges: bpy.props.BoolProperty(name="Edges", description="Switch for drawing edges", default=True)
	bDrawVerts: bpy.props.BoolProperty(name="Verts", description="Switch for drawing verts", default=True)
	bDrawTris: bpy.props.BoolProperty(name="Tris", description="Switch for calculating triangles", default=True)
	bDrawSubd: bpy.props.BoolProperty(name="Subd", description="Switch for calculating Subdivision Level", default=True)
	bDrawDim: bpy.props.BoolProperty(name="Dim", description="Switch for calculating Object Dimensions", default=True)
	#Additional Properties
	groupNames: bpy.props.IntProperty(name="Group names after", description="When the number of of selected object is bigger than the value it will be replaced by Number of Objects", default=2)

	def draw(self, context):
		layout = self.layout
		#GlobalStats Box
		SelectedStatBox = layout.box()
		globalStatBox = layout.box()
		globalStatBox.label(text="Global Stats Options")
		GRow = globalStatBox.row(align=True)
		GRow.prop(self, "gFontSize")
		GRow.prop(self, "gLocX")
		GRow.prop(self, "gLocY")
		GRow.prop(self, "gStatColor")
		GRow.prop(self, "globalStatesColor")
		globalStatBox.label(text="Statistics for all visible objects")
		#SelectedStats Box
		SelectedStatBox.label(text="Selected Objects Stats Options")
		SRow = SelectedStatBox.row(align=True)
		#SRow.prop(self, "bDispSelected")
		SRow.prop(self, "sFontSize")
		SRow.prop(self, "sLocX")
		SRow.prop(self, "sLocY")
		SRow.prop(self, 'sStatColor')
		SRow.prop(self, "highlightColor")
		SelectedStatBox.label(text="Statistics for all selected objects")
		#Box for additional properties
		AddProp = layout.box()
		AddProp.label(text="Additional Options")
		NameRow = AddProp.row(align=True)
		NameRow.label(text="Filename Options")
		NameRow.prop(self, "fFontSize")
		NameRow.prop(self, "nameColor")
		MatRow = AddProp.row(align=True)
		MatRow.label(text="Material Options")
		MatRow.prop(self, "mFontSize")
		MatRow.prop(self, "matColor")
		MatRow.prop(self, "groupNames")
		ShadowRow = AddProp.row(align=True)
		ShadowRow.label(text="Shadow Options")
		ShadowRow.prop(self, "bDispShadow")
		ShadowRow.prop(self, "shOffsetX")
		ShadowRow.prop(self, "shOffsetY")
		ShadowRow.prop(self, "shadowColor")


class AStats_Switches(bpy.types.Panel):
	bl_label = "AStats"
	bl_idname = "VIEW3D_PT_Switches"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'WINDOW'

	def draw(self, context):
		layout = self.layout
		layout.ui_units_x = 6
		selectedBox = layout.box()
		globalBox = layout.box()
		globalBox.label(text="Global Stats")
		selectedBox.label(text="Selection Stats")
		addBox = layout.box()
		addBox.label(text="Extra Options")
		#global box
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDispGlobal', icon='FORCE_CHARGE')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalPivot')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalOrient')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalObjects')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalFaces')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalEdges')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalVerts')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalMem')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalFlname')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalVer')
		globalBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawGlobalEng')
		#selected box
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDispSelected', icon='FORCE_CHARGE')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bShowMats')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawFaces')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawEdges')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawVerts')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawTris')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawSubd')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDrawDim')
		selectedBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bDispActive', icon='LAYER_ACTIVE')
		#additional box
		addBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bNameGrouping')
		addBox.prop(bpy.context.preferences.addons[__name__].preferences, 'bFontScaling')


def getValue(name):
	return getattr(bpy.context.preferences.addons[__name__].preferences, name)


def addmenu_callback(self, context):
	self.layout.popover("VIEW3D_PT_Switches", icon='INFO', text='')


def setValue(name, value):
	return setattr(bpy.context.preferences.addons[__name__].preferences, name, value)


def remap(value, low1, high1, low2, high2):
	return low2 + (value - low1) * (high2 - low2) / (high1 - low1)


def relativeScale(size):
	if (getValue("bFontScaling")) == True:
		x = remap(size, 0, 1000, 0, bpy.context.area.width)
		y = remap(size, 0, 1000, 0, bpy.context.area.height)
		return int((x + y) / 2)
	else:
		return size


def add_draw(posX, posY, size, color, text):
	blf.position(font_id, posX, posY, 0)
	blf.size(font_id, size, 72)
	blf.color(font_id, color[0], color[1], color[2], 1)
	blf.draw(font_id, text)


def setDrawParams(fontName, xName, yName, shiftX, shiftY, colorName, text, width, height, side):

	active_tools_panel = bpy.context.area.regions[2]

	lWidth = active_tools_panel.width

	size = relativeScale(getValue(fontName))
	if side == "left":
		posX = getValue(xName) + lWidth + shiftX
	else:
		posX = getValue(xName) + lWidth + shiftX
	posY = height - getValue(yName) - shiftY
	add_draw(posX, posY, size, getValue(colorName), text)


def getGlobalStates():
	states = []
	#filename
	flnm = os.path.basename(bpy.data.filepath)
	if flnm: flnm = flnm.rstrip(".blend")
	else: flnm = ""
	states.append(flnm)
	#transform orientation
	states.append(bpy.context.scene.transform_orientation_slots[0].type)
	#get pivot
	states.append(bpy.context.tool_settings.transform_pivot_point)
	#snap target
	states.append(bpy.context.tool_settings.snap_target)
	#element snap to
	states.append(bpy.context.tool_settings.snap_elements)
	return states


def getTriCount(object):
	if getValue('bDispSelected') == True:
		tris = 0
		notSelected = []
		object.update_from_editmode()
		for poly in object.data.polygons:
			if poly.select:
				tris += 1 + (poly.loop_total - 3)
		return tris


def getDataFromSelectedObjects():
	if getValue('bDispSelected') == True:
		sum = [0, 0, 0, 0]
		for obj in bpy.context.selected_objects:
			if obj.type == "MESH":
				data = obj.data
				bm = bmesh.new()
				bm.from_mesh(obj.data)
				sum[3] += len(bm.calc_loop_triangles())
				bmesh.types.BMesh.free
				sum[2] += len(data.polygons)
				sum[1] += len(data.edges)
				sum[0] += len(data.vertices)
		return sum


def getSelectionStats():

	if getValue('bDispSelected') == True:
		tris = 0
		faces = 0
		edges = 0
		verts = 0
		subd = "0 / 0"
		dim = " 1.0 / 1.0 / 1.0"
		scene = bpy.context.scene
		bStat = scene.statistics(bpy.context.view_layer).split("|")
		modes = ["EDIT_LATTICE", "EDIT_CURVE", "EDIT_TEXT"]

		unit_settings = str(scene.unit_settings.length_unit)
		unit =  0.01    if unit_settings == "CENTIMETERS" else \
				0.0254  if unit_settings == "INCHES"      else \
				0.3048  if unit_settings == "FEET"        else \
				1.0     if unit_settings == "METERS"      else \
				1000.0  if unit_settings == "KILOMETERS"  else \
				1609.34 if unit_settings == "MILES"       else 0.001

		for modifier in bpy.context.active_object.modifiers:
			if modifier.type == "SUBSURF":
				mod = bpy.data.objects[str(bpy.context.active_object.name)].modifiers['Subdivision']
				subd = str(mod.levels) + " / " + str(mod.render_levels)

		dim = bpy.context.active_object.dimensions
		dim_scale = scene.unit_settings.scale_length
		dimXYZ = str(round(dim[0] / unit * dim_scale, 2))  + " / " +  str(round(dim[1] / unit * dim_scale, 2))  + " / " +  str(round(dim[2] / unit * dim_scale, 2))

		if bpy.context.mode in modes:
			verts = bStat[1].split(':')[1].split("/")[0]
		else:
			if bpy.context.scene.tool_settings.mesh_select_mode[0] == True:
				if bpy.context.mode == "EDIT_MESH":
					verts = bStat[1].split(':')[1].split("/")[0]
					edges = bStat[2].split(':')[1].split("/")[0]
					faces = bStat[3].split(':')[1].split("/")[0]
			if bpy.context.scene.tool_settings.mesh_select_mode[1] == True:
				if bpy.context.mode == "EDIT_MESH":
					verts = bStat[1].split(':')[1].split("/")[0]
					edges = bStat[2].split(':')[1].split("/")[0]
					faces = bStat[3].split(':')[1].split("/")[0]
			if bpy.context.scene.tool_settings.mesh_select_mode[2] == True:
				if bpy.context.mode == "EDIT_MESH":
					verts = bStat[1].split(':')[1].split("/")[0]
					edges = bStat[2].split(':')[1].split("/")[0]
					faces = bStat[3].split(':')[1].split("/")[0]
					if getValue('bDrawTris'):
						for obj in bpy.context.selected_objects:
							if obj.type == "MESH" and bpy.context.mode == "EDIT_MESH":
								tris += getTriCount(obj)
		return [verts, edges, faces, tris, subd, dimXYZ]


def getGlobalStats():

	bad_type = ["LATTICE", "CURVE", "FONT"]
	stats = [0, 0, 0, 0, 0, 0, 0, 0]
	stats[4] = len(bpy.context.visible_objects)

	engine = bpy.context.scene.render.engine
	if engine == 'BLENDER_EEVEE': stats[7] = "Eevee"
	elif engine == 'CYCLES': stats[7] = "Cycles"
	else: stats[7] = "Workbench"

	if bpy.context.mode == "OBJECT":
		bStat = bpy.context.scene.statistics(bpy.context.view_layer).split("|")
		stats[6] = bStat[7]
		stats[5] = bStat[6].split(':')[1].split("/")[0]
		stats[0] = bStat[2].split(":")[1]
		for object in bpy.context.visible_objects:
			if object.type == "MESH":
				stats[1] += len(object.data.edges)
		stats[2] = bStat[4].split(":")[1]
		stats[3] = bStat[3].split(":")[1]
	elif bpy.context.object.type in bad_type:
		for object in bpy.context.visible_objects:
			if object.type == "MESH":
				bStat = bpy.context.scene.statistics(bpy.context.view_layer).split("|")
				stats[6] = bStat[3]
				stats[5] = bStat[2].split(':')[1].split("/")[0]
				stats[0] = bStat[1].split(':')[1].split("/")[0]
	else:
		for object in bpy.context.visible_objects:
			if object.type == "MESH":
				bStat = bpy.context.scene.statistics(bpy.context.view_layer).split("|")
				stats[6] = bStat[6]
				stats[5] = bStat[5].split(':')[1].split("/")[0]
				stats[3] += len(object.data.polygons)
				stats[1] += len(object.data.edges)
				stats[0] += len(object.data.vertices)
	return stats


def getMaterialsFromSelection():
	if getValue('bDispSelected') == True:
		mats = []
		text = ''
		for obj in bpy.context.selected_objects:
			if obj.type == "MESH":
				obj.update_from_editmode()
				data = obj.data
				if bpy.context.mode == "EDIT_MESH":
					if len(data.materials) > 0:
						for polygon in data.polygons:
							material = data.materials[polygon.material_index]
							if polygon.select:
								if material != None:
									if material.name not in mats:
										mats.append(material.name)
				else:
					for material in data.materials:
						if material != None:
							mats.append(material.name)
		if len(mats) > getValue("groupNames") and getValue('bNameGrouping') == True:
			text = str(len(mats)) + " Materials"
		else:
			for index in range(0, len(mats)):
				if index == 0:
					text += str(mats[index])
				elif index == (len(mats)):
					text += ', ' + str(mats[index])
				else:
					text += ', ' + str(mats[index])
		return text


def displayShadow():
	blf.enable(font_id, blf.SHADOW)
	blf.shadow(font_id, 3, getValue('shadowColor')[0], getValue('shadowColor')[1], getValue('shadowColor')[2], 0.8)
	blf.shadow_offset(font_id, getValue('shOffsetX'), getValue('shOffsetY'))


def getObjectNames():
	text = ""
	if len(bpy.context.selected_objects) > getValue("groupNames") and getValue('bNameGrouping') == True:
		text = str(len(bpy.context.selected_objects)) + " Objects"
	else:
		for object in range(len(bpy.context.selected_objects)):
			if object > 0:
				text += ", " + bpy.context.selected_objects[object].name
			else:
				text += bpy.context.selected_objects[object].name
	return text


def draw_callback_px(self, context):

	act = bpy.context.active_object
	if act is not None:

		width = bpy.context.area.width
		height = bpy.context.area.height
		if getValue('bDispShadow') == True:
			displayShadow()

		#Draw global stats for visible objects
		if getValue('bDispGlobal') == True:
			globalStates = getGlobalStates()
			globalValues = getGlobalStats()
			shiftY = 0
			size = relativeScale(getValue('gFontSize'))
			if getValue('bDrawGlobalFlname'):
				saved = '*' if bpy.data.is_dirty else ''
				text = globalStates[0]
				shiftY = relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('fFontSize', 'gLocX', 'gLocY', 0, shiftY, 'nameColor', '[' + saved + text + ']' if text else text, width, height, 'left')
			if getValue('bDrawGlobalPivot'):
				text = globalStates[2]
				shiftY += relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'globalStatesColor', text, width, height, 'left')
			if getValue('bDrawGlobalOrient'):
				text = globalStates[1]
				shiftY += relativeScale(getValue('gFontSize')) * 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'globalStatesColor', text, width, height, 'left')
			if getValue('bDrawGlobalObjects'):
				shiftY += relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'gStatColor', globalnames[4], width, height, 'left')
				shiftX = len(globalnames[4]) * (relativeScale(getValue('gFontSize')) / 2)
				shiftX += relativeScale(getValue('gFontSize')) / 3.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftY, 'gStatColor', str(globalValues[4]), width, height, 'left')
			if getValue('bDrawGlobalFaces'):
				shiftY += relativeScale(getValue('gFontSize')) * 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'gStatColor', globalnames[3], width, height, 'left')
				shiftX = len(globalnames[3]) * (relativeScale(getValue('gFontSize')) / 2)
				shiftX += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftY, 'gStatColor', str(globalValues[3]), width, height, 'left')
			if getValue('bDrawGlobalEdges'):
				shiftY += relativeScale(getValue('gFontSize')) * 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'gStatColor', globalnames[1], width, height, 'left')
				shiftX = len(globalnames[1]) * (relativeScale(getValue('gFontSize')) / 2)
				shiftX += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftY, 'gStatColor', str(globalValues[1]), width, height, 'left')
			if getValue('bDrawGlobalVerts'):
				shiftY += relativeScale(getValue('gFontSize')) * 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'gStatColor', globalnames[0], width, height, 'left')
				shiftX = len(globalnames[0]) * (relativeScale(getValue('gFontSize')) / 2)
				shiftX += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftY, 'gStatColor', str(globalValues[0]), width, height, 'left')
			if getValue('bDrawGlobalMem'):
				shiftY += relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'gStatColor', globalnames[5], width, height, 'left')
				shiftX = len(globalnames[5]) * (relativeScale(getValue('gFontSize')) / 2)
				shiftX += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftY, 'gStatColor', str(globalValues[5]), width, height, 'left')
			if getValue('bDrawGlobalVer'):
				shiftY += relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftY, 'gStatColor', globalnames[6], width, height, 'left')
				shiftX = (len(globalnames[6])-1) * (relativeScale(getValue('gFontSize')) / 2)
				shiftX += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftY, 'gStatColor', str(globalValues[6]), width, height, 'left')
			if getValue('bDrawGlobalEng'):
				shiftYL = shiftY + relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftYL, 'gStatColor', globalnames[7], width, height, 'left')
				shiftXL = shiftX + (len(globalnames[7]) * (relativeScale(getValue('gFontSize')) / 2))
				shiftXL += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftYL, 'gStatColor', str(globalValues[7]), width, height, 'left')


		#Draw stats for selected objects
		if getValue('bDispSelected') == True:
			scene = bpy.context.scene
			totalComponents = getDataFromSelectedObjects()
			totalSelected = getSelectionStats()
			objectName = getObjectNames()
			shiftX_b = ((len(globalnames[4]) * 5) * (relativeScale(getValue('gFontSize')))) / 10

			shiftY = relativeScale(getValue('sFontSize')) * 2.0
			setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b, shiftY, 'sStatColor', str(objectName), width, height, 'left')

			rendered = 0
			for area in bpy.context.screen.areas:
				if area.type == 'VIEW_3D':
					for space in area.spaces:
						if space.type == 'VIEW_3D' and space.shading.type == 'RENDERED':
							rendered += 1
			if (getValue('bShowMats')) and (bpy.context.mode == "OBJECT" or not rendered):
				if getMaterialsFromSelection():
					shiftX_m = int(((len(objectName)) * (relativeScale(getValue('gFontSize')))) / 1.5)
					setDrawParams('mFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX_m, shiftY, 'matColor', "(" + getMaterialsFromSelection() + ")", width, height, 'left')
			#faces
			if (getValue('bDispActive') and scene.tool_settings.mesh_select_mode[2] and getValue('bDrawFaces')) or (not getValue('bDispActive') and getValue('bDrawFaces')):
				shiftY += relativeScale(getValue('sFontSize')) * 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b, shiftY, 'sStatColor', names[2], width, height, 'left')
				shiftX = len(names[0]) * (relativeScale(getValue('sFontSize')) / 2)
				if bpy.context.mode == "EDIT_MESH":
					if scene.tool_settings.mesh_select_mode[2]:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'highlightColor', str(totalSelected[2]), width, height, 'left')
						shiftX += len(str(totalSelected[2])) * (relativeScale(getValue('sFontSize')) / 1.5)
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', ' /', width, height, 'left')
					else:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalSelected[2]) + ' /', width, height, 'left')
						shiftX += len(str(totalSelected[2])) * (relativeScale(getValue('sFontSize')) / 1.5)
				shiftX += relativeScale(getValue('sFontSize')) / 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalComponents[2]), width, height, 'left')
			#edges
			if (getValue('bDispActive') and scene.tool_settings.mesh_select_mode[1] and getValue('bDrawEdges')) or (not getValue('bDispActive') and getValue('bDrawEdges')):
				shiftY += relativeScale(getValue('sFontSize')) * 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b, shiftY, 'sStatColor', names[1], width, height, 'left')
				shiftX = len(names[1]) * (relativeScale(getValue('sFontSize')) / 2)
				if bpy.context.mode == "EDIT_MESH":
					if scene.tool_settings.mesh_select_mode[1]:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'highlightColor', str(totalSelected[1]), width, height, 'left')
						shiftX += len(str(totalSelected[1])) * (relativeScale(getValue('sFontSize')) / 1.5)
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', ' /', width, height, 'left')
					else:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalSelected[1]) + ' /', width, height, 'left')
						shiftX += len(str(totalSelected[1])) * (relativeScale(getValue('sFontSize')) / 1.5)
				shiftX += relativeScale(getValue('sFontSize')) / 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalComponents[1]), width, height, 'left')
			#verts
			if (getValue('bDispActive') and scene.tool_settings.mesh_select_mode[0] and getValue('bDrawVerts')) or (not getValue('bDispActive') and getValue('bDrawVerts')):
				shiftY += relativeScale(getValue('sFontSize')) * 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b, shiftY, 'sStatColor', names[0], width, height, 'left')
				shiftX = len(names[0]) * (relativeScale(getValue('sFontSize')) / 2)
				if bpy.context.mode == "EDIT_MESH" or bpy.context.mode in ["EDIT_LATTICE", "EDIT_CURVE", "EDIT_TEXT"]:
					if scene.tool_settings.mesh_select_mode[0]:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'highlightColor', str(totalSelected[0]), width, height, 'left')
						shiftX += len(str(totalSelected[0])) * (relativeScale(getValue('sFontSize')) / 1.5)
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', ' /', width, height, 'left')
					else:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalSelected[0]) + ' /', width, height, 'left')
						shiftX += len(str(totalSelected[0])) * (relativeScale(getValue('sFontSize')) / 1.5)
				shiftX += relativeScale(getValue('sFontSize')) / 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalComponents[0]), width, height, 'left')
			#tris
			if ((getValue('bDispActive')) and scene.tool_settings.mesh_select_mode[2] and getValue('bDrawTris')) or (not getValue('bDispActive') and getValue('bDrawTris')):
				shiftY += relativeScale(getValue('sFontSize')) * 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b, shiftY, 'sStatColor', names[3], width, height, 'left')
				shiftX = len(names[0]) * (relativeScale(getValue('sFontSize')) / 2)
				if bpy.context.mode == "EDIT_MESH":
					if scene.tool_settings.mesh_select_mode[2]:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'highlightColor', str(totalSelected[3]), width, height, 'left')
						shiftX += len(str(totalSelected[3])) * (relativeScale(getValue('sFontSize')) / 1.5)
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', ' /', width, height, 'left')
					else:
						setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalSelected[3]) + ' /', width, height, 'left')
						shiftX += len(str(totalSelected[3])) * (relativeScale(getValue('sFontSize')) / 1.5)
				shiftX += relativeScale(getValue('sFontSize')) / 1.5
				setDrawParams('sFontSize', 'sLocX', 'sLocY', shiftX_b + shiftX, shiftY, 'sStatColor', str(totalComponents[3]), width, height, 'left')
			#subd
			if getValue('bDrawSubd'):
				shiftYL += relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftYL, 'gStatColor', "Subd : ", width, height, 'left')
				shiftXL += len(str(totalSelected[4])) * (relativeScale(getValue('gFontSize')) / 2)
				shiftXL += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftYL, 'gStatColor', str(totalSelected[4]), width, height, 'left')
			#dimensions
			if getValue('bDrawDim'):
				unit_settings = str(scene.unit_settings.length_unit)
				unit =  " (cm): " if unit_settings == "CENTIMETERS" else \
						" (in): " if unit_settings == "INCHES"      else \
						" (ft): " if unit_settings == "FEET"        else \
						" (m) : " if unit_settings == "METERS"      else \
						" (km): " if unit_settings == "KILOMETERS"  else \
						" (ml): " if unit_settings == "MILES"       else " (mm): "
				shiftYL += relativeScale(getValue('gFontSize')) * 2.0
				setDrawParams('gFontSize', 'gLocX', 'gLocY', 0, shiftYL, 'gStatColor', "Dim" + unit, width, height, 'left')
				shiftXL += len(str(totalSelected[5])) * (relativeScale(getValue('gFontSize')) / 2)
				shiftXL += relativeScale(getValue('gFontSize')) / 1.5
				setDrawParams('gFontSize', 'gLocX', 'gLocY', shiftX, shiftYL, 'gStatColor', str(totalSelected[5]), width, height, 'left')


def register():
	bpy.utils.register_class(AddonPreferences)
	bpy.utils.register_class(AStats_Switches)
	bpy.types.VIEW3D_HT_header.append(addmenu_callback)
	StatsText["handler"] = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, (None, None), 'WINDOW', 'POST_PIXEL')


def unregister():
	bpy.utils.unregister_class(AddonPreferences)
	bpy.utils.unregister_class(AStats_Switches)
	bpy.types.VIEW3D_HT_header.remove(addmenu_callback)
	bpy.types.SpaceView3D.draw_handler_remove(StatsText["handler"], 'WINDOW')
