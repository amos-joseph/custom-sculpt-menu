
bl_info = {
    "name": "Custom Sculpt Menu",
    "description": "A custom sculpt menu with all the tools I use the most arranged just the way I like them.",
    "author": "Amos Joseph",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "warning": "",
    "wiki_url": "",
    "category": "Sculpt Menu"
    }

import bpy
from bpy.types import (
        Menu,
        Operator,
        )
from bl_ui.space_toolsystem_common import ToolSelectPanelHelper


# Sculpt Menus - W
class SCULPT_M_SculptMenu(Menu):
    bl_idname = "SCULPT_M_SculptMenu"
    bl_label = "Sculpt Menu"
    
    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=750)

    def draw(self, context):
        layout = self.layout
        
        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.scale_y = 1.2
        col.operator("wm.tool_set_by_id",
                    text='Draw', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.draw')).name = "builtin_brush.Draw" 
        col.operator("wm.tool_set_by_id",
                    text='Draw Sharp', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.draw_sharp')).name = "builtin_brush.Draw Sharp" 
        col.operator("wm.tool_set_by_id",
                    text='Claystrips', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.clay_strips')).name = 'builtin_brush.Clay Strips'
        col.operator("wm.tool_set_by_id",
                    text="Clay", icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.clay')).name = 'builtin_brush.Clay'
        col.operator("wm.tool_set_by_id",
                    text="Crease", icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.crease')).name = 'builtin_brush.Crease'
        col.operator("wm.tool_set_by_id", text='Pinch',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.pinch')).name = 'builtin_brush.Pinch'
        col.operator("wm.tool_set_by_id", text='Flatten',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.flatten')).name = 'builtin_brush.Flatten'
        col.operator("wm.tool_set_by_id", text='Scrape',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.scrape')).name = 'builtin_brush.Scrape'
        col.operator("wm.tool_set_by_id", text='Smooth',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.smooth')).name = 'builtin_brush.Smooth'
        col.operator("wm.tool_set_by_id",
                    text='Inflate', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.inflate')).name = 'builtin_brush.Inflate'
        col.operator("wm.tool_set_by_id",
                    text='Blob', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.blob')).name = 'builtin_brush.Blob'
        col.operator("wm.tool_set_by_id", text='Fill',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.fill')).name = 'builtin_brush.Fill'
        col.operator("wm.tool_set_by_id", text='Layer',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.layer')).name = 'builtin_brush.Layer'
        col.operator("wm.tool_set_by_id", text='Cloth',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.cloth')).name = 'builtin_brush.Cloth'            
                        
        # Second column, aligned
        col = split.column(align=True)
        col.scale_y = 1.2
        
        col.operator("wm.tool_set_by_id",
                        text='Grab', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.grab')).name = 'builtin_brush.Grab'
        col.operator("wm.tool_set_by_id",
                        text='Elastic Deform', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.elastic_deform')).name = 'builtin_brush.Elastic Deform'
        col.operator("wm.tool_set_by_id",
                        text='Snakehook', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.snake_hook')).name = 'builtin_brush.Snake Hook'
        col.operator("wm.tool_set_by_id", text='Pose',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.pose')).name = 'builtin_brush.Pose'
        col.menu(SCULPT_M_Masking.bl_idname,text="Masking")
        col.menu(SCULPT_M_Faceset.bl_idname,text="Face Sets")
        col.menu(SCULPT_M_Trim.bl_idname,text="Trim")
        col.menu(SCULPT_M_Transform.bl_idname,text="Transform")
        col.menu(SCULPT_M_Symmetrize.bl_idname,text="Symmetrize")
        col.menu(SCULPT_M_Remesh.bl_idname,text="Remesh")
        area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
        space = next(space for space in area.spaces if space.type == 'VIEW_3D')
        col.prop(space.overlay, "show_wireframes");
        mesh = context.object.data
        col.prop(mesh, "use_mirror_x", text="X Mirror", toggle=True)
        col.prop(mesh, "use_mirror_y", text="Y Mirror", toggle=True)
        col.prop(mesh, "use_mirror_z", text="Z Mirror", toggle=True)

# Pie Sculpt 2
class SCULPT_M_Masking(Menu):
    bl_idname = "SCULPT_M_Masking"
    bl_label = "Masking"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2
        
        col.operator("wm.tool_set_by_id", text='Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.mask')).name = 'builtin_brush.Mask'
        col.operator("wm.tool_set_by_id", text='Lasso Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle("ops.sculpt.lasso_mask")).name = 'builtin.lasso_mask' 
        col.operator("wm.tool_set_by_id", text='Box Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle("ops.sculpt.border_mask")).name = 'builtin.box_mask' 
        col.operator("wm.tool_set_by_id", text='Line Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle("ops.sculpt.line_mask")).name = 'builtin.line_mask'   
        props = col.operator("paint.mask_flood_fill", text='Invert Mask')
        props.mode = 'INVERT'
        props = col.operator("paint.mask_flood_fill", text='Clear Mask')
        props.mode = 'VALUE'  


# Face Set Menu
class SCULPT_M_Faceset(Menu):
    bl_idname = "SCULPT_M_Faceset"
    bl_label = "Face Set"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2
        
        col.operator("wm.tool_set_by_id", text='Draw Face Sets',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.draw_face_sets')).name = 'builtin_brush.Draw Face Sets'
        col.operator("wm.tool_set_by_id", text='Lasso Face Set',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.sculpt.lasso_face_set')).name = 'builtin.lasso_face_set'
        col.operator("wm.tool_set_by_id", text='Box Face Set',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.sculpt.border_face_set')).name = 'builtin.box_face_set'
        col.operator("wm.tool_set_by_id", text='Edit Face Set',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.sculpt.face_set_edit')).name = 'builtin.face_set_edit'

# Trim Menu
class SCULPT_M_Trim(Menu):
    bl_idname = "SCULPT_M_Trim"
    bl_label = "Trim"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2
        
        col.operator("wm.tool_set_by_id", text='Line Project',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.sculpt.line_project')).name = 'builtin.line_project'
        col.operator("wm.tool_set_by_id", text='Lasso Trim',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.sculpt.lasso_trim')).name = 'builtin.lasso_trim'
        col.operator("wm.tool_set_by_id", text='Box Trim',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.sculpt.box_trim')).name = 'builtin.box_trim'
                        
# Translate Menu
class SCULPT_M_Transform(Menu):
    bl_idname = "SCULPT_M_Transform"
    bl_label = "Transform"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2
        
        col.operator("wm.tool_set_by_id", text='Move',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.translate')).name = 'builtin.move'
        col.operator("wm.tool_set_by_id", text='Rotate',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.rotate')).name = 'builtin.rotate'
        col.operator("wm.tool_set_by_id", text='Scale',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.resize')).name = 'builtin.scale'
        col.operator("wm.tool_set_by_id", text='Transform',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.transform')).name = 'builtin.transform'
# Symmetrize Menu
class SCULPT_M_Symmetrize(Menu):
    bl_idname = "SCULPT_M_Symmetrize"
    bl_label = "Symmetrize"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2        
        props = col.operator("sculptmenu.symmetrize", text='+X to -X')
        props.direction = 'POSITIVE_X'  
        props = col.operator("sculptmenu.symmetrize", text='-X to +X')
        props.direction = 'NEGATIVE_X'  
        props = col.operator("sculptmenu.symmetrize", text='+Y to -Y')
        props.direction = 'POSITIVE_Y'  
        props = col.operator("sculptmenu.symmetrize", text='-Y to +Y')
        props.direction = 'NEGATIVE_Y'  
        props = col.operator("sculptmenu.symmetrize", text='+Z to -Z')
        props.direction = 'POSITIVE_Z'  
        props = col.operator("sculptmenu.symmetrize", text='-Z to +Z')
        props.direction = 'NEGATIVE_Z'  
        
# Remesh Menu
class SCULPT_M_Remesh(Menu):
    bl_idname = "SCULPT_M_Remesh"
    bl_label = "Remesh"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2        
        props = col.operator("sculptmenu.remesh", text='.06')
        props.voxel_size = .06 
        props = col.operator("sculptmenu.remesh", text='.05')
        props.voxel_size = .05 
        props = col.operator("sculptmenu.remesh", text='.04')
        props.voxel_size = .04 
        props = col.operator("sculptmenu.remesh", text='.03')
        props.voxel_size = .03 
        props = col.operator("sculptmenu.remesh", text='.02')
        props.voxel_size = .02 
        props = col.operator("sculptmenu.remesh", text='.01')
        props.voxel_size = .01 
        props = col.operator("sculptmenu.remesh", text='.015')
        props.voxel_size = .015
        props = col.operator("sculptmenu.remesh", text='.0075')
        props.voxel_size = .0075
        props = col.operator("sculptmenu.remesh", text='.005')
        props.voxel_size = .005

class SCULPT_OP_Symmetrize(Operator):
    bl_idname = "sculptmenu.symmetrize"
    bl_label = "Symmetrize"
    
    direction: bpy.props.StringProperty(name="Symmetry Direction")

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = self.direction
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data')
        return {'FINISHED'}
    
class SCULPT_OP_Remesh(Operator):
    bl_label = "Remesh"
    bl_idname = "sculptmenu.remesh"
    bl_description = "Remesh selected object."
    
    voxel_size: bpy.props.FloatProperty(name="Voxel Size for Remesh")

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = self.voxel_size
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to ' + str(round(self.voxel_size, 4)) + ' voxel size')
        return {'FINISHED'}

classes = (
    SCULPT_M_SculptMenu,
    SCULPT_M_Masking,
    SCULPT_M_Faceset,
    SCULPT_M_Trim,
    SCULPT_M_Transform,
    SCULPT_M_Symmetrize,
    SCULPT_OP_Symmetrize,
    SCULPT_M_Remesh,
    SCULPT_OP_Remesh,
    )

addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # Sculpt Menu
        km = wm.keyconfigs.addon.keymaps.new(name='Sculpt Menu')
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS')
        kmi.properties.name = "SCULPT_M_SculptMenu"
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
