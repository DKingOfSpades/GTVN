# FASET intro
image oscar = "oscar.png"
image oscar_glitch:
    At("oscar.png", glitch)
    pause 0.2
    At("oscar.png", chromatic_offset)
    pause 0.1
    At("oscar.png", glitch)
    pause 0.3
    At("oscar.png", chromatic_offset)
    pause 0.2
    At("oscar.png", glitch)
    pause 0.3
    At("oscar.png", chromatic_offset)
    pause 0.1
    At("oscar.png", glitch)
    pause 0.2
    At("oscar.png", chromatic_offset)
    pause 0.3
    repeat

label intro_faset:
    camera:
        perspective True
    scene bg culc lecture:
        subpixel True
        xzoom 1.75 yzoom 1.75 zoom 1.5
    play music "audio/bgm_waiting.mp3" fadein 1.0 volume 0.5
    "Only a few more weeks until your first class at Tech!"
    "Since you are a first year, you were invited to come to the FASET orientation. It's your last day of orientation in fact, so its time to register for classes!"
    "Many students were able to do FASET orientation before you, so you might have gotten the short end of the stick. Let's just hope that you are least able to grab some useful and major related classes at some convienient times."
    "Speaking of which, lets work on our registration!"
    show oscar:
        xpos 0.1 ypos 0.1 zoom 0.8

label player_name_selection:
    "First, what is your name?"
    hide oscar
    default player_name = "George P. Burdell"
    default first_name = "George"
    menu:
        "George P. Burdell":
            jump player_name_a

        "Georgia P. Burdell":
            jump player_name_b

label player_name_a:
    jump player_name_selection_common

label player_name_b:
    $ player_name = "Georgia P. Burdell"
    $ first_name = "Georgia"
    jump player_name_selection_common

label player_name_selection_common:
    show oscar:
        xpos 0.1 ypos 0.1 zoom 0.8
    "Oscar" "Nice to meet you, [first_name]. My name is Oscar, here to help you along with your FASET registration."
label player_major_selection:
    "Oscar" "I'll need a couple of more details before registering classes. {p}What is your major?"
    define major = "Computer Science" # default major
    call screen text_input("What is your major?", "major")
    $ major = major.strip() # removes whitespace at the ends

    "Oscar" "Hmm, [major], quite the interesting major."
    "Oscar" "Which freshman housing are you gonna be staying on campus? UwU. {p}Oh wait, I think decisions for that has already come out. {p}Let me check..."
    default housing = renpy.random.choice(["Armstrong", "Brown", "Caldwell", "Cloudman", "Field", "Fitten", "Folk", "Freeman", "Fulmer", "Glenn", "Hanson", "Harris", "Harrison", "Hefner", "Hopkins", "Howell", "Matheson", "Montag", "Perry", "Smith", "Towers", "Woodruff"])
    "Oscar" "Your hosing is... {p}{color=#0f0}{b}[housing]{/b}{/color}!"
    "Oscar" "And finally, it's time to determine your classes! Let me just pull up the class registration site for you."
    hide oscar
    show oscar_glitch:
        xpos 0.1 ypos 0.1 zoom 0.8
    "Oscar" "Wait what? whats hap{glitch=50.0}peni{b}ng??? {/b}how i{b}s -.# ${/b}&?\W@-{/glitch}"
    "{glitch=100.0}{b}Oscar{/b}{/glitch}" "{glitch=50.0}Aa{b}aaAAaAAAaaaAAA{w}AAaaaAaaaAAAAAa{/b} {p}somethi{w}ng is goin{w}g wro--{/glitch}"
    hide oscar_glitch
    show oscar:
        xpos 0.1 ypos 0.1 zoom 0.8
    "Oscar" "This is your new list of registered classes:"
    return
