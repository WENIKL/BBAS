init offset = -2









init python:
    gui.init(1920, 1080)













define gui.accent_color = "#ffbe00"


define gui.idle_color = '#888888'



define gui.idle_small_color = '#aaaaaa'


define gui.hover_color = "#ffbe00"




define gui.selected_color = '#ffffff'


define gui.insensitive_color = '#8888887f'



define gui.muted_color = '#512800'
define gui.hover_muted_color = '#7a3d00'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'





define gui.text_font = "trebuc.ttf"


define gui.name_text_font = "DejaVuSans.ttf"


define gui.interface_text_font = "DejaVuSans.ttf"


define gui.text_size = 26


define gui.name_text_size = 30


define gui.interface_text_size = 28


define gui.label_text_size = 30


define gui.notify_text_size = 20


define gui.title_text_size = 28





define gui.main_menu_background = "gui/main_menu.webp"
define gui.game_menu_background = "gui/game_menu.png"







define gui.textbox_height = 265



define gui.textbox_yalign = 1.0





define gui.name_xpos = 520
define gui.name_ypos = -50




define gui.name_xalign = 0.0



define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False





define gui.dialogue_xpos = 430
define gui.dialogue_ypos = 10


define gui.dialogue_width = 930




define gui.dialogue_text_xalign = 0.0









define gui.button_width = None
define gui.button_height = None


define gui.button_borders = Borders(6, 6, 6, 6)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color












define gui.choice_button_width = 490
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(5, 8, 5, 8)
define gui.choice_button_text_font = "trebuc.ttf"
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = gui.accent_color
define gui.choice_button_text_hover_color = gui.text_color
define gui.choice_button_text_insensitive_color = gui.interface_text_color









define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color


define config.thumbnail_width = 384
define config.thumbnail_height = 216


define gui.file_slot_cols = 3
define gui.file_slot_rows = 10









define gui.navigation_xpos = 150


define gui.skip_ypos = 15


define gui.notify_ypos = 120


define gui.choice_spacing = 0


define gui.navigation_spacing = 6


define gui.pref_spacing = 15


define gui.pref_button_spacing = 0


define gui.page_spacing = 0


define gui.slot_spacing = 15


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(6, 6, 6, 6)


define gui.confirm_frame_borders = Borders(60, 60, 60, 60)


define gui.skip_frame_borders = Borders(24, 8, 75, 8)


define gui.notify_frame_borders = Borders(24, 8, 60, 8)


define gui.frame_tile = False











define gui.bar_size = 38
define gui.scrollbar_size = 7
define gui.slider_size = 38



define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)


define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = None



define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 180
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 180
define gui.history_text_ypos = 0
define gui.history_text_width = 1000
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 15, 0, 30)



define gui.nvl_list_length = 6



define gui.nvl_height = 173



define gui.nvl_spacing = 15



define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"






init python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(15, 25, 15, 0)



    if renpy.variant("small"):
        
        
        gui.text_size = 32
        gui.name_text_size = 54
        gui.notify_text_size = 28
        gui.interface_text_size = 32
        gui.button_text_size = 36
        gui.label_text_size = 51
        
        
        gui.textbox_height = 300
        gui.name_xpos = 120
        gui.text_xpos = 135
        gui.text_width = 1650
        
        gui.dialogue_width = 1450
        gui.dialogue_xpos = 430
        gui.dialogue_ypos = 20
        
        
        gui.slider_size = 54
        gui.scrollbar_size = 20
        
        gui.choice_button_width = 600
        
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        
        gui.history_height = 285
        gui.history_text_width = 1035
        
        gui.quick_button_text_size = 30
        
        
        gui.file_slot_cols = 3
        
        gui.slot_spacing = 7
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
