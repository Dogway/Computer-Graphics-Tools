# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>


bl_info = {
    "name": "UOZA - Selection Pie",
    "author": "Dogway, Wazou",
    "version": (1, 0, 0),
    "blender": (2, 82, 0),
    "description": "Select Mode & Tools Pie Menu",
    "location": "3D View",
    "warning": "",
    "category": "3D View",
    "wiki_url": "https://blenderartists.org/t/uoza-production-pies-for-blender-2-8x"
}


import bpy
from bpy.types import (
        Menu,
        Operator,
        )
from bpy.props import EnumProperty


class UOZA_OT_select_tools(bpy.types.Operator):
    bl_idname = "uoza_selections.select_tools"
    bl_label = "Select tools"
    bl_options = {'REGISTER'}

    select_tools: EnumProperty(
        items=(('select_circle', "Select Circle", ""),
               ('select_box', "Select Box", ""),
               ('select', "Select", ""),
               ),
        default='select'
    )

    def execute(self, context):

        if self.select_tools == 'select_circle':
            bpy.ops.wm.tool_set_by_id(name="builtin.select_circle")

        elif self.select_tools == 'select_box':
            bpy.ops.wm.tool_set_by_id(name="builtin.select_box")

        elif self.select_tools == 'select':
            bpy.ops.wm.tool_set_by_id(name="builtin.select")

        return {'FINISHED'}


class UOZA_OT_view_selection(bpy.types.Operator):
    """
    CLICK - View Selected
    SHIFT - View All"""
    bl_idname = "uoza_pie_menus.view_selection"
    bl_label = "View Selection"
    bl_options = {'REGISTER'}

    def invoke(self, context, event):
        if event.shift:
            bpy.ops.view3d.view_all()
        else:
            bpy.ops.view3d.view_selected()

        return {'FINISHED'}


class UOZA_MT_selection_object_mode(Menu):
    bl_idname = "UOZA_MT_selection_object_mode"
    bl_label = "Uoza Selection Pie"
    bl_context_mode = "OBJECT"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("uoza_selections.select_tools", text="Select Circle", icon='ANTIALIASED').select_tools = 'select_circle'
        #6 - RIGHT
        pie.operator("uoza_selections.select_tools", text="Select Box", icon='STICKY_UVS_LOC').select_tools = 'select_box'
        #2 - BOTTOM
        pie.operator("object.select_all", text="Invert Selection", icon='ZOOM_PREVIOUS').action = 'INVERT'
        #8 - TOP
        pie.operator("uoza_selections.select_tools", text="Select", icon='RESTRICT_SELECT_OFF').select_tools = 'select'
        #7 - TOP - LEFT
        pie.operator("view3d.zoom_border", text="Box Zoom", icon='STICKY_UVS_LOC')
        #9 - TOP - RIGHT
        pie.operator("uoza_pie_menus.view_selection", text="Focus In/Out", icon='VIS_SEL_10')
        #1 - BOTTOM - LEFT
        pie.operator("uoza.isolate", text="Isolate", icon='CAMERA_DATA')
        #3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.operator("uoza.select_camera", text="Select Camera", icon='CAMERA_DATA')
        row = col.row(align=True)
        row.operator("object.select_by_type", text="Select By Type", icon='SNAP_VOLUME')
        row = col.row(align=True)
        row.operator("object.select_grouped", text="Select Grouped", icon='GROUP_VERTEX')
        row = col.row(align=True)
        row.operator("object.select_linked", text="Select Linked", icon='CONSTRAINT_BONE')
        row = col.row(align=True)
        row.operator("object.select_random", text="Select Random", icon='GROUP_VERTEX')


class UOZA_MT_selection_edit_mode(Menu):
    bl_idname = "UOZA_MT_selection_edit_mode"
    bl_label = "Uoza Selection Edit Pie"
    bl_context_mode = "EDIT_MESH"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        ob_type = ""
        for ob in bpy.context.selected_objects:
            ob_type = "curve" if ob.type == "CURVE" else "mesh"

        #4 - LEFT
        pie.operator("uoza_selections.select_tools", text="Select Circle", icon='ANTIALIASED').select_tools = 'select_circle'
        #6 - RIGHT
        pie.operator("uoza_selections.select_tools", text="Select Box", icon='STICKY_UVS_LOC').select_tools = 'select_box'
        #2 - BOTTOM
        print(ob_type)
        if ob_type is not "":
            pie.operator(ob_type + ".select_all", text="Invert Selection", icon='ZOOM_PREVIOUS').action = 'INVERT'
        else:
            pie.operator("view3d.noop", text="Invert Selection", icon='ZOOM_PREVIOUS')
        #8 - TOP
        pie.operator("uoza_selections.select_tools", text="Select", icon='RESTRICT_SELECT_OFF').select_tools = 'select'
        #7 - TOP - LEFT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.operator("mesh.loop_to_region", text="Select Loop Inner Region", icon='FACESEL')
        row = col.row(align=True)
        row.operator("mesh.region_to_loop", text="Select Boundary Loop", icon='MESH_PLANE')
        row = col.row(align=True)
        if ob_type is not "":
            row.operator(ob_type + ".select_nth", text="Select Checker", icon='PARTICLE_POINT')
        else:
            row.operator("view3d.noop", text="Select Checker", icon='PARTICLE_POINT')
        row = col.row(align=True)
        if ob_type is not "":
            row.operator(ob_type + ".select_similar", text="Select Similar", icon='PIVOT_INDIVIDUAL')
        else:
            row.operator("view3d.noop", text="Select Similar", icon='PIVOT_INDIVIDUAL')
        #9 - TOP - RIGHT
        pie.operator("uoza_pie_menus.view_selection", text="Focus In/Out", icon='VIS_SEL_10')
        #1 - BOTTOM - LEFT
        if hasattr(bpy.ops, "SmartSelectLoop"):
            pie.operator("mesh.smart_select_loop", text="Select Loop", icon='ZOOM_PREVIOUS')
        else:
            pie.operator("mesh.loop_multi_select", text="Select Loop", icon='ZOOM_PREVIOUS').ring = False
        #3 - BOTTOM - RIGHT
        if hasattr(bpy.ops, "SmartSelectRing"):
            pie.operator("mesh.smart_select_ring", text="Select Ring", icon='ZOOM_PREVIOUS')
        else:
            pie.operator("mesh.loop_multi_select", text="Select Ring", icon='ZOOM_PREVIOUS').ring = True


addon_keymaps = []


def register():
    bpy.utils.register_class(UOZA_OT_select_tools)
    bpy.utils.register_class(UOZA_OT_view_selection)
    bpy.utils.register_class(UOZA_MT_selection_object_mode)
    bpy.utils.register_class(UOZA_MT_selection_edit_mode)

    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:

        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'C', 'PRESS')
        kmi.properties.name = "UOZA_MT_selection_object_mode"
        addon_keymaps.append((km, kmi))

        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D', region_type='WINDOW')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'C', 'PRESS')
        kmi.properties.name = "UOZA_MT_selection_edit_mode"
        addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(UOZA_OT_select_tools)
    bpy.utils.unregister_class(UOZA_OT_view_selection)
    bpy.utils.unregister_class(UOZA_MT_selection_object_mode)
    bpy.utils.unregister_class(UOZA_MT_selection_edit_mode)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
