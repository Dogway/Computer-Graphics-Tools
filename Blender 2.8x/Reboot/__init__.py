# Add-on information
bl_info = {
    "name": "Reboot",
    "author": "(saidenka) meta-androcto",
    "version": (0, 1),
    "blender": (2, 82, 0),
    "location": "File Menu",
    "description": "Reboot Blender without save",
    "warning": "",
    "wiki_url": "https://blenderartists.org/t/reboot-blender-addon/640465",
    "tracker_url": "",
    "category": "System"
}


import bpy
import os, sys
import subprocess


class BLENDER_OT_Restart(bpy.types.Operator):
    bl_idname = "wm.restart_blender"
    bl_label = "Reboot Blender"
    bl_description = "Blender Restart"
    bl_options = {'REGISTER'}

    def execute(self, context):
        py = os.path.join(os.path.dirname(__file__), "wm.console_toggle.py")
        filepath = bpy.data.filepath
        if (filepath != ""):
            subprocess.Popen([sys.argv[0], filepath, '-P', py])
        else:
            subprocess.Popen([sys.argv[0], '-P', py])
        bpy.ops.wm.quit_blender()

        return {'FINISHED'}


def menu_draw(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("wm.restart_blender", text="Restart", icon='PLUGIN')
    layout.separator()
    prefs = bpy.context.preferences
    view = prefs.view
    layout.prop(view, "use_save_prompt")


def register():
    bpy.utils.register_class(BLENDER_OT_Restart)
    bpy.types.TOPBAR_MT_file.append(menu_draw)


def unregister():
    bpy.utils.unregister_class(BLENDER_OT_Restart)
    bpy.types.TOPBAR_MT_file.remove(menu_draw)


if __name__ == "__main__":
    register()
