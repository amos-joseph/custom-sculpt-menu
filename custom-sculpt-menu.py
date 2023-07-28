
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


# Sculpt Menus
class SCULPT_MT_SculptMenu(Menu):
    bl_idname = "SCULPT_MT_SculptMenu"
    bl_label = "Sculpt Menu"

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
                    text='Sharp', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.draw_sharp')).name = "builtin_brush.Draw Sharp" 
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
        col.operator("wm.tool_set_by_id", text='Fill',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.fill')).name = 'builtin_brush.Fill'
        col.operator("wm.tool_set_by_id", text='Smooth',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.smooth')).name = 'builtin_brush.Smooth'
        col.operator("wm.tool_set_by_id",
                    text='Inflate', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.inflate')).name = 'builtin_brush.Inflate'
        col.operator("wm.tool_set_by_id",
                    text='Blob', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.blob')).name = 'builtin_brush.Blob'
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
                        text='Elastic', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.elastic_deform')).name = 'builtin_brush.Elastic Deform'
        col.operator("wm.tool_set_by_id",
                        text='Snake', icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.snake_hook')).name = 'builtin_brush.Snake Hook'
        col.operator("wm.tool_set_by_id", text='Pose',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.pose')).name = 'builtin_brush.Pose'
        col.operator("sculptmenu.remesh", text='Remesh').voxel_size = 0 
        col.menu(SCULPT_MT_Remesh.bl_idname,text="Remesh Detail")
        col.operator(
            "sculpt.dynamic_topology_toggle",
            icon='CHECKBOX_HLT' if context.sculpt_object.use_dynamic_topology_sculpting else 'CHECKBOX_DEHLT',
            text="Dyntopo"
        )
        col.operator("sculptmenu.floodfill", text='Flood Fill')
        area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
        space = next(space for space in area.spaces if space.type == 'VIEW_3D')
        col.prop(space.overlay, "show_wireframes");
        col.menu(SCULPT_MT_Faceset.bl_idname,text="Face Sets")
        col.menu(SCULPT_MT_Trim.bl_idname,text="Trim")
        col.menu(SCULPT_MT_Symmetrize.bl_idname,text="Symmetrize")
        
        mesh = context.object.data
        col.prop(mesh, "use_mirror_x", text="X Mirror", toggle=True)
        col.prop(mesh, "use_mirror_y", text="Y Mirror", toggle=True)
        col.prop(mesh, "use_mirror_z", text="Z Mirror", toggle=True)

# Mask and Transform Menu
class SCULPT_MT_MaskTransMenu(Menu):
    bl_idname = "SCULPT_MT_MaskTransMenu"
    bl_label = "Mask and Transform Menu"

    def draw(self, context):
        layout = self.layout
        
        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.scale_y = 1.2
        col.operator("wm.tool_set_by_id", text='Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('brush.sculpt.mask')).name = 'builtin_brush.Mask'
        col.operator("wm.tool_set_by_id", text='Lasso Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle("ops.sculpt.lasso_mask")).name = 'builtin.lasso_mask' 
        col.operator("wm.tool_set_by_id", text='Box Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle("ops.sculpt.border_mask")).name = 'builtin.box_mask' 
        col.operator("wm.tool_set_by_id", text='Line Mask',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle("ops.sculpt.line_mask")).name = 'builtin.line_mask'   
        col.operator("paint.mask_flood_fill", text='Invert Mask').mode = 'INVERT'
        col.operator("paint.mask_flood_fill", text='Clear Mask').mode = 'VALUE'  
        col.operator("sculptmenu.maskcommands", text='Smooth Mask').mode = 'SMOOTH'
        col.operator("sculptmenu.maskcommands", text='Sharpen Mask').mode = 'SHARPEN'
        col.operator("sculptmenu.maskcommands", text='Slice to Object').mode = 'SLICE'
              
        # Second column, aligned
        col = split.column(align=True)
        col.scale_y = 1.2
        
        col.operator("wm.tool_set_by_id", text='Move',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.translate')).name = 'builtin.move'
        col.operator("wm.tool_set_by_id", text='Rotate',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.rotate')).name = 'builtin.rotate'
        col.operator("wm.tool_set_by_id", text='Scale',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.resize')).name = 'builtin.scale'
        col.operator("wm.tool_set_by_id", text='Transform',
                        icon_value=ToolSelectPanelHelper._icon_value_from_icon_handle('ops.transform.transform')).name = 'builtin.transform'
        col.operator("sculptmenu.setpivot", text='Pivot to Mask Border').mode='BORDER'
        col.operator("sculptmenu.setpivot", text='Pivot to Unmasked').mode='UNMASKED'
        col.operator("sculptmenu.setpivot", text='Pivot to Origin').mode='ORIGIN'
        col.operator("sculptmenu.setpivot", text='Pivot to Vertex').mode='ACTIVE'

# Face Set Menu
class SCULPT_MT_Faceset(Menu):
    bl_idname = "SCULPT_MT_Faceset"
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
class SCULPT_MT_Trim(Menu):
    bl_idname = "SCULPT_MT_Trim"
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
        
# Symmetrize Menu
class SCULPT_MT_Symmetrize(Menu):
    bl_idname = "SCULPT_MT_Symmetrize"
    bl_label = "Symmetrize"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2        
        col.operator("sculptmenu.symmetrize", text='+X to -X').direction = 'POSITIVE_X'  
        col.operator("sculptmenu.symmetrize", text='-X to +X').direction = 'NEGATIVE_X'  
        col.operator("sculptmenu.symmetrize", text='+Y to -Y').direction = 'POSITIVE_Y'  
        col.operator("sculptmenu.symmetrize", text='-Y to +Y').direction = 'NEGATIVE_Y'  
        col.operator("sculptmenu.symmetrize", text='+Z to -Z').direction = 'POSITIVE_Z'  
        col.operator("sculptmenu.symmetrize", text='-Z to +Z').direction = 'NEGATIVE_Z'  
        
# Remesh Menu
class SCULPT_MT_Remesh(Menu):
    bl_idname = "SCULPT_MT_Remesh"
    bl_label = "Remesh"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.scale_y = 1.2  
        col.operator("sculptmenu.remesh", text='.5').voxel_size = .5      
        col.operator("sculptmenu.remesh", text='.1').voxel_size = .1       
        col.operator("sculptmenu.remesh", text='.06').voxel_size = .06 
        col.operator("sculptmenu.remesh", text='.05').voxel_size = .05 
        col.operator("sculptmenu.remesh", text='.04').voxel_size = .04 
        col.operator("sculptmenu.remesh", text='.03').voxel_size = .03 
        col.operator("sculptmenu.remesh", text='.02').voxel_size = .02 
        col.operator("sculptmenu.remesh", text='.01').voxel_size = .01 
        col.operator("sculptmenu.remesh", text='.015').voxel_size = .015
        col.operator("sculptmenu.remesh", text='.0075').voxel_size = .0075
        col.operator("sculptmenu.remesh", text='.005').voxel_size = .005

class SCULPT_OT_SetPivot(Operator):
    bl_idname = "sculptmenu.setpivot"
    bl_label = "Set Pivot for Transform"
    
    mode: bpy.props.StringProperty(name="Pivot Mode")

    def execute(self, context):

        bpy.ops.sculpt.set_pivot_position(mode=self.mode)
        return {'FINISHED'}

class SCULPT_OT_FloodFill(Operator):
    bl_idname = "sculptmenu.floodfill"
    bl_label = "Dyntopo Flood Fill"

    def execute(self, context):

        bpy.ops.sculpt.detail_flood_fill()
        return {'FINISHED'}
    
class SCULPT_OT_MaskCommands(Operator):
    bl_idname = "sculptmenu.maskcommands"
    bl_label = "Run various mask operators"
    
    mode: bpy.props.StringProperty(name="Pivot Mode")

    def execute(self, context):

        if self.mode == 'SMOOTH':
            bpy.ops.sculpt.mask_filter(filter_type='SMOOTH')
        elif self.mode == 'SHARPEN':
            bpy.ops.sculpt.mask_filter(filter_type='SHARPEN')
        elif self.mode == 'SLICE':
            bpy.ops.mesh.paint_mask_slice(new_object=True)
        
        return {'FINISHED'}

class SCULPT_OT_Symmetrize(Operator):
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
    
class SCULPT_OT_Remesh(Operator):
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

        dyntopo = context.sculpt_object.use_dynamic_topology_sculpting
        if dyntopo == True:
            bpy.ops.sculpt.dynamic_topology_toggle()

        if self.voxel_size == 0:
            bpy.ops.object.voxel_remesh()
            self.report({'INFO'}, bl_info.get('name') + ': Remeshed to ' + str(round(bpy.context.object.data.remesh_voxel_size, 4)) + ' voxel size')
        else:
            bpy.context.object.data.remesh_voxel_size = self.voxel_size
            bpy.ops.object.voxel_remesh()
            self.report({'INFO'}, bl_info.get('name') + ': Remeshed to ' + str(round(self.voxel_size, 4)) + ' voxel size')
        
        if dyntopo == True:
            bpy.ops.sculpt.dynamic_topology_toggle()

        return {'FINISHED'}

classes = (
    SCULPT_MT_SculptMenu,
    SCULPT_MT_MaskTransMenu,
    SCULPT_MT_Faceset,
    SCULPT_MT_Trim,
    SCULPT_MT_Symmetrize,
    SCULPT_OT_Symmetrize,
    SCULPT_MT_Remesh,
    SCULPT_OT_Remesh,
    SCULPT_OT_SetPivot,
    SCULPT_OT_MaskCommands,
    SCULPT_OT_FloodFill,
    )

addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # Sculpt Menu
        km = wm.keyconfigs.addon.keymaps.new(name='Sculpt')
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=True)
        kmi.properties.name = SCULPT_MT_SculptMenu.bl_idname
        addon_keymaps.append((km, kmi))
        kmi = km.keymap_items.new('wm.call_menu', 'M', 'PRESS')
        kmi.properties.name = SCULPT_MT_MaskTransMenu.bl_idname
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
