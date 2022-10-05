init -100 python:
    class Location(object):
        def __init__(self, x, y, name, j, is_active):
            self.x = x
            self.y = y
            self.name = name
            self.j = j
            self.is_active = is_active

    Locations = []


    Locations.append(Location(1130, 660, "Tech Tower", "tech_tower", True))
    Locations.append(Location(1678, 958, "North Ave Dining", "north_ave_dining", True))

label map_scene_change:
    $ current_location_img = "bg " + current_location.lower()
    if renpy.has_image(current_location_img):
        scene expression current_location_img:
            xsize 1920
            ysize 1080
    return

label tech_tower:
    call map_scene_change
    "Tech Tower pressed"
    return

label north_ave_dining:
    "Nave pressed"
    return
