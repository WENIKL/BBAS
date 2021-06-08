













define config.name = _("Большой брат: Другая история")





define gui.show_name = True




define config.version = "0.06.5.09"





define gui.about = _p("""
""")






define build.name = "BigBrother_AnotherStory"








define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "audio/main.ogg"

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5









define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "hide"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)








default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = 'BB_AS'



init python:
    config.has_autosave = True
    config.autosave_frequency = None
    config.autosave_on_choice  = False







define config.window_icon = 'gui/window_icon.png'





define config.minimum_presplash_time = 1.0
define config.mouse_hide_time = 10
default preferences.desktop_rollback_side = "disable"

init python:
    def json_callback(d):
        d["day"]    = day
        d["tm"]     = tm
        d["wd"]     = weekdays[GetWeekday(day)][0]
        d["desc"]   = save_name
        d["auto"]   = str(number_autosave)
        d["quick"]  = str(number_quicksave)

    config.default_fullscreen = False
    config.save_json_callbacks.append(json_callback)






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpym', None)
    build.classify('**/.**', None)
    build.classify('game/tl/**.rpy', None)
    build.classify('game/**.rpy', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/*save*/*.*', None)




    build.archive("extra", "all")
    build.classify('game/extra/**.png', 'extra')
    build.classify('game/extra/**.jpg', 'extra')
    build.classify('game/extra/**.webp', 'extra')
    build.classify('game/extra/**.rpyc', 'extra')


    build.archive("img_fix", "all")
    build.classify('game/images/interface/tip.webp', 'img_fix')
    build.classify('game/images/interface/poss/cams/ep06.webp', 'img_fix')
    build.classify('game/images/interface/poss/cams/ep07.webp', 'img_fix')
    build.classify('game/images/interface/poss/secretbook/ep04.webp', 'img_fix')
    build.classify('game/images/interface/poss/blog/ep05*.webp', 'img_fix')
    build.classify('game/images/interface/poss/partygirl/ep05*.webp', 'img_fix')
    build.classify('game/images/interface/poss/smoke/*.webp', 'img_fix')
    build.classify('game/images/Ann/cams/cooking/01c.webp', 'img_fix')






    build.archive("images", "all")

    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.webp', 'images')

    build.archive('video', 'all')
    build.classify('game/**.webm', 'video')

    build.archive('audio', 'all')
    build.classify('game/audio/**.ogg', 'audio')
    build.classify('game/audio/**.mp3', 'audio')
    build.classify('game/audio/**.wav', 'audio')

    build.archive('translate', 'all')
    build.classify('game/tl/**.**', 'translate')

    build.archive('scripts', 'all')
    build.classify('game/*.rpyc', 'scripts')
    build.classify('game/core/**.rpyc', 'scripts')
    build.classify('game/dialogues/**.rpyc', 'scripts')
    build.classify('game/events/**.rpyc', 'scripts')

    build.archive('font', 'all')
    build.classify('game/**.ttf', 'font')
    build.classify('game/**.otf', 'font')




    build.documentation('*.html')
    build.documentation('*.txt')


























    build.include_i686 = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
