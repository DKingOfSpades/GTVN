label robot_gal:
    $ prev_location_img = current_location_img
    $ current_location_img = "bg " + current_location.lower() + " lecture"
    if renpy.has_image(current_location_img) and current_location_img != prev_location_img:
        scene expression current_location_img:
            xsize 1920
            ysize 1080
        with fade

    "Still can’t get used to how loud it is before lecture."

    "Agitated Student" "But it isn’t friggin fair! Robojackets can’t just give up. She is one of us!"

    "Two of my classmates walk past me talking loudly as they sit in the row in front of me."

    "Dismissive Student" "Look. I get it, she means a lot to you guys, but it’s another robo girl. There’s newer and better."

    "Robo girl?!{p}I can’t help but listen in."

    "Agitated Student" "You DON’T get it. Winri literally represents Robojackets! I can’t imagine any of the teams without her-{p}and don’t call her “robo girl.”"

    "Winri?"

    "Dismissive Student" "She basically belongs to the SCC. She can’t even leave the SCC anymore. Just do your best while she’s here."

    "Agitated Student" "But-"

    "They both go quiet as the lecture starts, but my mind wouldn’t let go of what I heard."

    "Winri in the SCC…{p}I should go look after my classes tomorrow"

    "{b}You unlocked the Student Competition Center on the map!{/b}"

    $ Locations[21].is_active = True

    return

label lend_a_hand:
    "I finally wandered over here. Time to find Winri."

    "*opens door*"

    # $ current_location_img = "bg " + current_location.lower() + " security" TODO
    # if renpy.has_image(current_location_img):
    #     scene expression current_location_img:
    #         xsize 1920
    #         ysize 1080

    "Desk Worker" "Hello"

    "I awkwardly stare at him."

    "Desk Worker" "Buzzcard please."

    "I quickly take out my buzzcard and show it to him. He barely glances at it before uttering a quick “thank you” and gesturing to my left."

    # $ current_location_img = "bg " + current_location.lower() + " hallway"
    # if renpy.has_image(current_location_img):
    #     scene expression current_location_img:
    #         xsize 1920
    #         ysize 1080


    "I glance down the long hallway and awkwardly keep walking forward. I pass by several rooms each with large whiteboards covered in endless diagrams, equations, and hasty calculations"

    "I hear a voice coming from a room further down."

    mc "Hello?"

    unknown "You’re back already? Did the bot go backwards again? I told you to check the wiring before you tested it."

    mc "uuuuhhhh. What?"

    unknown "huh?"

    "I hear loud clanging and a small yelp before a figure pops around the corner."

    show winri laugh at center with moveinleft:
        zoom 0.45

    Winri "Hello! Sorry! I thought you were one of the RJ  members. I swear one of them is always here. I’m Winri! You are….?"

    mc "I- I"

    "I stutter while trying to process everything. Her smile was bright and peppy, but her body was that of many robotic parts"

    mc "I’m [player_name]"

    show winri happy

    Winri "ahahah.I must have surprised you! Welcome to the SCC! What brings you here? Are you here to join the RoboJackets?"

    show winri neutral

    "Winri stares excitedly at me."

    "I can’t bring myself to tell her I only came from curiosity about her."

    menu:
        "Could you tell me about RoboJackets?":
            "Can’t bring myself to say deny her."
            show winri happy
            Winri "Of course!!"
            "She turns and gestures me to follow her."
            "She leads me back to the rooms I passed earlier as she tells me all about Robojackets (TODO). She also explains how they gave her pieces and parts from their projects."
            "Her claw was from RoboNav, shoes from RoboCup? Honestly, the names were blowing right over my head."
            Winri "And over here is our workshop!"
            "She shows the room she first came from and all I can see are tools, parts, and prototypes cluttered everywhere. she walks straight to a high work table and then turns around to wave me over."
            "CLANG" with hpunch
            show winri down
            "Winri is stares wide eyed at the floor, {w}at her hand."
            mc "Are you okay?"
            "I carefully pick it up."
            show winri embarrased
            "Now that I look closely, Winri doesn’t seem much advanced. Her parts are from different past projects from robojackets after all. but if they start new projects each year, why are her parts so old?"
            Winri "Thank you. Weird right? A robot building robots, yet can’t even keep herself together."
            show winri laugh
            "She laughs slightly embarrassed"
            mc "But, are you okay? Do you need help?"
            Winri "Oh it’s all good. I can just ask one of the RoboMembers to reattach it tomorrow."
            mc "I can do it instead."
            show winri embarrased
            "Why did I say that?? I don’t have any tools or anything."
            "Winri blinks in surprise and then gestures her head to one of the tool cabinets. It is conveniently labeled \"screwdrivers\""
            show winri happy at left with move
            Winri "Chonkii! Can you bring out the bin?"
            show chonkii at right with moveinbottom
            "I hear a light whirring followed closely by loud scraping sounds."
            "A bin filled with metal scraps, screws, bolts, and other parts slowly slid from under the work table. behind it, a cute Roomba looking bot was pushing it."
            Winri "This is Chonkii, one of the BattleBots. They let me keep it, you know- to keep me company around here."
            mc " It’s cute. But you understand it? Or more like- Chonkii can understand you?"
            "I start digging through the bin looking for an appropriate screwdriver to reattach her hand."
            Winri "Sort of? I am not too sure how. Maybe it’s because Chonkii is like me."
            hide chonkii with moveoutright
            show winri confused at center with move
            "I find a flathead screwdriver and Winri’s places her arm on the work table so I can reattach her hand. I can feel her staring down at me as I try and focus on getting all the screws in."
            mc "What do you mean \"like you?\""
            show winri disheveled
            Winri " I was made here too. Might be hard to believe, but I once didn’t have all these different parts. Though, I can’t really remember that time well."
            mc "You can’t remember?"
            Winri "I am outdated. I need so many new parts and software it seems like a headache to even think about fixing. My parts easily wear out and fall off, but I can always patch up. Though when I replace large or too many parts, there is a chance that I will lose a piece of my memories with it."
            mc "What-{w} Can’t the SCC help?"
            "As I say this I adjust the last screw and Winri flexes her wrist"
            Winri "The SCC won’t fund my upgrades, but that’s expected. There is new and better. They are probably waiting for me to completely break down and then will replace me with the newest tech."
            mc "What?! They can’t do that!"
            show winri happy
            Winri "That’s just the facts. But seriously, thank you for helping me. You really should consider joining Robojackets!"
            mc "Maybe I will."
            Winri "We should be at the org fair soon! Come learn more then okay?"
            "Winri starts walking me back to the entrance."
            mc "But-"
            Winri "No buts! They should see you there! Next time I see you should be in a meet! I have a lot to show you if you do decide to join!"

        "Not really":
            show winri confused
            Winri "Then why are you here?"
            "She looks at me confused."
            "I struggle to find any words."
            show winri disheveled
            Winri "You know what, it’s fine. Though, this place isn’t really for people to be wandering through.{w}Come look for the RoboJackets at the Org Fair that’s coming up okay?"
    hide winri
    "She walks me to the door and waves me off. I think I see her freeze for a moment through the glass."
    "But-{w} can she even leave here?"
    "Maybe I should try looking for ways to help Winri out."
    return
