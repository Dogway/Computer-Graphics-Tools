import bpy
from bpy.types import Menu

class VIEW3D_PIE_Select(Menu):
    bl_label = "Select Mode"
    bl_idname = "VIEW3D_PIE_Select"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

        pie.operator("object.msm_from_object", text = "Vertex", icon = 'VERTEXSEL').mode = 'vert'
        pie.operator("object.msm_from_object", text = "Edge", icon = 'EDGESEL').mode = 'edge'
        pie.operator("object.msm_from_object", text = "Face", icon = 'FACESEL').mode = 'face'
        pie.operator("object.mode_set", text = "Object", icon = "OBJECT_DATA")

def register():
    bpy.utils.register_class(VIEW3D_PIE_Select)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_Select)


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="VIEW3D_PIE_Select")
