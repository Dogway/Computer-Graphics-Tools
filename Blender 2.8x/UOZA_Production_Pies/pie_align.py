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
    "name": "UOZA - Align Pie",
    "author": "MACHIN3, Dogway",
    "version": (2, 2, 0),
    "blender": (2, 83, 4),
    "description": "Align Pie",
    "location": "View3D",
    "warning": "",
    "category": "3D View",
    "wiki_url": "https://blenderartists.org/t/uoza-productionpies-2-2-for-blender",
}

import bpy
from bpy.props import EnumProperty, BoolProperty
from bpy.types import Menu, Operator
from mathutils import Matrix, Vector, Euler

axis_items = [("X", "X", ""),
              ("Y", "Y", ""),
              ("Z", "Z", "")]

align_mode_items = [("VIEW", "View", ""),
                    ("AXES", "Axes", "")]

align_type_items = [("MIN", "Min", ""),
                    ("MAX", "Max", ""),
                    ("MINMAX", "Min/Max", ""),
                    ("ZERO", "Zero", ""),
                    ("AVERAGE", "Average", ""),
                    ("CURSOR", "Cursor", "")]

align_direction_items = [("LEFT", "Left", ""),
                         ("RIGHT", "Right", ""),
                         ("TOP", "Top", ""),
                         ("BOTTOM", "Bottom", ""),
                         ("HORIZONTAL", "Horizontal", ""),
                         ("VERTICAL", "Vertical", "")]

align_axis_mapping_dict = {"X": 0, "Y": 1, "Z": 2}

def get_loc_matrix(location):
    return Matrix.Translation(location)


def get_rot_matrix(rotation):
    return rotation.to_matrix().to_4x4()


def get_sca_matrix(scale):
    scale_mx = Matrix()
    for i in range(3):
        scale_mx[i][i] = scale[i]
    return scale_mx


def get_right_and_up_axes(context, mx):
    r3d = context.space_data.region_3d

    # get view right (and up) vectors in 3d space
    view_right = r3d.view_rotation @ Vector((1, 0, 0))
    view_up = r3d.view_rotation @ Vector((0, 1, 0))

    # get the right and up axes in the objects or world space, depending on the axis that was passed in
    axes_right = []
    axes_up = []

    for idx, axis in enumerate([Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((0, 0, 1))]):
        dot = view_right.dot(mx.to_3x3() @ axis)
        axes_right.append((dot, idx))

        dot = view_up.dot(mx.to_3x3() @ axis)
        axes_up.append((dot, idx))

    axis_right = max(axes_right, key=lambda x: abs(x[0]))
    axis_up = max(axes_up, key=lambda x: abs(x[0]))

    # determine flip
    flip_right = True if axis_right[0] < 0 else False
    flip_up = True if axis_up[0] < 0 else False

    return axis_right[1], axis_up[1], flip_right, flip_up


class UOZA_OT_align(bpy.types.Operator):
    bl_idname = "uoza.align"
    bl_label = "Uoza Object Align"
    bl_options = {'REGISTER', 'UNDO'}


    direction: EnumProperty(
        items=(("LEFT", "Left", ""),
            ("RIGHT", "Right", ""),
            ("TOP", "Top", ""),
            ("BOTTOM", "Bottom", ""),
               ),
        default='BOTTOM'
    )


    type: EnumProperty(name="Type", items=align_type_items, default="MINMAX")

    axis: EnumProperty(name="Axis", items=axis_items, default="X")
    direction: EnumProperty(name="Axis", items=align_direction_items, default="LEFT")

    local: BoolProperty(name="Local Space", default=True)


    @classmethod
    def poll(cls, context):
        return bpy.context.mode == "OBJECT" and bpy.context.selected_objects

    def execute(self, context):

        self.align(context, self.type, align_axis_mapping_dict[self.axis], self.direction, local=self.local)

        return {'FINISHED'}

    def align(self, context, type, axis, direction, local=True):
        active = context.active_object

        objs = bpy.context.selected_objects

        # calculate axis from viewport

        mx = active.matrix_world
        axis_right, axis_up, flip_right, flip_up = get_right_and_up_axes(context, mx=mx if local else Matrix())

        axis = axis_right if direction in ['RIGHT', 'LEFT'] else axis_up

        locax = []
        for obj in objs:
            oloc, orot, osca = obj.matrix_world.decompose()
            locax.append(oloc[axis])

        # get min or max target value

        if direction == 'RIGHT':
            target = min(locax) if flip_right else max(locax)

        elif direction == 'LEFT':
            target = max(locax) if flip_right else min(locax)

        elif direction == 'TOP':
            target = min(locax) if flip_up else max(locax)

        elif direction == 'BOTTOM':
            target = max(locax) if flip_up else min(locax)

        # re-combine components into world matrix

        for obj in objs:

            oloc, orot, osca = obj.matrix_world.decompose()

            locx = target if axis == 0 else oloc[0]
            locy = target if axis == 1 else oloc[1]
            locz = target if axis == 2 else oloc[2]
            loc = get_loc_matrix(Vector((locx, locy, locz)))

            orotx, oroty, orotz = orot.to_euler('XYZ')
            rot = get_rot_matrix(Euler((orotx, oroty,orotz), 'XYZ'))
            sca = get_sca_matrix(osca)

            obj.matrix_world = loc @ rot @ sca

class UOZA_MT_align_object_mode(Menu):
    bl_idname = "UOZA_MT_align_object_mode"
    bl_label = "Uoza Smart Align Pie"
    bl_context_mode = "OBJECT"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("uoza.align", text="LEFT", icon='TRIA_LEFT_BAR').direction = 'LEFT'
        #6 - RIGHT
        pie.operator("uoza.align", text="RIGHT", icon='TRIA_RIGHT_BAR').direction = 'RIGHT'
        #2 - BOTTOM
        pie.operator("uoza.align", text="BOTTOM", icon='TRIA_DOWN_BAR').direction = 'BOTTOM'
        #8 - TOP
        pie.operator("uoza.align", text="TOP", icon='TRIA_UP_BAR').direction = 'TOP'


classes = [
    UOZA_MT_align_object_mode,
    UOZA_OT_align,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
