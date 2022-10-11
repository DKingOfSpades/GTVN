# Helpful Tips

# Place under image scene or show to tint:
# matrixcolor TintMatrix("<hexcode color>")


init -100 python:
    register_stat("Brain", "brain")
    register_stat("Brawn", "brawn")
    register_stat("Charm", "charm")
    register_stat("Guts", "guts")
    register_stat("Honey", "honey")
    register_stat("Fatigue", "fatigue", 0, 6)
    register_stat("Perception", "perception", hidden=True)
    # all events in dse-events.rpy depend on this variable
    AP = 0

    # Morning
    dp_period("Morning", "morning_act")
    dp_choice("Attend Class", "class")
    dp_choice("Eat", "eat", show="\"Dining\" in current_location")
    dp_choice("Study", "study", show="\"Dorm\" in current_location or current_location == \"Crossland\" or current_location == \"CULC\" or current_location == \"Student Center\"")
    dp_choice("Exercise", "exercise", show="\"Dorm\" in current_location or current_location == \"Tech Green\" or current_location == \"Burger Bowl\" or current_location == \"Campus Recreation Center\"")
    dp_choice("Sleep In", "sleepin", show="fatigue > 0 and \"Dorm\" in current_location")
    dp_choice("Travel", "travel")
    dp_choice("Talk to ...", "talk")
    dp_choice("Text ...", "text")
    dp_choice("Call ...", "calling")
    dp_choice("Discover", "discover")

    # Noon
    dp_period("Noon", "noon_act")
    dp_choice("Listen to Lecture", "class")
    dp_choice("Eat", "eat", show="\"Dining\" in current_location")
    dp_choice("Study", "study", show="\"Dorm\" in current_location or current_location == \"Crossland\" or current_location == \"CULC\" or current_location == \"Student Center\"")
    dp_choice("Exercise", "exercise", show="\"Dorm\" in current_location or current_location == \"Tech Green\" or current_location == \"Burger Bowl\" or current_location == \"Campus Recreation Center\"")
    dp_choice("Nap", "nap", show="fatigue > 0")
    dp_choice("Travel", "travel")
    dp_choice("Talk to ...", "talk")
    dp_choice("Text ...", "text")
    dp_choice("Call ...", "calling")
    dp_choice("Discover", "discover")

    # Evening
    dp_period("Evening", "evening_act")
    dp_choice("Attend Lecture", "class")
    dp_choice("Eat", "eat", show="\"Dining\" in current_location")
    dp_choice("Study", "study", show="\"Dorm\" in current_location or current_location == \"Crossland\" or current_location == \"CULC\" or current_location == \"Student Center\"")
    dp_choice("Exercise", "exercise", show="\"Dorm\" in current_location or current_location == \"Tech Green\" or current_location == \"Burger Bowl\" or current_location == \"Campus Recreation Center\"")
    dp_choice("Nap", "nap", show="fatigue > 0")
    dp_choice("Travel", "travel")
    dp_choice("Talk to ...", "talk")
    dp_choice("Text ...", "text")
    dp_choice("Call ...", "calling")
    dp_choice("Discover", "discover")

    # Night
    dp_period("Night", "night_act")
    dp_choice("Sleep", "sleep", show="\"Dorm\" in current_location")
    dp_choice("Eat", "eat", show="\"Dining\" in current_location")
    dp_choice("Study", "study", show="\"Dorm\" in current_location or current_location == \"Crossland\" or current_location == \"CULC\" or current_location == \"Student Center\"")
    dp_choice("Exercise", "exercise", show="\"Dorm\" in current_location or current_location == \"Tech Green\" or current_location == \"Burger Bowl\" or current_location == \"Campus Recreation Center\"")
    dp_choice("Travel", "travel")
    dp_choice("Talk to ...", "talk")
    dp_choice("Text ...", "text")
    dp_choice("Call ...", "calling")
    dp_choice("Discover", "discover")

# Game start
label start:

    call intro_faset

    scene bg tech tower:
        subpixel True blur 5.0
        xzoom 1.15 yzoom 1.15 zoom 1.5
    # play music "audio/bgm_waiting.mp3" fadein 1.0 volume 0.5
    stop music
    call bgm_campus_start
    $ current_location = "Dorms"
    $ current_x = 1568
    $ current_y = 490
    $ AP = 10
label day:
    $ show_date = False
    # Increment the day and check for month changes.
    call next_day_check

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = None
    $ noon_act = None
    $ evening_act = None
    $ night_act = None


    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.

    # call screen day_planner(["Morning", "Noon", "Evening", "Night"])

# We process each of the three periods of the day, in turn.
    $ AP = 10 - fatigue
    $ hungry = True
    call bgm_period_change_morning
label morning:

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below.
    $ period = "Morning"
    $ sleep_in_check = False
    $ show_date = True
    call screen day_planner("Morning")
    $ act = morning_act

    # Execute the events for the morning.

    call events_run_period

    "AP: [AP]"

    if AP > 0:
        $ sleep_in_check = True
        jump morning

    # That's it for the morning, so we fall through to the
    # afternoon.
    $ AP = 10 - fatigue
    call bgm_period_change_noon
label noon:

    # It's possible that we will be skipping noon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the noon.
    if check_skip_period():
        call bgm_period_change_evening
        jump evening

    # The rest of this is the same as for the morning.

    $ period = "Noon"
    $ show_date = True
    call screen day_planner("Noon")
    $ act = noon_act

    call events_run_period

    if AP > 0:
        jump noon

    $ AP = 10 - fatigue
    call bgm_period_change_evening
label evening:

    # The evening is the same as the noon.
    if check_skip_period():
        call bgm_period_change_night
        $ fatigue+=1
        jump night

    $ period = "Evening"
    $ show_date = True
    call screen day_planner("Evening")
    $ act = evening_act

    call events_run_period

    if AP > 0:
        jump evening

    $ AP = 10 - fatigue
    $ fatigue+=1
    call bgm_period_change_night
label night:

    if check_skip_period():
        $ AP = 3

    $ period = "Night"
    $ sleep_check = False
    $ show_date = True
    call screen day_planner("Night")
    $ act = night_act

    call events_run_period

    if sleep_check:
        jump day
    if AP > 0:
        jump night

    "Oh no, I accidentally pulled an allnighter..."

    $ fatigue+=2

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day

    camera:
        perspective True
    play music "audio/bgm_waiting.mp3" fadein 1.0 volume 0.5
    "Welcome to the first demo for a dating sim featuring O'Tekku-chan and VGDev-san!"
    "This is a collab game between VGDev and Anime O’Tekku."
    "It will be a dating sim/visual novel that introduces players to the neat things around campus with a personalized tour with a lot of GT inside jokes and stuff, as you visit different notable spots in campus."
    "There are two love interests planned so far:"
    show otekku excited:
        subpixel True anchor (-550, -179) zoom 1.5
    "O\'Tekku-chan is a deredere (supportive and positive), a workaholic that sacrifices sleep for study but never sacrifices the time she spends watching anime and geeking out with others"
    "Hence her innate need for coffee, also a bit smug, and when she gets really tired and stressed, she becomes nihilistic"
    hide otekku
    show vgdev excited
    "VGDevsan is kuudere (cool and dependable) that is very knowledgeable in game development and skilled in organizing team projects. He’s a bit goofy, but comes off as cool when hes talking about his passion, games and their development"
    hide vgdev
    "More love interests will be added with enough interest from other clubs coming to collab for this game"
    show buzz excited:
        subpixel True anchor (-400, -250) zoom 1.3
    "Buzz will be an awesome wingman that’ll help you get with one of the love interests"
    hide buzz
    "We’ll be using RenPy as our engine, which includes almost all the bare essentials to a visual novel. The other work to do will be scripting/writing, music/sfx, and artwork. 5 endings planned so far, a route for each love interest, no love interest, a difficult to get Buzz route, and the hardest to get harem route."
    $ affection = 2

    show otekku excited:
        subpixel True anchor (-550, -179) zoom 1.5
    Otekku "Heyyyyyy senpai!"
    Otekku "Saw you at the corner of my eye!"
    Otekku "Burdell-san, would you want to have lunch with me off-campus?"

label otekku_lunch_selection:
    show otekku shy:
    Otekku "I've been meaning to hang out with you for a while, since we've come back to campus and all."
    $ hungry = True
menu:
    "Yeah sure, I'd be down to hang and eat, my treat.":
        jump otekku_lunch_a
    "I'm running a bit low on money right now, can we just eat at the dining hall?":
        jump otekku_lunch_b
    "Sorry, Ive already eaten lunch, maybe another time?":
        jump otekku_lunch_c

label otekku_lunch_a:
    "path not scripted yet"
    $ hungry = False
    jump otekku_lunch_selection_common

label otekku_lunch_b:
    show extra normal at left
    "Random Girl" "Bruh the dining halls suck ass"
    hide extra
    show otekku frustrated
    Otekku "..."
    jump otekku_lunch_selection_common

label otekku_lunch_c:
    show otekku sad with dissolve
    Otekku "I see then... I guess I'll see you later today at club!"
    $ affection -= 1
    jump otekku_lunch_selection_common

label otekku_lunch_selection_common:
    "yada yada, bastetball game go"
label background:
    Otekku "Come on! Let's go the gym."
    scene bg gym with fade

    show otekku outofshape at left
    Otekku "You got here faster than I did!"
label bgm:
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 0.5
    Otekku "Oh, the basketball team is playing?"
    Otekku "It's too loud. I'll meet you in the studio."

    stop music fadeout 1.0
    scene bg classroom
    with fade

label sfx_example:
    "The two of you are in the same class"
    play sound "audio/sfx_whistle_short.mp3"
    show otekku sad
    Otekku "Awww. It's already time."

    if hungry:
        Otekku "I still havent eaten anything today, see ya!"
    else:
        Otekku "Wanna get some thing small to eat?"

    if affection < 2:
        "You feel like your affection with her has decreased a bit today."
