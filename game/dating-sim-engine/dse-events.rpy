# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.

# TODO: add our events


# Declare characters. The color argument colorizes the
# name of the character.
init:
    $ t = Character('Teacher')
    $ gg = Character('Glasses Girl', color=(192, 255, 192, 255))
    $ sg = Character('Sporty Girl', color=(255, 255, 192, 255))
    $ bg = Character('Both Girls')
    $ narrator = Character(' ')

    $ Otekku = Character('O\'Tekku-chan', image="otekku", color="#FFD700")
    $ VGDev = Character('VGDev-san', image="vgdev", color="#64C617")
    $ Buzz = Character('Buzz', image="buzz", color="#FFD700")
    $ Winri = Character('Winri', image="winri", color="#B87333")

    $ LilGuy = Character("VGDev President", color="#FF8733")
    $ unknown = Character('?', color="#867900")
    $ Professor = Character("Professor", color="#444444")
    $ Ralph = Character('Ralph', image="ralph", color="#FFD700")

init:
    # First up, we define some simple events for the various actions, that
    # are run only if no higher-priority event is about to occur.

    $ event("class", "act == 'class'", event.only(), priority=200)
    $ event("class_continue", "act == 'class'", priority=210)
    $ event("study", "act == 'study'", event.solo(), priority=200)
    $ event("hang", "act == 'hang'", event.solo(), priority=200)
    $ event("exercise", "act == 'exercise'", event.solo(), priority=200)


    $ event("nap1", "act == 'nap'", event.choose_one('nap'), priority=200)
    $ event("nap2", "act == 'nap'", event.choose_one('nap'), priority=200)
    $ event("nap3", "act == 'nap' and fatigue > 2", event.choose_one('nap'), priority=200)
    $ event("travel", "act == 'travel'", event.only(), priority=200)
    $ event("talk", "act == 'talk'", event.only(), priority=200)
    $ event("text", "act == 'text'", event.only(), priority=200)
    $ event("calling", "act == 'calling'", event.only(), priority=200)
    $ event("discover", "act == 'discover'", event.only(), priority=200)
    $ event("sleep", "act == 'sleep'", event.only(), priority=200)
    $ event("sleepin", "act == 'sleepin'", event.only(), priority=200)
    $ event("eat", "act == 'eat'", event.solo(), priority=200)

    # These are Buzz's events
    $ event("buzz_first_meeting", "act == 'class'", event.once(), event.only())
    $ event("buzz_gym_1", "act == 'exercise'", "period == 'evening'", event.once(), event.depends("buzz_first_meeting"), event.only())
    $ event("buzz_dorm_1", "act == 'hang'", "current_location == 'Dorms'", "theweekday == 'Sunday'", "period == 'noon'", event.once(), event.depends("buzz_first_meeting"), priority=180) #possibly placeholder until it has a better spot

    # This is an first winri event, that runs once when we first go to class.
    $ event("robot_gal", "act == 'class'", event.once(), event.only())
    $ event("lend_a_hand", "act == 'talk' and current_location == 'Student Competition Center'", event.once(), event.depends("robot_gal"), event.only())

    # This is an first otekku event, that runs once when we first discover.
    $ event("biscord_gremlin", "act == 'discover'", event.once(), event.only())

    # ralph the rambling wreck
    $ event("hit_and_run", "act == 'travel' and current_location == 'Tech Green' and period != 'night'", event.once(), event.only())

    # vgdev events
    # $ event ("club_fair_day", "day == 25 and month == 8 and current_location == \"Tech Green\"")
    $ event("club_fair_collision", "act == 'discover' and day == 24 and month == 8 and current_location == \"Tech Green\"", event.once(), event.only())
    $ event("game_presentation", "act == 'discover' and theweekday == \"Friday\" and month == 8 and period == \"Evening\" and current_location == \"Howey\"", event.once(), event.only(), event.depends("club_fair_collision"))
    $ event("first_dev_meeting", "act == 'gamedev'", event.once(), event.only(), event.depends("game_presentation"))


# General events
label nap1:

    "A little nap can't hurt, can it?"
    $ fatigue -= 2

    "This time, I got so much energy back! {w}{b}-2 Fatigue{/b}"

    $ AP -= renpy.random.randint(3, 7)

    return

label nap2:

    "A little nap can't hurt, can it?"
    $ fatigue -= 1

    "I feel a little better rested at least. {w}{b}-1 Fatigue{/b}"

    $ AP -= renpy.random.randint(1, 5)

    return

label nap3:

    "A little nap can't hurt, can it?"
    $ fatigue -= 2

    # This will end the current period and skip the next one.
    jump events_skip_period

    "Oh god, what is the time?!?! Did I oversleep?{p}{b}-2 Fatigue{/b}"
    $ AP = 10 - fatigue

    return

label travel:

    "I should probably head somewhere else..."

    $ prev_x = current_x
    $ prev_y = current_y

    call screen map_screen

label talk:

    "Who would you like to talk to?"

    "todo: choice dialougue screen for the different available npc options located at your location"

    "then trigger an event inside another event"

    $ AP -= 0

    return

label text:

    "Who would you like to text?"

    "todo: choice dialougue screen for the different available npc options to text"

    "then trigger an event inside another event"

    $ AP -= 1

    return

label calling:

    "Who would you like to call?"

    "todo: choice dialougue screen for the different available npc options to call"

    "then trigger an event inside another event"

    $ AP -= 2

    return

label discover:

    "not yet implemented, but will have you either meet a new character or discover a new location on the map"

    "if there are no more locations to be discovered, return nothing"

    $ AP -= 2

    return

label sleep:
    $ prev_location_img = current_location_img
    $ current_location_img = "bg dorm"
    if renpy.has_image(current_location_img) and current_location_img != prev_location_img:
        scene expression current_location_img:
            xsize 1920
            ysize 1080
        with fade

    if AP > 4:
        "Might as well go to sleep early to get some more energy for tomorrow. {w}{b}-2 Fatigue{/b}"
        $ fatigue -= 2
    else:
        "I guess I'll plop into my bed and get ready for a good night's sleep. {w}{b}-1 Fatigue{/b}"
        $ fatigue -= 1

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    $ sleep_check = True

    return

label sleepin:


    "I don't really feel like doing much this morning, so let's just sleep in. {w}{b}-1 Fatigue{/b}"
    $ fatigue -= 1

    # This will end the current period.
    call events_end_period

    $ sleep_in_check = True

    return

label eat:

    "You eat at the dining hall. It was mediocre at best, like usual."

    "You leave feeling satiated."

    $ hungry = False

    $ AP -= 2

    return

label class:
    $ prev_location_img = current_location_img
    $ current_location_img = "bg " + current_location.lower() + " lecture"

    if renpy.has_image(current_location_img) and current_location_img != prev_location_img:
        scene expression current_location_img:
            xsize 1920
            ysize 1080
        with fade
    "I make it to class just in time, and proceed to listen to the teacher droning on about a wide range of topics, none of which are remotely interesting. {w}{b}+10 BRAIN{/b}"
    $ brain += 10
    $ AP -= 3

    return

# For when event still happens.
label class_continue:

    "I proceed to listen to the teacher droning on about a wide range of topics, none of which are remotely interesting. {w}{b}+10 BRAIN{/b}"
    $ brain += 10
    $ AP -= 3

    return

label study:

    "I open up my textbooks, and start reading about the topics I should have been reading about in class. {w}{b}+10 BRAIN{/b}"

    $ brain += 10
    $ AP -= 3

    return

label hang:

    "I spend the afternoon hanging out with my friends, killing some time. {w}{b}+10 CHARM{/b}"

    $ charm += 10
    $ AP -= 3

    return

label exercise:

    "I decide to go out for a run to keep myself in shape. {w}{b}+10 BRAWN{/b}"

    $ brawn += 10
    $ AP -= 3

    return
