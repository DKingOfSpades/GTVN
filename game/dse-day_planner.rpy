# This contains code for the day planner. You probably
# don't want to change this file.
#
# If you want to change the appearance of the day planner,
# look for the dp_ styles in styles.rpy


init -100 python:

    # The title of the done button.
    dp_done_title = "Done Planning"

    # A map from period name to the information we know about that
    # period.
    __periods = { }

    # The period we're updating.
    __period = None

    class __Period(object):

        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        __periods[name] = store.__period = __Period(name, var)

    __None = object()

    def dp_choice(name, value=__None, enable="True", show="True"):

        if not __period:
            raise Exception("Choices must be part of a defined period.")

        if value is __None:
            value = name

        __period.acts.append((name, value, enable, show))

    def __set_noncurried(var, value):
        setattr(store, var, value)
        return True

    __set = renpy.curry(__set_noncurried)

# Our Day Planner displays the stats, and buttons for the user to choose
# what to do during each period of time defined in "periods".
screen day_planner(period):
    # indicate to Ren'Py engine that this is a choice point
    $ renpy.choice_for_skipping()
    frame:
        style "dayplanner_frame"
        # use display_stats(name=True, bar=True, value=True, max=True)
        use display_planner(period)

screen display_planner(period):
    frame:
        style_group "dp"
        vbox:
            spacing 10
            $ can_continue = True
            if AP > 7:
                label "Early [period]" xalign 0.5
            elif AP > 3:
                label period xalign 0.5
            else:
                label "Late [period]" xalign 0.5
            if period not in __periods:
                $ raise Exception("Period %r was never defined." % period)
            $ this_period = __periods[period]
            $ selected_choice = getattr(store, this_period.var)

            $ valid_choice = False


            for name, curr_val, enable, should_show in this_period.acts:
                $ show_this = eval(should_show)
                $ enable = eval(enable)

                $ selected = (selected_choice == curr_val)

                if show_this:
                    if enable:
                        textbutton name xalign 0.5 action SetField(store, this_period.var, curr_val)
                    else:
                        textbutton name xalign 0.5

                if show_this and enable and selected:
                    $ valid_choice = True

            if not valid_choice:
                $ can_continue = False

            if (can_continue):
                textbutton dp_done_title style "dp_done_button" action Return() xalign 0.5
            else:
                textbutton dp_done_title style "dp_done_button" xalign 0.5
