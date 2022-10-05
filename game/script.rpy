# Helpful Tips

# Place under image scene or show to tint:
# matrixcolor TintMatrix("<hexcode color>")

# Declare characters. The color argument colorizes the
# name of the character.
default Otekku = Character('O\'Tekku-chan', image="otekku", color="#FFD700")
default VGDev = Character('VGDev-san', image="vgdev", color="#64C617")
default Buzz = Character('Buzz', image="buzz", color="#FFD700")
# Game start
label start:
    $ current_location = ""
    call intro_faset
    camera:
        perspective True
    scene bg tech tower:
        subpixel True blur 5.0
        xzoom 1.15 yzoom 1.15 zoom 1.5
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
    default affection = 2

    show otekku excited:
        subpixel True anchor (-550, -179) zoom 1.5
    Otekku "Heyyyyyy senpai!"
    Otekku "Saw you at the corner of my eye!"
    Otekku "Burdell-san, would you want to have lunch with me off-campus?"

label otekku_lunch_selection:
    show otekku shy:
    Otekku "I've been meaning to hang out with you for a while, since we've come back to campus and all."
    default hungry = True
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
