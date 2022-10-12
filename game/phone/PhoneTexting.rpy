# Here's the code for the phone!
# All phone images are in the "phone" folder (use phone/some_image.png)

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "George" ##The name of the main character, used to place them on the screen

#Other Characters
define hachiko = "Otakudos"
define devon = "Devon"
define buzz = "Buzz"
define jack = "Jack"
define winri = "Winri"

define mel = "mel"
define finn = "FINNBALE"
define nine = "NineBall"

init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/sfx_recieve_text.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/sfx_send_text.ogg")
    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0


transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0


transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            yinitial 1.0
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100

                # If there is a choice menu, move the messages up so the latest can still be seen
                if len(items) > 0:
                    null height len(items) * 100

        # Adding in choice menu
        if len(items) > 0:
            frame:
                yalign 0.9
                xalign 0.5
                ysize len(items) * 115
                xsize 480
                background Solid("#000000")
                foreground None

                vbox:
                    yalign 0.9
                    for i in items: #For each choice, add its button
                        button:
                            action i.action
                            xalign 0.5
                            frame:
                                background Solid("#808b96")
                                foreground None
                                xysize (450,90)

                                text i.caption:
                                    align (0.5,0.5)
                                    text_align 0.5
                                    size 26


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == MC_Name:
                $ message_frame = "phone/phone_send_frame.png"
            else:
                $ message_frame = "phone/phone_received_frame.png"

            hbox:
                spacing 10
                if d.who == MC_Name:
                    box_reverse True

                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == MC_Name:
                        $ message_icon = "phone/phone_george_icon.png"
                    elif d.who == hachiko:
                        $ message_icon = "phone/phone_Otakudos_icon.png"
                    elif d.who == devon:
                        $ message_icon = "phone/phone_devon_icon.png"
                    elif d.who == jack:
                        $ message_icon = "phone/phone_jack_icon.png"
                    elif d.who == nine:
                        $ message_icon = "phone/phone_NineBall_icon.png"
                    elif d.who == mel:
                        $ message_icon = "phone/phone_mel_icon.png"
                    elif d.who == finn:
                        $ message_icon = "phone/phone_FINNBALE_icon.png"
                    else:
                        $ message_icon = "phone/phone_received_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()

                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != MC_Name and previous_d_who != d.who:
                        text d.who

                    frame:
                        padding (20,20)


                        background Frame(message_frame, 23,23,23,23)
                        xsize 350

                        if d.current:
                            if d.who == MC_Name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)
                            xsize 350
                            slow_cps False


                            if d.who == MC_Name :
                                color "#FFF"
                                text_align 1.0
                                xpos -580
                            else:
                                color "#000"


                            id d.what_id
        $ previous_d_who = d.who

style phoneFrame is default

style phoneFrame_frame:
    background Transform("phone/phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("phone/phone_foreground.png", xcenter=0.5,yalign=0.5)

    ysize 815
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True
