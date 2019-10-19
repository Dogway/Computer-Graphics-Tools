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
    "name": "msm_from_object",
    "author": "Dogway",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Switches to object mode and changes mesh select mode",
    "category": "3D View"}

import bpy
from bpy_extras import view3d_utils

class MsmFromObject(bpy.types.Operator):
    """Switches to object mode and changes mesh select mode"""
    bl_idname = "object.msm_from_object"
    bl_label = "msm_from_object"
    bl_options = {'REGISTER', 'UNDO'}

    mode : bpy.props.StringProperty(
        name = "mode",
        default = "edge"
    )

    def execute(self, context):
        # get the context arguments
        scene = context.scene
        region = context.region
        rv3d = context.region_data
        coord = self.x, self.y
        scene = bpy.context.scene 
        viewlayer = bpy.context.view_layer

        # get the ray from the viewport and mouse
        view_vector = view3d_utils.region_2d_to_vector_3d(region, rv3d, coord)
        ray_origin = view3d_utils.region_2d_to_origin_3d(region, rv3d, coord)
        ray_target = ray_origin + (view_vector *-10)
        ray_goal = ray_origin + (view_vector *1000)

        rayresult = scene.ray_cast(viewlayer, ray_target, ray_goal)


        obj = rayresult[4]
        if obj is None:
            self.report({'WARNING'}, "Nothing is selected")
            return {'CANCELLED'}
        else
            if bpy.context.object.mode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = obj

            if bpy.context.object.mode == 'OBJECT':
                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

            if self.mode == 'vert':
                bpy.ops.mesh.select_mode(type="VERT")
            elif self.mode == 'edge':
                bpy.ops.mesh.select_mode(type="EDGE")
            elif self.mode == 'face':
                bpy.ops.mesh.select_mode(type="FACE")

            return {'FINISHED'}


    def invoke(self, context, event):
        if context.space_data.type == 'VIEW_3D':
            self.x = event.mouse_x
            self.y = event.mouse_y
            return self.execute(context)
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}


def register():
    bpy.utils.register_class(MsmFromObject)


def unregister():
    bpy.utils.register_class(MsmFromObject)



if __name__ == "__main__":
    register()
