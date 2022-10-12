#Phone function for texting and apps
#Supports basic functionality

# NVL characters are used for the phone texting
define george_nvl = Character("xX_burdelli_Xx", kind=nvl, callback=Phone_SendSound)
define hachiko_nvl = Character("Otakudos", kind=nvl, callback=Phone_ReceiveSound)
define devon_nvl = Character("Devon", kind = nvl, callback=Phone_ReceiveSound)
define jack_nvl = Character("Jack", kind = nvl, callback=Phone_ReceiveSound)

define mel_nvl = Character("mel", kind = nvl, callback=Phone_ReceiveSound)
define nine_nvl = Character("NineBall", kind = nvl, callback=Phone_ReceiveSound)
define finn_nvl = Character("FINNBALE", kind = nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label phone_test:
    scene bg culc lecture with dissolve:
        subpixel True
        xzoom 1.75 yzoom 1.75 zoom 1.5
    pause 1.0

    #Phone conversation start

    #show placeholder e1m2_b:
    #   ease 0.5 xalign 0.7

    nvl_narrator "George added Hachiko to the group"
    george_nvl "Mario movie watch party?"
    nvl_narrator "Hachiko added Devon to the group"
    hachiko_nvl "SETH ROGAN DONKEY KONG SETH ROGAN DONKEY KONG"
    hachiko_nvl "{image=emoji/pog.png}"
    devon_nvl "we were watching it today?"
    george_nvl "Yep"
    devon_nvl "can't, got like 7 things to do today"
    george_nvl "bruh"
    hachiko_nvl "bruh"
    nvl_narrator "Jack joined the group"
    jack_nvl "bruh"
    "--End of Test--"
    return
