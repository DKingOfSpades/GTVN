label robot_gal:
    $ current_location_img = "bg " + current_location.lower() + " lecture"
    if renpy.has_image(current_location_img):
        scene expression current_location_img:
            xsize 1920
            ysize 1080

    "Still can’t get used to how loud it is before lecture."

    "Agitated Student" "But it isn’t friggin fair! Robojackets can’t just give up. She is one of us!"

    "Two of my classmates walk past me talking loudly as they sit in the row in front of me."

    "Dismissive Student" "Look. I get it, she means a lot to you guys, but it’s another robo girl. There’s newer and better."

    "Robo girl?!{p} I can’t help but listen in."

    "Agitated Student" "You DON’T get it. Winri literally represents Robojackets! I can’t imagine any of the teams without her-{p} and don’t call her “robo girl.”"

    "Winri?"

    "Dismissive Student" "She basically belongs to the SCC. She can’t even leave the SCC anymore. Just do your best while she’s here."

    "Agitated Student" "But-"

    "They both go quiet as the lecture starts, but my mind wouldn’t let go of what I heard."

    "Winri in the SCC…{p} I should go look after my classes sometime this week"

    "{b}You unlocked the Student Competition Center on the map!{/b}"

    $ Locations[21].is_active = True

    return
