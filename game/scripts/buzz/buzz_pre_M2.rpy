label buzz_first_meeting:
    #(in hallway)

    #"<building name + room number>? Yup, this is it."
    #(transition to inside lecture hall)
    $ prev_location_img = current_location_img
    $ current_location_img = "bg " + current_location.lower() + " lecture"
    if renpy.has_image(current_location_img) and current_location_img != prev_location_img:
        scene expression current_location_img:
            xsize 1920
            ysize 1080
        with fade
    "Alright, 5 minutes until lecture begins."
    unknown "EXCUSE ME FELLOW STUDENT" #(1st run dialogue)
    mc "!" with hpunch
    #(screen rattle)
    unknown "Apologies my fellow student, I have startled you."
    #unknown "Greetings." (after completing 1 route)
    #(show Buzz with a pan up) figure this out later
    "Woah, he’s huge. And that head…?"
    mc "Oh no, I’m fine. What do you need?"
    "Is he… the school’s mascot? Is that really just a costume? But it looks so real. Is he even human then? Is-"
    unknown "I was going to ask if this is the lecture for Professor Rose?" #rework after M2 demo to work with the randomized class
    "Yeah, I think so."
    unknown "Thank you, fellow student."
    unknown "If I may ask, what is your name?"
    Buzz "My name is Nathan Harrison, but everyone calls me Buzz. This is my second year."
    mc "I’m [player_name], first year, nice to meet you Buzz."
    Buzz "Nice to meet you!" #(big smile)
    $ all_menu = [True, True, True]
label buzz_menu_loop:
    menu:
        "If you don’t mind me asking, what’s going on with your head?" if all_menu[0]:
            $ all_menu[0] = False
            Buzz "My head? Is there something strange about it?"
            mc "Uh, no, forget I said anything."
            jump buzz_menu_loop
        "So where are you from?" if all_menu[1]:
            $ all_menu[1] = False
            Buzz "I am from Atnalta."
            "Atnalta? I’ve never heard of that place before."
            Buzz "No, you would not have."
            mc "?"
            Buzz "That is because it is in another dimension!"
            "Oh. This guy is a weirdo."
            mc "Oh… yeah, that’s cool."
            jump buzz_menu_loop
        "You seem to really like working out, eh?" if all_menu[2]:
            $ all_menu[2] = False
            Buzz "I sure do! If you care to join me, I will be at the recreation center every day in the evening, come join me sometime!"
            mc "Cool, I will keep that in mind."
            jump buzz_menu_loop
    Buzz "It seems that our professor has arrived."
    Professor "Welcome to this course. I will be your professor. Please call me Doctor Rose."
    Professor "Today we will be covering the syllabus and some material."
    "I proceed to listen to the teacher droning on about a wide range of topics, none of which are remotely interesting. {w}{b}+10 BRAIN{/b}"
    $ brain += 10
    $ AP -= 3
    # scene blackscreen
    # with fade
    return

label buzz_gym_1:
    Buzz "Hello [player_name], I see that you have come to the Campus Recreation Center."
    Buzz "Do you wish to join me in developing our muscles?"
    menu:
        "Oh, I’d love to!":
            call work_out_with_buzz1
        "Sure, why not":
            call work_out_with_buzz2
        "I’m only here to check out the place.":
            call check_out_gym
    return
label work_out_with_buzz1:
    Buzz "Wonderful!" #(insert cg of working out?)
    hide Buzz
    scene blackscreen with fade
    "I spent the afternoon vigorously working out with Buzz"
    $ AP -= 4
    $ brawn += 15
    return

label work_out_with_buzz2:
    Buzz "Alright, let’s get you started."
    hide Buzz with fade
    "I spent the afternoon working out with Buzz."
    $ AP -= 3
    $ brawn += 10
    return

label check_out_gym:
    Buzz "That is a shame. Then farewell until next time."
    "Later."
    hide Buzz
    with wipe
    "I explored the CRC and saw the various machines and the pools."
    $ AP -= 1
    return

label buzz_dorm_1:
    Buzz "We meet again, Burdell!"
    "Oh, hi there."
    Buzz "What brings you here, Burdell?"
    "I live here."
    Buzz "I see, I see. I was here to visit a friend. May I accompany you for the afternoon?"
    menu:
        "Sure":
            jump dorm_tour_with_buzz
        "Sorry, I actually have something I need to do":
            jump no_dorm_tour
    return

label no_dorm_tour:
    Buzz "Oh… that is a shame." #(disappointed expression)
    Buzz "Well then, until we meet again, Burdell."
    "See you later."
    hide Buzz with fade
    return

label dorm_tour_with_buzz:
    scene blackscreen with fade
    "I showed Buzz around my room znd we made small talk"
    $ AP -= 1
    return
