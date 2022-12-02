# GTVN Designed Music Engine
# for the use case of layered music that fades in and out of volume
init python:
    renpy.music.register_channel("bgm_morning", "music", loop=True, stop_on_mute=False, tight=True)
    renpy.music.register_channel("bgm_noon", "music", loop=True, stop_on_mute=False, tight=True)
    renpy.music.register_channel("bgm_evening", "music", loop=True, stop_on_mute=False, tight=True)
    renpy.music.register_channel("bgm_night", "music", loop=True, stop_on_mute=False, tight=True)

label bgm_campus_start:
    $ renpy.music.play("audio/bgm_campus_morning.mp3", channel="bgm_morning", loop=True, synchro_start=True, fadein=2)
    $ renpy.music.play("audio/bgm_campus_noon.mp3", channel="bgm_noon", loop=True, synchro_start=True, fadein=2)
    $ renpy.music.play("audio/bgm_campus_evening.mp3", channel="bgm_evening", loop=True, synchro_start=True, fadein=2)
    $ renpy.music.play("audio/bgm_campus_night.mp3", channel="bgm_night", loop=True, synchro_start=True, fadein=2)
    $ music_playing = "campus"
    return

label bgm_tech_square_start:
    $ renpy.music.play("audio/bgm_tech_square_morning.mp3", channel="bgm_morning", loop=True, synchro_start=True, fadein=2)
    $ renpy.music.play("audio/bgm_tech_square_noon.mp3", channel="bgm_noon", loop=True, synchro_start=True, fadein=2)
    $ renpy.music.play("audio/bgm_tech_square_evening.mp3", channel="bgm_evening", loop=True, synchro_start=True, fadein=2)
    $ renpy.music.play("audio/bgm_tech_square_night.mp3", channel="bgm_night", loop=True, synchro_start=True, fadein=2)
    $ music_playing = "square"
    return

label bgm_period_change_morning:
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_noon')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_evening')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_night')
    $ renpy.music.set_volume(1.00, delay=2, channel='bgm_morning')
    return

label bgm_period_change_noon:
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_morning')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_evening')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_night')
    $ renpy.music.set_volume(1.00, delay=2, channel='bgm_noon')
    return

label bgm_period_change_evening:
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_morning')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_noon')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_night')
    $ renpy.music.set_volume(1.00, delay=2, channel='bgm_evening')
    return

label bgm_period_change_night:
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_morning')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_noon')
    $ renpy.music.set_volume(0.00, delay=2, channel='bgm_evening')
    $ renpy.music.set_volume(1.00, delay=2, channel='bgm_night')
    return

# Charater BGMs
label bgm_otekku_start:
    $ music_to_return = music_playing
    $ renpy.music.play("audio/bgm_otekku.mp3", channel="bgm_morning", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_otekku.mp3", channel="bgm_noon", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_otekku.mp3", channel="bgm_evening", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_otekku.mp3", channel="bgm_night", loop=True, synchro_start=True, fadein=1)
    return

label bgm_vgdev_start:
    $ music_to_return = music_playing
    $ renpy.music.play("audio/bgm_vgdev.mp3", channel="bgm_morning", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_vgdev.mp3", channel="bgm_noon", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_vgdev.mp3", channel="bgm_evening", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_vgdev.mp3", channel="bgm_night", loop=True, synchro_start=True, fadein=1)
    return

label bgm_buzz_start:
    $ music_to_return = music_playing
    $ renpy.music.play("audio/bgm_buzz_phonk.mp3", channel="bgm_morning", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_buzz_phonk.mp3", channel="bgm_noon", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_buzz_phonk.mp3", channel="bgm_evening", loop=True, synchro_start=True, fadein=1)
    $ renpy.music.play("audio/bgm_buzz_phonk.mp3", channel="bgm_night", loop=True, synchro_start=True, fadein=1)
    return

label bgm_char_end:
    if (music_to_return == "campus"):
        call bgm_campus_start
    elif (music_to_return == "square"):
        call bgm_tech_square_start
    return
