import bpy
from .pie_modes import *
from .operators import *
# from .pie_menus_operators.pie_views import *
from bpy.types import Menu
# from bpy.types import Menu, Header
# from .pie_snapping import WAZOU_SNAP_OT_elements





# # shading Menu
# class Shading(bpy.types.Menu):        
#     bl_label = " Shading"
#
#     def draw(self, context):
#         layout = self.layout
#         obj = context.object
#         view = context.space_data
#         # fx_settings = view.fx_settings
#
#
#         if bpy.context.object is not None:
#             mesh = context.active_object.data
#
#         # col = layout.column()
#         # if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
#         #     col.prop(fx_settings, "use_ssao", text="AO")
#         #     if fx_settings.use_ssao:
#         #         ssao_settings = fx_settings.ssao
#         #         subcol = col.column(align=True)
#         #         subcol.prop(ssao_settings, "color")
#         #         subcol.prop(ssao_settings, "samples")
#         #         subcol.prop(ssao_settings, "attenuation")
#         #         subcol.prop(ssao_settings, "distance_max")
#         #         subcol.prop(ssao_settings, "factor")
#
#         if view.viewport_shade == 'SOLID':
#             if view.use_matcap:
#                 layout.template_icon_view(view, "matcap_icon")
#             layout.prop(view, "use_matcap")
#
#         layout.separator()
#         layout.prop(obj, "draw_type", text="", icon='OUTLINER_OB_LATTICE')
#         layout.prop(obj, "show_transparent", text="Transparency")
#         layout.prop(obj.data, "show_double_sided")
#         layout.prop(view, "show_backface_culling")
#         layout.prop(view, "show_occlude_wire")
#         layout.prop(obj, "show_x_ray", text="X-Ray")
#
#         layout.separator()
#
#         layout.menu("WAZOU_MT_mesh_display_overlays", text="Mesh display", icon='OBJECT_DATAMODE')
#         layout.prop(obj.data, "show_normal_face", text="Show Normals")
#         if context.object.data.use_auto_smooth:
#             layout.prop(mesh, "auto_smooth_angle", text="Auto Smooth Angle")
#         layout.prop(obj.data, "use_auto_smooth")
#         layout.operator("shading.flat", icon='ALIASED')
#         layout.operator("shading.smooth", icon='ANTIALIASED')
#
#         layout.separator()
#
#         layout.prop(view, "lock_camera")
#         layout.operator("scene.togglegridaxis", text="Show/Hide Grid", icon="MESH_GRID")
#         layout.prop(view, "show_only_render")
#         layout.operator("wire.selectedall", text="Wire", icon='WIRE')
#
#
# def view3d_Shading_menu(self, context):
#     layout = self.layout
#     if context.object is not None:
#         layout.menu("Shading", icon='WIRE')
#
# def view3d_Search_menu(self, context):
#     layout = self.layout
#     layout.operator("wm.search_menu",text="Search", icon='VIEWZOOM')
#
# def view3d_Add_Primitives(self, context):
#     layout = self.layout
#     layout.menu("INFO_MT_add", text=" Primitives", icon='OBJECT_DATAMODE')
#
# def view3d_Add_Material(self, context):
#     layout = self.layout
#     if context.object is not None and bpy.context.object.mode == "OBJECT":
#         layout.operator("object.wpm_create_material", text="Add Material", icon='MATERIAL')

######################
#     Pie Menus      #
######################

########################################################################################################################
# PIE MODES - TAB
########################################################################################################################
class WAZOU_PIE_MENUS_MT_modes(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_modes"
    bl_label = "Wazou Select Modes"

    def draw(self, context):
        layout = self.layout
        toolsettings = context.tool_settings
        pie = layout.menu_pie()

        if context.object.type == 'MESH':
            # 4 - LEFT
            pie.operator("wazou_pie_menus.vertex", text="Vertex", icon='VERTEXSEL')
            # 6 - RIGHT
            pie.operator("wazou_pie_menus.face", text="Face", icon='FACESEL')
            # 2 - BOTTOM
            pie.operator("wazou_pie_menus.edge", text="Edge", icon='EDGESEL')
            # 8 - TOP
            pie.operator("wazou_pie_menus.object", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT

            pie.operator("wazou_pie_menus.xray", text="Xray", icon='XRAY')
            # shading = context.space_data.shading
            # pie.prop(shading, "show_xray", text="Xray", icon='XRAY')
            # 9 - TOP - RIGHT
            pie.operator("sculpt.sculptmode_toggle", text="Sculpt", icon='SCULPTMODE_HLT')
            # 1 - BOTTOM - LEFT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.scale_y = 1.5
            row.operator("wazou_pie_menus.texture_paint", text="Texture Paint", icon='TPAINT_HLT')
            row = col.row(align=True)
            row.scale_y = 1.5
            row.operator("wazou_pie_menus.vertex_paint", text="Vertex Paint", icon='VPAINT_HLT')
            row = col.row(align=True)
            row.scale_y = 1.5
            row.operator("wazou_pie_menus.weight_paint", text="Weight Paint", icon='WPAINT_HLT')
            # row = col.row(align=True)
            # row.scale_y = 1.5
            # row.operator("mode.pie_particle_edit", text="Particle Edit", icon='PARTICLEMODE')

            # 3 - BOTTOM - RIGHT
            # split = pie.split()
            # col = split.column(align=True)
            # row = col.row(align=True)
            # row.separator()
            # row = col.row(align=True)
            # row.separator()
            # row = col.row(align=True)
            # row.separator()
            # row = col.row(align=True)
            # row.separator()
            # row = col.row(align=True)
            pie.prop(toolsettings, "use_mesh_automerge", text="Auto Merge")
            # row = col.row(align=True)
            # row.operator("verts.faces", text="Vertex/Faces", icon='LOOPSEL')
            # row = col.row(align=True)
            # row.operator("verts.edges", text="Vertex/Edges", icon='VERTEXSEL')
            # row = col.row(align=True)
            # row.operator("verts.edgesfaces", text="Vertex/Edges/Faces", icon='OBJECT_DATAMODE')
            # row = col.row(align=True)
            # row.operator("edges.faces", text="Edges/Faces", icon='FACESEL')


        elif context.object.type == 'CURVE':
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()



        elif context.object.type == 'ARMATURE':
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.operator("object.posemode_toggle", text="Pose", icon='POSE_HLT')
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("object.editmode_toggle", text="Edit Mode", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()

        elif context.object.type == 'FONT':
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()


        elif context.object.type == 'SURFACE':
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()


        elif context.object.type == 'META':
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()


        elif context.object.type == 'LATTICE':
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()
        elif context.object.type == 'CAMERA':
            view = context.space_data
            cam = context.object.camera
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.operator("ui.eyedropper_depth", text="DOF Distance (Pick)", icon='EYEDROPPER')
            # 8 - TOP
            pie.prop(view, "lock_camera", text="Lock Camera To View", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.prop(view, "lock_cursor", text="Lock Camera To Cursor", icon='PIVOT_CURSOR')
            # 1 - BOTTOM - LEFT
            pie.prop(cam, "dof_object", text="Focus on Object", icon='FULLSCREEN_EXIT')
            # 3 - BOTTOM - RIGHT



        elif context.object.type == 'LIGHT':
            WM = bpy.context.window_manager
            # row.prop(WM, "material_alpha", text="Transparency")



            # pie.prop(context.object.data.energy, "Energy")

            # light = context.light

            # layout.row().prop(light, "type", expand=True)

            # layout.use_property_split = True

            # col = layout.column()
            # pie.prop(light, "color")
            # pie.prop(light, "energy")
            # pie.prop(light, "specular_factor", text="Specular")

            # 4 - LEFT
            # pie.operator("wazou_menu.lights", text="Light")
            # pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')
            # pie.separator()
            # 6 - RIGHT
            # pie.separator()
            # 2 - BOTTOM
            # pie.separator()
            # 8 - TOP
            # pie.prop("object.data.energy", text="Energy", icon='OUTLINER_OB_LIGHT')
            # 7 - TOP - LEFT bpy.context.object.data.size = 1.75977
            # pie.prop("object.data.size", text="Size", icon='FULLSCREEN_ENTER')
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()


########################################################################################################################
# PIE VIEWS - SPACE
########################################################################################################################
def cursor_Position(self, context, event, pos_x, pos_y):
    self.pos_x = event.mouse_x
    self.pos_y = event.mouse_y

    return(self.pos_x, self.pos_y)

class WAZOU_PIE_MENUS_MT_area_views(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_area_views"
    bl_label = "Wazou Change Views"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT


        pie.operator("view3d.view_persportho", text="Persp/Ortho", icon='VIEW_PERSPECTIVE')
        #6 - RIGHT
        pie.operator("view3d.localview", text="Local View", icon='OBJECT_DATAMODE')

        #2 - BOTTOM
        pie.operator_context = "INVOKE_DEFAULT"
        pie.operator("wazou_pie_menus.join_areas", text='Join Areas')


        #8 - TOP
        pie.operator("wazou_pie_menus.view_menu", text="3D View", icon= 'VIEW3D').ui_type_variable="VIEW_3D"

        #7 - TOP - LEFT
        pie.operator("wazou_pie_menus.view_menu", text="Shader Editor", icon='NODE_MATERIAL').ui_type_variable = "ShaderNodeTree"

        #9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.view_menu", text="Image Editor", icon='IMAGE').ui_type_variable = "VIEW"

        #1 - BOTTOM - LEFT
        w = context.region.width
        h = context.region.height
        dir = 'HORIZONTAL' if h > w else 'VERTICAL'
        layout.operator_context = "INVOKE_REGION_WIN"
        op = pie.operator("screen.area_split", text="Split Areas")
        op.direction = dir

        #3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)
        scale_x_y = 1.2
        row = col.row(align=True)
        row.scale_x = row.scale_y = scale_x_y
        row.operator("wazou_pie_menus.view_menu", text="", icon='OUTLINER').ui_type_variable = "OUTLINER"
        row.operator("wazou_pie_menus.view_menu", text="", icon='PROPERTIES').ui_type_variable = "PROPERTIES"
        row.operator("wazou_pie_menus.view_menu", text="", icon='PREFERENCES').ui_type_variable = "PREFERENCES"
        row.operator("wazou_pie_menus.view_menu", text="", icon='FILEBROWSER').ui_type_variable = "FILE_BROWSER"

        row = col.row(align=True)
        row.scale_x = row.scale_y = scale_x_y
        row.operator("wazou_pie_menus.view_menu", text="", icon='ACTION').ui_type_variable = "DOPESHEET"
        row.operator("wazou_pie_menus.view_menu", text="", icon='GRAPH').ui_type_variable = "FCURVES"
        row.operator("wazou_pie_menus.view_menu", text="", icon='NLA').ui_type_variable = "NLA_EDITOR"
        row.operator("wazou_pie_menus.view_menu", text="", icon='SEQUENCE').ui_type_variable = "SEQUENCE_EDITOR"
        # row.operator("object.view_menu", text="", icon='CLIP').ui_type_variable = "CLIP_EDITOR"


        row = col.row(align=True)
        row.scale_x = row.scale_y = scale_x_y
        row.operator("wazou_pie_menus.view_menu", text="", icon='TEXT').ui_type_variable = "TEXT_EDITOR"
        row.operator("wazou_pie_menus.view_menu", text="", icon='CONSOLE').ui_type_variable = "CONSOLE"
        row.operator("wazou_pie_menus.view_menu", text="", icon='INFO').ui_type_variable = "INFO"

        row = col.row(align=True)
        row.scale_x = row.scale_y = scale_x_y
        row.operator("screen.region_quadview", text="", icon='VIEW_ORTHO')
        row.operator("screen.screen_full_area", text="", icon='FULLSCREEN_ENTER')
        row.operator("screen.area_dupli", text="", icon='DUPLICATE')

########################################################################################################################
# PIE ACTIVE TOOLS - CTRL + SPACE
########################################################################################################################

class WAZOU_PIE_MENUS_MT_active_tools(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_active_tools"
    bl_label = "Wazou Active Tools"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("wazou_pie_menus.active_tools", text="Cursor", icon='PIVOT_CURSOR').active_tools = 'cursor'
        #6 - RIGHT
        pie.operator("wazou_pie_menus.active_tools", text="Select", icon='RESTRICT_SELECT_OFF').active_tools = 'select'
        #2 - BOTTOM
        pie.operator("wazou_pie_menus.active_tools", text="Rotate", icon='DRIVER_ROTATIONAL_DIFFERENCE').active_tools = 'rotate'
        #8 - TOP
        pie.operator("wazou_pie_menus.active_tools", text="Select Box", icon='STICKY_UVS_LOC').active_tools = 'select_box'
        #7 - TOP - LEFT
        pie.operator("wazou_pie_menus.active_tools", text="Select Circle", icon='ANTIALIASED').active_tools = 'select_circle'
        #9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.active_tools", text="Select Lasso", icon='TRACKING').active_tools = 'select_lasso'
        #1 - BOTTOM - LEFT
        pie.operator("wazou_pie_menus.active_tools", text="Move", icon='ORIENTATION_GLOBAL').active_tools = 'move'
        #3 - BOTTOM - RIGHT
        pie.operator("wazou_pie_menus.active_tools", text="Scale", icon='SNAP_FACE').active_tools = 'scale'


########################################################################################################################
# PIE SNAPPING - SHIFT + TAB
########################################################################################################################
# Pie Snapping - Shift + Tab
class WAZOU_PIE_MENUS_MT_snapping(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_snapping"
    bl_label = "Wazou Snapping"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("wazou_pie_menus.snap", text="Snap Vertex", icon='SNAP_VERTEX').snap_elements='vertex'
        # 6 - RIGHT
        pie.operator("wazou_pie_menus.snap", text="Snap Face", icon='SNAP_FACE').snap_elements = 'face'
        # # 2 - BOTTOM
        pie.operator("wazou_pie_menus.snap", text="Snap Edge", icon='SNAP_EDGE').snap_elements = 'edge'
        # # 8 - TOP
        pie.prop(context.tool_settings, "use_snap", text="Snap On/Off")
        # # 7 - TOP - LEFT
        pie.operator("wazou_pie_menus.snap", text="Snap Volume", icon='SNAP_VOLUME').snap_elements = 'volume'
        # # 9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.snap", text="Snap Increment", icon='SNAP_INCREMENT').snap_elements = 'increment'
        # 1 - BOTTOM - LEFT
        if bpy.context.scene.tool_settings.snap_elements != {'INCREMENT'}:
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.scale_x = 1.3
            row.scale_y = 1.2
            row.operator("wazou_pie_menus.snap", text="Active").snap_elements = 'active'
            row = col.row(align=True)
            row.scale_x = 1.3
            row.scale_y = 1.2
            row.operator("wazou_pie_menus.snap", text="Median").snap_elements = 'median'
            row = col.row(align=True)
            row.scale_x = 1.3
            row.scale_y = 1.2
            row.operator("wazou_pie_menus.snap", text="Center").snap_elements = 'center'
            row = col.row(align=True)
            row.scale_x = 1.3
            row.scale_y = 1.2
            row.operator("wazou_pie_menus.snap", text="Closest").snap_elements = 'closest'
        else:
            pie.separator()

        # 3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)

        if bpy.context.scene.tool_settings.snap_elements in [{'VERTEX'}, {'EDGE'}, {'FACE'}, {'VOLUME'}]:
            row.scale_y = 1.3
            row.prop(context.tool_settings, "use_snap_align_rotation", text="Align rotation", icon='SNAP_NORMAL')

        if bpy.context.scene.tool_settings.snap_elements == {'INCREMENT'}:
            row = col.row(align=True)
            row.scale_y = 1.3
            row.prop(context.tool_settings, "use_snap_grid_absolute", text="Absolute Grid Snap", icon='SNAP_GRID')


        elif bpy.context.scene.tool_settings.snap_elements == {'VOLUME'}:
            row = col.row(align=True)
            row.scale_y = 1.3
            row.prop(context.tool_settings, "use_snap_peel_object", text="Snap Peel Object", icon='SNAP_PEEL_OBJECT')


        elif bpy.context.scene.tool_settings.snap_elements == {'FACE'}:
            row = col.row(align=True)
            row.scale_y = 1.3
            row.prop(context.tool_settings, "use_snap_project", text="Snap Object", icon='PIVOT_CURSOR')

        else:
            row.separator()

########################################################################################################################
# PIE APPLY TRANSFOMS - CTRL + A
########################################################################################################################
# Pie Apply Transforms - Ctrl + A
class WAZOU_PIE_MENUS_MT_apply_clear_transforms(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_apply_clear_transforms"
    bl_label = "Wazou Apply Transforms"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("wazou_pie_menus.apply_clear_transforms", text="Clear All",
                     icon='EMPTY_AXIS').apply_clear = 'clear_all'
        #6 - RIGHT
        pie.operator("wazou_pie_menus.apply_clear_transforms", text="Apply Scale",
                     icon='FILE_TICK').apply_clear = 'apply_scale'
        #2 - BOTTOM
        pie.operator("wazou_pie_menus.apply_clear_transforms", text="Apply Rot/Sca",
                     icon='FILE_TICK').apply_clear = 'apply_rot_scale'
        #8 - TOP
        pie.operator("wazou_pie_menus.apply_clear_transforms", text="Apply Location",
                     icon='FILE_TICK').apply_clear = 'apply_location'
        #7 - TOP - LEFT
        pie.operator("wazou_pie_menus.apply_clear_transforms", text="Apply All",
                     icon='FILE_TICK').apply_clear = 'apply_all'
        #9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.apply_clear_transforms", text="Apply Rotation",
                     icon='FILE_TICK').apply_clear = 'apply_rotation'

        #1 - BOTTOM - LEFT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.apply_all_delta", text="Apply All Delta", icon='EMPTY_AXIS')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.location_clear", text="Clear Location", icon='EMPTY_AXIS')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.rotation_clear", text="Clear Rotation", icon='EMPTY_AXIS')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.scale_clear", text="Clear Scale", icon='EMPTY_AXIS')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.origin_clear", text="Clear Origin", icon='EMPTY_AXIS')

        #3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.convert", text="Apply Visual Geometry to Mesh", icon='FILE_TICK').target='MESH'
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.visual_transform_apply", text="Apply Visual Transforms", icon='FILE_TICK')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.duplicates_make_real", text="Make Duplicates Real", icon='USER')
########################################################################################################################
# PIE PIVOT/ORIGIN - SHIFT + S
########################################################################################################################
# Pie Origin/Pivot - Shift + S
class WAZOU_PIE_MENUS_MT_origin_pivot(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_origin_pivot"
    bl_label = "Wazou Origin Pivot"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("object.origin_set", text="Origin To 3D Cursor", icon='PIVOT_CURSOR').type = 'ORIGIN_CURSOR'
        # 6 - RIGHT
        pie.operator("view3d.snap_cursor_to_selected", text="Cursor to Selected", icon='PIVOT_CURSOR')
        # 2 - BOTTOM
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.snap_selected_to_grid", text="Sel to Grid", icon='RESTRICT_SELECT_OFF')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.snap_selected_to_cursor", text="Sel to Cursor (O)",icon='RESTRICT_SELECT_OFF').use_offset = True
        # 8 - TOP
        pie.operator("wazou_pie_menus.pivot_to_selection", text="Origin To Selection", icon='PIVOT_BOUNDBOX')
        # 7 - TOP - LEFT
        pie.operator("object.origin_set", text="Origin To Geometry", icon='PIVOT_BOUNDBOX').type = 'ORIGIN_GEOMETRY'
        # 9 - TOP - RIGHT
        pie.operator("view3d.snap_selected_to_cursor", text="Selection to Cursor", icon='RESTRICT_SELECT_OFF').use_offset = False
        # 1 - BOTTOM - LEFT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.origin_to_selected", text="O to Active", icon='PIVOT_BOUNDBOX')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("wazou_pie_menus.pivot_to_bottom", text="O to Bottom", icon='PIVOT_BOUNDBOX')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.origin_set", text="O to Center of Mass", icon='PIVOT_BOUNDBOX').type = 'ORIGIN_CENTER_OF_MASS'
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("object.origin_set", text="Geometry To O", icon='PIVOT_BOUNDBOX').type = 'GEOMETRY_ORIGIN'

        # 3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)

        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.snap_cursor_to_center", text="Cursor to Center", icon='PIVOT_CURSOR')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.snap_cursor_to_active", text="Cursor to Active", icon='PIVOT_CURSOR')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.snap_cursor_to_grid", text="Cursor to Grid", icon='PIVOT_CURSOR')

########################################################################################################################
# PIE ALIGN - ALT + X
########################################################################################################################
# Pie Align - Alt + X
class WAZOU_PIE_MENUS_MT_align(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_align"
    bl_label = "Wazou Align"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("wazou_pie_menus.align", text="Align X", icon='TRIA_LEFT').align_elements = 'x'
        #6 - RIGHT
        pie.operator("wazou_pie_menus.align", text="Align Z", icon='TRIA_DOWN').align_elements = 'z'
        #2 - BOTTOM
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_x = 0.8
        row.scale_y = 1.5
        row.operator("wazou_pie_menus.align", text="Align Y", icon='PLUS').align_elements = 'y'
        row = col.row()
        row.scale_y = 1
        cursor = context.scene.cursor
        row.column().prop(cursor, "location", text="Cursor Location")
        row = col.row()
        row.operator("wazou_pie_menus.cursor_rot_loc", text="Clear Loc").clear_cursor = 'loc'
        row = col.row()
        row.column().prop(cursor, "rotation_euler", text="Cursor Rotation")
        row = col.row()
        row.operator("wazou_pie_menus.cursor_rot_loc", text="Clear Rot").clear_cursor = 'rot'
        row = col.row()
        row.operator("wazou_pie_menus.cursor_rot_loc", text="Clear Cursor").clear_cursor = 'loc_rot'
        # row.prop(cursor, "location", text="Location")
        # row = col.row(align=True)
        # rotation_mode = cursor.rotation_mode
        # if rotation_mode == 'QUATERNION':
        #     row.prop(cursor, "rotation_quaternion", text="Rotation")
        # elif rotation_mode == 'AXIS_ANGLE':
        #     row.prop(cursor, "rotation_axis_angle", text="Rotation")
        # else:
        #     row.prop(cursor, "rotation_euler", text="Rotation")
        #
        # row = col.row(align=True)
        # row.prop(cursor, "rotation_mode", text="")

        #8 - TOP
        pie.operator("wazou_pie_menus.align", text="Align To Y-0").align_elements = 'to_y_0'
        #7 - TOP - LEFT
        pie.operator("wazou_pie_menus.align", text="Align To X-0").align_elements = 'to_x_0'
        #9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.align", text="Align To Z-0").align_elements = 'to_z_0'
        #1 - BOTTOM - LEFT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row = col.row(align=True)
        row.separator()
        row.label(text="ALIGN CENTER")
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("wazou_pie_menus.align", text="Align:   -X").align_elements = 'center_x_left'
        row.operator("wazou_pie_menus.align", text="+X").align_elements = 'center_x_right'
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("wazou_pie_menus.align", text="Align:   -Y").align_elements = 'center_y_front'
        row.operator("wazou_pie_menus.align", text="+Y").align_elements = 'center_y_back'
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("wazou_pie_menus.align", text="Align:   -Z").align_elements = 'center_z_top'
        row.operator("wazou_pie_menus.align", text="+Z").align_elements = 'center_z_bottom'



        # pie.separator()
        #3 - BOTTOM - RIGHT
        # pie.separator()

        if context.object.mode == 'OBJECT':
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row.label(text="ALIGN ACTIVE")
            row = col.row(align=True)
            row.scale_y = 1.3
            row.operator("wazou_pie_menus.align", text="Align: X").align_elements = 'active_x'
            row = col.row(align=True)
            row.scale_y = 1.3
            row.operator("wazou_pie_menus.align", text="Align: Y").align_elements = 'active_y'
            row = col.row(align=True)
            row.scale_y = 1.3
            row.operator("wazou_pie_menus.align", text="Align: Z").align_elements = 'active_z'
        else:
            pie.separator()


########################################################################################################################
# PIE DELETE - X
########################################################################################################################
class WAZOU_PIE_MENUS_MT_delete(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_delete"
    bl_label = "Wazou Delete"

    # @classmethod
    # def poll(cls, context):
    #     return context.object is not None and context.object.mode == "EDIT"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        #4 - LEFT
        pie.operator("mesh.delete", text="Delete Vertices", icon='VERTEXSEL').type='VERT'
        #6 - RIGHT
        pie.operator("mesh.delete", text="Delete Faces", icon='FACESEL').type='FACE'
        #2 - BOTTOM
        pie.operator("mesh.delete", text="Delete Edges", icon='EDGESEL').type='EDGE'
        #8 - TOP
        pie.operator("mesh.dissolve_edges", text="Dissolve Edges", icon='SNAP_EDGE')
        #7 - TOP - LEFT
        pie.operator("mesh.dissolve_verts", text="Dissolve Vertices", icon='SNAP_VERTEX')
        #9 - TOP - RIGHT
        pie.operator("mesh.dissolve_faces", text="Dissolve Faces", icon='SNAP_FACE')
        #1 - BOTTOM - LEFT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("wazou_pie_menus.limited_dissolve", text="Limited Dissolve", icon= 'STICKY_UVS_LOC')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.delete_edgeloop", text="Delete Edge Loops", icon='EDGESEL')
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.edge_collapse", text="Edge Collapse", icon='UV_EDGESEL')
        #3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.delete", text="Only Edge & Faces", icon='SNAP_FACE').type='EDGE_FACE'
        row = col.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.delete", text="Only Faces", icon='FACESEL').type='ONLY_FACE'


########################################################################################################################
# PIE SELECTION - A
########################################################################################################################
# Pie Selection Object Mode - A
class WAZOU_PIE_MENUS_MT_selection_object_mode(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_selection_object_mode"
    bl_label = "Pie Selections Mode"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.separator()
        #6 - RIGHT
        pie.separator()
        #2 - BOTTOM
        pie.operator("object.select_all", text="Invert Selection", icon='ZOOM_PREVIOUS').action='INVERT'
        #8 - TOP
        pie.operator("wazou_pie_menus.mesh_selection", text="Select/Deselect", icon='RESTRICT_SELECT_OFF')
        #7 - TOP - LEFT
        pie.operator("wazou_pie_menus.view_selection", text="View Selected/All", icon='VIS_SEL_10')
        #9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.local_view", text="View Global/Local", icon='CAMERA_DATA')
        #1 - BOTTOM - LEFT
        pie.operator("wazou_pie_menus.select_hierarchy", text="Select hierachy", icon='CON_CHILDOF')
        #3 - BOTTOM - RIGHT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.operator("object.select_by_type", text="Select By Type", icon='SNAP_VOLUME')
        row = col.row(align=True)
        row.operator("object.select_grouped", text="Select Grouped", icon='GROUP_VERTEX')
        row = col.row(align=True)
        row.operator("object.select_linked", text="Select Linked", icon='CONSTRAINT_BONE')
        row = col.row(align=True)
        row.operator("object.select_random", text="Select Random", icon='GROUP_VERTEX')
        row = col.row(align=True)
        row.operator("object.select_by_layer", text="Select By Layer", icon='GROUP_VERTEX')

# Pie Selection Edit Mode
class WAZOU_PIE_MENUS_MT_selection_edit_mode(Menu):
    bl_idname = "WAZOU_PIE_MENUS_MT_selection_edit_mode"
    bl_label = "Pie Selections Edit Mode"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        pie.separator()
        #6 - RIGHT
        pie.separator()
        #2 - BOTTOM
        pie.operator("mesh.select_all", text="Invert Selection", icon='ZOOM_PREVIOUS').action='INVERT'
        #8 - TOP
        pie.operator("wazou_pie_menus.mesh_selection", text="Select/Deselect", icon='RESTRICT_SELECT_OFF')
        #7 - TOP - LEFT
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.operator("wazou_pie_menus.select_loop_inner_region", text="Select Loop Inner Region", icon='FACESEL')
        row = col.row(align=True)
        row.operator("mesh.region_to_loop", text="Select Boundary Loop", icon='MESH_PLANE')
        row = col.row(align=True)
        row.operator("mesh.select_nth", text="Checker Select", icon='PARTICLE_POINT')
        row = col.row(align=True)
        row.operator("mesh.select_similar", text="Select Similar", icon='PIVOT_INDIVIDUAL')
        #9 - TOP - RIGHT
        pie.operator("wazou_pie_menus.select_all_by_selection", text="Complete Select", icon='STICKY_UVS_LOC')
        #1 - BOTTOM - LEFT
        pie.operator("mesh.loop_multi_select", text="Select Ring", icon='ZOOM_PREVIOUS').ring=True
        #3 - BOTTOM - RIGHT
        pie.operator("mesh.loop_multi_select", text="Select Loop", icon='ZOOM_PREVIOUS').ring=False

#Pie View Animation Etc - Space
# class WAZOU_PIE_MENUS_MT_animation_etc(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_animation_etc"
#     bl_label = "Animation Etc"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         #4 - LEFT
#         pie.operator("object.view_menu", text="Timeline", icon= 'TIME').ui_type_variable="TIMELINE"
#         #6 - RIGHT
#         pie.operator("object.view_menu", text="Dope Sheet", icon= 'ACTION').ui_type_variable="DOPESHEET_EDITOR"
#         #2 - BOTTOM
#         pie.operator("object.view_menu", text="NLA Editor", icon= 'NLA').ui_type_variable="NLA_EDITOR"
#         #8 - TOP
#         pie.operator("object.view_menu", text="Graph Editor", icon= 'IPO').ui_type_variable="GRAPH_EDITOR"
#         #7 - TOP - LEFT
#         pie.operator("object.view_menu", text="Movie Clip Editor", icon= 'RENDER_ANIMATION').ui_type_variable="CLIP_EDITOR"
#         #9 - TOP - RIGHT
#         pie.operator("object.view_menu", text="Sequence Editor", icon= 'SEQUENCE').ui_type_variable="SEQUENCE_EDITOR"
#         #1 - BOTTOM - LEFT
#         pie.operator("object.view_menu", text="Logic Editor", icon= 'LOGIC').ui_type_variable="LOGIC_EDITOR"
#         #3 - BOTTOM - RIGHT

#Pie View File Properties Etc - Space
# class WAZOU_PIE_MENUS_MT_file_properties_etc(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_file_properties_etc"
#     bl_label = "Pie File Properties..."
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         #4 - LEFT
#         pie.operator("object.view_menu", text="Properties", icon= 'BUTS').ui_type_variable="PROPERTIES"
#         #6 - RIGHT
#         pie.operator("object.view_menu", text="Outliner", icon= 'OOPS').ui_type_variable="OUTLINER"
#         #2 - BOTTOM
#         pie.operator("object.view_menu", text="User Preferences", icon= 'PREFERENCES').ui_type_variable="USER_PREFERENCES"
#         #8 - TOP
#         pie.operator("object.view_menu", text="Text Editor", icon= 'FILE_TEXT').ui_type_variable="TEXT_EDITOR"
#         #7 - TOP - LEFT
#         pie.operator("object.view_menu", text="File Browser", icon= 'FILESEL').ui_type_variable="FILE_BROWSER"
#         #1 - BOTTOM - LEFT
#         pie.operator("object.view_menu", text="Python Console", icon= 'CONSOLE').ui_type_variable="CONSOLE"
#         #9 - TOP - RIGHT
#         pie.operator("object.view_menu", text="Info", icon= 'INFO').ui_type_variable="INFO"
#         #3 - BOTTOM - RIGHT
#
# ########################################################################################################################
# # PIE SHADING - Z
# ########################################################################################################################
# class PieShadingView(Menu):
#     bl_idname = "pie.shadingview"
#     bl_label = "Pie Shading"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("object.shadingvariable", text="Material", icon='MATERIAL').variable = 'MATERIAL'
#         # 6 - RIGHT
#         pie.operator("object.shadingvariable", text="Wireframe", icon='WIRE').variable = 'WIREFRAME'
#         # 2 - BOTTOM
#         pie.operator("object.material_list_menu", icon='MATERIAL_DATA')
#
#         # 8 - TOP
#         pie.operator("object.shadingvariable", text="Solid", icon='SOLID').variable = 'SOLID'
#         # 7 - TOP - LEFT
#         pie.operator("object.shadingvariable", text="Texture", icon='TEXTURE_SHADED').variable = 'TEXTURED'
#         # 9 - TOP - RIGHT
#         pie.operator("object.shadingvariable", text="Render", icon='SMOOTH').variable = 'RENDERED'
#         # 1 - BOTTOM - LEFT
#         pie.operator("shading.smooth", text="Shade Smooth", icon='SOLID')
#         # 3 - BOTTOM - RIGHT
#         pie.operator("shading.flat", text="Shade Flat", icon='MESH_ICOSPHERE')
#
# ########################################################################################################################
# # PIE SHADING 2 SHIFT - Z
# ########################################################################################################################
# # Pie Object Shading- Shift + Z
# class PieObjectShading(Menu):
#     bl_idname = "pie.objectshading"
#     bl_label = "Pie Shading Object"
#
#     @classmethod
#     def poll(cls, context):
#         view = context.space_data
#         return (view)
#
#     def draw(self, context):
#
#         layout = self.layout
#
#         toolsettings = context.tool_settings
#
#         obj = context.object
#         view = context.space_data
#         fx_settings = view.fx_settings
#
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("scene.togglegridaxis", text="Show/Hide Grid", icon="MESH_GRID")
#         # 6 - RIGHT
#         pie.operator("wire.selectedall", text="Wire", icon='WIRE')
#         # 2 - BOTTOM
#         box = pie.split().column()
#         row = box.row(align=True)
#
#         if view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
#             row = box.row(align=True)
#             row.prop(fx_settings, "use_dof")
#             row = box.row(align=True)
#             row.prop(fx_settings, "use_ssao", text="AO")
#             if fx_settings.use_ssao:
#                 ssao_settings = fx_settings.ssao
#                 row = box.row(align=True)
#                 row.prop(ssao_settings, "factor")
#                 row = box.row(align=True)
#                 row.prop(ssao_settings, "distance_max")
#                 row = box.row(align=True)
#                 row.prop(ssao_settings, "attenuation")
#                 row = box.row(align=True)
#                 row.prop(ssao_settings, "samples")
#                 row = box.row(align=True)
#                 row.prop(ssao_settings, "color")
#         # 8 - TOP
#         if len([obj for obj in context.selected_objects if context.object is not None if
#                 obj.type in ['MESH', 'CURVE']]):
#             box = pie.split().column()
#             row = box.row(align=True)
#             row.prop(obj, "show_x_ray", text="X-Ray")
#             row = box.row(align=True)
#             row.prop(view, "show_occlude_wire", text="Hidden Wire")
#             row = box.row(align=True)
#             row.prop(view, "show_backface_culling", text="Backface Culling")
#         else:
#             pie.separator()
#
#         # 7 - TOP - LEFT
#         if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH']):
#             mesh = context.active_object.data
#             box = pie.split().column()
#             row = box.row(align=True)
#             row.prop(mesh, "show_normal_face", text="Show Normals Faces", icon='FACESEL')
#             row = box.row()
#             row.menu("WAZOU_MT_mesh_display_overlays", text="Mesh display", icon='OBJECT_DATAMODE')
#         else:
#             pie.separator()
#         # 9 - TOP - RIGHT
#         if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH']):
#             box = pie.split().column()
#             row = box.row(align=True)
#             row.prop(mesh, "show_double_sided", text="Double sided")
#             row = box.row(align=True)
#             row.prop(mesh, "use_auto_smooth")
#             if mesh.use_auto_smooth:
#                 row = box.row(align=True)
#                 row.prop(mesh, "auto_smooth_angle", text="Angle")
#             row = box.row(align=True)
#             row.prop(view, "show_background_images", text="Background Images")
#
#         else:
#             pie.separator()
#
#         # 1 - BOTTOM - LEFT
#
#         box = pie.split().column()
#         row = box.row(align=True)
#         row.prop(view, "show_only_render")
#         row = box.row(align=True)
#         row.prop(view, "show_world")
#         row = box.row(align=True)
#         row.prop(view, "show_outline_selected")
#         row = box.row(align=True)
#         row.prop(view, "show_background_images", text="Background Images")
#
#         # 3 - BOTTOM - RIGHT
#         box = pie.split().column()
#         row = box.row(align=True)
#         row.prop(view, "use_matcap", text="Matcaps")
#         if view.use_matcap:
#             row = box.row(align=True)
#             row.menu("meshdisplay.matcaps", text="Choose Matcaps", icon='MATCAP_02')
#
#
# # Overlays
# class MeshDisplayMatcaps(bpy.types.Menu):
#     bl_idname = "meshdisplay.matcaps"
#     bl_label = "Mesh Display Matcaps"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     def draw(self, context):
#         layout = self.layout
#         view = context.space_data
#         layout.template_icon_view(view, "matcap_icon")

########################################################################################################################
# PIE VIEWS - Q
########################################################################################################################
# class WAZOU_PIE_MENUS_MT_pie_views(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_pie_views"
#     bl_label = "Pie View All Sel Glob..."
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         #4 - LEFT
#         pie.operator("view3d.view_all", text="View All").center = True
#         #6 - RIGHT
#         pie.operator("view3d.view_selected", text="View Selected")
#         #2 - BOTTOM
#         pie.operator("persp.orthoview", text="Persp/Ortho", icon='RESTRICT_VIEW_OFF')
#         #8 - TOP
#         pie.operator("view3d.localview", text="Local/Global")
#         #7 - TOP - LEFT
#         pie.operator("screen.region_quadview", text="Toggle Quad View", icon='SPLITSCREEN')
#         #1 - BOTTOM - LEFT
#         pie.operator("screen.screen_full_area", text="Full Screen", icon='FULLSCREEN_ENTER')
#         #9 - TOP - RIGHT
#         #3 - BOTTOM - RIGHT

########################################################################################################################
# PIE PROPORTIONAL - O
########################################################################################################################
# Pie ProportionalEditObj - O
# class WAZOU_PIE_MENUS_MT_proportional_obj(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_proportional_obj"
#     bl_label = "Wazou Proportional Object"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("wazou_proportional.object", text="Linear", icon='LINCURVE').proportional = 'linear'
#         # 6 - RIGHT
#         pie.operator("wazou_proportional.object", text="Root", icon='ROOTCURVE').proportional = 'root'
#         # 2 - BOTTOM
#         pie.operator("wazou_proportional.object", text="Sharp", icon='SHARPCURVE').proportional = 'sharp'
#         # 8 - TOP
#         pie.prop(context.tool_settings, "use_proportional_edit_objects",text="Proportional On/Off", icon_only=True)
#         # 7 - TOP - LEFT
#         pie.operator("wazou_proportional.object", text="Sphere", icon='SPHERECURVE').proportional = 'sphere'
#         # 9 - TOP - RIGHT
#         pie.operator("wazou_proportional.object", text="Smooth", icon='SMOOTHCURVE').proportional = 'smooth'
#         # 1 - BOTTOM - LEFT
#         pie.operator("wazou_proportional.object", text="Constant", icon='NOCURVE').proportional = 'constant'
#         # 3 - BOTTOM - RIGHT
#         pie.operator("wazou_proportional.object", text="Random", icon='RNDCURVE').proportional = 'random'

# Pie ProportionalEditEdt - O
# class WAZOU_PIE_MENUS_MT_proportional_edit(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_proportional_edit"
#     bl_label = "Wazou Proportional Edit"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         if bpy.context.scene.tool_settings.proportional_edit == 'PROJECTED':
#             pie.operator("wazou_proportional.object", text="Projected", icon='PROP_ON').proportional = 'projected'
#         else:
#             pie.operator("wazou_proportional.object", text="Projected", icon='PROP_OFF').proportional = 'projected'
#         # 6 - RIGHT
#         if bpy.context.scene.tool_settings.proportional_edit == 'CONNECTED':
#             pie.operator("wazou_proportional.object", text="Connected", icon='PROP_ON').proportional = 'connected'
#         else:
#             pie.operator("wazou_proportional.object", text="Connected", icon='PROP_OFF').proportional = 'connected'
#         # 2 - BOTTOM
#         split = pie.split()
#         col = split.column(align=True)
#         row = col.row(align=True)
#         row.scale_x = 1.4
#         row.scale_y = 1.3
#         row.operator("wazou_proportional.object", text="Sharp", icon='SHARPCURVE').proportional = 'sharp'
#         row = col.row(align=True)
#         row.scale_x = 1.4
#         row.scale_y = 1.3
#         row.operator("wazou_proportional.object", text="Root", icon='ROOTCURVE').proportional = 'root'
#         row = col.row(align=True)
#         row.scale_x = 1.4
#         row.scale_y = 1.3
#         row.operator("wazou_proportional.object", text="Linear", icon='LINCURVE').proportional = 'linear'
#         # 8 - TOP
#         if bpy.context.scene.tool_settings.proportional_edit == 'ENABLED':
#             pie.operator("wazou_proportional.enable_disable", text="Proportional ON", icon='PROP_ON')
#         else:
#             pie.operator("wazou_proportional.enable_disable", text="Proportional OFF", icon='PROP_OFF')
#         # 7 - TOP - LEFT
#         pie.operator("wazou_proportional.object", text="Sphere", icon='SPHERECURVE').proportional = 'sphere'
#         # 9 - TOP - RIGHT
#         pie.operator("wazou_proportional.object", text="Smooth", icon='SMOOTHCURVE').proportional = 'smooth'
#         # 1 - BOTTOM - LEFT
#         pie.operator("wazou_proportional.object", text="Constant", icon='NOCURVE').proportional = 'constant'
#         # 3 - BOTTOM - RIGHT
#         pie.operator("wazou_proportional.object", text="Random", icon='RNDCURVE').proportional = 'random'

########################################################################################################################
# PIE NORMALS ALT + Q
########################################################################################################################
# Pie Normals - ALT + Q
# class WAZOU_PIE_MENUS_MT_pivot_point(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_pivot_point"
#     bl_label = "Wazou Pivot Point"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         pie.prop(context.tool_settings, 'transform_pivot_point', expand=True)
#         pie.prop(context.tool_settings, 'use_transform_pivot_point_align', expand=True, text='Only Origins')
#
# ########################################################################################################################
# # PIE SAVE/OPEN - CTRL + S
# ########################################################################################################################
# #Pie Save/Open
# class PieSaveOpen(Menu):
#     bl_idname = "pie.saveopen"
#     bl_label = "Pie Save/Open"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         #4 - LEFT
#         pie.operator("wm.read_homefile", text="New", icon='NEW')
#         #6 - RIGHT
#         pie.operator("file.save_incremental", text="Incremental Save", icon='SAVE_COPY')
#         #2 - BOTTOM
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("import_scene.obj", text="Import OBJ", icon='IMPORT')
#         box.operator("export_scene.obj", text="Export OBJ", icon='EXPORT')
#         box.separator()
#         box.operator("import_scene.fbx", text="Import FBX", icon='IMPORT')
#         box.operator("export_scene.fbx", text="Export FBX", icon='EXPORT')
#         #8 - TOP
#         pie.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')
#         #7 - TOP - LEFT
#         pie.operator("wm.open_mainfile", text="Open file", icon='FILE_FOLDER')
#         #9 - TOP - RIGHT
#         pie.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
#         #1 - BOTTOM - LEFT
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("wm.recover_auto_save", text="Recover Auto Save...", icon='RECOVER_AUTO')
#         box.operator("wm.recover_last_session", text="Recover Last Session", icon='RECOVER_LAST')
#         box.operator("wm.revert_mainfile", text="Revert", icon='FILE_REFRESH')
#         #3 - BOTTOM - RIGHT
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("wm.link", text="Link", icon='LINK_BLEND')
#         box.operator("wm.append", text="Append", icon='APPEND_BLEND')
#         box.menu("WAZOU_MT_ExternalData", text="External Data", icon='EXTERNAL_DATA')
#



########################################################################################################################
# PIE ORIENTATION - ALT + SPACE
########################################################################################################################
# Pie Orientation - Alt + Space
# class WAZOU_PIE_MENUS_MT_orientation(Menu):
#     bl_idname = "WAZOU_PIE_MENUS_MT_orientation"
#     bl_label = "Wazou Orientations"
#
#     def draw(self, context):
#         layout = self.layout
#
#         pie = layout.menu_pie()
#         pie.prop(context.scene, "transform_orientation", expand=True)

# ########################################################################################################################
# # PIE VIEWS - Q
# ########################################################################################################################
#
# # Pie View All Sel Glob Etc - Q
# class PieViewallSelGlobEtc(Menu):
#     bl_idname = "pie.vieallselglobetc"
#     bl_label = "Pie View All Sel Glob..."
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("view3d.view_all", text="View All").center = True
#         # 6 - RIGHT
#         pie.operator("view3d.view_selected", text="View Selected")
#         # 2 - BOTTOM
#         pie.operator("persp.orthoview", text="Persp/Ortho", icon='RESTRICT_VIEW_OFF')
#         # 8 - TOP
#         pie.operator("view3d.localview", text="Local/Global")
#         # 7 - TOP - LEFT
#         pie.operator("screen.region_quadview", text="Toggle Quad View", icon='SPLITSCREEN')
#         # 1 - BOTTOM - LEFT
#         pie.operator("screen.screen_full_area", text="Full Screen", icon='FULLSCREEN_ENTER')
#         # 9 - TOP - RIGHT
#         # 3 - BOTTOM - RIGHT
#
#
# # Pie views numpad - Q
# class PieViewNumpad(Menu):
#     bl_idname = "pie.viewnumpad"
#     bl_label = "Pie Views Ortho"
#
#     def draw(self, context):
#         layout = self.layout
#         ob = bpy.context.object
#         obj = context.object
#         pie = layout.menu_pie()
#         scene = context.scene
#         rd = scene.render
#
#         # 4 - LEFT
#         pie.operator("view3d.viewnumpad", text="Left", icon='TRIA_LEFT').type = 'LEFT'
#         # 6 - RIGHT
#         pie.operator("view3d.viewnumpad", text="Right", icon='TRIA_RIGHT').type = 'RIGHT'
#         # 2 - BOTTOM
#         pie.operator("view3d.viewnumpad", text="Bottom", icon='TRIA_DOWN').type = 'BOTTOM'
#         # 8 - TOP
#         pie.operator("view3d.viewnumpad", text="Top", icon='TRIA_UP').type = 'TOP'
#         # 7 - TOP - LEFT
#         pie.operator("view3d.viewnumpad", text="Front").type = 'FRONT'
#         # 9 - TOP - RIGHT
#         pie.operator("view3d.viewnumpad", text="Back").type = 'BACK'
#         # 1 - BOTTOM - LEFT
#         box = pie.split().column()
#         row = box.row(align=True)
#         if context.space_data.lock_camera == False:
#             row.operator("wm.context_toggle", text="Lock Cam to View",
#                          icon='UNLOCKED').data_path = "space_data.lock_camera"
#         elif context.space_data.lock_camera == True:
#             row.operator("wm.context_toggle", text="Lock Cam to View",
#                          icon='LOCKED').data_path = "space_data.lock_camera"
#
#         row = box.row(align=True)
#         row.operator("view3d.viewnumpad", text="View Cam", icon='VISIBLE_IPO_ON').type = 'CAMERA'
#         row.operator("view3d.camera_to_view", text="Cam to view", icon='MAN_TRANS')
#
#         if ob.lock_rotation[0] == False:
#             row = box.row(align=True)
#             row.operator("object.lockcameratransforms", text="Lock Transforms", icon='LOCKED')
#
#         elif ob.lock_rotation[0] == True:
#             row = box.row(align=True)
#             row.operator("object.lockcameratransforms", text="UnLock Transforms", icon='UNLOCKED')
#         row = box.row(align=True)
#         row.prop(rd, "use_border", text="Border")
#         # 3 - BOTTOM - RIGHT
#         pie.operator("wm.call_menu_pie", text="View All/Sel/Glob...", icon='BBOX').name = "pie.vieallselglobetc"
#
#
# ########################################################################################################################
# # PIE SCULPT - W & SHIFT + W
# ########################################################################################################################
#
# # Pie Sculp Pie Menus - W
# class PieSculptPie(Menu):
#     bl_idname = "pie.sculpt"
#     bl_label = "Pie Sculpt"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("paint.brush_select", text="Crease", icon='BRUSH_CREASE').sculpt_tool = 'CREASE'
#         # 6 - RIGHT
#         pie.operator("paint.brush_select", text="Clay", icon='BRUSH_CLAY').sculpt_tool = 'CLAY'
#         # 2 - BOTTOM
#         pie.operator("paint.brush_select", text='Flatten', icon='BRUSH_FLATTEN').sculpt_tool = 'FLATTEN'
#         # 8 - TOP
#         pie.operator("paint.brush_select", text='Brush', icon='BRUSH_SCULPT_DRAW').sculpt_tool = 'DRAW'
#         # 7 - TOP - LEFT
#         pie.operator("paint.brush_select", text='Snakehook', icon='BRUSH_SNAKE_HOOK').sculpt_tool = 'SNAKE_HOOK'
#
#         # 9 - TOP - RIGHT
#         pie.operator("paint.brush_select", text='Grab', icon='BRUSH_GRAB').sculpt_tool = 'GRAB'
#         # 1 - BOTTOM - LEFT
#         pie.operator("paint.brush_select", text='Inflate/Deflate', icon='BRUSH_INFLATE').sculpt_tool = 'INFLATE'
#         # 3 - BOTTOM - RIGHT
#         pie.operator("paint.brush_select", text='Mask', icon='BRUSH_MASK').sculpt_tool = 'MASK'
#
# # Pie Sculp Pie Menus 2 - Shift + W
# class PieSculpttwo(Menu):
#     bl_idname = "pie.sculpttwo"
#     bl_label = "Pie Sculpt 2"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("paint.brush_select", text='Claystrips', icon='BRUSH_CREASE').sculpt_tool = 'CLAY_STRIPS'
#         # 6 - RIGHT
#         pie.operator("paint.brush_select", text='Blob', icon='BRUSH_BLOB').sculpt_tool = 'BLOB'
#         # 2 - BOTTOM
#         pie.operator("paint.brush_select", text='Simplify', icon='BRUSH_DATA').sculpt_tool = 'SIMPLIFY'
#
#         # 8 - TOP
#         pie.operator("paint.brush_select", text='Smooth', icon='BRUSH_SMOOTH').sculpt_tool = 'SMOOTH'
#         # 7 - TOP - LEFT
#         pie.operator("paint.brush_select", text='Pinch/Magnify', icon='BRUSH_PINCH').sculpt_tool = 'PINCH'
#         # 9 - TOP - RIGHT
#         pie.operator("sculpt.polish", text='Polish', icon='BRUSH_FLATTEN')
#         # 1 - BOTTOM - LEFT
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("paint.brush_select", text='Twist', icon='BRUSH_ROTATE').sculpt_tool = 'ROTATE'
#         box.operator("paint.brush_select", text='Scrape/Peaks', icon='BRUSH_SCRAPE').sculpt_tool = 'SCRAPE'
#         box.operator("sculpt.sculptraw", text='SculptDraw', icon='BRUSH_SCULPT_DRAW')
#
#         # 3 - BOTTOM - RIGHT
#         box = pie.split().column()
#         row = box.row(align=True)
#         box.operator("paint.brush_select", text='Layer', icon='BRUSH_LAYER').sculpt_tool = 'LAYER'
#         box.operator("paint.brush_select", text='Nudge', icon='BRUSH_NUDGE').sculpt_tool = 'NUDGE'
#         box.operator("paint.brush_select", text='Thumb', icon='BRUSH_THUMB').sculpt_tool = 'THUMB'
#         box.operator("paint.brush_select", text='Fill/Deepen', icon='BRUSH_FILL').sculpt_tool = 'FILL'
#
# ########################################################################################################################
# # PIE TEXT EDITOR - CTRL + ALT + RMB
# ########################################################################################################################
# # Pie Text Editor
# class PieTextEditor(Menu):
#     bl_idname = "pie.texteditor"
#     bl_label = "Pie Text Editor"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         if bpy.context.area.type == 'TEXT_EDITOR':
#             #4 - LEFT
#             pie.operator("text.comment", text="Comment", icon='FONT_DATA')
#             #6 - RIGHT
#             pie.operator("text.uncomment", text="Uncomment", icon='NLA')
#             #2 - BOTTOM
#             pie.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')
#             #8 - TOP
#             pie.operator("text.start_find", text="Search", icon='VIEWZOOM')
#             #7 - TOP - LEFT
#             pie.operator("text.indent", text="Tab (indent)", icon='FORWARD')
#             #9 - TOP - RIGHT
#             pie.operator("text.unindent", text="UnTab (unindent)", icon='BACK')
#             #1 - BOTTOM - LEFT
#             pie.operator("text.save", text="Save Script", icon='SAVE_COPY')
#             #3 - BOTTOM - RIGHT
#
# ########################################################################################################################
# # PIE ANIMATION - ALT + A
# ########################################################################################################################
# # Pie Animation
# class PieAnimation(Menu):
#     bl_idname = "pie.animation"
#     bl_label = "Pie Animation"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("screen.animation_play", text="Reverse", icon='PLAY_REVERSE').reverse = True
#         # 6 - RIGHT
#         if not context.screen.is_animation_playing:  # Play / Pause
#             pie.operator("screen.animation_play", text="Play", icon='PLAY')
#         else:
#             pie.operator("screen.animation_play", text="Stop", icon='PAUSE')
#         # 2 - BOTTOM
#         # pie.operator(toolsettings, "use_keyframe_insert_keyingset", toggle=True, text="Auto Keyframe ", icon='REC')
#         pie.operator("insert.autokeyframe", text="Auto Keyframe ", icon='REC')
#         # 8 - TOP
#         pie.menu("VIEW3D_MT_object_animation", icon="CLIP")
#         # 7 - TOP - LEFT
#         pie.operator("screen.frame_jump", text="Jump REW", icon='REW').end = False
#         # 9 - TOP - RIGHT
#         pie.operator("screen.frame_jump", text="Jump FF", icon='FF').end = True
#         # 1 - BOTTOM - LEFT
#         pie.operator("screen.keyframe_jump", text="Previous FR", icon='PREV_KEYFRAME').next = False
#         # 3 - BOTTOM - RIGHT
#         pie.operator("screen.keyframe_jump", text="Next FR", icon='NEXT_KEYFRAME').next = True
#
#
# ########################################################################################################################
# # PIE UV's -
# ########################################################################################################################
# # Pie UV's Select Mode
# class PIE_IMAGE_MT_uvs_select_mode(Menu):
#     bl_label = "UV Select Mode"
#     bl_idname = "pie.uvsselectmode"
#
#     def draw(self, context):
#         layout = self.layout
#
#         layout.operator_context = 'INVOKE_REGION_WIN'
#         toolsettings = context.tool_settings
#         pie = layout.menu_pie()
#         # do smart things depending on whether uv_select_sync is on
#
#         if toolsettings.use_uv_select_sync:
#
#             props = pie.operator("wm.context_set_value", text="Vertex", icon='VERTEXSEL')
#             props.value = "(True, False, False)"
#             props.data_path = "tool_settings.mesh_select_mode"
#
#             props = pie.operator("wm.context_set_value", text="Edge", icon='EDGESEL')
#             props.value = "(False, True, False)"
#             props.data_path = "tool_settings.mesh_select_mode"
#
#             props = pie.operator("wm.context_set_value", text="Face", icon='FACESEL')
#             props.value = "(False, False, True)"
#             props.data_path = "tool_settings.mesh_select_mode"
#
#         else:
#             props = pie.operator("wm.context_set_string", text="Vertex", icon='UV_VERTEXSEL')
#             props.value = 'VERTEX'
#             props.data_path = "tool_settings.uv_select_mode"
#
#             props = pie.operator("wm.context_set_string", text="Face", icon='UV_FACESEL')
#             props.value = 'FACE'
#             props.data_path = "tool_settings.uv_select_mode"
#
#             props = pie.operator("wm.context_set_string", text="Edge", icon='UV_EDGESEL')
#             props.value = 'EDGE'
#             props.data_path = "tool_settings.uv_select_mode"
#
#             props = pie.operator("wm.context_set_string", text="Island", icon='UV_ISLANDSEL')
#             props.value = 'ISLAND'
#             props.data_path = "tool_settings.uv_select_mode"
#
#
# # Pie UV's Weld/Align
# class Pie_UV_W(Menu):
#     bl_idname = "pie.uvsweldalign"
#     bl_label = "Pie UV's Welde/Align"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         # 4 - LEFT
#         pie.operator("uv.align", text="Align X").axis = 'ALIGN_X'
#         # 6 - RIGHT
#         pie.operator("uv.align", text="Align Y").axis = 'ALIGN_Y'
#         # 2 - BOTTOM
#         pie.operator("uv.align", text="Straighten").axis = 'ALIGN_S'
#         # 8 - TOP
#         pie.operator("uv.align", text="Align Auto").axis = 'ALIGN_AUTO'
#         # 7 - TOP - LEFT
#         pie.operator("uv.weld", text="Weld", icon='AUTOMERGE_ON')
#         # 9 - TOP - RIGHT
#         pie.operator("uv.remove_doubles", text="Remouve doubles")
#         # 1 - BOTTOM - LEFT
#         pie.operator("uv.align", text="Straighten X").axis = 'ALIGN_T'
#         # 3 - BOTTOM - RIGHT
#         pie.operator("uv.align", text="Straighten Y").axis = 'ALIGN_U'




# Vertex Groups
# class WAZOU_PIE_MENUS_MT_lights(bpy.types.Operator):
#     bl_idname = "WAZOU_PIE_MENUS_MT_lights"
#     bl_label = "Wazou Lights"
#
#     def execute(self, context):
#         return {'FINISHED'}
#
#     def check(self, context):
#         return True
#
#     @classmethod
#     def poll(cls, context):
#         return context.active_object is not None
#
#     def draw(self, context):
#         layout = self.layout
#
#         light = context.light
#
#         layout.row().prop(light, "type", expand=True)
#
#         layout.use_property_split = True
#
#         col = layout.column()
#         col.prop(light, "color")
#         col.prop(light, "energy")
#         col.prop(light, "specular_factor", text="Specular")
#
#         # col.separator()
#         #
#         # if light.type in {'POINT', 'SPOT', 'SUN'}:
#         #     col.prop(light, "shadow_soft_size", text="Radius")
#         # elif light.type == 'AREA':
#         #     col.prop(light, "shape")
#         #
#         #     sub = col.column(align=True)
#         #
#         #     if light.shape in {'SQUARE', 'DISK'}:
#         #         sub.prop(light, "size")
#         #     elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
#         #         sub.prop(light, "size", text="Size X")
#         #         sub.prop(light, "size_y", text="Y")
#
#     def invoke(self, context, event):
#         dpi_value = bpy.context.preferences.view.ui_scale
#         return context.window_manager.invoke_props_dialog(self, width=dpi_value * 300, height=800)




CLASSES =  [WAZOU_PIE_MENUS_MT_modes,
            WAZOU_PIE_MENUS_MT_snapping,
            WAZOU_PIE_MENUS_MT_active_tools,
            WAZOU_PIE_MENUS_MT_align,
            WAZOU_PIE_MENUS_MT_origin_pivot,
            WAZOU_PIE_MENUS_MT_apply_clear_transforms,
            WAZOU_PIE_MENUS_MT_area_views,
            WAZOU_PIE_MENUS_MT_delete,
            WAZOU_PIE_MENUS_MT_selection_object_mode,
            WAZOU_PIE_MENUS_MT_selection_edit_mode,
            ]

def register():
    for cls in CLASSES:
        try:
            bpy.utils.register_class(cls)
        except:
            print(f"{cls.__name__} already registered")


def unregister():
    for cls in CLASSES :
        if hasattr(bpy.types, cls.__name__):
            bpy.utils.unregister_class(cls)