'''
BEGIN GPL LICENSE BLOCK

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

END GPL LICENCE BLOCK
'''

bl_info = {
    'name': 'Apply Delta Transforms',
    'author': 'Dogway',
    'version': (0, 0, 1),
    'blender': (2, 80, 0)}

import bpy
import mathutils
from mathutils import  *

class ApplyDelta(bpy.types.Operator):
    bl_idname = "object.apply_all_delta"
    bl_label = "Apply Delta Transforms"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        ob = bpy.context.active_object

        loc = ob.location.copy()
        sca = ob.scale.copy()
        rot = ob.rotation_euler.copy()

        locd = ob.delta_location.copy()
        scad = ob.delta_scale.copy()
        rotd = ob.delta_rotation_euler.copy()

        bpy.ops.object.location_clear(clear_delta=True)
        bpy.ops.object.scale_clear(clear_delta=True)
        bpy.ops.object.rotation_clear(clear_delta=True)

        bpy.context.object.location = loc + locd
        bpy.context.object.scale = Vector(x * y for x, y in zip(sca, scad))
        # Probably need to run the cross product
        bpy.context.object.rotation_euler = Vector(x + y for x, y in zip(rot, rotd))

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ApplyDelta)


def unregister():
    bpy.utils.unregister_class(ApplyDelta)


if __name__ == "__main__":
    register()

