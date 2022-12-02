
label club_fair_collision:
    # I can't think of any changes that need to happen with the background but put them here if needed.

    "Man, this org fair is PACKED."

    "It's hard to figure out where anything is."

    show devon neutral at center with moveinright:
        zoom 0.75
    call bgm_devon_start
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
            call devon_menu

            VGDev "Well, I'll be seeing you!"
            VGDev "Feel free to check out our table for any questions or to meet Little Guy!"
            hide devon
        "It's fine, see you around.":
            VGDev "Oh, uh, bye!"
        "Be more careful, idiot.":
            "He frowns, picks up his flyers, and runs off."
            "Great work! Just. Stellar job there."
    return
label devon_menu:
    $ all_menu = [True, True, True]
label devon_menu_loop:
    menu:
        "Your stack seems pretty thick." if all_menu[0]:
            $ all_menu[0] = False
            VGDev "Uh, yeah, I actually haven't passed any flyers out."
            VGDev "Don't wanna come on too strong, y'know?"
            VGDev "Might scare people away."
            jump devon_menu_loop
        "What game are you planning to make?" if all_menu[1]:
            $ all_menu[1] = False
            "He winces."
            VGDev "As much as I'd love to tell you that (and I really would LOVE to), we have to keep those a secret."
            VGDev "I'm really proud of the concept though. You should definitely consider joining me."
            jump devon_menu_loop
        "Can I have a flyer?" if all_menu[2]:
            $ all_menu[2] = False
            VGDev "Sure!"
            show vgdev poster with moveinbottom:
                xalign 0.9
                yalign 0.5
                zoom 0.5
            "He hands me a flyer."
            "VGDev: We make games.{p}Check us out at Howey L3 this Friday Evening!"
            hide vgdev poster
            jump devon_menu_loop
    call bgm_char_end
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
        xoffset 600
    LilGuy "Welcome everyone, to our inaugural VGDev meeting!"

    show lilguy jum smile left
    "The room erupts with claps and cheers."
    show lilguy stand exasperated left
    LilGuy "I will be your club president, Lil Guy. Today, we will be hearing our 6 game leads pitch each of their games."
    show lilguy point panic left
    LilGuy "We’re going to let this wheel decide who presents first. On the count of 3, I want everybody to shout “SPIN THAT WHEEL!” with me. Ready? (TODO: wheel animation)"
    LilGuy "3"
    LilGuy "2"
    LilGuy "1"
    "Everyone" "SPIN THAT WHEEL!"

    LilGuy "Alright, first up is Ren!"
    "Ren" "Hello. I’m Ren, and this is MeteorRise."
    "Ren" "What is MeteorRise you ask?"
    "Ren" "MeteorRise is a 2nd person bullet hell platform shooter."
    "Ren" "In this world, witches are set across worlds to cull aliens and angels."
    "Ren" "Mercenaries of the corporation SERV…"
    show lilguy jum smile right with move and fade:
        xoffset -600
    LilGuy "Thank you Ren and your game MeteorRise!"
    LilGuy "Moving on! 3! 2! 1!"
    "Everyone" "SPIN THAT WHEEL!"
    LilGuy "And our next pitch will be Joon!"
    "Joon" "Hello everyone. I’m Joon."
    "Joon" "This is Grove, a mystical 3D bullet hell rogue-like adventure set in a distant grove where an college party is being held."
    "Joon" "You play as a spirit that will explore the grove and eliminate bad vibes, and…"
    show lilguy point panic left with move and fade:
        xoffset 600
    LilGuy "Thank you very much, Joon. On 1! 3! 2! 1!"
    "Everyone" "SPIN THAT WHEEL!"
    LilGuy "And it lands on Android!"
    "Android" "Uh, hi. This is going to be quick so let’s see if I can do this."
    "Android" "My game is Sanguine Service. It will be a 3D first person puzzle shooter set in a maid cafe in hell."
    "Android" "In the story, we are in a dystopian future where our protagonist is playing in a game show with their life on the line."
    "Ooh, that sounds a little like Octopus Game in certain ways."
    "Android" "And must serve cold vengance dishes to the angel customers you encounter, while pleasing demons with your cooking…"
    show lilguy jum pout right with move and fade:
        xoffset -600
    LilGuy "A round of applause for Android and Sanguine Service!"
    LilGuy "Alright, let’s find out who’s next."
    "Everyone" "SPIN THAT WHEEL!"
    LilGuy "Next up is Case!"
    "Case" "Hey, I’m Case, and this is Meowlchemy: The Moment of Catastrophe."
    "Case" "Meowlchemy is a 3D rougue-like puzzle game with a fantastical cat."
    "Case" "Her name is Tangerine."
    "Cute!"
    "Case" "You'll get to combine wierd and wacky elements to find to create chemical reactions of all sorts."
    "Case" "As for what we are looking for for our team…"
    show lilguy point panic left with move and fade:
        xoffset 600
    LilGuy "Thank you Case for Meowlchemy!"
    LilGuy "Only 2 left! Let’s pick up that energy a bit. 3! 2! 1!"
    "Everyone" "SPIN THAT WHEEL!"
    LilGuy "And next up we have Abdel!"
    "Abdel" "Just a heads up, my presentation isn’t going to look as great as everyone else’s"
    "Abdel" "Moist is a rougelike horror game. Its main mechanic will be travesing the deeps of the sea in your submarine."
    "Abdel" "Also, Wet will be made in Existential engine"
    "Oh, so it’s going to be written in C++. That sounds hard."
    "Abdel" "Now as for design…"
    show lilguy stand surprise right with move and fade:
        xoffset -600
    LilGuy "And that was Adbel with Moist!"
    LilGuy "And for the last one, say it with me!"
    "Everyone" "SPIN THAT WHEEL!"

    "Oh, Devon's finally up."
    hide lilguy
    show devon neutral at center with moveinright:
        zoom 0.75
    call bgm_devon_start
    VGDev "Um, hi."

    VGDev "I’m Devon."

    "Alright, man. Focus. You can do this!"

    VGDev "My game is called QSVN."

    VGDev "That’s a provisional title."

    VGDev "The game takes place in the fictional college of Quinton State University."

    VGDev "You are a freshman hoping to find passion, and maybe even love!"

    VGDev "This happens to be a massive collaborative effort, between this club, VGDev, Anime O’Tekku, and potentially more as we go on!"

    VGDev "Each club will craft their own fictional representation of themselves to put into the game."

    show devon happy

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

    $ helped = False

    menu:
        "Help him":
            show devon cheerful

            VGDev "Yes, you in the back?"

            "Alright!"

            mc "So, what are some of the clubs you want to add to this game?"

            VGDev "Great question! So…"

            "That got him REALLY fired up."

            "Further note to self: he can talk about games and game design."

            VGDev "…so, that’s the answer."

            "Alright, alright! Looks like the room is talking now!"

            VGDev "Here’s a quick demo! Enjoy~"

            $ helped = True
        "Leave him":
            "Nah, he can handle this."

            show devon neutral

            "..."

            "Wow, still nothing huh."

            "Looks like he gave up."

            VGDev "...anyways, here’s the demo."

    show devon cheerful
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

    "The rest of the presentations pass by normally, and the meeting ends with energy."

    show devon neutral

    "Okay, better go congratulate him."

    "He did well, especially considering how reserved he seemed when we first met."

    show devon happy

    VGDev "Oh, hi."

    VGDev "...wait a minute."

    show devon neutral

    VGDev "It’s you! I bumped into you at the org fair!"

    if helped:
        show devon happy
        VGDev "T-thanks for the help."
        VGDev "I uh, wasn’t expecting that."
    show devon neutral
    VGDev "Thanks for swinging by! How did you like the demo? I've been working on it myself for a week now."

    mc "I loved it! I hope we can work together on this!"

    VGDev "Alright, what years are you all in?"

    "A" "First."

    "B" "First year!"

    "C" "Freshman..."

    "Interesting. Only first years. Wonder why."

    VGDev "If you’ve all joined the Biscord, there’s not much I have for you. Later."

    "He left..."

    "I should keep tabs on him. See what he gets up to."

    VGDev "Oh, wait!"

    "Hm?"

    "I forgot to ask your name. Or if I did I forgot it. I always do this."

    "It's [player_name]."

    "Alright. Thanks again!"

    hide devon
    call bgm_char_end

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
