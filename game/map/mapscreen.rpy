screen map_screen():
    frame:
        xalign 0.0
        yalign 0.0
        background "map/map.png"
        for l in Locations:
            if l.is_active:
                imagebutton:
                    xpos l.x
                    ypos l.y
                    idle "map/" + l.j + "_idle.png"
                    hover "map/" + l.j + "_hover.png"
                    activate_sound("audio/sfx_ui_button_select.mp3") # sound when clicked
                    hover_sound("audio/sfx_ui_button.mp3") #sound when hovered
                    action [SetVariable("current_location", l.name), SetVariable("current_x", l.x), SetVariable("current_y", l.y), Jump("map_scene_change")]
