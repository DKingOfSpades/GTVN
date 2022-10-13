init -100 python:
    import math

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
    Locations.append(Location(1299, 549, "Bobby Dodd Stadium", "bobby_dodd_stadium", False))
    Locations.append(Location(1568, 490, "Dorms", "dorms", True))
    Locations.append(Location(1631, 707, "Brittain Dining", "brittain_dining", False))
    Locations.append(Location(1141, 213, "Greek Life", "greek_life", False))
    Locations.append(Location(961, 199, "Klaus", "klaus", False))
    Locations.append(Location(740, 408, "Tech Green", "tech_green", True))
    Locations.append(Location(872, 392, "CULC", "culc", True))
    Locations.append(Location(1076, 433, "Crossland", "crossland", True))
    Locations.append(Location(862, 518, "Skiles", "skiles", True))
    Locations.append(Location(516, 431, "Student Center", "student_center", False))
    Locations.append(Location(-4, 201, "Campus Recreation Center", "campus_recreation_center", True))
    Locations.append(Location(-4, 54, "Dorms 2", "dorms_2", False))
    Locations.append(Location(184, 69, "Willage Dining", "willage_dining", False))
    Locations.append(Location(524, 353, "Ferst Center of the Arts", "ferst_center_of_the_arts", False))
    Locations.append(Location(702, 184, "Howey", "howey", True))
    Locations.append(Location(500, 288, "Boggs", "boggs", True))
    Locations.append(Location(218, 84, "Burger Bowl", "burger_bowl", False))
    Locations.append(Location(1092, 203, "Russ Chandler Stadium", "russ_chandler_stadium", False))
    Locations.append(Location(1300, 54, "McCamish Pavilion", "mccamish_pavilion", False))
    Locations.append(Location(300, -100, "Student Competition Center", "student_competition_center", False))

label map_scene_change:
    python:
        import math
        delta = int(math.ceil(math.sqrt((current_x-prev_x)**2 + (current_y-prev_y)**2)))
    if delta > 1000:
        $ AP-=2
    elif delta == 0:
        $ AP-=0
    else:
        $ AP-=1
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
    call map_scene_change
    "Nave pressed"
    return

label bobby_dodd_stadium:
    call map_scene_change
    "bobby dodd pressed"
    return

label dorms:
    call map_scene_change
    "Home pressed"
    return

label brittain_dining:
    call map_scene_change
    "Brittain pressed"
    return

label greek_life:
    call map_scene_change
    "greek life pressed"
    return

label klaus:
    call map_scene_change
    "Klaus pressed"
    return

label tech_green:
    call map_scene_change
    "tech green pressed"
    return

label culc:
    call map_scene_change
    "culc pressed"
    return

label crossland:
    call map_scene_change
    "crossland pressed"
    return

label skiles:
    call map_scene_change
    "skiles pressed"
    return

label student_center:
    call map_scene_change
    "Student center pressed"
    return

label campus_recreation_center:
    call map_scene_change
    "crc pressed"
    return

label dorms_2:
    call map_scene_change
    "west campus dorms pressed"
    return

label willage_dining:
    call map_scene_change
    "willage pressed"
    return

label ferst_center_of_the_arts:
    call map_scene_change
    "Ferst Center of the Arts pressed"
    return

label howey:
    call map_scene_change
    "Howey pressed"
    return

label boggs:
    call map_scene_change
    "Boggs pressed"
    return

label burger_bowl:
    call map_scene_change
    "burger bowl pressed"
    return

label russ_chandler_stadium:
    call map_scene_change
    "russ chandler stadium pressed"
    return

label mccamish_pavilion:
    call map_scene_change
    "McCamish Pavilion pressed"
    return

label student_competition_center:
    call map_scene_change
    "scc traversed"
    return
