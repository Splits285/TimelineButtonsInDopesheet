bl_info = {
    "name": "Timeline buttons in dopesheet",
    "author": "Splits285",
    "blender": (2, 80, 0),
    "version": (0, 0, 4),
    "description": "Adds the timeline's current frame, frame-start-end(+preview) sliders, auto-key toggle, and a neat FPS slider to the dopesheet.",
    "doc_url": "https://github.com/Splits285/TimelineButtonsInDopesheet",
    "tracker_url": "https://github.com/Splits285/TimelineButtonsInDopesheet/issues",
    "category": "Dope Sheet",
    "support": "COMMUNITY",
}

import bpy

#Read all about it @ https://docs.blender.org/api/current/bpy.types.UILayout.html
#Create the thing
class CUSTOM_PT_slider_panel(bpy.types.Panel):
    bl_label = "Custom Slider Panel"
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'HEADER'

    def draw(self, context):
        layout = self.layout
       ##Current frame slider
        row = layout.row()
        row.ui_units_x = 3.2
        row.prop(context.scene, "frame_current", text="")
        ##Auto keying toggle radio button, somehow toggles its icon to filled on its own
        row = layout.row()
        row.prop(context.scene.tool_settings, "use_keyframe_insert_auto", icon='RADIOBUT_OFF', icon_only=True)
       ##Preview range toggle button
        row = layout.row(align=True)
        row.ui_units_x = 7.5
        row.prop(context.scene, "use_preview_range", icon='PREVIEW_RANGE', icon_only=True)
        
       ##Frame range sliders, preview being active controls which slider is shown just as in the timeline window
        if context.scene.use_preview_range:
            row.prop(context.scene, "frame_preview_start", text="Start")
            row.prop(context.scene, "frame_preview_end", text="End")
        else:
            row.prop(context.scene, "frame_start", text="Start")
            row.prop(context.scene, "frame_end", text="End")
       ##FPS slider
        row = layout.row()
        row.ui_units_x = 2.7
        row.prop(context.scene.render, "fps", text="FPS")

#Add our elements. They could be .prepend-ed as well but that looks weird being ahead of the window type button.
def register():
    bpy.utils.register_class(CUSTOM_PT_slider_panel)
    bpy.types.DOPESHEET_HT_header.append(CUSTOM_PT_slider_panel.draw)

#Remove them.
def unregister():
    bpy.types.DOPESHEET_HT_header.remove(CUSTOM_PT_slider_panel.draw)
    bpy.utils.unregister_class(CUSTOM_PT_slider_panel)

#Spawn automatically if we're __main__.py I guess.
if __name__ == "__main__":
    register()
