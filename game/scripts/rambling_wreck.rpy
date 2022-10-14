transform passerby:
    yalign 0.5
    xalign 1.5
    linear 3.0 xalign 0.5

label hit_and_run:
    "I'm just taking a stroll, minding my own buisness, when suddenly-"

    show ralph happy:
        zoom 0.75
        yalign 0.5

        xalign -0.5
        easein_back 2.0 xalign 1.5

    "The Rambling Wreck almost ran over me."

    "What is my luck today?"

    mc "HEY! Watch where u are going!" with hpunch

    show ralph at passerby

    Ralph "I'm so so sorry about that."

    show ralph bashful

    Ralph "I was just in a rush to my classes that I didn't see you there."

    mc "I can't believe you've done this."

    hide ralph with moveoutright

    Ralph "Well I gotta go now see ya!"

    mc "Hey wait!"

    "The wreck left their toast on the ground. {w}I guess I'll throw it away."
    return
