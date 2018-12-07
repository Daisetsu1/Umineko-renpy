# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = True
 
    
    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
    
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

#screen main_menu:

#    # This ensures that any other menu screen is replaced.
#    tag menu

#    # The background of the main menu.
##    window:
##        style "mm_root"

#    # The main menu buttons.
#    frame:
#        style_group "mm"
#        xalign .98
#        yalign .98

#        has vbox
        
#        if persistent.UMINEKOEND == 11:
            
#            textbutton _("Start Game") action ShowMenu("episodes")
#            textbutton _("Tea Party") action Start("teatime_1")
#            textbutton _("Load Game") action ShowMenu("load")
#            textbutton _("Preferences") action ShowMenu("preferences")
#            #textbutton _("Music Box") action ShowMenu("music")
#            #textbutton _("Tips") action ShowMenu("tips")
#            textbutton _("Help") action Help()
#            textbutton _("Quit") action Quit(confirm=False)
            
#        elif persistent.UMINEKOEND == 12:
            
#            textbutton _("Start Game") action ShowMenu("episodes")
#            textbutton _("Tea Party") action Start("teatime_1")
#            textbutton _("????") action Start("ura_teatime")
#            textbutton _("Load Game") action ShowMenu("load")
#            textbutton _("Preferences") action ShowMenu("preferences")
#            #textbutton _("Music Box") action ShowMenu("music")
#            #textbutton _("Tips") action ShowMenu("tips")
#            textbutton _("Help") action Help()
#            textbutton _("Quit") action Quit(confirm=False)
        
#        elif persistent.UMINEKOEND == 20:
            
#            textbutton _("Start Game") action ShowMenu("episodes")
#            textbutton _("Tea Party") action Start("teatime_1")
#            textbutton _("????") action Start("ura_teatime")
#            textbutton _("Load Game") action ShowMenu("load")
#            textbutton _("Preferences") action ShowMenu("preferences")
#            #textbutton _("Music Box") action ShowMenu("music")
#            textbutton _("Tips") action ShowMenu("tips")
#            textbutton _("Help") action Help()
#            textbutton _("Quit") action Quit(confirm=False)

#init -2 python:

#    # Make all the main menu buttons be the same size.
#    style.mm_button.size_group = "mm"


style r_menu_info:
    font "DejaVuSans.ttf"
    size 56
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]

##############################################################################
# Navigation
#
# Right-click menu
screen navigation():
    tag menu
    on "show" action Play("se20", "sys_se/zyosys1.ogg")
    key "game_menu" action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
    if renpy.android:
        imagebutton auto "android_menu_%s.png" xpos (1800.0/1920.0) ypos (32.0/1080.0) action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
    
    $ sys_x = 40.0
    $ sys_y = 60.0
    
#    $ allminutes, seconds = divmod(int(persistent.runtime), 60)
    $ hours, minutes = divmod(int(persistent.runtime), 3600)
#    $ curr_allminutes, curr_seconds = divmod(int(curr_play), 60)
    $ curr_hours, curr_minutes = divmod(int(persistent.curr_play), 3600)
#    $ curr_hours = (int(persistent.curr_play) // 3600)
#    $ hours = (int(persistent.runtime) // 3600)
#    $ curr_minutes = (int(persistent.curr_play) // 60)
    $ curr_minutes = (curr_minutes / 60)
#    $ minutes = (int(persistent.runtime) // 60)
    $ minutes = (minutes / 60)
    $ curr_minutes2 = (int(persistent.curr_play) // 60)
    $ minutes2 = (int(persistent.runtime) // 60)
    
#    $ r_for_title = 1
    
    add "background/efe/black.png" at sysmenutext
    
    if _preferences.language == None:
        text "Chapter: [r_click_chp[0]]" xanchor 1.0 xpos (1840/1920.0) ypos (805.0/1080.0) at sysmenutext2 style style.r_menu_info
    elif _preferences.language == 'japanese':
        text "chapter: [r_click_chp[1]]" xanchor 1.0 xpos (1840/1920.0) ypos (805.0/1080.0) at sysmenutext2 style style.r_menu_info
    if curr_minutes2 < 60:
        if _preferences.language == None:
            text "Playtime: [curr_minutes] Minutes" xanchor 1.0 xpos (1840/1920.0) ypos (885.0/1080.0) at sysmenutext2 style style.r_menu_info
        elif _preferences.language == 'japanese':
            text "playtime: [curr_minutes]分" xanchor 1.0 xpos (1840/1920.0) ypos (875.0/1080.0) at sysmenutext2 style style.r_menu_info
    else:
        if _preferences.language == None:
            text "Playtime: [curr_hours] Hours [curr_minutes] Minutes" xanchor 1.0 xpos (1840/1920.0) ypos (885.0/1080.0) at sysmenutext2 style style.r_menu_info
        elif _preferences.language == 'japanese':
            text "playtime: [curr_hours]時間 [curr_minutes]分" xanchor 1.0 xpos (1840/1920.0) ypos (875.0/1080.0) at sysmenutext2 style style.r_menu_info
    if minutes2 < 60:
        if _preferences.language == None:
            text "Total Playtime: [minutes] Minutes" xanchor 1.0 xpos (1840/1920.0) ypos (965.0/1080.0) at sysmenutext2 style style.r_menu_info
        elif _preferences.language == 'japanese':
            text "total playtime: [minutes]分" xanchor 1.0 xpos (1840/1920.0) ypos (945.0/1080.0) at sysmenutext2 style style.r_menu_info
    else:
        if _preferences.language == None:
            text "Total Playtime: [hours] Hours [minutes] Minutes" xanchor 1.0 xpos (1840/1920.0) ypos (965.0/1080.0) at sysmenutext2 style style.r_menu_info
        elif _preferences.language == 'japanese':
            text "total playtime: [hours]時間 [minutes]分" xanchor 1.0 xpos (1840/1920.0) ypos (945.0/1080.0) at sysmenutext2 style style.r_menu_info
    
#    imagebutton idle sys_load_i hover sys_load_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('save_new') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click1
    imagebutton idle sys_load_i hover sys_load_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('saveload') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click1
    $ sys_y += 80.0
    
    if chars_r_click == 1:
        if scenario_Number == 1:
            imagebutton idle sys_char_i hover sys_char_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_main_ep1_def') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click2
        elif scenario_Number == 2:
            imagebutton idle sys_char_i hover sys_char_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_main_ep2_def') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click2
        elif scenario_Number == 3:
            imagebutton idle sys_char_i hover sys_char_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_main_ep3_def') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click2
        elif scenario_Number == 4:
            imagebutton idle sys_char_i hover sys_char_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_main_ep4_def') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click2
    else:
        imagebutton idle sys_char_NA_i hover sys_char_NA_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action Play ("se20", "sys_se/zyosys5.ogg") hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click2
    
    $ sys_y += 80.0
    if tips_r_click == 1:
        if scenario_Number == 1:
            imagebutton idle sys_tips_i hover sys_tips_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_tips_1') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click3
        elif scenario_Number == 2:
            imagebutton idle sys_tips_i hover sys_tips_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_tips_2') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click3
        elif scenario_Number == 3:
            imagebutton idle sys_tips_i hover sys_tips_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_tips_3') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click3
        elif scenario_Number == 4:
            imagebutton idle sys_tips_i hover sys_tips_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('rmenu_tips_4') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click3
    else:
        imagebutton idle sys_tips_NA_i hover sys_tips_NA_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action Play ("se20", "sys_se/zyosys5.ogg") hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click3
    
    $ sys_y += 80.0
    imagebutton idle sys_config_i hover sys_config_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), SetVariable("config_pg", 1), ShowMenu('preferences') ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click4
    $ sys_y += 80.0
    imagebutton idle sys_title_i hover sys_title_h xpos (sys_x/1920.0) ypos (sys_y/1080.0) focus_mask True action [ Play ("se20", "sys_se/zyosys1.ogg"), MainMenu() ] hovered Play ("se10", "sys_se/zyosys0.ogg") unhovered [Hide("gui_tooltip")] at r_click5
    
screen rmenu_main_ep1_def:
    timer 0.01 action ShowMenu('rmenu_main_ep1')
screen rmenu_main_ep2_def:
    if r_hyouji_side == 0:
        timer 0.01 action ShowMenu('rmenu_main_ep2')
    elif r_hyouji_side == 1:
        timer 0.01 action ShowMenu('rmenu_main_ep2_2')
screen rmenu_main_ep3_def:
    if r_hyouji_side == 0:
        timer 0.01 action ShowMenu('rmenu_main_ep3')
    elif r_hyouji_side == 1:
        timer 0.01 action ShowMenu('rmenu_main_ep3_2')
screen rmenu_main_ep4_def:
    if r_hyouji_side == 0:
        timer 0.01 action ShowMenu('rmenu_main_ep4')
    elif r_hyouji_side == 1:
        timer 0.01 action ShowMenu('rmenu_main_ep4_2')
    elif r_hyouji_side == 2:
        timer 0.01 action ShowMenu('rmenu_main_ep4_3')

init -2:
    transform r_click1:
        xpos -(416.0/1920.0)
        linear 0.14 xpos (40.0/1920.0)
    transform r_click2:
        xpos -(416.0/1920.0)
        linear 0.18 xpos (40.0/1920.0)
    transform r_click3:
        xpos -(416.0/1920.0)
        linear 0.22 xpos (40.0/1920.0)
    transform r_click4:
        xpos -(416.0/1920.0)
        linear 0.26 xpos (40.0/1920.0)
    transform r_click5:
        xpos -(416.0/1920.0)
        linear 0.3 xpos (40.0/1920.0)
    transform sysmenutext:
        alpha 0.0
        linear 0.3 alpha 0.7
    transform sysmenutext2:
        alpha 0.0
        linear 0.3 alpha 1.0

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen save:
    on "show" action [calc_total_run()]
    tag menu
    use all_pause
    use navigation
    
#screen save_new:

#    # This ensures that any other menu screen is replaced.
#    tag menu

#    use navigation
#    use file_picker

#screen load:

#    # This ensures that any other menu screen is replaced.
#    tag menu

#    use navigation
#    use file_picker

#init -2 python:
#    style.file_picker_frame = Style(style.menu_frame)

#    style.file_picker_nav_button = Style(style.small_button)
#    style.file_picker_nav_button_text = Style(style.small_button_text)

#    style.file_picker_button = Style(style.large_button)
#    style.file_picker_text = Style(style.large_button_text)

    
init python:
    
    def the_lastline(d):
        mylast_line = store._last_raw_what
        d["last_line"] = mylast_line
        d["chapter"] = r_click_chp
        if scenario_Number == 1:
            d["episode"] = "Episode 1: Legend of the golden witch"
        elif scenario_Number == 2:
            d["episode"] = "Episode 2: Turn of the golden witch"
        elif scenario_Number == 3:
            d["episode"] = "Episode 3: Banquet of the golden witch"
        elif scenario_Number == 4:
            d["episode"] = "Episode 4: Alliance of the golden witch"
        elif scenario_Number == 5:
            d["episode"] = "Episode 5: End of the golden witch"
        elif scenario_Number == 6:
            d["episode"] = "Episode 6: Dawn of the golden witch"
        elif scenario_Number == 7:
            d["episode"] = "Episode 7: Requiem of the golden witch"
        elif scenario_Number == 8:
            d["episode"] = "Episode 8: Twilight of the golden witch"
    
    config.save_json_callbacks = [the_lastline]
    
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0.0
    y=0.0
screen load_save_slot_old:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    $x1=x+(25.0/1920.0)
    $y1=y+(25.0/1080.0)
    add FileScreenshot(number,empty="saveload/nodata.png") xpos x1 ypos y1
    $x2=x+(24.0/1920.0)
    $y2=y+(180.0/1080.0)
    text file_text xpos x2 ypos y2 size 20

screen load_save_slot:
    $ file_time = FileTime(number, format=_("%Y/%m/%d  %I:%M %p"), empty=" ")
    $ last_phrase = FileJson(number, "last_line", empty=" ", missing=" ")
    $ file_episode = FileJson(number, "episode", empty=" ", missing=" ")
    $ file_chapter = FileJson(number, "chapter", empty=" ", missing=" ")
    if _preferences.language == None:
        $ file_chapter2 = file_chapter[0]
    elif _preferences.language == 'japanese':
        $ file_chapter2 = file_chapter[1]
    $ last_phrase2 = last_phrase[:32]
    $x1=x+(25.0/1920.0)
    $y1=y+(25.0/1080.0)
    add FileScreenshot(number) xpos x1 ypos y1
    $x2=x+(25.0/1920.0)
    $y2=y+(193.0/1080.0)
    text "{font=times.ttf}[file_time]\n[last_phrase2]..." xpos x2 ypos y2 size 22

## ■██▓▒░ SAVE SCREEN ░▒▓███████████████████████████████████■
screen save_new:
    tag menu # This ensures that any other menu screen is replaced.
    key "game_menu" action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
    use all_pause
    
    add "background/efe/black.png" alpha 0.7
    add "saveload/caption.png" at caption # We add the save title image on top of the background
    add saveload_save_h at save
    add "saveload/hana_save.png" at hana_saveload
    add "saveload/hane_save.png" at hane
    imagebutton idle saveload_load_i hover saveload_load_h xpos (32.0/1920.0) ypos (530.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/zyosys7.ogg"), ShowMenu('load') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_exit_i hover saveload_exit_h xpos (32.0/1920.0) ypos (602.0/1080.0) focus_mask None action [ Play ("se20", se1100.pick()), Return() ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page1_i hover saveload_page1_h selected_idle saveload_page1_h xpos (32.0/1920.0) ypos (700.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(1) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page2_i hover saveload_page2_h selected_idle saveload_page2_h xpos (32.0/1920.0) ypos (772.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(2) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page3_i hover saveload_page3_h selected_idle saveload_page3_h xpos (32.0/1920.0) ypos (844.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(3) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page4_i hover saveload_page4_h selected_idle saveload_page4_h xpos (32.0/1920.0) ypos (916.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(4) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page5_i hover saveload_page5_h selected_idle saveload_page5_h xpos (32.0/1920.0) ypos (988.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(5) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    $ y=192.0 # ypos for the first save slot
#    for i in range(0, 4): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
    for i in range(0, 3): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
        imagebutton auto "saveload/savearea_%s.png" xpos (496.0/1920.0) ypos (y/1080.0) focus_mask None action  [ Play ("se9", "sys_se/mizu_d.ogg"), FileAction(i) ] at saveload_slot
        use load_save_slot(number=i, x=(496.0/1920.0), y=(y/1080.0)) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.
        $ y+=291.0 # We increase the y variable so every next save slot is moved 124px lower.
    $ y=160.0
#    for j in range(4, 8):
    for j in range(3, 6):
        imagebutton auto "saveload/savearea_%s.png" xpos (848.0/1920.0) ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/mizu_d.ogg"), FileAction(j) ] at saveload_slot
        use load_save_slot(number=j, x=(848.0/1920.0), y=(y/1080.0))
        $ y+=291.0
    $ y=128.0
    for k in range(6, 9):
        imagebutton auto "saveload/savearea_%s.png" xpos (1200.0/1920.0) ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/mizu_d.ogg"), FileAction(k) ] at saveload_slot
        use load_save_slot(number=k, x=(1200.0/1920.0), y=(y/1080.0))
        $ y+=291.0
    $ y=96.0
    for l in range(9, 12):
        imagebutton auto "saveload/savearea_%s.png" xpos (1552.0/1920.0) ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/mizu_d.ogg"), FileAction(l) ] at saveload_slot
        use load_save_slot(number=l, x=(1552.0/1920.0), y=(y/1080.0))
        $ y+=291.0

## ■██▓▒░ LOAD SCREEN ░▒▓███████████████████████████████████■
screen load:
    tag menu # This ensures that any other menu screen is replaced.
    
    if not r_for_title == 1:
        add "background/efe/black.png" alpha 0.7
        imagebutton idle saveload_save_i hover saveload_save_h xpos (32.0/1920.0) ypos (458.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/zyosys7.ogg"), ShowMenu('save_new') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        key "game_menu" action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
        use all_pause
    else:
        use title_background
#        add "saveload/bg.png"
        add "background/efe/black.png" alpha 0.5
    add "saveload/caption.png" at caption
    add saveload_load_h at load
    add "saveload/hana_load.png" at hana_saveload
    add "saveload/hane_load.png" at hane
    imagebutton idle saveload_exit_i hover saveload_exit_h xpos (32.0/1920.0) ypos (602.0/1080.0) focus_mask None action [ Play ("se20", se1100.pick()), Return() ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page1_i hover saveload_page1_h selected_idle saveload_page1_h xpos (32.0/1920.0) ypos (700.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(1) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page2_i hover saveload_page2_h selected_idle saveload_page2_h xpos (32.0/1920.0) ypos (772.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(2) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page3_i hover saveload_page3_h selected_idle saveload_page3_h xpos (32.0/1920.0) ypos (844.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(3) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page4_i hover saveload_page4_h selected_idle saveload_page4_h xpos (32.0/1920.0) ypos (916.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(4) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton idle saveload_page5_i hover saveload_page5_h selected_idle saveload_page5_h xpos (32.0/1920.0) ypos (988.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/page.ogg"), FilePage(5) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    $ y=192.0 # ypos for the first save slot
#    for i in range(0, 4):
    for i in range(0, 3):
        imagebutton auto "saveload/loadarea_%s.png" xpos (496.0/1920.0) ypos (y/1080.0) focus_mask None action FileAction(i) at saveload_slot
        use load_save_slot(number=i, x=(496.0/1920.0), y=(y/1080.0))
        $ y+=291.0
    $ y=160.0
#    for j in range(4, 8):
    for j in range(3, 6):
        imagebutton auto "saveload/loadarea_%s.png" xpos (848.0/1920.0) ypos (y/1080.0) focus_mask None action FileAction(j) at saveload_slot
        use load_save_slot(number=j, x=(848.0/1920.0), y=(y/1080.0))
        $ y+=291.0
    $ y=128.0
    for k in range(6, 9):
        imagebutton auto "saveload/loadarea_%s.png" xpos (1200.0/1920.0) ypos (y/1080.0) focus_mask None action FileAction(k) at saveload_slot
        use load_save_slot(number=k, x=(1200.0/1920.0), y=(y/1080.0))
        $ y+=291.0
    $ y=96.0
    for l in range(9, 12):
        imagebutton auto "saveload/loadarea_%s.png" xpos (1552.0/1920.0) ypos (y/1080.0) focus_mask None action FileAction(l) at saveload_slot
        use load_save_slot(number=l, x=(1552.0/1920.0), y=(y/1080.0))
        $ y+=291.0

default sl_slot = 0
default sl_page = 1

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
screen saveload:
    tag menu # This ensures that any other menu screen is replaced.
    
    if not r_for_title == 1:
        key "game_menu" action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
        use all_pause
    else:
        use title_background
    add "background/efe/black.png" alpha 0.6
    
    viewport id "saveload":
        area (0, 0, 1832, 1080)
        draggable True
        mousewheel True
        child_size (1600,10310) #(200*51) + 110 or maybe (200*50) + 180 + 110?
        
        $ y=180
        $ x=160
        $ f_num=1
        for i in range(0, 50):
            $ file_time = FileTime(i, format=_("%Y/%m/%d  %H:%M"), empty=" ", page=1)
            $ file_episode = FileJson(i, "episode", empty="{vspace=28}empty", missing=" ", page=1)
            $ file_chapter = FileJson(i, "chapter", empty=" ", missing=" ", page=1)
            if _preferences.language == None:
                $ file_chapter2 = file_chapter[0]
            elif _preferences.language == 'japanese':
                $ file_chapter2 = file_chapter[1]
            
            imagebutton idle saveload_box hover saveload_box_selected selected_idle saveload_box_selected xpos x ypos y focus_mask None action [SetVariable("sl_slot",i), Play ("se20", "sys_se/zyosys1.ogg")] hovered Play ("se10", "sys_se/zyosys0.ogg")
            add FileScreenshot(i, empty="saveload/nodata.png", page=1) xpos (x+5) ypos (y+5)
            text "[f_num]." xpos (x+335) ypos y font "timesbd.ttf" size 74
            text "[file_time]" xanchor 1.0 xpos (x+1590) ypos (y+5) font "timesbd.ttf" size 50
            text "[file_episode]" xpos (x+335) ypos (y+72) font "micross.ttf" size 44
            text "[file_chapter2]" xpos (x+335) ypos (y+128) font "micross.ttf" size 44
            $ y+=200
            $ f_num+=1
#    if sl_slot < 12:
    $ sl_page = 1
#    else:
#        $ sl_page = 2
    add "saveload/caption.png" at caption
    add "r_click/sysmenu/fg.png" yalign 1.0
    add "config/vscrollbar.png" xcenter (1875.0/1920.0) ycenter (584.0/1080.0)
    vbar value YScrollValue("saveload") style style.sl_vbar
    imagebutton idle saveload_load2_i hover saveload_load2_h insensitive saveload_load2_l xcenter (1083.0/1920.0) ycenter (1034.0/1080.0) focus_mask None action [FileLoad(sl_slot, confirm=True, page=sl_page), Play ("se20", "sys_se/zyosys3.ogg")]
    imagebutton idle saveload_save2_i hover saveload_save2_h insensitive saveload_save2_l xcenter (1292.0/1920.0) ycenter (1034.0/1080.0) focus_mask None action [FileSave(sl_slot, confirm=True, page=sl_page), Play ("se20", "sys_se/zyosys3.ogg")]
    imagebutton idle saveload_delete_i hover saveload_delete_h insensitive saveload_delete_l xcenter (1513.0/1920.0) ycenter (1034.0/1080.0) focus_mask None action [FileDelete(sl_slot, confirm=True, page=sl_page), Play ("se20", "sys_se/zyosys3.ogg")]
    imagebutton idle exit_i hover exit_h xpos (1856.0/1920.0) ypos (1064.0/1080.0) xanchor 1.0 yanchor 1.0 focus_mask None action [ Play ("se20", se1100.pick()), Return() ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    
style sl_vbar:
    bar_vertical True
    bar_invert True
    xmaximum 26
    ymaximum 784
    xcenter (1875.0/1920.0)
    ycenter (584.0/1080.0)
    top_bar None
    bottom_bar None
    thumb "saveload/vscrollbar_thumb.png"
    thumb_offset 0
    thumb_shadow None

init -2:
    transform caption:
#        xpos (32.0/1920.0) ypos 0
        xpos (64.0/1920.0) ypos (32.0/1080.0)
    transform save:
        xpos (32.0/1920.0) ypos (458.0/1080.0)
    transform load:
        xpos (32.0/1920.0) ypos (530.0/1080.0)
    transform hana:
        xalign 1.0 yalign 1.0 zoom 2.0
    transform hana_saveload:
#        xpos (1182.0/1920.0) ypos (233.0/1080.0)
        xpos (config.screen_width - 18) ypos (config.screen_height - 23) anchor (1.0,1.0)
    transform hane:
        xpos (32.0/1920.0) ypos (128.0/1080.0)
    transform saveload_slot:
        alpha 0.75
    
##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
    #_preferences.text_cps
screen preferences_old:

    tag menu
    if not r_for_title == 1:
        key "game_menu" action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
    
    add "config/old/bg.png"
    add "config/caption.png" at caption
    imagebutton auto "title/menu/exit_%s.png" xpos 1722 ypos 988 focus_mask None action [Play("se20", "sys_se/zyosys3.ogg"), Return()] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton auto "config/old/def_%s.png" xpos 876 ypos 908 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('config_yesno') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    textbutton "Audio Emphasis On" xpos 64 ypos 988 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('emphasize audio', 'enable') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    textbutton "Audio Emphasis Off" xpos 504 ypos 988 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('emphasize audio', 'disable') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    textbutton "Bgm Text (JP)" xpos 960 ypos 988 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "bgm_lang", 0) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    textbutton "Bgm Text (EN)" xpos 1300 ypos 988 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "bgm_lang", 1) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    if config_pg == 1:
        add "config/old/fg.png"
        imagebutton auto "config/old/fullscreen_%s.png" xpos 275 ypos 216 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('display', 'fullscreen') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/window_%s.png" xpos 534 ypos 216 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('display', 'any window') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        textbutton "Resize" xpos (534.0/1920.0) ypos (266.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('display', 'window') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/slow_%s.png" xpos 305 ypos 458 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('text speed', 25) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/fast_%s.png" xpos 469 ypos 458 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('text speed', 50) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/instant_%s.png" xpos 619 ypos 458 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('text speed', 0) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/yes_%s.png" xpos 302 ypos 725 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('skip', 'all') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/no_%s.png" xpos 514 ypos 725 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('skip', 'seen') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/yes_%s.png" xpos 302 ypos 869 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "bgm_text", True) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/no_%s.png" xpos 514 ypos 869 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "bgm_text", False) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/yes_%s.png" xpos 1262 ypos 209 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('wait for voice', 'enable') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/no_%s.png" xpos 1474 ypos 209 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), Preference('wait for voice', 'disable') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/msgmenu_%s.png" xpos 1228 ypos 869 focus_mask None action [ Play ("se20", "sys_se/page.ogg"), SetVariable("config_pg", 2) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        frame xpos 305 ypos 608:
            style_group "pref"
            has vbox
            bar value Preference("auto-forward time")
        frame xpos 1265 ypos 476:
            style_group "pref"
            has vbox
            bar value Preference("music volume")
        frame xpos 1265 ypos 640:
            style_group "pref"
            has vbox
            bar value Preference("sound volume")
        frame xpos 1265 ypos 804:
            style_group "pref"
            has vbox
            bar value Preference("voice volume")
    elif config_pg == 2:
        add "config/old/msgmenu_idle.png" xpos 204 ypos 144
        imagebutton auto "config/old/msgwnd_%s.png" xpos 126 ypos 474 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "msgwnd", "efe/msgwnd.png"), SetField(persistent, "chrwnd", "efe/chrwnd.png") ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/msgwnd2_%s.png" xpos 1020 ypos 233 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "msgwnd", "efe/msgwnd2.png"), SetField(persistent, "chrwnd", "efe/chrwnd2.png") ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/msgwnd3_%s.png" xpos 128 ypos 231 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "msgwnd", "efe/msgwnd3.png"), SetField(persistent, "chrwnd", "efe/chrwnd3.png") ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/msgwnd4_%s.png" xpos 1026 ypos 474 focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), SetField(persistent, "msgwnd", "efe/msgwnd4.png"), SetField(persistent, "chrwnd", "efe/chrwnd4.png") ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        imagebutton auto "config/old/back_%s.png" xpos 546 ypos 140 focus_mask None action [ Play ("se20", "sys_se/page.ogg"), SetVariable("config_pg", 1) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    
    if config.developer == True:
        text "Music [_preferences.volumes[music]]" xpos (1650.0/1920.0) ypos (20.0/1080.0)
        text "Sound [_preferences.volumes[sfx]]" xpos (1650.0/1920.0) ypos (50.0/1080.0)
        text "Voice [_preferences.volumes[voice]]" xpos (1650.0/1920.0) ypos (80.0/1080.0)
        text "AFM [_preferences.afm_time]" xpos (1650.0/1920.0) ypos (110.0/1080.0)

init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "config/slider_full.png"
    style.pref_slider.right_bar = "config/slider_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 440
    style.pref_slider.ymaximum = 36    
init python: 
    if renpy.android:
        config_y = 1460
    else:
#        config_y = 1680
        config_y = 1840

screen preferences:

    tag menu
    
    if not r_for_title == 1:
        key "game_menu" action [Play("se10", "sys_se/zyosys3.ogg"), Return()]
        add "background/efe/black.png" alpha 0.7
        use all_pause
    else:
        use title_background
        add "background/efe/black.png" alpha 0.5
    
    viewport id "config":
        area (128, 0, 1610, 1080)
        draggable True
        mousewheel True
        child_size (1610,config_y)
#        vbox:
#            null height 190
        
#        $ x = 1680.0
        $ x = 1840.0
        $ y1 = 200.0
        if not renpy.android:
            $ y2 = 474.0 #254.0
            $ y3 = 200.0
            $ y4 = 504.0
            
#            add "config/category_1.png" ypos (y1/x)
            add category_1 ypos (y1/x)
            $ y1 += 62.0
            add menu_000_01 ypos (y1/x) xalign 0.0                 # ypos is same    # screen size
            if _preferences.language == None:
                add menu_001_05 ypos (y1/x) xpos (844.0/1610.0)        # ypos is same    # windowed
            elif _preferences.language == 'japanese':
                $ y1 -= 21.0
                add menu_001_05 ypos (y1/x) xpos (882.0/1610.0)                      # windowed
                $ y1 += 21.0
            $ y1 += 80.0
            add menu_000_12 ypos (y1/x) xalign 0.0                                   # FMV
            $ y3 += 62
            imagebutton idle menu_001_06_i hover menu_001_06_h selected_idle menu_001_06_s_i selected_hover menu_001_06_s_h xpos (1198.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('display', 'fullscreen') ] hovered Play ("se10", se1002)
            $ y3 += 58
            if _preferences.language == None:
                imagebutton idle menu_001_05_1_i hover menu_001_05_1_h selected_idle menu_001_05_1_s_i selected_hover menu_001_05_1_s_h xpos (844.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('display', 'any window') ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_05_2_i hover menu_001_05_2_h selected_idle menu_001_05_2_s_i selected_hover menu_001_05_2_s_h xpos (1022.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('display', 'window') ] hovered Play ("se10", se1002)
            elif _preferences.language == 'japanese':
                $ y3 -= 7.0
                imagebutton idle menu_001_05_1_i hover menu_001_05_1_h selected_idle menu_001_05_1_s_i selected_hover menu_001_05_1_s_h xpos (877.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('display', 'any window') ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_05_2_i hover menu_001_05_2_h selected_idle menu_001_05_2_s_i selected_hover menu_001_05_2_s_h xpos (1104.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('display', 'window') ] hovered Play ("se10", se1002)
                $ y3 += 7.0
            $ y3 += 22
            imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1346.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "fmv", False) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "fmv", True) ] hovered Play ("se10", se1002)
            $ y1 += 78.0
            $ y3 += 438.0 #358.0
        else:
            $ y2 = 254.0 #394.0
            $ y3 = 560.0 #480.0
            $ y4 = 284.0
        
#        add "config/category_2.png" ypos (y1/x)
        add category_2 ypos (y1/x)
        $ y1 += 62.0
        add menu_000_02 ypos (y1/x) xalign 0.0                                       # BGM
        $ y1 += 80.0
        add menu_000_03 ypos (y1/x) xalign 0.0                                       # Sound Effects
        $ y1 += 80.0
        add menu_000_04 ypos (y1/x) xalign 0.0                                       # Voices
        $ y1 += 78.0
#        add "config/category_3.png" ypos (y1/x)
        add category_3 ypos (y1/x)
        $ y1 += 62.0
        add menu_000_05 ypos (y1/x) xalign 0.0                                       # Window
        $ y1 += 80.0
        add menu_000_06 ypos (y1/x) xalign 0.0                                       # Text speed
        $ y1 += 80.0
        add menu_000_07 ypos (y1/x) xalign 0.0                                       # Auto speed
        $ y1 += 80.0
        add menu_000_15 ypos (y1/x) xalign 0.0                                       # Game Lang.
        $ y1 += 80.0
        add menu_000_16 ypos (y1/x) xalign 0.0                                       # Achievements
        $ y1 += 80.0
        add menu_000_08 ypos (y1/x) xalign 0.0                                       # Skip unread text
        $ y1 += 80.0
        add menu_000_09 ypos (y1/x) xalign 0.0                                       # BGM Text
        $ y1 += 80.0
        add menu_000_10 ypos (y1/x) xalign 0.0                                       # Wait for Voice
        $ y1 += 80.0
        add menu_000_11 ypos (y1/x) xalign 0.0                                       # Bgm Text Lang.
        $ y1 += 80.0
        if persistent.tsuru_flg:
            add menu_000_17 ypos (y1/x) xalign 0.0                                       # Tsuru flag
        else:
            add menu_000_locked xalign 0.0 ypos (y1/x)
        
        add slider_mm ypos (y2/x) xpos (1192.0/1610.0)
        $ y2 += 80.0
        add slider_mm ypos (y2/x) xpos (1192.0/1610.0)
        $ y2 += 80.0
        add slider_mm ypos (y2/x) xpos (1192.0/1610.0)
        $ y2 += 220.0
        add slider_sf ypos (y2/x) xpos (1192.0/1610.0)
        $ y2 += 80.0
        add slider_sf ypos (y2/x) xpos (1192.0/1610.0)
        
        imagebutton idle type_1_i hover type_1_h selected_idle type_1_s_i selected_hover type_1_s_h xpos (952.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "config_msgwnd", 3), SetField(persistent, "msgwnd", "efe/msgwnd3.png"), SetField(persistent, "chrwnd", "efe/chrwnd3.png") ] hovered Play ("se10", se1002)
        imagebutton idle type_2_i hover type_2_h selected_idle type_2_s_i selected_hover type_2_s_h xpos (1116.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "config_msgwnd", 2), SetField(persistent, "msgwnd", "efe/msgwnd2.png"), SetField(persistent, "chrwnd", "efe/chrwnd2.png") ] hovered Play ("se10", se1002)
        imagebutton idle type_3_i hover type_3_h selected_idle type_3_s_i selected_hover type_3_s_h xpos (1280.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "config_msgwnd", 1), SetField(persistent, "msgwnd", "efe/msgwnd.png"), SetField(persistent, "chrwnd", "efe/chrwnd.png") ] hovered Play ("se10", se1002)
        imagebutton idle type_4_i hover type_4_h selected_idle type_4_s_i selected_hover type_4_s_h xpos (1444.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "config_msgwnd", 4), SetField(persistent, "msgwnd", "efe/msgwnd4.png"), SetField(persistent, "chrwnd", "efe/chrwnd4.png") ] hovered Play ("se10", se1002)
        
        $ y3 += 103
        $ slider_x = 1192.0
#        $ slider_y = 803.0
        $ t_sp_cfg = 25
        
        for tmp2 in range(0,11):
            if not tmp2 == 10:
                imagebutton idle slider_sp_i hover slider_sp_h selected_idle slider_sp_s_i selected_hover slider_sp_s_h xpos (slider_x/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('text speed', t_sp_cfg) ] hovered Play ("se10", se1002)
                $ t_sp_cfg += 5
            else:
                imagebutton idle slider_sp_i hover slider_sp_h selected_idle slider_sp_s_i selected_hover slider_sp_s_h xpos (slider_x/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('text speed', 0) ] hovered Play ("se10", se1002)
            $ slider_x += 36.0
        
        $ y3 += 80.0
        $ slider_x = 1192.0
#        $ slider_y = 883.0
        $ afm_cfg = 3
        
        for tmp2 in range(0,11):
            imagebutton idle slider_sp_i hover slider_sp_h selected_idle slider_sp_s_i selected_hover slider_sp_s_h xpos (slider_x/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('auto-forward time', afm_cfg) ] hovered Play ("se10", se1002)
            $ slider_x += 36.0
            $ afm_cfg += 2
        
        $ y3 += 59.0
        if _preferences.language == None:
            imagebutton idle menu_001_07_i hover menu_001_07_h selected_idle menu_001_07_s_i selected_hover menu_001_07_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Language(None) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_08_i hover menu_001_08_h selected_idle menu_001_08_s_i selected_hover menu_001_08_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Language("japanese") ] hovered Play ("se10", se1002)
        elif _preferences.language == 'japanese':
            imagebutton idle menu_001_07_i hover menu_001_07_h selected_idle menu_001_07_s_i selected_hover menu_001_07_s_h xpos (1355.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Language(None) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_08_i hover menu_001_08_h selected_idle menu_001_08_s_i selected_hover menu_001_08_s_h xpos (1456.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Language("japanese") ] hovered Play ("se10", se1002)
        $ y3 += 80.0
        if _preferences.language == None:
            imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1346.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "ach_toggle", False) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "ach_toggle", True) ] hovered Play ("se10", se1002)
        elif _preferences.language == 'japanese':
            imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "ach_toggle", False) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "ach_toggle", True) ] hovered Play ("se10", se1002)
        $ y3 += 80.0
        if _preferences.language == None:
            imagebutton idle menu_001_02_i hover menu_001_02_h selected_idle menu_001_02_s_i selected_hover menu_001_02_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('skip', 'seen') ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_01_i hover menu_001_01_h selected_idle menu_001_01_s_i selected_hover menu_001_01_s_h xpos (1470.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('skip', 'all') ] hovered Play ("se10", se1002)
        elif _preferences.language == 'japanese':
            imagebutton idle menu_001_02_i hover menu_001_02_h selected_idle menu_001_02_s_i selected_hover menu_001_02_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('skip', 'seen') ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_01_i hover menu_001_01_h selected_idle menu_001_01_s_i selected_hover menu_001_01_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('skip', 'all') ] hovered Play ("se10", se1002)
        $ y3 += 80.0
        if _preferences.language == None:
            imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1346.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_text", False) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_text", True) ] hovered Play ("se10", se1002)
        elif _preferences.language == 'japanese':
            imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_text", False) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_text", True) ] hovered Play ("se10", se1002)
        $ y3 += 80.0
        if _preferences.language == None:
            imagebutton idle menu_001_02_i hover menu_001_02_h selected_idle menu_001_02_s_i selected_hover menu_001_02_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('wait for voice', 'disable') ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_01_i hover menu_001_01_h selected_idle menu_001_01_s_i selected_hover menu_001_01_s_h xpos (1470.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('wait for voice', 'enable') ] hovered Play ("se10", se1002)
        elif _preferences.language == 'japanese':
            imagebutton idle menu_001_02_i hover menu_001_02_h selected_idle menu_001_02_s_i selected_hover menu_001_02_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('wait for voice', 'disable') ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_01_i hover menu_001_01_h selected_idle menu_001_01_s_i selected_hover menu_001_01_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), Preference('wait for voice', 'enable') ] hovered Play ("se10", se1002)
        $ y3 += 80.0
        if _preferences.language == None:
            imagebutton idle menu_001_07_i hover menu_001_07_h selected_idle menu_001_07_s_i selected_hover menu_001_07_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_lang", 1) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_08_i hover menu_001_08_h selected_idle menu_001_08_s_i selected_hover menu_001_08_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_lang", 0) ] hovered Play ("se10", se1002)
        elif _preferences.language == 'japanese':
            imagebutton idle menu_001_07_i hover menu_001_07_h selected_idle menu_001_07_s_i selected_hover menu_001_07_s_h xpos (1355.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_lang", 1) ] hovered Play ("se10", se1002)
            imagebutton idle menu_001_08_i hover menu_001_08_h selected_idle menu_001_08_s_i selected_hover menu_001_08_s_h xpos (1456.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "bgm_lang", 0) ] hovered Play ("se10", se1002)
        $ y3 += 80.0
        if persistent.tsuru_flg:
            if _preferences.language == None:
                imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1346.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "tsurupettan", False) ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "tsurupettan", True) ] hovered Play ("se10", se1002)
            elif _preferences.language == 'japanese':
                imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "tsurupettan", False) ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "tsurupettan", True) ] hovered Play ("se10", se1002)
        
        $ y3 += 80.0
        if persistent.UMINEKOEND >= 50:
            add menu_000_13 ypos (y3/x) xalign 0.0
            if _preferences.language == None:
                imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1346.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm", False) ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm", True) ] hovered Play ("se10", se1002)
            elif _preferences.language == 'japanese':
                imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm", False) ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm", True) ] hovered Play ("se10", se1002)
            $ y3 += 80.0
            add menu_000_14 ypos (y3/x) xalign 0.0
            if _preferences.language == None:
                imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1346.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm2", False) ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1491.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm2", True) ] hovered Play ("se10", se1002)
#                text "This overrides some of \nthe original Anime tracks" xpos (840.0/1610.0) ypos ((y3+11.0)/x) size 26 font "times.ttf"
            elif _preferences.language == 'japanese':
                imagebutton idle menu_001_04_i hover menu_001_04_h selected_idle menu_001_04_s_i selected_hover menu_001_04_s_h xpos (1364.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm2", False) ] hovered Play ("se10", se1002)
                imagebutton idle menu_001_03_i hover menu_001_03_h selected_idle menu_001_03_s_i selected_hover menu_001_03_s_h xpos (1482.0/1610.0) ypos (y3/x) focus_mask None action [ Play ("se20", se1001), SetField(persistent, "anime_bgm2", True) ] hovered Play ("se10", se1002)
#                text "これは元のアニメトラックの\n一部をオーバーライドします" xpos (484.0/1610.0) ypos ((y3+11.0)/x) size 26 font "msgothic.ttc"
        else:
            $ y3 += 4.0
            add menu_000_locked ypos (y3/x) xalign 0.0
            $ y3 += 80.0
            add menu_000_locked ypos (y3/x) xalign 0.0
        
        $ slider_x = 1192.0
#        $ slider_y = 424.0
        $ config_vol = 0.0
        
        for tmp in range(0,11):
            imagebutton idle slider_vol[0][tmp] hover slider_vol[1][tmp] selected_idle slider_vol[2][tmp] selected_hover slider_vol[3][tmp] xpos (slider_x/1610.0) ypos (y4/x) focus_mask None action [ Play ("se20", se1001), Preference('music volume', config_vol) ] hovered Play ("se10", se1002)
            $ y4 += 80.0
            imagebutton idle slider_vol[0][tmp] hover slider_vol[1][tmp] selected_idle slider_vol[2][tmp] selected_hover slider_vol[3][tmp] xpos (slider_x/1610.0) ypos (y4/x) focus_mask None action [ Play ("se20", se1001), Preference('sound volume', config_vol) ] hovered Play ("se10", se1002)
            $ y4 += 80.0
            imagebutton idle slider_vol[0][tmp] hover slider_vol[1][tmp] selected_idle slider_vol[2][tmp] selected_hover slider_vol[3][tmp] xpos (slider_x/1610.0) ypos (y4/x) focus_mask None action [ Play ("se20", se1001), Preference('voice volume', config_vol) ] hovered Play ("se10", se1002)
            $ y4 -= 160.0
            $ slider_x += 36.0
            $ config_vol += 0.1
        
    add "config/vscrollbar.png" xcenter (1876.0/1920.0) yanchor 0.5 ypos (580.0/1080.0)
    vbar value YScrollValue("config") style style.c_vbar
    
    add "config/caption.png" at caption
    add "r_click/sysmenu/fg.png" yalign 1.0
    
    imagebutton idle exit_i hover exit_h xpos (1739.0/1920.0) ypos (997.0/1080.0) focus_mask None action [Play("se20", "sys_se/zyosys3.ogg"), Return()] hovered Play ("se10", "sys_se/zyosys0.ogg")
    imagebutton auto "config/def_%s.png" xalign 0.5 yanchor 1.0 ypos (1064.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/zyosys1.ogg"), ShowMenu('config_yesno') ] hovered Play ("se10", "sys_se/zyosys0.ogg")
    
    if config.developer == True:
        text "Music [_preferences.volumes[music]]" xpos (1650.0/1920.0) ypos (20.0/1080.0)
        text "Sound [_preferences.volumes[sfx]]" xpos (1650.0/1920.0) ypos (50.0/1080.0)
        text "Voice [_preferences.volumes[voice]]" xpos (1650.0/1920.0) ypos (80.0/1080.0)
        text "AFM   [_preferences.afm_time]" xpos (1650.0/1920.0) ypos (110.0/1080.0)
        text "TXTSP [_preferences.text_cps]" xpos (1650.0/1920.0) ypos (140.0/1080.0)
        

style c_vbar:
    bar_vertical True
    bar_invert True
    xmaximum 26
    ymaximum 784
#    yalign 0.5
    xcenter (1876.0/1920.0)
    yanchor 0.5
    ypos (580.0/1080.0)
    top_bar None
    bottom_bar None
    thumb "config/vscrollbar_thumb.png"
    thumb_offset 0
    thumb_shadow None

init python:
#    slider_vol = ["config/slider_vol_0_%s.png", "config/slider_vol_01_%s.png", "config/slider_vol_02_%s.png", "config/slider_vol_03_%s.png", "config/slider_vol_04_%s.png", "config/slider_vol_05_%s.png", "config/slider_vol_06_%s.png", "config/slider_vol_07_%s.png", "config/slider_vol_08_%s.png", "config/slider_vol_09_%s.png", "config/slider_vol_10_%s.png"],
    slider_vol = [[im.MatrixColor(im.Crop("config/slider.png", (0,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (41,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (80,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (120,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (160,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (200,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (240,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (280,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (320,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (360,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (400,0,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))],
                [im.MatrixColor(im.Crop("config/slider.png", (0,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (41,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (80,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (120,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (160,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (200,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (240,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (280,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (320,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (360,0,36,36)), im.matrix.opacity(0.7)),
                    im.MatrixColor(im.Crop("config/slider.png", (400,0,36,36)), im.matrix.opacity(0.7))],
                [im.MatrixColor(im.Crop("config/slider.png", (0,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (41,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (80,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (120,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (160,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (200,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (240,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (280,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (320,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (360,0,36,36)), im.matrix.brightness(-0.5)),
                    im.MatrixColor(im.Crop("config/slider.png", (400,0,36,36)), im.matrix.brightness(-0.5))],
                [im.Crop("config/slider.png", (0,0,36,36)),
                    im.Crop("config/slider.png", (41,0,36,36)),
                    im.Crop("config/slider.png", (80,0,36,36)),
                    im.Crop("config/slider.png", (120,0,36,36)),
                    im.Crop("config/slider.png", (160,0,36,36)),
                    im.Crop("config/slider.png", (200,0,36,36)),
                    im.Crop("config/slider.png", (240,0,36,36)),
                    im.Crop("config/slider.png", (280,0,36,36)),
                    im.Crop("config/slider.png", (320,0,36,36)),
                    im.Crop("config/slider.png", (360,0,36,36)),
                    im.Crop("config/slider.png", (400,0,36,36))]
                    ]
                    

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:
    on "show" action Play("se9", se1000)
    modal True
    
    if r_for_title == 0:
        $ renpy.force_autosave()
    
    fixed:
        xcenter (930.0/1920.0) ycenter (540.0/1080.0) xmaximum 510 ymaximum 312
        if message == layout.ARE_YOU_SURE:
            add "r_click/sysmenu/you_sure.png" alpha (230.0/255.0)
        elif message == layout.DELETE_SAVE:
            add "r_click/sysmenu/delete_save.png" alpha (230.0/255.0)
        elif message == layout.OVERWRITE_SAVE:
            add "r_click/sysmenu/overwrite_save.png" alpha (230.0/255.0)
        elif message == layout.LOADING:
            add "r_click/sysmenu/loading.png" alpha (230.0/255.0)
        elif message == layout.QUIT:
            add "r_click/sysmenu/quit.png" alpha (230.0/255.0)
        elif message == layout.MAIN_MENU:
            add "r_click/sysmenu/title_bg.png" alpha (230.0/255.0)
        
        imagebutton auto "title/menu/unlock_yes_%s.png" xpos (50.0/510.0) ypos (128.0/312.0) focus_mask None action yes_action
        imagebutton auto "title/menu/unlock_no_%s.png" xpos (50.0/510.0) ypos (213.0/312.0) focus_mask None action [ no_action, Play ("se9", se1000) ]
    
    
#    window:
#        style "gm_root"

#    frame:
#        style_group "yesno"

#        xfill True
#        xmargin .05
#        ypos .1
#        yanchor 0
#        ypadding .05
        
#        has vbox:
#            xalign .5
#            yalign .5
#            spacing 30
            
#        label _(message):
#            xalign 0.5

#        hbox:
#            xalign 0.5
#            spacing 100
            
#            textbutton _("Yes") action yes_action
#            textbutton _("No") action no_action


#init -2 python:    
#    style.yesno_button.size_group = "yesno"
#    style.yesno_label_text.text_align = 0.5init python:


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

#    key "a" action Preference("auto-forward", "toggle")
#    key "x" action HideInterface()             # h?
#    text "AFM [_preferences.afm_enable]" xpos (1650.0/1920.0) ypos (110.0/1080.0)
    
    if renpy.android == True:
#        imagebutton auto "android_skip_%s.png" action Skip()
#        imagebutton auto "android_auto_%s.png" action Preference("auto-forward", "toggle")
        imagebutton auto "android_menu_%s.png" xpos (1800.0/1920.0) ypos (32.0/1080.0) action ShowMenu("save")
    
    timer 0.5 action [time_calc(), ach_chk()]
    
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
    def _custom_overlay():
        renpy.show_screen("custom_ovl")
    
    def _auto_indicator_custom():
        if renpy.has_screen("auto_indicator"):
            if _preferences.afm_enable and not renpy.get_screen("auto_indicator"):
                renpy.show_screen("auto_indicator")
            elif not _preferences.afm_enable and renpy.get_screen("auto_indicator"):
                renpy.hide_screen("auto_indicator")
            return
    config.overlay_functions.append(_auto_indicator_custom)
    config.overlay_functions.append(_custom_overlay)
    
    def ach_check():
        cg_counter()
        if persistent.runtime >= 180000 and not achievement.has(19):
            get_achievement(19)
        if renpy.count_seen_dialogue_blocks() >= 30000 and not achievement.has(20):     ## has approx. 68609 lines
            get_achievement(20)
    ach_chk = renpy.curry(ach_check)
    
    if not persistent.tips_new:
        persistent.tips_new = [[False for x in range(0,10)] for x in range(0,9)]
    if not persistent.grim_new:
        persistent.grim_new = [[False for x in range(0,15)] for x in range(0,5)]
    if not persistent.cha_new:
        persistent.cha_new = [[[[False for x in range(0,5)] for x in range(0,60)] for x in range(0,4)] for x in range(0,10)]
    
    def tips_check(mod,epi,num):
        if mod == "tips":
            persistent.tips_new[epi][num] = 2
        elif mod == "grim":
            persistent.grim_new[epi][num] = 2
        tips = 0
        grim = 0
        if not achievement.has(2) and epi == 1:
            for x in range(1,8):
                if persistent.tips_new[1][x] == 2:
                    tips+=1
            for x in range(1,12):
                if persistent.grim_new[1][x] == 2:
                    grim+=1
            if tips == 7 and grim == 11:
                get_achievement(2)
        if not achievement.has(4) and epi == 2:
            for x in range(1,8):
                if persistent.tips_new[2][x] == 2:
                    tips+=1
                if persistent.grim_new[2][x] == 2:
                    grim+=1
            if tips == 7 and grim == 7:
                get_achievement(4)
        if not achievement.has(6) and epi == 3:
            for x in range(1,7):
                if persistent.tips_new[3][x] == 2:
                    tips+=1
            for x in range(1,14):
                if persistent.grim_new[3][x] == 2:
                    grim+=1
            if tips == 6 and grim == 13:
                get_achievement(6)
        if not achievement.has(8) and epi == 4:
            for x in range(1,8):
                if persistent.tips_new[4][x] == 2:
                    tips+=1
            for x in range(1,13):
                if persistent.grim_new[4][x] == 2:
                    grim+=1
            if tips == 7 and grim == 12:
                get_achievement(8)
    tips_chk = renpy.curry(tips_check)
    
    def cha_check(epi,side,cha,con,con_end):
        global r
        global r_ma
        persistent.cha_new[epi][side][cha][con] = 2
        cha_add = 0
        if not achievement.has(3) and epi == 1:
            for x in range(1,20):
                for y in range(1,r[x][condition_end]+1):
                    if persistent.cha_new[1][1][x][y] == 2:
                        cha_add+=1
            for x in range(1,3):
                for y in range(1,r_ma[x][condition_end]+1):
                    if persistent.cha_new[1][2][x][y] == 2:
                        cha_add+=1
            if cha_add == 43:
                get_achievement(3)
        if not achievement.has(5) and epi == 2:
            for x in range(1,cha_kazu_ep2):
                for y in range(1,r[x][condition_end]+1):
                    if persistent.cha_new[2][1][x][y] == 2:
                        cha_add+=1
            for x in range(1,cha_kazu_ep2_2):
                for y in range(1,r_ma[x][condition_end]+1):
                    if persistent.cha_new[2][2][x][y] == 2:
                        cha_add+=1
            if cha_add == 58:
                get_achievement(5)
        if not achievement.has(7) and epi == 3:
            for x in range(1,20):
                for y in range(1,r[x][condition_end]+1):
                    if persistent.cha_new[3][1][x][y] == 2:
                        cha_add+=1                                # 37 states
            for x in range(1,cha_kazu_ep3_2):
                for y in range(1,r_ma[x][condition_end]+1):
                    if persistent.cha_new[3][2][x][y] == 2:
                        cha_add+=1                                # 17 states
            for y in range(1,r[r_enj][condition_end]+1):
                if persistent.cha_new[3][1][r_enj][y] == 2:
                    cha_add+=1                                    # 1 states
            if cha_add == 55:
                get_achievement(7)
        if not achievement.has(9) and epi == 4:
            for x in range(1,20):
                for y in range(1,r[x][condition_end]+1):
                    if persistent.cha_new[4][1][x][y] == 2:
                        cha_add+=1                                # 38 states
            for x in range(1,cha_kazu_ep4_2):
                for y in range(1,r_ma[x][condition_end]+1):
                    if persistent.cha_new[4][2][x][y] == 2:
                        cha_add+=1                                # 27 states
            for x in range(1,cha_kazu_ep4_3):
                for y in range(1,r_enj_ma[x][condition_end]+1):
                    if persistent.cha_new[4][3][x][y] == 2:
                        cha_add+=1                                # 19 states
            if cha_add == 84:
                get_achievement(9)
    cha_chk = renpy.curry(cha_check)
    
    def config_check():
        if not achievement.has(10):
            if not preferences.text_cps == 50 or not preferences.skip_unseen == False or not preferences.wait_voice == True or not preferences.afm_time == 3 or not _preferences.volumes['music'] == 0.6 or not _preferences.volumes['sfx'] == 0.7 or not (_preferences.volumes['voice'] > 0.75 and _preferences.volumes['voice'] < 0.85)or not persistent.bgm_text == True or not persistent.bgm_lang == 0 or not persistent.config_msgwnd == 3 or not persistent.fmv == True or not persistent.anime_bgm == False or not persistent.anime_bgm2 == False or not persistent.tsurupettan == False:
                ## remember to change fmv for non-portable versions
                get_achievement(10)
#    config_chk = renpy.curry(config_check)
    
    
##############################################################################
# More parameters go here.
#

screen custom_ovl:
    key "a" action Preference("auto-forward", "toggle")
    if renpy.android == True:
        imagebutton auto "android_skip_%s.png" xpos (10.0/1920.0) ypos (716.0/1080.0) action Skip()
        imagebutton auto "android_auto_%s.png" xpos (10.0/1920.0) ypos (806.0/1080.0) action Preference("auto-forward", "toggle")
#        imagebutton auto "android_menu_%s.png" xpos (10.0/1920.0) ypos (896.0/1080.0) action ShowMenu("save")
    

screen auto_indicator:
#    on "show" action Play("se20", "sys_se/System3.ogg")
#    on "hide" action Play("se20", "sys_se/System2.ogg")
    on "show" action Play("se20", "sys_se/son.ogg")
    on "hide" action Play("se20", "sys_se/soff.ogg")
    if persistent.bgm_text:
        $ auto_y = (90.0/1080.0)
    else:
        $ auto_y = (40.0/1080.0)
    if not config.skipping:
        add "auto_arrow" xpos (34.0/1920.0) ypos auto_y
    elif config.skipping:
        add "auto_arrow" xpos (106.0/1920.0) ypos auto_y

screen skip_indicator:
    
    ## Added new lines to 00library from github that will likely stay after update     # they seem to have stayed
    
#    on "show" action Play("se20", "sys_se/System3.ogg")
#    on "hide" action Play("se20", "sys_se/System2.ogg")
    on "show" action Play("se20", "sys_se/son.ogg")
    on "hide" action Play("se20", "sys_se/soff.ogg")
    if persistent.bgm_text:
        $ fast_y = (82.0/1080.0)
    else:
        $ fast_y = (32.0/1080.0)
    if not renpy.game.context().seen_current(True) and not _preferences.skip_unseen:
#    if not renpy.game.context().seen_current(True) or not _skipping:
        add "fast_forward_disabled_arrow" xpos (26.0/1920.0) ypos fast_y
    else:
        add "fast_forward_arrow" xpos (26.0/1920.0) ypos fast_y


## for 30000 click trophy: if renpy.count_seen_dialogue_blocks == 30000:

screen trophy(trop_id,trop_id2):
    on "show" action Play("se10", "sys_se/trophy.ogg")
    zorder 255
    add "trophies/caption.png" at _trophy1
    add "trophies/TROP0%s.png" % trop_id at _trophy2
    text "You have earned a trophy!" at _trophy3
    text trop_id2 at _trophy4
    timer 4.3 action Hide('trophy')

screen autosave:
    zorder 255
    add "saveload/autosave.png" at _autosave
    
    timer 8.0 action Hide('autosave')

screen chp_notify(x):
    zorder 255
    if _preferences.language == None:
        text r_click_chp[0] at _chp_notify style style.chp_notify_
    elif _preferences.language == 'japanese':
        text r_click_chp[1] at _chp_notify_jp style style.chp_notify_jp
    
    timer 5.0 action Hide('chp_notify')
    
style chp_notify_:
    size 40
    #drop_shadow (2, 2)
    font "default.ttf"
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    
style chp_notify_jp:
    size 54
    #drop_shadow (2, 2)
    font "msgothic.ttc"
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    
transform _chp_notify:
    xpos (32.0/1920.0)
    yanchor 1.0 ypos (1056.0/1080.0)
    on show:
        alpha 0.0
        linear 0.8 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.8 alpha 0.0

transform _chp_notify_jp:
    xpos (20.0/1920.0)
    yanchor 1.0 ypos (1060.0/1080.0)
    on show:
        alpha 0.0
        linear 0.8 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.8 alpha 0.0

transform _autosave:
    xanchor 1.0 xpos (1896.0/1920.0)
    ypos (20.0/1080.0)
    on show:
        alpha 0.0
        linear 0.8 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.2 alpha 0.0
    
transform _trophy1:
    xpos (560.0/1920.0)
    on show:
        ypos -(110.0/1080.0) alpha 0.0
        easein 0.3 ypos (10.0/1080.0) alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0
transform _trophy2:
    size (100,100)
    xpos (615.0/1920.0)
    on show:
        ypos -(105.0/1080.0) alpha 0.0
        easein 0.3 ypos (15.0/1080.0) alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0
transform _trophy3:
    xpos (725.0/1920.0)
    on show:
        ypos -(88.0/1080.0) alpha 0.0
        easein 0.3 ypos (32.0/1080.0) alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0
transform _trophy4:
    xpos (725.0/1920.0)
    on show:
        ypos -(50.0/1080.0) alpha 0.0
        easein 0.3 ypos (70.0/1080.0) alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

screen disable_keys:
#    modal True
    zorder 255
    if skip_id == 0:
        key "rollback" action NullAction()
        key "game_menu" action NullAction()
        key "hide_windows" action NullAction()
        key "dismiss" action Play("se20", "sys_se/zyosys5.ogg")
        key "skip" action NullAction()
        key "toggle_skip" action NullAction()
        key "fast_skip" action NullAction()
    else:
        key "rollback" action Show('to_skip')
        key "game_menu" action Show('to_skip')
        key "hide_windows" action Show('to_skip')
        key "dismiss" action Show('to_skip')
        key "skip" action Show('to_skip')
        key "toggle_skip" action Show('to_skip')
        key "fast_skip" action Show('to_skip')
        key "K_RETURN" action Jump("skip")
    

screen to_skip:
    zorder 255
    key "rollback" action NullAction()
    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()
    key "dismiss" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip" action NullAction()
    if skip_id == 0:
        pass
    else:
        key "K_RETURN" action Jump("skip")
    
    if renpy.android == True:
        imagebutton auto "skip_%s.png" action Jump("skip") xpos (1758.0/1920.0) ypos (973.0/1080.0) at skip_screen
    else:
        text "Press ENTER to skip" style style.skip_screen at skip_screen
    
    timer 3.0 action Hide('to_skip')
transform skip_screen:
    xpos (32.0/1920.0) ypos (1060.0/1080.0) anchor (0.0,1.0)
    alpha 0.0
    linear 0.3 alpha 1.0
    pause 2.4
    linear 0.3 alpha 0.0

style skip_screen:
    font "times.ttf"
    size 48
    outlines [(1, "#000000", 0, 0)]


screen notify:
    zorder 100

    text message at _notify_transform style "notify"

    # This controls how long it takes between when the screen is
    # first shown, and when it begins hiding.
#    timer 3.25 action Hide('notify')
    timer 4.0 action Hide('notify')

transform _notify_transform:
    # These control the position.
#    xalign .02
    xanchor 0.0 yanchor 0.0
    xpos (26.0/1920.0)

    # These control the actions on show and hide.
#    on show:
#        alpha 0 yalign -0.015
#        linear .3 alpha 1.0 yalign .015
#    on hide:
#        linear .5 alpha 0.0 yalign -0.015
#    on show:
#        yalign (-66.0/1080.0)
#        linear 1.0 yalign .015
#    on hide:
#        linear 1.0 yalign (-66.0/1080.0)
    on show:
        ypos (-56.0/1080.0)
        linear 1.0 ypos (20.0/1080.0)
    on hide:
        linear 1.0 ypos (-56.0/1080.0)
    
init python:
    style.notify = Style(style.default)
    style.notify.font = "default.ttf"
    style.notify.outlines = [(1, "#000000", 0, 0)]
    style.notify.size = 46
    style.notify.color = "#befffd"
    
#    style.notify['r_menu'].font = "DejaVuSans.ttf"
#    style.notify['r_menu'].outlines = [(1, "#000000", 0, 0)]
#    style.notify['r_menu'].size = 56
#    style.notify['r_menu'].color = "#ffffff"
    
    
    def overlay_button():
        if button_show:
            ui.imagebutton("skip_idle.png","skip_hover.png",clicked=ui.jumps("skip"),xpos=(1758.0/1920.0),ypos=(973.0/1080.0))# or ui.jumps
    config.overlay_functions.append(overlay_button)
    
    def se_pause(btn_res = 0):
        if btn_res == 1:
            renpy.music.set_pause(True, channel='voice')
            renpy.music.set_pause(True, channel='vo2')
            renpy.music.set_pause(True, channel='vo3')
            renpy.music.set_pause(True, channel='vo4')
            renpy.music.set_pause(True, channel='vo5')
            renpy.music.set_pause(True, channel='vo6')
            renpy.music.set_pause(True, channel='vo7')
            renpy.music.set_pause(True, channel='me1')
            renpy.music.set_pause(True, channel='me2')
            renpy.music.set_pause(True, channel='me3')
            renpy.music.set_pause(True, channel='me4')
            renpy.music.set_pause(True, channel='me5')
            renpy.music.set_pause(True, channel='se1')
            renpy.music.set_pause(True, channel='se2')
            renpy.music.set_pause(True, channel='se3')
            renpy.music.set_pause(True, channel='se9')
            renpy.music.set_pause(True, channel='sound')
            renpy.music.set_pause(True, channel='maria')
        else:
            renpy.music.set_pause(False, channel='voice')
            renpy.music.set_pause(False, channel='vo2')
            renpy.music.set_pause(False, channel='vo3')
            renpy.music.set_pause(False, channel='vo4')
            renpy.music.set_pause(False, channel='vo5')
            renpy.music.set_pause(False, channel='vo6')
            renpy.music.set_pause(False, channel='vo7')
            renpy.music.set_pause(False, channel='me1')
            renpy.music.set_pause(False, channel='me2')
            renpy.music.set_pause(False, channel='me3')
            renpy.music.set_pause(False, channel='me4')
            renpy.music.set_pause(False, channel='me5')
            renpy.music.set_pause(False, channel='se1')
            renpy.music.set_pause(False, channel='se2')
            renpy.music.set_pause(False, channel='se3')
            renpy.music.set_pause(False, channel='se9')
            renpy.music.set_pause(False, channel='sound')
            renpy.music.set_pause(False, channel='maria')
        
    _se_pause = renpy.curry(se_pause)
    
screen all_pause:
    on "show" action _se_pause(1)
    on "hide" action _se_pause(0)
    
label skip:
    
    $ seplay(9,"sys_se/sskip.ogg")
    
    scene black
    hide screen disable_keys
    with t22
    
    $ fede(0,1.0)
    $ E_A()
    $ config.allow_skipping = True
    
    if skip_id == 10:
        $ skip_id = 0
        jump umi1_17b
    elif skip_id == 5:
        $ skip_id = 0
        with Pause(1.0)
        jump umi1_1
    elif skip_id == 6:
        $ skip_id = 0
        with Pause(1.0)
        jump umi1_10
    elif skip_id == 11:
        $ skip_id = 0
        jump teatime_1b
    elif skip_id == 15:
        $ skip_id = 0
        with Pause(1.0)
        jump umi2_opning2
    elif skip_id == 16:
        $ skip_id = 0
        with Pause(1.0)
        jump umi2_9
    elif skip_id == 20:
        $ skip_id = 0
        jump umi2_17b
    elif skip_id == 21:
        $ skip_id = 0
        jump teatime_2b
    elif skip_id == 26:
        $ skip_id = 0
        with Pause(1.0)
        jump umi3_6
    elif skip_id == 30:
        $ skip_id = 0
        jump umi3_18b
    elif skip_id == 31:
        $ skip_id = 0
        jump ura_teatime_3b
    elif skip_id == 41:
        $ skip_id = 0
        jump teatime_4b
    elif skip_id == 42:
        $ skip_id = 0
        jump ura_teatime_4b
    elif skip_id == 50:
        $ skip_id = 0
        $ renpy.full_restart(label="splash2")
    
    

screen unlock_yesno:
    modal True
    
    fixed:
        xcenter (947.0/1920.0) ycenter (486.0/1080.0) xmaximum 510 ymaximum 312
        add "title/menu/unlock_kaku_bg.png"
        imagebutton auto "title/menu/unlock_yes_%s.png" xpos (47.0/510.0) ypos (113.0/312.0) focus_mask None action [ShowMenu('_unlock'), Stop("music"), Play ("se9", "sys_se/zyosys1.ogg"), With(t22)]
        imagebutton auto "title/menu/unlock_no_%s.png" xpos (47.0/510.0) ypos (198.0/312.0) focus_mask None action [ Hide('unlock_yesno'), Play ("se9", "sys_se/zyosys1.ogg") ]
screen _unlock:
    add "background/efe/black.png"
    timer 1.0 action Start('unlock')

screen config_yesno:
    modal True
    
    fixed:
        xcenter (947.0/1920.0) ycenter (486.0/1080.0) xmaximum 510 ymaximum 312
        add "config/def_kaku_bg.png"
        if renpy.android or not renpy.loadable("movie/no81.mkv"):
            imagebutton auto "title/menu/unlock_yes_%s.png" xpos (47.0/510.0) ypos (113.0/312.0) focus_mask None action [ Hide('config_yesno'), Play ("se9", "sys_se/zyosys1.ogg"), Preference('text speed', 50), Preference('skip', 'all'), SetField(persistent, "bgm_text", True), SetField(persistent, "bgm_lang", 0), Preference('wait for voice', 'enable'), Preference('music volume', 0.6), Preference('sound volume', 0.7), Preference('voice volume', 0.8), Preference('auto-forward time', 3), SetField(persistent, "msgwnd", "efe/msgwnd3.png"), SetField(persistent, "config_msgwnd", 3), SetField(persistent, "chrwnd", "efe/chrwnd3.png"), SetField(persistent, "fmv", False), SetField(persistent, "anime_bgm", False), SetField(persistent, "anime_bgm2", False), SetField(persistent, "tsurupettan", False) ]
        else:
            imagebutton auto "title/menu/unlock_yes_%s.png" xpos (47.0/510.0) ypos (113.0/312.0) focus_mask None action [ Hide('config_yesno'), Play ("se9", "sys_se/zyosys1.ogg"), Preference('text speed', 50), Preference('skip', 'all'), SetField(persistent, "bgm_text", True), SetField(persistent, "bgm_lang", 0), Preference('wait for voice', 'enable'), Preference('music volume', 0.6), Preference('sound volume', 0.7), Preference('voice volume', 0.8), Preference('auto-forward time', 3), SetField(persistent, "msgwnd", "efe/msgwnd3.png"), SetField(persistent, "config_msgwnd", 3), SetField(persistent, "chrwnd", "efe/chrwnd3.png"), SetField(persistent, "fmv", True), SetField(persistent, "anime_bgm", False), SetField(persistent, "anime_bgm2", False), SetField(persistent, "tsurupettan", False) ]
        imagebutton auto "title/menu/unlock_no_%s.png" xpos (47.0/510.0) ypos (198.0/312.0) focus_mask None action [ Hide('config_yesno'), Play ("se9", "sys_se/zyosys1.ogg") ]
    

label unlock:
    $ E_A()
    $ _game_menu_screen = None
    if ep_unlock == 2:
        $ persistent.UMINEKOEND = 20
        $ persistent.UMINEKOEND_flg = 20
    elif ep_unlock == 3:
        $ persistent.UMINEKOEND = 30
        $ persistent.UMINEKOEND_flg = 30
    elif ep_unlock == 4:
        $ persistent.UMINEKOEND = 40
        $ persistent.UMINEKOEND_flg = 40
    elif ep_unlock == 5:
        $ persistent.UMINEKOEND = 50
        $ persistent.UMINEKOEND_flg = 50
        $ persistent.UMINEKOEND_BGM_flg = 1
    if ep_unlock >= 3:
        $ persistent.tsuru_flg = True
    play sound "SE/key_ring2.ogg"
    scene black with t22
    
    with Pause(2.0)
    play sound "se/A6_24636.ogg"
    show text006 with t22
    with Pause(12.0)
    $ renpy.pause(0.001, hard=True)
    scene black with t22
    $ E_A()
#    call splash2
    $ renpy.full_restart(label="splash2")

screen exit:
    tag menu
    
    add "background/efe/black.png"
    timer 6.0 action renpy.quit

init python:
    
    sys_load_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,0,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5))
    sys_load_h = im.Crop("r_click/sysmenu/sysmenu.png", (0,0,416,80))
    
    sys_char_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,80,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5))
    sys_char_h = im.Crop("r_click/sysmenu/sysmenu.png", (0,80,416,80))
    sys_char_NA_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,80,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5) * im.matrix.opacity(0.5))
    sys_char_NA_h = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,80,416,80)), im.matrix.opacity(0.5))
    
    sys_tips_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,160,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5))
    sys_tips_h = im.Crop("r_click/sysmenu/sysmenu.png", (0,160,416,80))
    sys_tips_NA_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,160,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5) * im.matrix.opacity(0.5))
    sys_tips_NA_h = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,160,416,80)), im.matrix.opacity(0.5))
    
    sys_config_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,240,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5))
    sys_config_h = im.Crop("r_click/sysmenu/sysmenu.png", (0,240,416,80))
    
    sys_title_i = im.MatrixColor(im.Crop("r_click/sysmenu/sysmenu.png", (0,320,416,80)), im.matrix.brightness(-0.5) * im.matrix.contrast(0.5))
    sys_title_h = im.Crop("r_click/sysmenu/sysmenu.png", (0,320,416,80))
    
    slider_mm = LiveComposite((400,30), (0,0), im.Crop("config/slider.png", (1,122,64,30)), (320,0), im.Crop("config/slider.png", (112,122,80,30)))
    slider_sf = LiveComposite((401,30), (0,0), im.Crop("config/slider.png", (0,154,102,30)), (311,0), im.Crop("config/slider.png", (102,154,90,30)))
    
    slider_sp_i = im.MatrixColor(im.Crop("config/slider.png", (0,79,36,36)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))
    slider_sp_h = im.MatrixColor(im.Crop("config/slider.png", (0,79,36,36)), im.matrix.opacity(0.7))
    slider_sp_s_i = im.MatrixColor(im.Crop("config/slider.png", (0,79,36,36)), im.matrix.brightness(-0.5))
    slider_sp_s_h = im.Crop("config/slider.png", (0,79,36,36))
    
    type_1_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,304,154,64)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))
    type_1_h = im.MatrixColor(im.Crop("config/menu_001.png", (358,304,154,64)), im.matrix.opacity(0.7))
    type_1_s_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,304,154,64)), im.matrix.brightness(-0.5))
    type_1_s_h = im.Crop("config/menu_001.png", (358,304,154,64))
    
    type_2_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,376,154,64)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))
    type_2_h = im.MatrixColor(im.Crop("config/menu_001.png", (358,376,154,64)), im.matrix.opacity(0.7))
    type_2_s_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,376,154,64)), im.matrix.brightness(-0.5))
    type_2_s_h = im.Crop("config/menu_001.png", (358,376,154,64))
    
    type_3_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,448,154,64)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))
    type_3_h = im.MatrixColor(im.Crop("config/menu_001.png", (358,448,154,64)), im.matrix.opacity(0.7))
    type_3_s_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,448,154,64)), im.matrix.brightness(-0.5))
    type_3_s_h = im.Crop("config/menu_001.png", (358,448,154,64))
    
    type_4_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,520,154,64)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))
    type_4_h = im.MatrixColor(im.Crop("config/menu_001.png", (358,520,154,64)), im.matrix.opacity(0.7))
    type_4_s_i = im.MatrixColor(im.Crop("config/menu_001.png", (358,520,154,64)), im.matrix.brightness(-0.5))
    type_4_s_h = im.Crop("config/menu_001.png", (358,520,154,64))
    
    category_1 = ConditionSwitch("_preferences.language == None", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,0), im.Crop("config/category.png", (0,0,400,62)), (453,0), im.Crop("config/category.png", (423,0,16,64)), (469,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1122,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))), "_preferences.language == 'japanese'", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,0), im.Crop("config/category.png", (0,0,176,56)), (237,0), im.Crop("config/category.png", (423,0,16,64)), (253,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1338,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))))
    category_2 = ConditionSwitch("_preferences.language == None", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,6), im.Crop("config/category.png", (0,62,400,56)), (453,0), im.Crop("config/category.png", (423,0,16,64)), (469,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1122,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))), "_preferences.language == 'japanese'", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,0), im.Crop("config/category.png", (0,56,176,56)), (237,0), im.Crop("config/category.png", (423,0,16,64)), (253,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1338,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))))
    category_3 = ConditionSwitch("_preferences.language == None", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,6), im.Crop("config/category.png", (0,118,368,56)), (426,0), im.Crop("config/category.png", (423,0,16,64)), (442,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1149,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))), "_preferences.language == 'japanese'", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,0), im.Crop("config/category.png", (0,112,224,56)), (277,0), im.Crop("config/category.png", (423,0,16,64)), (293,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1298,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))))
#    category_4 = ConditionSwitch("_preferences.language == None", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,6), im.Crop("config/category.png", (0,174,416,56)), (480,0), im.Crop("config/category.png", (423,0,16,64)), (496,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1095,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))), "_preferences.language == 'japanese'", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,0), im.Crop("config/category.png", (0,168,256,56)), (318,0), im.Crop("config/category.png", (423,0,16,64)), (334,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1257,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))))
#    category_5 = ConditionSwitch("_preferences.language == None", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,6), im.Crop("config/category.png", (0,230,424,50)), (488,6), im.Crop("config/category.png", (181,174,240,56)), (723,0), im.Crop("config/category.png", (423,0,16,64)), (739,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (852,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))), "_preferences.language == 'japanese'", LiveComposite((1610,64), (0,0), im.Crop("config/category.png", (423,0,67,64)), (64,0), im.Crop("config/category.png", (0,224,416,56)), (480,0), im.Crop("config/category.png", (423,0,16,64)), (496,0), im.Tile(im.Crop("config/category.png", (439,0,16,64)), (1095,64)), (1591,0), im.Crop("config/category.png", (474,0,16,64))))
    
    menu_000_01 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,0,480,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,0,346,72)))
    menu_000_02 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,72,440,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,72,294,72)))
    menu_000_03 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,144,840,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,144,312,72)))
    menu_000_04 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,216,560,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,216,260,72)))
    menu_000_05 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,288,480,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,288,450,80)))
    menu_000_06 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,368,880,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,368,500,80)))
    menu_000_07 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,448,760,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,448,452,80)))
    menu_000_08 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,528,680,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,528,500,80)))
    menu_000_09 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,608,680,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,608,500,80)))
    menu_000_10 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,688,600,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,688,312,80)))
    menu_000_11 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,768,720,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,768,580,80)))
    menu_000_12 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,848,512,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,848,330,80)))
    menu_000_13 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,928,400,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,928,350,80)))
    menu_000_14 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,1008,840,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,1008,484,80)))
    menu_000_14b = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_000.png", (0,1008,840,80)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_000.png", (0,1008,484,80)), im.matrix.brightness(-0.5)))
    menu_000_15 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,1088,560,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,1088,340,80)))
    menu_000_locked = im.Crop("config/menu_000.png", (640,0,240,72))
    menu_000_16 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,1168,512,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,1168,272,80)))
    menu_000_17 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_000.png", (0,1248,480,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_000.png", (0,1248,400,80)))
    
    menu_001_01_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (284,0,128,80)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,0,116,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_01_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (284,0,128,80)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,0,116,72)), im.matrix.opacity(0.7)))
    menu_001_01_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (284,0,128,80)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,0,116,72)), im.matrix.brightness(-0.5)))
    menu_001_01_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (284,0,128,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (396,0,116,72)))
    
    menu_001_02_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (284,80,92,80)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,72,116,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_02_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (284,80,92,80)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,72,116,72)), im.matrix.opacity(0.7)))
    menu_001_02_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (284,80,92,80)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,72,116,72)), im.matrix.brightness(-0.5)))
    menu_001_02_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (284,80,92,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (396,72,116,72)))
    
    menu_001_03_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (420,0,92,80)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,0,116,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_03_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (420,0,92,80)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,0,116,72)), im.matrix.opacity(0.7)))
    menu_001_03_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (420,0,92,80)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,0,116,72)), im.matrix.brightness(-0.5)))
    menu_001_03_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (420,0,92,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (396,0,116,72)))
    
    menu_001_04_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (384,80,128,80)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,72,116,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_04_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (384,80,128,80)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,72,116,72)), im.matrix.opacity(0.7)))
    menu_001_04_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (384,80,128,80)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (396,72,116,72)), im.matrix.brightness(-0.5)))
    menu_001_04_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (384,80,128,80)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (396,72,116,72)))
    
    menu_001_05 = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (182,232,330,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (220,232,292,72)))
    
    menu_001_05_1_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (90,272,92,40)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (1,279,220,44)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_05_1_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (90,272,92,40)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (1,279,220,44)), im.matrix.opacity(0.7)))
    menu_001_05_1_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (90,272,92,40)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (1,279,220,44)), im.matrix.brightness(-0.5)))
    menu_001_05_1_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (90,272,92,40)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (1,279,220,44)))
    menu_001_05_2_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (28,232,154,40)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (133,232,75,44)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_05_2_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (28,232,154,40)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (133,232,75,44)), im.matrix.opacity(0.7)))
    menu_001_05_2_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (28,232,154,40)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (133,232,75,44)), im.matrix.brightness(-0.5)))
    menu_001_05_2_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (28,232,154,40)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (133,232,75,44)))
    
    menu_001_06_i = im.MatrixColor(im.Crop("config/menu_001.png", (112,160,400,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7))
    menu_001_06_h = im.MatrixColor(im.Crop("config/menu_001.png", (112,160,400,72)), im.matrix.opacity(0.7))
    menu_001_06_s_i = im.MatrixColor(im.Crop("config/menu_001.png", (112,160,400,72)), im.matrix.brightness(-0.5))
    menu_001_06_s_h = im.Crop("config/menu_001.png", (112,160,400,72))
    
    menu_001_07_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (92,648,92,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (127,648,74,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_07_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (92,648,92,72)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (127,648,74,72)), im.matrix.opacity(0.7)))
    menu_001_07_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (92,648,92,72)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (127,648,74,72)), im.matrix.brightness(-0.5)))
    menu_001_07_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (92,648,92,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (127,648,74,72)))
    
    menu_001_08_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (0,648,92,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (0,648,127,72)), im.matrix.brightness(-0.5) * im.matrix.opacity(0.7)))
    menu_001_08_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (0,648,92,72)), im.matrix.opacity(0.7)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (0,648,127,72)), im.matrix.opacity(0.7)))
    menu_001_08_s_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("config/menu_001.png", (0,648,92,72)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("config/menu_001.png", (0,648,127,72)), im.matrix.brightness(-0.5)))
    menu_001_08_s_h = ConditionSwitch("_preferences.language == None", im.Crop("config/menu_001.png", (0,648,92,72)), "_preferences.language == 'japanese'", im.Crop("config/menu_001.png", (0,648,127,72)))
    
    saveload_save_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,0,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (184,0,144,60)))
    saveload_save_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,0,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (184,0,144,60)))
    
    saveload_load_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,60,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (184,60,144,60)))
    saveload_load_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,60,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (184,60,144,60)))
    
    saveload_exit_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,120,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (184,120,144,60)))
    saveload_exit_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,120,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (184,120,144,60)))
    
    saveload_save2_i = LiveComposite((140,60), (0,0), Solid("#371b1b"), (0,0), im.Crop("saveload/menu.png", (184,0,140,60)))
    saveload_save2_h = LiveComposite((140,60), (0,0), Solid("#ff2929"), (0,0), im.Crop("saveload/menu.png", (184,0,140,60)))
    saveload_save2_l = LiveComposite((140,60), (0,0), Solid("#252525"), (0,0), im.MatrixColor(im.Crop("saveload/menu.png", (184,0,140,60)), im.matrix.brightness(-0.5)))
    
    saveload_load2_i = LiveComposite((150,60), (0,0), Solid("#371b1b"), (0,0), im.Crop("saveload/menu.png", (184,60,150,60)))
    saveload_load2_h = LiveComposite((150,60), (0,0), Solid("#ff2929"), (0,0), im.Crop("saveload/menu.png", (184,60,150,60)))
    saveload_load2_l = LiveComposite((150,60), (0,0), Solid("#252525"), (0,0), im.MatrixColor(im.Crop("saveload/menu.png", (184,60,150,60)), im.matrix.brightness(-0.5)))
    
    saveload_delete_i = LiveComposite((174,60), (0,0), Solid("#371b1b"), (0,0), im.Crop("saveload/menu.png", (184,180,174,60)))
    saveload_delete_h = LiveComposite((174,60), (0,0), Solid("#ff2929"), (0,0), im.Crop("saveload/menu.png", (184,180,174,60)))
    saveload_delete_l = LiveComposite((174,60), (0,0), Solid("#252525"), (0,0), im.MatrixColor(im.Crop("saveload/menu.png", (184,180,174,60)), im.matrix.brightness(-0.5)))
    
    saveload_page1_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,0,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (0,0,176,60)))
    saveload_page1_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,0,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (0,0,176,60)))
    
    saveload_page2_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,60,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (0,60,176,60)))
    saveload_page2_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,60,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (0,60,176,60)))
    
    saveload_page3_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,120,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (0,120,176,60)))
    saveload_page3_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,120,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (0,120,176,60)))
    
    saveload_page4_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,180,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (0,180,176,60)))
    saveload_page4_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,180,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (0,180,176,60)))
    
    saveload_page5_i = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,240,420,60)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("saveload/menu.png", (0,240,176,60)))
    saveload_page5_h = LiveComposite((420,60), (0,0), im.MatrixColor(im.Crop("saveload/plate.png", (0,240,420,60)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("saveload/menu.png", (0,240,176,60)))
    
    saveload_box_UD = LiveComposite((1600,5), (0,0), Solid("#fff"))
    saveload_box_LR = LiveComposite((5,190), (0,0), Solid("#fff"))
    saveload_box_selected = LiveComposite((1600,190), (0,0), Solid("#ffffff7f"), (0,0), saveload_box_UD, (0,185), saveload_box_UD, (0,0), saveload_box_LR, (1595,0), saveload_box_LR)
    saveload_box = LiveComposite((1600,190), (0,0), Solid("#ffffff3f"), (0,0), saveload_box_UD, (0,185), saveload_box_UD, (0,0), saveload_box_LR, (1595,0), saveload_box_LR)
    