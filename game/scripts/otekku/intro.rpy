label biscord_gremlin:
    "I try to find some clubs you can join online, and stumble over a large Biscord server"

    "\"Anime O Tekku?\"{p}Like an anime club?"

    "I guess I can introduce myself"

    nvl_narrator "{b}xX_burdelli_Xx{/b} joined the party"
    mc_nvl "Hey I’m [player_name], first year [major] undergrad. I like all sorts of anime, and read a little bit of manga too."
    mel_nvl "welcome to the club [first_name]!"
    finn_nvl "Whaddup"
    call bgm_otekku_start
    hachiko_nvl "freshman gang! i've been lurking in this server for a while until I got into Tech. My name is Hachiko, 1st year CS major"
    hachiko_nvl "i also watch and read all sorts of stuff, can't really chose a specific genre to be a fav tho"
    hachiko_nvl "what kind of shows are ur favorite {b}@xX_burdelli_Xx{/b}?"
    menu(nvl=True):
        "I watch some shounen shows here and there. Nothing much":
            mc_nvl "I watch some shounen shows here and there. Nothing much"
            hachiko_nvl "ooo i watch a lot of sports anime! my favs include haiku and spicy ice"
            hachiko_nvl "but never too late for u to watch more stuff!"
            mel_nvl "everyone's gotta start from somewhere"
            mel_nvl "even finn, one of our officers, barely watches anything"
            finn_nvl "Yeah i stay uptodate with a couple of light novels, but nothing else really besides that"
        "I'm a die hard Mecha fan! Both classic & modern, super & real!":
            mc_nvl "I'm a die hard Mecha fan! Both classic & modern, super & real!"
            hachiko_nvl "im not that huge mecha fan myself, but my favorite so far has probably got to be Eva"
            hachiko_nvl "maybe I should try to get into it more"
            nine_nvl "Been looking around for another for ages! My favorite mecha franchises are Macross and the game franchise mech warrior"
        "isekai trash, yeah im that kind of person":
            mc_nvl "Isekai trash, yeah im that kind of person"
            hachiko_nvl "Love to see another isekai trash enjoyer here"
            hachiko_nvl "Can't say isekai is usually ever that good but it's always a guilty pleasure of mine"
            mel_nvl "xd same here"
        "I live for CGDCT, slice of life is my blood, my lifeline":
            mc_nvl "I live for CGDCT, slice of life is my blood, my lifeline"
            hachiko_nvl "like hs slice of life? you okay-on?"
            nine_nvl "Sorry u lost me there. ur making me die slowly inside"
            hachiko_nvl "not really my cup of tea honestly, but some people here are apparently big fans, can be chill sometimes"
            hachiko_nvl "maybe u can meet grand wizard jerry"
            mel_nvl "{b}@Jerry the Wizard{/b} ^^^"
            mel_nvl "he might not respond that quickly, he's often busy with his job"
        "Currently obsessed with idols. I really like vocaloid too":
            mc_nvl "Currently obsessed with idols. I really like vocaloid too"
            hachiko_nvl "*O* i love vocaloid, esp the kagamine twins"
            finn_nvl "whats yalls opinion on vidols, theyve been getting quite popular lately"
            mc_nvl "Afraid I've only see the clips. But they are decently fun to watch"
            hachiko_nvl "yeppers! same here, omg some are the the cutest too"
    hachiko_nvl "Very cool ^o^ I was wondering when and where are the meetings?"
    mel_nvl "our meetings are every Saturday noon in the College of Computing Building. the first 3 hours we watch anime and the next 3 we socialize and do special events."
    mel_nvl "feel free to come in whenever you want and leave whenever you want too."
    hachiko_nvl "yeah! i'll make sure to come"
    mc_nvl "me too"
    "Afterwards, Hachiko and I talked for a whopping 2 more hours about anime"
    "Both of us suck at ending a conversation..."
    "I should go to the meeting this weekend."
    "{b}You unlocked Klaus Computing on the map!{/b}"

    $ Locations[6].is_active = True

    $ AP -= 4
    call bgm_char_end
    return

label anigang:
    show otekku neutral at center with moveinbottom:
        zoom 0.25
    call bgm_otekku_start
    Otekku "hey ur xX_burdelli_Xx right"
    "TODO: finish writing this part"
    hide otekku
    call bgm_char_end
    return
