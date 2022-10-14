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

init:
    # First up, we define some simple events for the various actions, that
    # are run only if no higher-priority event is about to occur.

    $ event("class", "act == 'class'", event.only(), priority=200)
    $ event("class_bad", "act == 'class'", priority=210)
    $ event("study", "act == 'study'", event.solo(), priority=200)
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
    $ event("buzz_first_meeting", "act == 'class'", event.once(), event.only(), priority=40)
    $ event("buzz_gym_1", "act == 'exercise'", "period == 'evening'", event.once(), event.depends("buzz_first_meeting"), priority=100)
    $ event("buzz_dorm_1", "act == 'hang'", "current_location == 'Dorms'", "theweekday == 'Sunday'", "period == 'noon'", event.once(), event.depends("buzz_first_meeting"), priority=180) #possibly placeholder until it has a better spot

    # This is an first winri event, that runs once when we first go to class.
    $ event("robot_gal", "act == 'class'", event.once(), event.only())
    $ event("lend_a_hand", "act == 'talk' and current_location == 'Student Competition Center'", event.once(), event.depends("robot_gal"), event.only())

    # This is an first otekku event, that runs once when we first discover.
    $ event("biscord_gremlin", "act == 'discover'", event.once(), event.only())

    # vgdev events
    # $ event ("club_fair_day", "day == 25 and month == 8 and current_location == \"Tech Green\"")
    $ event("club_fair_collision", "act == 'discover' and day == 25 and month == 8 and current_location == \"Tech Green\"", event.once())
    $ event("game_presentation", "act == 'discover' and theweekday == \"Saturday\" and month == 8 and period == \"Evening\" and current_location == \"Howey\"", event.once(), event.only(), event.depends("club_fair_collision"))
    $ event("first_dev_meeting", "act == 'gamedev'", event.once(), event.only(), event.depends("game_presentation"))

    # These are the events with glasses girl.
    #
    # The glasses girl is studying in the library, but we do not
    # talk to her.
    $ event("gg_studying",
            # This takes place when the action is 'study'.
            "act == 'study'",
            # This will only take place if no higher-priority
            # event will occur.
            event.solo(),
            # This takes place at least one day after seeing the
            # introduction event.
            event.depends("robot_gal"),
            # This takes priority over the study event.
            priority=190)

    # She asks to borrow our pen.
    $ event("borrow_pen",
            # This takes place when we go to study, and we have an int
            # >= 50.
            "act == 'study' and brain >= 50",
            # It runs only once.
            event.once(),
            # It requires the introduction event to have run at least
            # one day before.
            event.depends("robot_gal"))

    # After the pen, she smiles when she sees us.
    $ event("gg_smiling", "act == 'study'",
            event.solo(), event.depends("borrow_pen"),
            priority = 180)

    # The bookslide.
    $ event("bookslide", "act == 'study' and brain == 100",
            event.once(), event.depends("borrow_pen"))

    # She makes us cookies.
    $ event("cookies", "act == 'study'",
            event.once(), event.depends("bookslide"))

    # Her solo ending.
    $ event("gg_confess", "act == 'class'",
            event.once(), event.depends("cookies"))

    # Here are Sporty Girl's events that happen during the exercise act.
    $ event("catchme", "act == 'exercise'",
            event.depends('introduction'), event.once())
    $ event("cantcatchme", "act == 'exercise'",
            event.depends('catchme'), event.solo(), priority=190)
    $ event("caughtme", "act == 'exercise' and brawn >= 50",
            event.depends('catchme'), event.once())
    $ event("together", "act == 'exercise' and brawn >= 50",
            event.depends('caughtme'), event.solo(), priority=180)
    $ event("apart", "act == 'exercise' and brawn < 50",
            event.depends('caughtme'), event.solo(), priority=180)
    $ event("pothole", "act == 'exercise' and brawn >= 100",
            event.depends('caughtme'), event.once())
    $ event("dontsee", "act == 'exercise'",
            event.depends('pothole'), event.solo(), priority=170)
    $ event("sg_confess", "act == 'class'",
            event.depends('dontsee'), event.once())

    # Ending with both girls only happens if we have seen both of their final events
    # This needs to be higher-priority than either girl's ending.
    $ event('both_confess', 'act == "class"',
            event.depends("dontsee"), event.depends("cookies"),
            event.once(), priority = 50)


# GTVN events
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

# DSE events
label class:

    "I make it to class just in time, and proceed to listen to the teacher droning on about a wide range of topics, none of which are remotely interesting. {w}{b}+10 BRAIN{/b}"
    $ brain += 10
    $ AP -= 3

    return

# For test purposes only.
label class_bad:

    "You shouldn't be seeing this."

    "This is because class was declared with event.only(), which
     should suspend processing of further events."

    "This is really for testing purposes only."

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

# Below here are special events that are triggered when certain
# conditions are true.

label introduction:

    "I run to school, and make it to my seat just as the bell
     signalling the start of class rings."

    t "Before we start, I have an announcement to make."

    t "We will have two new students joining us. Girls, come on in."

    "Two girls walk in, and stand in front of the class."

    "They're twins."

    "Identical twins."

    "Identical black hair, and the same pretty face."

    "Despite that, it's still fairly easy to tell them apart."

    "The one on the left is wearing glasses."

    "Not too thick, but enough to let me know she probably reads alot
     of books."

    "If I look a little closely, I can find another difference."

    "The one on the right probably exercises a bit more."

    "I can tell by the muscle tone in her legs."

    "I realize that I'm staring at her legs, and quickly look up."

    "Suddenly, I realize that she's been talking for all this town."

    sg "... to this town. And we hope to be friends with all of you."

    sg "Well, that's about it. Sis, do you have anything to say?"

    "The girl with glasses pauses for a second, and then quickly says:"

    gg "{size=-4}It's good to meet you all.{/size}"

    "She stops, and goes back to not saying anything."

    t "Well, if that's all, you can take your seats and we can start
       the class."

    "They do, and our teacher begins his lecture."

    "I don't think anyone pays much attention to it, however."

    $ AP -= 3

    return



label gg_studying:

    "I head to the library, to get some studying done."

    "The glasses girl is there, but she's busy reading a book, taking
     notes as she does so."

    "I decide not to disturb her, and instead start reading my own
     book."

    $ brain += 10

    $ AP -= 3

    return

label borrow_pen:

    "I head to the library, to get some studying done."

    "The glasses girl is there, but she's busy reading a book."

    "I decide not to disturb her, and instead start reading my own
     book."

    "Suddenly, I feel a tap on my shoulder."

    "I look up, and see the glasses girl standing right next to me."

    gg "Excuse me, but can I borrow your pen?"

    gg "Mine ran out of ink."

    "I dig through my bag, to find the pen I had stashed there."

    "While I'm looking, I point out that she seems to come to the
     library alot."

    gg "Hm... I guess you're right."

    gg "There's so much stuff here, and I want to know about it all."

    gg "Surely, you must feel the same way, as you're here almost as
        much as I am."

    "I don't have the heart to tell her that I'm only here to study so
     that I don't fail out."

    "My hand brushes the pen, and I quickly pull it out and give it to
     her."

    gg "Thank you."

    "She says, and she goes back to studying."

    $ AP -= 3

    return

label gg_smiling:

    "I head to the library, to get some studying done."

    "The glasses girl is there, and smiles at me for a second before
     turning back to her book."

    "I decide not to disturb her, and instead start reading my own
     book."

    $ brain += 10
    $ AP -= 3

    return

label bookslide:

    "I head to the library, to get some studying done."

    "The glasses girl is standing right by the entrance, putting a
     book back into a bookcase containing science books."

    "It looks quite old, and quite weak, as if it could break at any
     time."

    "Suddenly, I hear a loud crack come from the bookcase."

    "Without thinking, I throw myself between the girl and the
     bookcase, pushing her out of the way in the process."

    "As the shelves fail one by one, I'm hit with large textbooks on
     topics ranging from Astronomy to Zoology."

    "She's safe, but I'm knocked off my feet by the falling books."

    "Before the dust even settled, the girl with glasses realized what
     happened and asked:"

    gg "Are you alright?"

    "I tell her that I am, all the while rubbing a bruise left by a
     particularly large Physics book."

    gg "You saved me."

    "She points out. I shrug... I guess I did, but it's not like I'm a
     hero or anything."

    "She extends out her hand, I take it, and she helps me to get up."

    gg "Wow... Um..."

    "She doesn't know what to say."

    "I suggest that we help clean up the mess, mostly to take her off
     the spot."

    "She agrees, and together we begin piling the books up into neat
     piles."

    "I end up walking her home. She doesn't say much, but we both seem to enjoy quiet companionship."

    "She lives farther than I thought, though, and I end up not having time for anything else by the time I get home."

    "But it was definitely worth it."

    $ AP -= 3

    #This will end the current period and skip the next one.
    jump events_skip_period

    return


label cookies:

    "I head to the library, to get some studying done."

    "The glasses girl is there, apparently waiting for me."

    "She's holding a package in her hands."

    gg "Here."

    "She says, and she hands me the package."

    "I take it from her, and open it."

    "It contains fresh homemade cookies. Ginger snaps, I think."

    gg "It's to thank you."

    "She points out... She's probably not used to this. Especially
     with guys."

    "I take one of them, and stick it in my mouth."

    "The taste is exquisite."

    "It's perhaps one of the best cookies I've ever tasted."

    "Of course it is. It's the only cookie I'd ever tasted that was
     made for me by a beutiful girl."

    "I tell her this... that it's delicious, not the girl part."

    "But I do let slip that if I could eat these every day, I'd be the
     happiest guy in the world."

    "At this, she can only blush."

    $ AP -= 3

    return

label gg_confess:

    "I once again barely make it to class on time."

    "I sit down, at my desk, and put some of my books into it."

    "My hand brushes a folded sheet of paper, one I didn't remember
     putting in there."

    "It's a girl's handwriting... \"Meet me on the roof at lunch.\""

    "That's all it says... no signature or anything."

    "Lunch is a few hours away, but the time passes like a blur."

    "It's all I can do to avoid racing up to the roof... but I give it
     some time anyway."

    "It wouldn't make sense for me to get there first."

    "I let two minutes elapse before leaving the classroom, and then
     slowly walk the flights of stairs up to the roof."

    "Standing there, I find the glasses girl."

    "She's holding what looks like a homemade lunch... big enough for
     two."

    "I look at it, then her, then remember what I had said after she
     made me the cookies."

    "Finally, I ask her... \"Does this mean?\""

    "She nods. It's all the confirmation I need."

    "I sit down next to my new girlfriend... and together we start
     eating her lunch."

    "I'm probably the happiest guy in the world."

    "But I still have to find out her name."

    ".:. Ending 1."

    $ renpy.full_restart()


label catchme:

    "I decide to go out for a run, to keep myself in shape."

    "As I'm running through the town, I see a girl."

    "She's one of the twins who transferred into my class."

    "She waves, and comes over to me."

    sg "I didn't know you were a runner."

    "I point out that I'm not really a runner... I just run a little
     bit at a time."

    "I ask her if she wants to run with me for a while."

    sg "As if! You couldn't keep up with me."

    "I point out that I probably can."

    sg "Well, let's see."

    "We set off running, but she quickly pulls past me."

    sg "See? Well, maybe we can try it again when you're a bit
        faster."

    sg "Until then, later."

    "Even though I'm jogging, she pulls away as if it is nothing."

    $ AP -= 3

    return

label cantcatchme:

    "I'm out running again, when the sporty girl catches up to me."

    sg "Still at it?"

    sg "Well, keep up the good work. One day you'll be as fast as me!"

    sg "Well, maybe."

    "She pulls out past me, and disappears into the distance. One day
     I'll catch up to her."

    $ brawn += 10

    $ AP -= 3

    return

label caughtme:

    "I'm out running again, when the sporty girl catches up to me."

    sg "Still at it?"

    sg "Well, keep up the good work. One day you'll be as fast as me!"

    sg "Well, maybe."


    "Today, however, I'm not about to let this stand unchallenged."

    "I break out into a run, and for the first time ever, I keep up
     with her."

    "We both run, neck and neck, me keeping up with her."

    "Finally, she starts slowing down, and we come to a stop
     together."

    sg "Not bad."

    "She pauses to catch her breath."

    sg "You've been practicing, and it really shows."

    sg "You've finally become fast enough to run with me."

    "I nod, accepting her praise."

    sg "We should do this more often... it's better to run with
        someone else, to keep the challenge up."

    "I nod again."

    sg "Well, shall we go?"

    "I nod a third time, and we take off, running side by side."

    $ brawn += 10
    $ AP -= 3

    return

label together:

    "I start running, and meet up with the sporty girl as she passes
     the street in front of my house."

    "She's still better than me... she's been running for over a mile
     before reaching this point."

    "Still, I can keep up with her for the rest of the run. And that's
     not bad."

    $ brawn += 10
    $ AP -= 3

    return

label apart:

    "I start running, and meet up with the sporty girl as she passes
     the street in front of my house."

    "I try to keep up with her, but she pulls away from me."

    "When she's a block away, she slows down and lets me catch up."

    sg "It's your own fault... this is what you get for not
        practicing."

    "She's right, of course, and I redouble my efforts to try to keep
     up with her."

    $ brawn += 10
    $ AP -= 3

    return

label pothole:

    "I start running, and meet up with the sporty girl as she passes
     the street in front of my house."

    "We run together for several miles."

    "I think about how much I've improved in our time together."

    "And, although she probably won't admit it, I think she's improved
     as well."

    "I guess a little friendly competition is usually for the best."

    "A small yelp pulls me out of my thought."

    sg "Ow!"

    "The sporty girl sits down, grabbing her ankle."

    "I ask her what happened."

    sg "I... hit a... pothole. Twisted my... ankle."

    "I wince in sympathy."

    "We wait a bit. I'm not sure what to do."

    "Finally, I ask her if she can walk on it."

    "She tries for a bit, but then winces in pain."

    sg "No, I don't think so."

    "I realize that we can't stay here."

    "And so, I crouch down and motion for her to climb up onto my
     back."

    sg "What are you doing?"

    "I explain that she can't stay out in the middle of the street
     forever, and she won't get any help until I can get her home."

    "And the only way to do that is for me to carry her."

    "She accepts this, and climbs up onto my back."

    "She wraps her arms around my neck, and I place my hands
     underneath her to make a seat."

    "I stand up, and start carrying her home."

    "She lives farther than I thought, though, and I end up not having time for anything else by the time I get home."

    "But it was definitely worth it."

    $ AP -= 3

    #This will end the current period and skip the next one.
    jump events_skip_period

    return

label dontsee:

    "I go running again."

    "But this time, I don't see the sporty girl."

    "I finish the course that we usually take, but it's not the same
     without her."

    $ AP -= 3

    return

label sg_confess:

    "I once again barely make it to class on time."

    "I sit down, at my desk, and put some of my books into it."

    "My hand brushes a folded sheet of paper, one I didn't remember
     putting in there."

    "It's a girl's handwriting... \"Meet me on the roof at lunch.\""

    "That's all it says... no signature or anything."

    "Lunch is a few hours away, but the time passes like a blur."

    "It's all I can do to avoid racing up to the roof... but I give it
     some time anyway."

    "It wouldn't make sense for me to get there first."

    "I let two minutes elapse before leaving the classroom, and then
     slowly walk the flights of stairs up to the roof."

    "Standing there, I find the sporty girl."

    "She's leaning on a crutch."

    "I look at it for a second, and she notices that."

    sg "I went to the doctor, and he gave me this."

    sg "Looks like we won't be running together for a while."

    "I nod."

    sg "And that's why I asked you here."

    sg "I couldn't stand the though of not seeing you for a few
        weeks."

    "I search my feelings, and realize I feel the same way."

    sg "So I thought..."

    "She doesn't say it... she doesn't need to."

    "We both know how we feel about each other."

    "And with that, we went from being running partners to partners in
     a deeper sense."

    "Now if I only knew her name..."

    ".:. Ending 2."

    $ renpy.full_restart()


label both_confess:

    "I once again barely make it to class on time."

    "I sit down, at my desk, and put some of my books into it."

    "My hand brushes a folded sheet of paper, then another."

    "I take the first one out, and read it."

    "It's a girl's handwriting... \"Meet me on the roof at lunch.\""

    "That's all it says... no signature or anything."

    "I take a look at the second one, and it says the same thing."

    "Sure, the handwriting is a little different, but..."

    "Lunch is a few hours away, but the time passes like a blur."

    "It's all I can do to avoid racing up to the roof... but I give it
     some time anyway."

    "I let two minutes elapse before leaving the classroom, and then
     slowly walk the flights of stairs up to the roof."

    "Standing there are the twins."

    "Both of them."

    "As in, the two notes came from the two twins."

    "I ask them what they are doing there, feigning ignorance."

    sg "Well, I invited you up here to confess to you..."

    sg "... and then I found out that my sister here was about to do
        the same thing."

    gg "{size=-4}...I was...{/size}"

    sg "When we found out, we were quite shocked, but after comparing
        notes, we decide what we're going to do..."

    "I quickly run through the possibilities in my head."

    "The best cases involve them never talking to me again."

    "The worst cases involve me being thrown off the roof."

    bg "We're going to share you!"

    "Eh?"

    "That wasn't something I considered."

    "Each of the girls grabs onto one of my arms."

    "I don't know what the future holds for us..."

    "... and I don't know if this will work out."

    "But I do know that one day I will work up the courage to find out
     their names."

    ".:. Ending 3."

    $ renpy.full_restart()
