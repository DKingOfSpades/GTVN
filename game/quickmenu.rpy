transform slide:
    yoffset -50
    easein .3 yoffset 0
    on hide:
        easeout .3 yoffset -100

transform appear:
    alpha 0.0
    linear .6 alpha 1.0
    on hide:
        linear .6 alpha 0.0

screen triangle():
    textbutton "V" action Show("triangle_menu") align (1.0, 0.0)

screen triangle_menu():

    modal True

    button:
        # Optional button
        # Everything outside the frame is a transparent button to hide the screen
        background None
        action Hide("triangle_menu")

    frame:
        align (1.0, 0.0)
        at slide
        has hbox
        textbutton "Option 1" action Show("option1_screen")
        textbutton "Option 2" action NullAction()
        textbutton "Option 3" action NullAction()
        textbutton "Option 4" action NullAction()
        textbutton "Λ" action Hide("triangle_menu")

screen option1_screen():
    modal True

    frame:
        xysize (400, 400)
        align (.5, .5)
        at appear

        has vbox
        text "Here the elements of the screen with text, images, buttons or whatever."

        # Don't forget a button to hide the screen
        # Here two examples:
        textbutton "Close the two screens":
            action [Hide("option1_screen"), Hide("triangle_menu")]
        textbutton "Close one screen":
            action Hide("option1_screen")
