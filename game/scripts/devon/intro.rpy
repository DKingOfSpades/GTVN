
label club_fair_collision:
    # I can't think of any changes that need to happen with the background but put them here if needed.

    "Man, this org fair is PACKED."

    "It's hard to figure out where anything is."

    show devon neutral at center with moveinright:
        zoom 0.75

    "!!" with hpunch

    "Shoot. Did I bump into someone?"

    "Guess I have to be careful with the Burdell-family gunshow."

    "I saw a flash of green and a panicked expression."

    unknown "Owww..."

    "Oh, it's a guy with green hair. Holding flyers? Or well, he probably was before I knocked him over."

    "That's smart. You don't have to go to them, cause they go to you."

    "Might as well hear what’s up with his club after giving him so much trouble."

    "His nametag says...Devon."

    show devon happy

    VGDev "S-sorry about that!"

    VGDev "I really need to look where I’m going…"

    menu:
        "It's fine, what club are you advertising for?":
            show devon cheerful
            VGDev "Oh, uh, the video game club!"
            VGDev "I’m actually one of the people who’re planning to make games."
            VGDev "We’re all supposed to hand out these flyers."
            mc "Your stack seems pretty thick."
            VGDev "Uh, yeah, I actually haven't passed any flyers out."
            VGDev "Don't wanna come on too strong, y'know?"
            VGDev "Might scare people away."
            mc "What game are you planning to make?"
            "He winces."
            VGDev "As much as I'd love to tell you that (and I really would LOVE to), we have to keep those a secret."
            VGDev "I'm really proud of the concept though. You should definitely consider joining me."
            mc "Can I have a flyer?"
            VGDev "Sure!"
            show vgdev poster with moveinbottom:
                xalign 0.9
                yalign 0.5
                zoom 0.5
            "He hands me a flyer."
            "VGDev: We make games.{p}Check us out at Howey L3 this Friday Evening!"
            hide vgdev poster
            VGDev "Well, I'll be seeing you!"
            VGDev "Feel free to check out our table for any questions or to meet Little Guy!"
            hide devon
        "It's fine, see you around.":
            VGDev "Oh, uh, bye!"
        "Be more careful, idiot.":
            "He frowns, picks up his flyers, and runs off."
            "Great work! Just. Stellar job there."
    return

label game_presentation:
    $ prev_location_img = current_location_img
    $ current_location_img = "bg " + current_location.lower() + " lecture" # Should only ever be Howey, but I'm too lazy to code myself
    if renpy.has_image(current_location_img) and current_location_img != prev_location_img:
        scene expression current_location_img:
            xsize 1920
            ysize 1080
        with fade

    show lilguy point talk left with moveinbottom:
        xalign 0.8
    LilGuy "Welcome everyone, to our inaugural VGDev meeting!"

    "The room erupts with claps and cheers."

    LilGuy "I will be your club president, Lil Guy. Today, we will be hearing our 6 game leads pitch each of their games."

    LilGuy "We’re going to let this wheel decide who presents first. On the count of 3, I want everybody to shout “SPIN THAT WHEEL!” with me. Ready?"

    "A few pitches happen, and they seem generally interesting. But I'm not here for them." with wipe

    LilGuy "Thank you Ren and your game MeteorRise!" with fade

    LilGuy "And that was Joon with Grove!" with fade

    LilGuy "A round of applause for Andrew and Sanguine Service!" with fade

    LilGuy "Thank you Case and Meowlchemy!" with fade

    LilGuy "And that was Adbel with Wet!" with fade

    "Oh, Devon's finally up." with fade

    VGDev "Um, hi."

    VGDev "I’m Devon."

    "Alright, man. Focus. You can do this!"

    VGDev "My game is called QSVN."

    VGDev "That’s a provisional title."

    VGDev "The game takes place in the fictional college of Quinton State University."

    VGDev "You are a freshman hoping to find passion, and maybe even love!"

    VGDev "This happens to be a massive collaborative effort, between this club, VGDev, Anime O’Tekku, and potentially more as we go on!"

    VGDev "Each club will craft their own fictional representation of themselves to put into the game."

    VGDev "Before I show off the demo, I’ve made plenty of time for questions!"

    "An audience member raises their hand."

    "That's relieving."

    "I thought I'd have to do the legwork."

    VGDev "Yes?"

    "Anonymous Rabblerouser" "AY CAN YOU BANG THE CHICKS BRO"

    "...oh."

    "Devon seems a bit surprised at the question, and takes a moment to respond."

    VGDev "Um, we’re not going to be adding anything past PG-13 to the game."

    VGDev "The college might take issue with us doing that, so I’ve decided to play it safe."

    "...note to self, he can’t ad-lib."

    "..."

    "Wow, it’s silent in here."

    "Almost like the room isn’t packed."

    "...come on, people, one of you has to have a question."

    "Look at the poor guy, he looks like he’s about to explode."

    "Maybe now’s my time to step in."

    menu:
        "Help him":
            VGDev "Yes, you in the back?"

            "Alright!"

            mc "So, what are some of the clubs you want to add to this game?"

            VGDev "Great question! So…"

            "That got him REALLY fired up."

            "Further note to self: he can talk about games and game design."

            VGDev "…so, that’s the answer."

            "Alright, alright! Looks like the room is talking now!"

            VGDev "Here’s a quick demo! Enjoy~"
        "Leave him":
            "Nah, he can handle this."

            "..."

            "Wow, still nothing huh."

            "Looks like he gave up."

            VGDev "...anyways, here’s the demo."

    "Alright, time to see how this is gonna look."

    "Oh, original intro music?"

    "He's got sprites done too!"

    "And effects!"

    "This looks pretty complete."

    "MAN, this guy is good at what he does!"

    "I can only imagine how fun this game is gonna be once he has a whole team at his fingertips!"

    "Alright, the place is a good bit more fired up!"

    "He’s definitely going to have at least a few people on board!"

    VGDev "And here’s the QR code for the Biscord server!"

    "Alright, let me get my phone out…"

    "Huh. Doesn’t seem like too many people are getting their phones out. Wonder why."

    "The rest of the presentations pass by normally, and the meeting ends with energy." with wipe

    "Okay, better go congratulate him."

    "He did well, especially considering how reserved he seemed when we first met."

    VGDev "Oh, hi."

    VGDev "...wait a minute."

    VGDev "It’s you! The guy who shoved me during the org fair!"

    "Yikes, these glares are going right through me."

    "Better clarify."

    mc "D-don't worry. It was an accident. We're chill."

    "The glares soften and everyone turns back to Devon."

    VGDev "Alright, what years are you all in?"

    "First."

    "First year!"

    "Freshman..."

    "Interesting. Only first years. Wonder why."

    VGDev "If you’ve all joined the Biscord, there’s not much I have for you. Later."

    "He left..."

    "I should keep tabs on him. See what he gets up to."

    VGDev "Oh, wait!"

    "Hm?"

    "I forgot to ask your name. Or if I did I forgot it. I always do this."

    "It's [player_name]."

    "Alright. Thanks again!"
    return

label first_dev_meeting:
    "Alright, I'm here."

    "I can't say the place is packed, but there's still a good few people here."

    "Oh, Devon waved."

    "Seems like he's about to start."

    "I'll just find a seat..."

    VGDev "Hi everyone."

    VGDev "This'll be the first meeting for QSVN."

    VGDev "So far, I have a form ready to catalog what everyone wants to do."

    VGDev "I'll post it in the Biscord."

    VGDev "Anyways, here's some of my goals for this development cycle."

    VGDev "I want a few more weeks, obviously."

    VGDev "I also want a soundtrack beyond one song."

    VGDev "Finally, I want some more enemies."

    VGDev "I've created a Drello board for all the tasks I want to get done."

    VGDev "Once you all sign up, we can use the Biscord to assign specific tasks."

    VGDev "I'll monitor you all as you progress."

    VGDev "Remember, get your things done in a timely manner, everyone!"

    VGDev "If we want this game to reach its initial goal quickly, we will need everyone to finish their individual tasks quickly."

    VGDev "If we do that, we can add even more to the game, and go beyond my initial vision."

    VGDev "But. I’m getting ahead of myself."

    VGDev "Here's a bit of information regarding what I want from the game."

    with fade

    "Wow, this is a lot of detail."

    "Can't call this a bit of information in any stretch of the imagination."

    "He seems pretty deadset on what he wants from the game."

    "Wonder how the others feel..."

    "...hey, where'd some of them go?"

    "And why do the others look so angry?"

    "I'll have to ask one of them as we go out."

    with fade

    VGDev "Alright, that's about all I have for you! Meeting adjourned!"

    "As people leave, they mumble complaints among themselves."

    "\"I thought I'd get to contribute...\""

    "\"I had some great ideas...\""

    "\"I wanted to put ඞ into the game...\""

    "I'll ignore wondering how you say that."

    "Point is, seems like people aren't getting what they wanted out of this."

    "Perhaps I should broach the topic with Devon the next time we speak."
    return
