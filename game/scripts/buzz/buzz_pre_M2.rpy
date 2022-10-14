label buzz_first_meeting:
    #(in hallway)

    #"<building name + room number>? Yup, this is it."
    #(transition to inside lecture hall)
    scene bg culc lecture:
        subpixel True
        xzoom 1.75 yzoom 1.75 zoom 1.5
    with fade
    "(Alright, 5 minutes until lecture begins.)"
    unknown "EXCUSE ME FELLOW STUDENT" #(1st run dialogue)
    "!" with hpunch
    #(screen rattle)
    unknown "Apologies my fellow student, I have startled you."
    #unknown "Greetings." (after completing 1 route)
    #(show Buzz with a pan up) figure this out later
    "(Woah, he’s huge. And that head…?)"
    "Oh no, I’m fine. What do you need?"
    "(Is he… the school’s mascot? Is that really just a costume? But it looks so real. Is he even human then? Is-)"
    unknown "I was going to ask if this is the lecture for Professor Rose?" #rework after M2 demo to work with the randomized class
    "Yeah, I think so."
    unknown "Thank you, fellow student."
    unknown "If I may ask, what is your name?"
    Buzz "My name is Nathan Harrison, but everyone calls me Buzz. This is my second year."
    "I’m [player_name], first year, nice to meet you Buzz."
    Buzz "Nice to meet you!" #(big smile)
    menu:
        "If you don’t mind me asking, what’s going on with your head?":
            call buzz_head
        "You seem to really like working out, eh?":
            call buzz_work_out
        "So where are you from?":
            call buzz_origin
    Buzz "It seems that our professor has arrived."
    Professor "Welcome to this course. I will be your professor. Please call me Doctor Rose."
    Professor "Today we will be covering the syllabus and some material."
    scene blackscreen
    with fade
    return

label buzz_head:
    Buzz "My head? Is there something strange about it?"
    "Uh, no, forget i said anything."
    return

label buzz_work_out:
    Buzz "I sure do! If you care to join me, I will be at the recreation center every day in the evening"
    "Cool, I will keep that in mind."
    return

label buzz_origin:
    Buzz "I am from Atnalta."
    "Atnalta? I’ve never heard of that place before."
    Buzz "No, you would not have."
    "?"
    Buzz "That is because it is in another dimension!"
    "(Oh. This guy is a weirdo.)"
    "Oh… yeah, that’s cool."
    return

label buzz_gym_1:
    Buzz "Hello [player_name], I see that you have come to the Campus Recreation Center."
    Buzz "Do you wish to join me in developing our muscles?"
    menu:
        "Oh, I’d love to!":
            jump work_out_with_buzz1
        "Sure, why not":
            jump work_out_with_buzz2
        "I’m only here to check out the place.":
            jump check_out_gym
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
