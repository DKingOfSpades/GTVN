# handles date/time
init python:
    show_date = False
    day = 21
    month = 8
    daynames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    theweekday =  daynames[(day%7)]
    day_max=31
    month_name = "August"

    month_information={
        1:("January",31),
        2:("February",28),
        3:("March",31),
        4:("April",30),
        5:("May",31),
        6:("June",30),
        7:("July",31),
        8:("August",31),
        9:("September",30),
        10:("October",31),
        11:("November",30),
        12:("December",31)}

    def date_overlay():
        if show_date:
            ui.text("%s %s" % (theweekday, period), xalign=1.0, yalign=0.035)
            ui.text("%s/%s" % (month, day), xalign=1.0, yalign=0.0)
            # ui.image ("%s" % theweekday + ".png", xalign=1.0, yalign=0.035)
            # ui.image ("%s" % month + ".png", xalign=0.965, yalign=0.0)
            # ui.image ("%s" % day + "d.png", xalign=1.0, yalign=0.0)


    config.overlay_functions.append(date_overlay)

label next_day_check:
    if day==day_max:
        $day=0
        $month+=1
        if month == 13:
            $ month = 1
        $month_name,day_max=month_information[month]#look up the dictionary
    $day+=1
    $theweekday =  daynames[(day%7)]

    return
