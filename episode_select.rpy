#style chp_choice:
#        size 60
#        drop_shadow (2, 2)
#        font "default.ttf"
#        color "#808080"
#        hover_color "#ffffff"
#        insensitive_color (255, 255, 255, 255)

screen title_background:
    if persistent.UMINEKOEND < 20:
        add "title/bg1.png"
    elif persistent.UMINEKOEND == 20 or persistent.UMINEKOEND == 21 or persistent.UMINEKOEND == 22:
        add "title/bg2.png"
    elif persistent.UMINEKOEND == 30 or persistent.UMINEKOEND == 31 or persistent.UMINEKOEND == 32:
        add "title/bg3.png"
    elif persistent.UMINEKOEND == 40 or persistent.UMINEKOEND == 41 or persistent.UMINEKOEND == 42:
        add "title/bg4.png"
    elif persistent.UMINEKOEND >= 50:
        add "title/bg5.png"

screen main_menu(predict=False):             ## take out () if not faster?
    tag menu
    
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    
    use title_background
    
    add "title/logo.png" at logo
    $ y=420.0
#    $ y=415.0
    $ y+=2.0
    $ y_new3 = y
    imagebutton idle start_i hover start_h focus_mask None action [ Play ("se20", "SE/bell1.ogg"), ShowMenu('episodes') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_start.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
    
    if persistent.UMINEKOEND >= 11:   #Tea 1 unlocked (Start, Tea Party, Continue2, Bookmark2, Config3, Picture Box1, Music Box1, Exit3)
        $ y+=60.0
        $ y_new4 = y
        imagebutton idle tea_i hover tea_h focus_mask None action [ Play ("se20", "SE/bell1.ogg"), ShowMenu('tea_episodes') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_tea.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
    if persistent.UMINEKOEND >= 12:   #Ura 1 unlocked (Start, Tea Party, ????, Continue3, Bookmark3, Config4, Picture Box2, Music Box2, Exit4)
        $ y+=60.0
        $ y_new5 = y
        imagebutton idle ura_i hover ura_h focus_mask None action [ Play ("se20", "SE/bell1.ogg"), ShowMenu('ura_episodes') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ura.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
    
#    if persistent.UMINEKOEND < 5:
#        $ y+=60.0
#        imagebutton idle config1_i hover config1_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("config_pg", 1), ShowMenu('preferences'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_config.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
#        $ y+=60.0
#        imagebutton idle exit1_i hover exit1_h focus_mask None action [ ShowMenu('exit'), Play ("se9", se18), Hide("gui_tooltip"), With(tquit) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_exit.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
    if persistent.UMINEKOEND < 11:
        $ y+=60.0
        if renpy.can_load("auto-1", test=False):
            imagebutton idle continue1_i hover continue1_h focus_mask None action [ FileLoad(1, page="auto", confirm=True, newest=True), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        else:
            imagebutton idle continue1_i hover continue1_h focus_mask None action Play ("se20", "sys_se/zyosys5.ogg") hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle load1_i hover load1_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('saveload'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_load.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle config2_i hover config2_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("config_pg", 1), ShowMenu('preferences'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_config.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle exit2_i hover exit2_h focus_mask None action [ ShowMenu('exit'), Play ("se9", se18), Hide("gui_tooltip"), With(tquit) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_exit.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
    elif persistent.UMINEKOEND == 11:
        $ y+=60.0
        if renpy.can_load("auto-1", test=False):
            imagebutton idle continue2_i hover continue2_h focus_mask None action [ FileLoad(1, page="auto", confirm=True, newest=True), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        else:
            imagebutton idle continue2_i hover continue2_h focus_mask None action Play ("se20", "sys_se/zyosys5.ogg") hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle load2_i hover load2_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('saveload'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_load.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle config3_i hover config3_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("config_pg", 1), ShowMenu('preferences'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_config.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new = y
        imagebutton idle picture1_i hover picture1_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('cg'), SetField(persistent, "UMINEKOEND_CG_flg", 0), Hide("gui_tooltip"), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_cg.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new2 = y
        imagebutton idle music1_i hover music1_h focus_mask None action [ ShowMenu('music_box'), Play ("se9", se17), Stop ("music"), Hide("gui_tooltip"), With(t18) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_bgm.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle exit3_i hover exit3_h focus_mask None action [ ShowMenu('exit'), Play ("se9", se18), Hide("gui_tooltip"), With(tquit) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_exit.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        
    elif persistent.UMINEKOEND == 12:
        $ y+=60.0
        if renpy.can_load("auto-1", test=False):
            imagebutton idle continue3_i hover continue3_h focus_mask None action [ FileLoad(1, page="auto", confirm=True, newest=True), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        else:
            imagebutton idle continue3_i hover continue3_h focus_mask None action Play ("se20", "sys_se/zyosys5.ogg") hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle load3_i hover load3_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), ShowMenu('saveload') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_load.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle config4_i hover config4_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("config_pg", 1), ShowMenu('preferences'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_config.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new = y
        imagebutton idle picture2_i hover picture2_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('cg'), SetField(persistent, "UMINEKOEND_CG_flg", 0), Hide("gui_tooltip"), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_cg.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new2 = y
        imagebutton idle music2_i hover music2_h focus_mask None action [ ShowMenu('music_box'), Play ("se9", se17), Stop ("music"), Hide("gui_tooltip"), With(t18) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_bgm.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle exit4_i hover exit4_h focus_mask None action [ ShowMenu('exit'), Play ("se9", se18), Hide("gui_tooltip"), With(tquit) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_exit.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        
    elif persistent.UMINEKOEND >= 20:
        $ y+=60.0
        if renpy.can_load("auto-1", test=False):
            imagebutton idle continue3_i hover continue3_h focus_mask None action [ FileLoad(1, page="auto", confirm=True, newest=True), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        else:
            imagebutton idle continue3_i hover continue3_h focus_mask None action Play ("se20", "sys_se/zyosys5.ogg") hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_continue.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle load3_i hover load3_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), ShowMenu('saveload') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_load.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new6 = y
        imagebutton idle chars_i hover chars_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('chars_episodes') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_chars.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new7 = y
        imagebutton idle tips_i hover tips_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('tips_episodes') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_tips.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle config5_i hover config5_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("config_pg", 1), ShowMenu('preferences'), Hide("gui_tooltip") ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_config.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new = y
        imagebutton idle picture3_i hover picture3_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), ShowMenu('cg'), SetField(persistent, "UMINEKOEND_CG_flg", 0), Hide("gui_tooltip"), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_cg.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        $ y_new2 = y
        imagebutton idle music3_i hover music3_h focus_mask None action [ ShowMenu('music_box'), Play ("se9", se17), Stop ("music"), Hide("gui_tooltip"), With(t18) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_bgm.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
        $ y+=60.0
        imagebutton idle exit5_i hover exit5_h focus_mask None action [ ShowMenu('exit'), Play ("se9", se18), Hide("gui_tooltip"), With(tquit) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_exit.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")] at ep_start(x,y)
    
    if persistent.UMINEKOEND_CG_flg == 1:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new)
    if persistent.UMINEKOEND_BGM_flg == 1:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new2)
    if persistent.UMINEKOEND_flg == 20 or persistent.UMINEKOEND_flg == 30 or persistent.UMINEKOEND_flg == 40:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new3)
    elif persistent.UMINEKOEND_flg == 11 or persistent.UMINEKOEND_flg == 21 or persistent.UMINEKOEND_flg == 31 or persistent.UMINEKOEND_flg == 41:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new4)
    elif persistent.UMINEKOEND_flg == 12 or persistent.UMINEKOEND_flg == 22 or persistent.UMINEKOEND_flg == 32 or persistent.UMINEKOEND_flg == 42:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new5)
    if persistent.UMINEKOEND_CHARS1_flg == 1 or persistent.UMINEKOEND_CHARS2_flg == 1 or persistent.UMINEKOEND_CHARS3_flg == 1 or persistent.UMINEKOEND_CHARS4_flg == 1:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new6)
    if persistent.UMINEKOEND_TIPS1_flg == 1 or persistent.UMINEKOEND_TIPS2_flg == 1 or persistent.UMINEKOEND_TIPS3_flg == 1 or persistent.UMINEKOEND_TIPS4_flg == 1:
        add im.Crop("title/new.png", (0,0,104,40)) at new_title(x, y_new7)
        
    imagebutton auto "title/trophy_%s.png" xpos (64.0/1920.0) ypos (64.0/1080.0) focus_mask None action [ ShowMenu('achievements'), Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), With(t23) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ach.png", my_tt_xpos=(44.0/853.0), my_tt_ypos=(176.0/480.0)) ] unhovered [Hide("gui_tooltip")]
    
    timer 60.0 action [ShowMenu("demo"), Hide("gui_tooltip"), _E_B2(0,0.5), With(t22)]
    
screen episodes:
    tag menu
    
    key "game_menu" action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ]
    
    $ y=420.0
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    $ y+=2.0
    use title_background
    add "title/logo.png" at logo
    add start_h at ep_start(x,y)
    
    if persistent.UMINEKOEND_flg == 20 or persistent.UMINEKOEND_flg == 30 or persistent.UMINEKOEND_flg == 40:
        add im.Crop("title/new.png", (0,0,104,40)) at ep_start(x+20.0,y+8.0)
    
    $ y+=60.0
    $ x+=240.0
    if persistent.UMINEKOEND < 11:
        imagebutton idle episode1_i hover episode1_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 1), ShowMenu('scenario_jump_q_start'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep1.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
    else:
        imagebutton idle episode1_i hover episode1_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 1), ShowMenu('scenario_jump_q'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep1.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
    $ y+=48.0
    if persistent.UMINEKOEND >= 20:
        if persistent.UMINEKOEND < 21:
            imagebutton idle episode2_i hover episode2_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 2), ShowMenu('scenario_jump_q_start'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep2.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        else:
            imagebutton idle episode2_i hover episode2_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 2), ShowMenu('scenario_jump_q'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep2.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        if persistent.UMINEKOEND_flg == 20:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0)
    else:
        imagebutton idle unlock_i hover unlock_h xpos ((x-10.0)/1920.0) ypos (y/1080.0) xanchor 1.0 focus_mask None action [ Play ("se9", se1001), SetVariable("ep_unlock", 2),ShowMenu('unlock_yesno') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_unlock.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        imagebutton idle episode2_l hover episode2_l xpos (x/1920.0) ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/zyosys5.ogg"), NullAction() ] hovered Show("gui_tooltip", my_picture="title/txt_box/text_warning.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) unhovered [Hide("gui_tooltip")]
    $ y+=48.0
    if persistent.UMINEKOEND >= 30:
        if persistent.UMINEKOEND < 31:
            imagebutton idle episode3_i hover episode3_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 3), ShowMenu('scenario_jump_q_start'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep3.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        else:
            imagebutton idle episode3_i hover episode3_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 3), ShowMenu('scenario_jump_q'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep3.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        if persistent.UMINEKOEND_flg == 30:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0)
    else:
        imagebutton idle unlock_i hover unlock_h xpos ((x-10.0)/1920.0) ypos (y/1080.0) xanchor 1.0 focus_mask None action [ Play ("se9", se1001), SetVariable("ep_unlock", 3),ShowMenu('unlock_yesno') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_unlock.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        imagebutton idle episode3_l hover episode3_l xpos (x/1920.0) ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/zyosys5.ogg"), NullAction() ] hovered Show("gui_tooltip", my_picture="title/txt_box/text_warning.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) unhovered [Hide("gui_tooltip")]
    $ y+=48.0
    if persistent.UMINEKOEND >= 40:
        if persistent.UMINEKOEND < 41:
            imagebutton idle episode4_i hover episode4_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 4), ShowMenu('scenario_jump_q_start'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep4.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        else:
            imagebutton idle episode4_i hover episode4_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 4), ShowMenu('scenario_jump_q'), Hide("gui_tooltip"), With(t10) ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_ep4.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        if persistent.UMINEKOEND_flg == 40:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0)
    else:
        imagebutton idle unlock_i hover unlock_h xpos ((x-10.0)/1920.0) ypos (y/1080.0) xanchor 1.0 focus_mask None action [ Play ("se9", se1001), SetVariable("ep_unlock", 4),ShowMenu('unlock_yesno') ] hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_unlock.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) ] unhovered [Hide("gui_tooltip")]
        imagebutton idle episode4_l hover episode4_l xpos (x/1920.0) ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/zyosys5.ogg"), NullAction() ] hovered Show("gui_tooltip", my_picture="title/txt_box/text_warning.png", my_tt_xpos=(100.0/1920.0), my_tt_ypos=(460.0/1080.0)) unhovered [Hide("gui_tooltip")]
    if persistent.UMINEKOEND >= 50:
        $ y+=48.0
        imagebutton idle trailer_i hover trailer_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action Start('umi_chiru') hovered [ Play ("se10", se1002), Show("gui_tooltip", my_picture="title/txt_box/text_trailer.png", my_tt_xpos=(44.0/853.0), my_tt_ypos=(176.0/480.0)) ] unhovered [Hide("gui_tooltip")]
    if persistent.UMINEKOEND < 50:
        $ y+=48.0
        imagebutton idle unlock_all_i hover unlock_all_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", se1001), SetVariable("ep_unlock", 5),ShowMenu('unlock_yesno') ] hovered [ Play ("se10", se1002) ] unhovered [Hide("gui_tooltip")]
    if renpy.android == True:
        $ y+=48.0
        imagebutton idle ep_back_i hover ep_back_h xpos (x/1920.0)ypos (y/1080.0) focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ] hovered Play ("se10", se1002) unhovered [Hide("gui_tooltip")]
    
screen tea_episodes:
    tag menu
    
    key "game_menu" action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ]
    
    use title_background
    $ y=420.0
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    $ y+=2.0
    add "title/logo.png" at logo
    add tea_h at ep_move(x,y+60.0,y)
    
    if persistent.UMINEKOEND_flg == 11 or persistent.UMINEKOEND_flg == 21 or persistent.UMINEKOEND_flg == 31 or persistent.UMINEKOEND_flg == 41:
        add im.Crop("title/new.png", (0,0,104,40)) at ep_move(x+20.0,y+68.0,y+8.0)
    
    $ y+=60.0
    $ x+=240.0
    imagebutton idle episode1_i hover episode1_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 1),ShowMenu('tea_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    if persistent.UMINEKOEND_flg == 11:
        add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if persistent.UMINEKOEND >= 21:
        $ y+=48.0
        imagebutton idle episode2_i hover episode2_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 2),ShowMenu('tea_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_flg == 21:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if persistent.UMINEKOEND >= 31:
        $ y+=48.0
        imagebutton idle episode3_i hover episode3_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 3),ShowMenu('tea_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_flg == 31:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if persistent.UMINEKOEND >= 41:
        $ y+=48.0
        imagebutton idle episode4_i hover episode4_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 4),ShowMenu('tea_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_flg == 41:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if renpy.android == True:
        $ y+=48.0
        imagebutton idle ep_back_i hover ep_back_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    
screen ura_episodes:
    tag menu
    
    key "game_menu" action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ]
    
    use title_background
    $ y=420.0
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    $ y+=2.0
    add "title/logo.png" at logo
    add ura_h at ep_move(x,y+120.0,y)
    
    if persistent.UMINEKOEND_flg == 12 or persistent.UMINEKOEND_flg == 22 or persistent.UMINEKOEND_flg == 32 or persistent.UMINEKOEND_flg == 42:
        add im.Crop("title/new.png", (0,0,104,40)) at ep_move(x+20.0,y+128.0,y+8.0)
    
    $ y+=60.0
    $ x+=240.0
    imagebutton idle episode1_i hover episode1_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 1),ShowMenu('ura_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    if persistent.UMINEKOEND_flg == 12:
        add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
        
    if persistent.UMINEKOEND >= 22:
        $ y+=48.0
        imagebutton idle episode2_i hover episode2_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 2),ShowMenu('ura_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_flg == 22:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
            
    if persistent.UMINEKOEND >= 32:
        $ y+=48.0
        imagebutton idle episode3_i hover episode3_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 3),ShowMenu('ura_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_flg == 32:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
            
    if persistent.UMINEKOEND >= 42:
        $ y+=48.0
        imagebutton idle episode4_i hover episode4_h focus_mask None action [ Play ("se9", se17), Stop ("music"), SetVariable("scenario_Number", 4),ShowMenu('ura_start'), Hide("gui_tooltip"), With(t10) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_flg == 42:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
            
    if renpy.android == True:
        $ y+=48.0
        imagebutton idle ep_back_i hover ep_back_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    
screen chars_episodes:
    tag menu
    
    key "game_menu" action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ]
    
    use title_background
    $ y=420.0
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    $ y+=2.0
    add "title/logo.png" at logo
    add chars_h at ep_move(x,y+300.0,y)
    
    if persistent.UMINEKOEND_CHARS1_flg == 1 or persistent.UMINEKOEND_CHARS2_flg == 1 or persistent.UMINEKOEND_CHARS3_flg == 1 or persistent.UMINEKOEND_CHARS4_flg == 1:
        add im.Crop("title/new.png", (0,0,104,40)) at ep_move(x+20.0,y+308.0,y+8.0)
    
    $ y+=60.0
    $ x+=240.0
    imagebutton idle episode1_i hover episode1_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 1), Start('rmenu_chars'), Hide("gui_tooltip") ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    if persistent.UMINEKOEND_CHARS1_flg == 1:
        add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if persistent.UMINEKOEND >= 30:
        $ y+=48.0
        imagebutton idle episode2_i hover episode2_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 2), Start('rmenu_chars'), Hide("gui_tooltip") ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_CHARS2_flg == 1:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    if persistent.UMINEKOEND >= 40:
        $ y+=48.0
        imagebutton idle episode3_i hover episode3_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 3), Start('rmenu_chars'), Hide("gui_tooltip") ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_CHARS3_flg == 1:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    if persistent.UMINEKOEND >= 50:
        $ y+=48.0
        imagebutton idle episode4_i hover episode4_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 4), Start('rmenu_chars'), Hide("gui_tooltip") ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_CHARS4_flg == 1:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if renpy.android == True:
        $ y+=48.0
        imagebutton idle ep_back_i hover ep_back_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Return() ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    
    
screen tips_episodes:
    tag menu
    
    key "game_menu" action [ Play ("se9", "sys_se/zyosys1.ogg"), Hide("gui_tooltip"), Return() ]
    
    use title_background
    $ y=420.0
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    $ y+=2.0
    add "title/logo.png" at logo
    add tips_h at ep_move(x,y+360.0,y)
    
    if persistent.UMINEKOEND_TIPS1_flg == 1 or persistent.UMINEKOEND_TIPS2_flg == 1 or persistent.UMINEKOEND_TIPS3_flg == 1 or persistent.UMINEKOEND_TIPS4_flg == 1:
        add im.Crop("title/new.png", (0,0,104,40)) at ep_move(x+20.0,y+368.0,y+8.0)
    
    $ y+=60.0
    $ x+=240.0
    imagebutton idle episode1_i hover episode1_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 1), Start('rmenu_tips'), Hide("gui_tooltip"), With(t23) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
    if persistent.UMINEKOEND_TIPS1_flg == 1:
        add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    
    if persistent.UMINEKOEND >= 30:
        $ y+=48.0
        imagebutton idle episode2_i hover episode2_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 2), Start('rmenu_tips'), Hide("gui_tooltip"), With(t23) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_TIPS2_flg == 1:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    if persistent.UMINEKOEND >= 40:
        $ y+=48.0
        imagebutton idle episode3_i hover episode3_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 3), Start('rmenu_tips'), Hide("gui_tooltip"), With(t23) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_TIPS3_flg == 1:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    if persistent.UMINEKOEND >= 50:
        $ y+=48.0
        imagebutton idle episode4_i hover episode4_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), SetVariable("scenario_Number", 4), Start('rmenu_tips'), Hide("gui_tooltip"), With(t23) ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)
        if persistent.UMINEKOEND_TIPS4_flg == 1:
            add im.Crop("title/new.png", (0,40,88,32)) at new_ep(x+10.0,y+6.0,0.3)
    if renpy.android == True:
        $ y+=48.0
        imagebutton idle ep_back_i hover ep_back_h focus_mask None action [ Play ("se9", "sys_se/zyosys1.ogg"), Return() ] hovered Play ("se10", se1002) at ep_button(x,(y/1080.0),0.3)

screen tea_start:
    tag menu
    
    if scenario_Number == 1:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 1), Start('teatime_1') ]
    elif scenario_Number == 2:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 2), Start('teatime_2') ]
    elif scenario_Number == 3:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 3), Start('teatime_3') ]
    elif scenario_Number == 4:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 4), Start('teatime_4') ]
    
screen ura_start:
    tag menu
    
    if scenario_Number == 1:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 1), Start('ura_teatime') ]
    elif scenario_Number == 2:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 2), Start('ura_teatime_2') ]
    elif scenario_Number == 3:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 3), Start('ura_teatime_3') ]
    elif scenario_Number == 4:
        add "background/efe/white.png"
        timer 5.0 action [ SetVariable("scenario_Number", 4), Start('ura_teatime_4') ]
    

#    $ _game_menu_screen = None
#    play se20 "se/A5_07201.ogg"
#    scene white with t10
#    $ E_A()
#    with Pause(2.0)
#    $ renpy.show_screen('scenario_jump_q_screen')
#    $ ui.interact()
#    jump _noisy_return
    
screen scenario_jump_q_start:
    tag menu
    
    add "background/efe/white.png"
    if scenario_Number == 1:
        timer 5.0 action [ Start('umi1_opning') ]
    elif scenario_Number == 2:
        timer 5.0 action [ Start('umi2_opning') ]
    elif scenario_Number == 3:
        timer 5.0 action [ Start('umi3_opning') ]
    elif scenario_Number == 4:
        timer 5.0 action [ Start('umi4_opning') ]

style chp_choice:
        size 59
        drop_shadow (2, 2)
        drop_shadow_color "#000"
        color "#808080"
        hover_color "#ffffff"
        insensitive_color (255, 255, 255, 255)
#        outlines [(2, "#000000", 2, 2)]
        selected_color "#ffffff"
        selected_hover_color "#ff1d1d"
        font "default.ttf"
        xalign 0.0
        text_align 0.0

screen scenario_jump_q:
    tag menu
    add "background/efe/chess1.png" xalign 0.5 yalign 0.5 #at chp_fadein
    add "background/efe/black.png" alpha (100.0/255.0)
    add "background/efe/hana1_.png" #at chp_fadein
    text "You may perform witchcraft\nto jump forward in time." size 59 font "default.ttf" drop_shadow (2, 2) at choice_caption
    textbutton "Cast the spell" text_style style.chp_choice xpos (598.0/1920.0) ypos (544.0/1080.0) focus_mask None action [ Hide('scenario_jump_q_screen'), Show('scenario_jump_name'), With(t22) ] hovered Play ("se10", se1002) #at choice_yes
    if scenario_Number == 1:
        textbutton "Don't cast the spell" text_style style.chp_choice xpos (598.0/1920.0) ypos (615.0/1080.0) focus_mask None action [ Hide('scenario_jump_q_screen'), Start('umi1_opning'), With(t22) ] hovered Play ("se10", se1002) #at choice_no
    elif scenario_Number == 2:
        textbutton "Don't cast the spell" text_style style.chp_choice xpos (598.0/1920.0) ypos (615.0/1080.0) focus_mask None action [ Hide('scenario_jump_q_screen'), Start('umi2_opning'), With(t22) ] hovered Play ("se10", se1002) #at choice_no
    elif scenario_Number == 3:
        textbutton "Don't cast the spell" text_style style.chp_choice xpos (598.0/1920.0) ypos (615.0/1080.0) focus_mask None action [ Hide('scenario_jump_q_screen'), Start('umi3_opning'), With(t22) ] hovered Play ("se10", se1002) #at choice_no
    elif scenario_Number == 4:
        textbutton "Don't cast the spell" text_style style.chp_choice xpos (598.0/1920.0) ypos (615.0/1080.0) focus_mask None action [ Hide('scenario_jump_q_screen'), Start('umi4_opning'), With(t22) ] hovered Play ("se10", se1002) #at choice_no
    add "background/efe/white.png" at chp_fadeout
    

style chp_sel:
        size 45
        drop_shadow (2, 2)
        drop_shadow_color "#000"
        color "#c7c7c7"
        hover_color "#ffffff"
        insensitive_color (199, 199, 199, 255)
#        outlines [(2, "#000000", 2, 2)]
        font "default.ttf"
        xalign 0.0
        text_align 0.0

screen scenario_jump_name:
    tag menu
    
    $ x = (240.0/1920.0)
    
    add "background/efe/chess1.png" xalign 0.5 yalign 0.5
    add "background/efe/black.png" alpha (200.0/255.0)
    add "background/efe/hana1_.png" alpha 0.7    # alpha not present in original
    if scenario_Number == 1:
        vbox:
            xcenter (985.0/1920.0) yanchor 0.0 ypos (28.0/1080.0)
            text "Please select your destination." size 45 font "default.ttf" drop_shadow (2, 2)
            null height 35              ## 45 ???
            textbutton "Arrival at Niijima Airport       Sat, Oct 4 1986  8:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Arrival at Rokkenjima            Sat, Oct 4 1986 10:30AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Guesthouse                       Sat, Oct 4 1986 12:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Dining Room                      Sat, Oct 4 1986  1:30PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Epitaph on the Portrait          Sat, Oct 4 1986  1:30PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Sandy Beach                      Sat, Oct 4 1986  3:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Letter and Umbrella              Sat, Oct 4 1986  6:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Legend of the Gold               Sat, Oct 4 1986 10:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Night of the Storm               Sat, Oct 4 1986 -------" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Six Chosen by the Key        Sun, Oct 5 1986  6:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Curtain-rise on Tragedy          Sun, Oct 5 1986  8:45AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Occult                           Sun, Oct 5 1986  1:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Two Who Are Close            Sun, Oct 5 1986  7:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Boiler Room                      Sun, Oct 5 1986 -------" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Besieged                         Sun, Oct 5 1986  8:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Golden Witch                 Sun, Oct 5 1986 11:30PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('start'), With(t22) ] hovered Play ("se10", se1002)
            hbox:
                textbutton "Notebook Fragment in a Wine Bottle" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('start'), With(t22) ] hovered Play ("se10", se1002)
                textbutton "Back to Main Menu  " xalign 1.0 text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
            
    elif scenario_Number == 2:
        vbox:
            xcenter (985.0/1920.0) yanchor 0.0 ypos (9.0/1080.0)
            hbox:
                text "Please select your destination." size 45 font "default.ttf" drop_shadow (2, 2)
                textbutton "Back to Main Menu  " xalign 1.0 text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
            null height 17
            textbutton "'Furniture'                                             " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Wonderful Utopia                                        " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "School Culture Festival                                 " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Chessboard Preparations          Sat, Oct 4 1986        " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Guest of Honor                   Sat, Oct 4 1986 10:45AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Witch's Move                 Sat, Oct 4 1986  1:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "'Furniture' and 'People'         Sat, Oct 4 1986  6:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Wedding Ring                     Sat, Oct 4 1986 10:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Halloween                        Sun, Oct 5 1986  6:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Jessica and Kanon                Sun, Oct 5 1986  6:43AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "New Rule                         Sun, Oct 5 1986  6:50AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "A Suspect                        Sun, Oct 5 1986  7:30AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Wolves and Sheep Puzzle          Sun, Oct 5 1986  1:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Devil's Proof                    Sun, Oct 5 1986  1:17PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Fleeting Resistance              Sun, Oct 5 1986  6:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Surrender                        Sun, Oct 5 1986  9:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Resurrection                     Sun, Oct 5 1986 11:30PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Banquet of the Witch             Sun, Oct 5 1986 11:59PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 18), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        
    elif scenario_Number == 3:
        vbox:
            xcenter (985.0/1920.0) yanchor 0.0 ypos (9.0/1080.0)
            text "Please select your destination." size 45 font "default.ttf" drop_shadow (2, 2)
            null height 17
            textbutton "Days as a Girl                   Sat, Oct 4 1986        " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "My Preparations Are Complete     Sat, Oct 4 1986  2:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Witch's Written Challenge    Sat, Oct 4 1986  8:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Possibility of a 19th Person     Sat, Oct 4 1986  9:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Rosa and the Witch of the Forest                        " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Beginning of the Ceremony    Sun, Oct 5 1986  0:00  " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Madam Beatrice                   Sun, Oct 5 1986 12:21AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Virgilia                         Sun, Oct 5 1986  6:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Skirmish                         Sun, Oct 5 1986  7:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Key to the Golden Land       Sun, Oct 5 1986  9:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Coronation                       Sun, Oct 5 1986 10:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The New Witch                    Sun, Oct 5 1986 10:30AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Warning of Sacrifices            Sun, Oct 5 1986 11:00AM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Battle to the Death in the Hall  Sun, Oct 5 1986  1:00PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Definition of a Witch        Sun, Oct 5 1986  1:30PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Real Magic                       Sun, Oct 5 1986  5:44PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Witch's Courtroom            Sun, Oct 5 1986  6:03PM" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
            hbox:
                textbutton "The Witch's Illusion             " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 18), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
                textbutton "Back to Main Menu  " xalign 1.0 text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
            
    elif scenario_Number == 4:
        vbox:
            xcenter (648.0/1920.0) ycenter (540.0/1080.0)
            text "Please select your destination." size 45 font "default.ttf" drop_shadow (2, 2)
            null height 35
            textbutton "The New Guest             " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Ange and Maria            " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Future 12 Years Later " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Red Truth, Blue Truth     " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Ange's Recollection       " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Mariage Sorciere          " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Lure Towards Illusions    " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "My World                  " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Sakutaro                  " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "To the Island of the Witch" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            null height 35
            textbutton "Back to Main Menu" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
        vbox:
            xcenter (1380.0/1920.0) ycenter (512.0/1080.0)
            textbutton "Ushiromiya Kinzo          " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Sweet World of Witches" text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Dungeon                   " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "My Mission                " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Final Family Conference   " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "The Next Head             " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Cause of the Tragedy      " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Journey's Endpoint        " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 18), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            textbutton "Ushiromiya Ange           " text_style style.chp_sel focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 19), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
            


screen scenario_jump_name_old:
    tag menu
    
    $ x = (240.0/1920.0)
    
    add "background/efe/chess1.png" xalign 0.5 yalign 0.5
    add "background/efe/black.png" alpha (200.0/255.0)
    add "background/efe/hana1_.png"
    if scenario_Number == 1:
#        add "title/chapters/caption_2.png" xpos 231 ypos 24
        text "Please select your destination." xpos x ypos (45.0/1080.0) size 45 font "default.ttf" drop_shadow (2, 2)
        $ y=135.0
        textbutton "Arrival at Niijima Airport                   Sat, Oct 4 1986  8:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Arrival at Rokkenjima                        Sat, Oct 4 1986 10:30AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Guesthouse                                   Sat, Oct 4 1986 12:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Dining Room                                  Sat, Oct 4 1986  1:30PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Epitaph on the Portrait                      Sat, Oct 4 1986  1:30PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Sandy Beach                                  Sat, Oct 4 1986  3:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Letter and Umbrella                          Sat, Oct 4 1986  6:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Legend of the Gold                           Sat, Oct 4 1986 10:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Night of the Storm                           Sat, Oct 4 1986 -------" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Six Chosen by the Key                    Sun, Oct 5 1986  6:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Curtain-rise on Tragedy                      Sun, Oct 5 1986  8:45AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Occult                                       Sun, Oct 5 1986  1:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Two Who Are Close                        Sun, Oct 5 1986  7:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Boiler Room                                  Sun, Oct 5 1986 -------" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Besieged                                     Sun, Oct 5 1986  8:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Golden Witch                             Sun, Oct 5 1986 11:30PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Notebook Fragment in a Wine Bottle" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('start'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Back to Main Menu  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
        
#        text "Please select your destination." xpos 240 ypos 45 size 45 font "default.ttf" drop_shadow (2, 2)
#        textbutton "Arrival at Niijima Airport              Sat, Oct 4 1986  8:00AM" style style.button_text['chp_sel'] xpos 240 ypos 135 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Arrival at Rokkenjima                   Sat, Oct 4 1986 10:30AM" style style.button_text['chp_sel'] xpos 240 ypos 184 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Guesthouse                              Sat, Oct 4 1986 12:00PM" style style.button_text['chp_sel'] xpos 240 ypos 234 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Dining Room                             Sat, Oct 4 1986  1:30PM" style style.button_text['chp_sel'] xpos 240 ypos 284 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Epitaph on the Portrait                 Sat, Oct 4 1986  1:30PM" style style.button_text['chp_sel'] xpos 240 ypos 333 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Sandy Beach                             Sat, Oct 4 1986  3:00PM" style style.button_text['chp_sel'] xpos 240 ypos 383 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Letter and Umbrella                     Sat, Oct 4 1986  6:00PM" style style.button_text['chp_sel'] xpos 240 ypos 432 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Legend of the Gold                      Sat, Oct 4 1986 10:00PM" style style.button_text['chp_sel'] xpos 240 ypos 482 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Night of the Storm                      Sat, Oct 4 1986 -------" style style.button_text['chp_sel'] xpos 240 ypos 531 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "The Six Chosen by the Key               Sun, Oct 5 1986  6:00AM" style style.button_text['chp_sel'] xpos 240 ypos 581 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Curtain-rise on Tragedy                 Sun, Oct 5 1986  8:45AM" style style.button_text['chp_sel'] xpos 240 ypos 630 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Occult                                  Sun, Oct 5 1986  1:00PM" style style.button_text['chp_sel'] xpos 240 ypos 680 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "The Two Who Are Close                   Sun, Oct 5 1986  7:00PM" style style.button_text['chp_sel'] xpos 240 ypos 729 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Boiler Room                             Sun, Oct 5 1986 -------" style style.button_text['chp_sel'] xpos 240 ypos 778 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Besieged                                Sun, Oct 5 1986  8:00PM" style style.button_text['chp_sel'] xpos 240 ypos 828 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "The Golden Witch                        Sun, Oct 5 1986 11:30PM" style style.button_text['chp_sel'] xpos 240 ypos 877 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Notebook Fragment in a Wine Bottle" style style.button_text['chp_sel'] xpos 240 ypos 927 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        textbutton "Back to Main Menu  " style style.button_text['chp_sel'] xpos 240 ypos 977 focus_mask None action [ Hide('scenario_jump_name'), Jump('exit_chapters') ] hovered Play ("se10", se1002)
        
#        imagebutton auto "title/chapters/ep1/ch1_%s.png" xpos 240 ypos 143 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch2_%s.png" xpos 240 ypos 191 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch3_%s.png" xpos 240 ypos 242 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch4_%s.png" xpos 240 ypos 292 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch5_%s.png" xpos 240 ypos 341 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch6_%s.png" xpos 240 ypos 391 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch7_%s.png" xpos 240 ypos 440 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch8_%s.png" xpos 240 ypos 490 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch9_%s.png" xpos 240 ypos 539 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch10_%s.png" xpos 240 ypos 589 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch11_%s.png" xpos 240 ypos 638 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch12_%s.png" xpos 240 ypos 688 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch13_%s.png" xpos 240 ypos 737 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch14_%s.png" xpos 240 ypos 787 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch15_%s.png" xpos 240 ypos 836 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch16_%s.png" xpos 240 ypos 886 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/ch17_%s.png" xpos 240 ypos 936 focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Jump('scenario_jump_data1') ] hovered Play ("se10", se1002)
#        imagebutton auto "title/chapters/ep1/exit_%s.png" xpos 240 ypos 984 focus_mask None action [ Hide('scenario_jump_name'), Jump('exit_chapters') ] hovered Play ("se10", se1002)
    
    if scenario_Number == 2:
        text "Please select your destination." xpos x ypos (23.0/1080.0) size 45 font "default.ttf" drop_shadow (2, 2)
        $ y=86.0
        textbutton "'Furniture'                              " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Wonderful Utopia                    " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "School Culture Festival                         " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Chessboard Preparations                      Sat, Oct 4 1986  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Guest of Honor                               Sat, Oct 4 1986 10:45AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Witch's Move                             Sat, Oct 4 1986  1:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "'Furniture' and 'People'                     Sat, Oct 4 1986  6:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Wedding Ring                                 Sat, Oct 4 1986 10:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Halloween                                    Sun, Oct 5 1986  6:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Jessica and Kanon                            Sun, Oct 5 1986  6:43AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "New Rule                                     Sun, Oct 5 1986  6:50AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "A Suspect                                    Sun, Oct 5 1986  7:30AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Wolves and Sheep Puzzle                      Sun, Oct 5 1986  1:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Devil's Proof                                Sun, Oct 5 1986  1:17PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Fleeting Resistance                          Sun, Oct 5 1986  6:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Surrender                                    Sun, Oct 5 1986  9:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Resurrection                                 Sun, Oct 5 1986 11:30PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Banquet of the Witch                         Sun, Oct 5 1986 11:59PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 18), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Back to Main Menu  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
    
    if scenario_Number == 3:
        text "Please select your destination." xpos x ypos (45.0/1080.0) size 45 font "default.ttf" drop_shadow (2, 2)
        $ y=110.0
        textbutton "Days as a Girl                 　             Sat, Oct 4 1986  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('scenario_jump_data2'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "My Preparations Are Complete   　             Sat, Oct 4 1986  2:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Witch's Written Challenge  　             Sat, Oct 4 1986  8:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Possibility of a 19th Person   　             Sat, Oct 4 1986  9:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Rosa and the Witch of the Forest 　                                  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Beginning of the Ceremony 　              Sun, Oct 5 1986  0:00  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Madam Beatrice               　               Sun, Oct 5 1986 12:21AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Virgilia                    　                Sun, Oct 5 1986  6:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Skirmish                     　               Sun, Oct 5 1986  7:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Key to the Golden Land   　               Sun, Oct 5 1986  9:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Coronation                   　               Sun, Oct 5 1986 10:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The New Witch                　               Sun, Oct 5 1986 10:30AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Warning of Sacrifices          　             Sun, Oct 5 1986 11:00AM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Battle to the Death in the Hall 　            Sun, Oct 5 1986  1:00PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Definition of a Witch   　                Sun, Oct 5 1986  1:30PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Real Magic                  　                Sun, Oct 5 1986  5:44PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Witch's Courtroom       　                Sun, Oct 5 1986  6:03PM" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "The Witch's Illusion　　　　　　　           　　　　　　　　　　　　　　　      " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 18), Start('scenario_jump_data3'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=50.0
        textbutton "Back to Main Menu  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
    
    if scenario_Number == 4:
#        $ x=285
        $ x=(400.0/1920.0)
        text "Please select your destination." xpos x ypos (110.0/1080.0) size 45 font "default.ttf" drop_shadow (2, 2)
        $ y=225.0
        textbutton "The New Guest" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 1), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Ange and Maria" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 2), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "The Future 12 Years Later" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 3), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Red Truth, Blue Truth" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 4), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Ange's Recollection" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 5), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Mariage Sorciere" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 6), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Lure Towards Illusions" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 7), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "My World" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 8), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Sakutaro" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 9), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "To the Island of the Witch" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 10), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=115.0
        textbutton "Back to Main Menu  " style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), Start('exit_chapters'), With(t22) ] hovered Play ("se10", se1002)
#        $ x=???
        $ x=(1070.0/1920.0)
        $ y=225.0
        textbutton "Ushiromiya Kinzo" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 11), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "The Sweet World of Witches" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 12), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Dungeon" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 13), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "My Mission" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 14), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Final Family Conference" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 15), Jump('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "The Next Head" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 16), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Cause of the Tragedy" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 17), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Journey's Endpoint" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 18), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
        $ y+=70.0
        textbutton "Ushiromiya Ange" style style.button_text['chp_sel'] xpos x ypos (y/1080.0) focus_mask None action [ Hide('scenario_jump_name'), SetVariable("BtnRes", 19), Start('scenario_jump_data4'), With(t22) ] hovered Play ("se10", se1002)
    
label start:
    stop music
    scene chess1
    show hana1_:
        alpha 0.7        # alpha not present in original
    show black:
        alpha (200.0/255.0)
    with None
    nvl clear
    
    scene black with t22
    $ _game_menu_screen = None
    $ renpy.free_memory()
    
    $ tips_r_click = 1
    $ chars_r_click = 1
    $ r_for_title = 0
    $ r_u_tea_flg = 0
    $ r_hyouji_cha = 0
    $ r_hyouji_side = 0
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 1
    
    $ clock_speed = 5.0         ## divide by 180 to get seconds (8 seconds per 1440 degrees (24 hours))
    $ min3 = 0
    $ clock_x = 0.5
    $ clock_y = 0.5
    $ clock_size = 0.3
    
    if BtnRes == 1:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 480
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_1 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_1
    elif BtnRes == 2:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 630
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_2 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_2
    elif BtnRes == 3:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 720
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_3 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_3
    elif BtnRes == 4:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 810
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_4 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_4
    elif BtnRes == 5:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 810
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_5 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_5
    elif BtnRes == 6:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 900
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_6 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_6
    elif BtnRes == 7:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1080
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_7 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_7
    elif BtnRes == 8:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1380
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_8 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_8
    elif BtnRes == 9:
        call scenario_jump_hiduke_1986_10_4
        call scenario_jump_exit_efe1
#        call jump_flg_set1_9 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_9
    elif BtnRes == 10:
        $ min1 = 1440
        $ min2 = 1800
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_10 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_10
    elif BtnRes == 11:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1965
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_11 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_11
    elif BtnRes == 12:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2220
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_12 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_12
    elif BtnRes == 13:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2580
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_13 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_13
    elif BtnRes == 14:
        call scenario_jump_hiduke_1986_10_5
        call scenario_jump_exit_efe1
#        call jump_flg_set1_14 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_14
    elif BtnRes == 15:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2640
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_15 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_15
    elif BtnRes == 16:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2850
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
#        call jump_flg_set1_16 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_16
    elif BtnRes == 17:
        call scenario_jump_exit_efe1
#        call jump_flg_set1_17 ## tips/chars
        $ renpy.block_rollback()
        jump umi1_17
    else:
        "An error has occured. \ Please restart the game."
        $ scenario_Number = 1
        jump umi1_opning
    
label scenario_jump_data2:
    $ _game_menu_screen = None
    stop music
    scene chess1
    show hana1_:
        alpha 0.7        # alpha not present in original
    show black:
        alpha (200.0/255.0)
    with None
    nvl clear
    
    scene black with t22
    $ _game_menu_screen = None
    $ renpy.free_memory()
    
    $ tips_r_click = 1
    $ chars_r_click = 1
    $ r_for_title = 0
    $ r_hyouji_cha = 0
    $ r_hyouji_side = 0
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 1
    
    $ clock_speed = 5.0
    $ min3 = 0
    $ clock_x = 0.5
    $ clock_y = 0.5
    $ clock_size = 0.3
    
    if BtnRes == 1:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_1
    elif BtnRes == 2:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_2
    elif BtnRes == 3:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_3
    elif BtnRes == 4:
        call scenario_jump_hiduke_1986_10_4
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_4
    elif BtnRes == 5:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 645
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_5
    elif BtnRes == 6:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 780
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_6
    elif BtnRes == 7:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1140
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_7
    elif BtnRes == 8:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1320
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_8
    elif BtnRes == 9:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1800
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_9
    elif BtnRes == 10:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 0
        $ min2 = 403
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_10
    elif BtnRes == 11:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1850
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_11
    elif BtnRes == 12:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1890
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_12
    elif BtnRes == 13:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2220
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_13
    elif BtnRes == 14:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2237
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_14
    elif BtnRes == 15:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2520
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_15
    elif BtnRes == 16:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2700
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_16
    elif BtnRes == 17:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2850
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_17
    elif BtnRes == 18:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2879
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi2_18


label scenario_jump_data3:
    $ _game_menu_screen = None
    stop music
    scene chess1
    show hana1_:
        alpha 0.7        # alpha not present in original
    show black:
        alpha (200.0/255.0)
    with None
    nvl clear
    
    scene black with t22
    $ _game_menu_screen = None
    $ renpy.free_memory()
    
    $ tips_r_click = 1
    $ chars_r_click = 1
    $ r_for_title = 0
    $ r_hyouji_cha = 0
    $ r_hyouji_cha_ma = 0
    $ r_hyouji_side = 0
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 1
    
    $ clock_speed = 5.0
    $ min3 = 0
    $ clock_x = 0.5
    $ clock_y = 0.5
    $ clock_size = 0.3
    
    if BtnRes == 1:
        call scenario_jump_hiduke_1986_10_4
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_1
    elif BtnRes == 2:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 840
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_2
    elif BtnRes == 3:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1200
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_3
    elif BtnRes == 4:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1260
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_4
    elif BtnRes == 5:
        call scenario_jump_hiduke_1986_10_4
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_5
    elif BtnRes == 6:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1440
        $ clock_speed = 0
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_6
    elif BtnRes == 7:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1461
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_7
    elif BtnRes == 8:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1800
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_8
    elif BtnRes == 9:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1860
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_9
    elif BtnRes == 10:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 1980
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_10
    elif BtnRes == 11:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2040
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_11
    elif BtnRes == 12:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2070
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_12
    elif BtnRes == 13:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2100
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_13
    elif BtnRes == 14:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2220
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_14
    elif BtnRes == 15:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2250
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_15
    elif BtnRes == 16:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2504
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_16
    elif BtnRes == 17:
        call scenario_jump_hiduke_1986_10_5
        $ min1 = 1440
        $ min2 = 2523
        $ clock_speed = ((min2 - min1) / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_17
    elif BtnRes == 18:
        call scenario_jump_hiduke_1986_10_5
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi3_18


label scenario_jump_data4:
    $ _game_menu_screen = None
    stop music
    scene chess1
    show hana1_:
        alpha 0.7        # alpha not present in original
    show black:
        alpha (200.0/255.0)
    with None
    nvl clear
    
    scene black with t22
    $ _game_menu_screen = None
    $ renpy.free_memory()
    
    $ tips_r_click = 1
    $ chars_r_click = 1
    $ r_for_title = 0
    $ r_hyouji_cha = 0
    $ r_hyouji_cha_ma = 0
    $ r_hyouji_side = 0
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 1
    $ r_hyouji = 2
    
    $ clock_speed = 5.0
    $ min3 = 0
    $ clock_x = 0.5
    $ clock_y = 0.5
    $ clock_size = 0.3
    
    if BtnRes == 1:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_1
    elif BtnRes == 2:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_2
    elif BtnRes == 3:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_3
    elif BtnRes == 4:
        $ min1 = 0
        $ min2 = 891
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_4
    elif BtnRes == 5:
        call scenario_jump_hiduke_1986_10_4
        $ min1 = 0
        $ min2 = 1087
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_5
    elif BtnRes == 6:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_6
    elif BtnRes == 7:
        call scenario_jump_exit_efe1
        call scenario_jump_hiduke_1998
        $ renpy.block_rollback()
        jump umi4_7
    elif BtnRes == 8:
        call scenario_jump_exit_efe1
        call scenario_jump_hiduke_enj_mirai
        $ renpy.block_rollback()
        jump umi4_8
    elif BtnRes == 9:
        scene black
        scene onlayer cinema2
        hide screen clock
        with t2
        $ _game_menu_screen = "save"
        $ renpy.block_rollback()
        jump umi4_9
    elif BtnRes == 10:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_10
    elif BtnRes == 11:
        $ min1 = 0
        $ min2 = 1308
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_11
    elif BtnRes == 12:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_12
    elif BtnRes == 13:
        call scenario_jump_hiduke_1986_10_4_2
        $ min1 = 0
        $ min2 = 1352
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_13
    elif BtnRes == 14:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_14
    elif BtnRes == 15:
        call scenario_jump_hiduke_1986_10_4_2
        $ min1 = 0
        $ min2 = 1380
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_15
    elif BtnRes == 16:
        call scenario_jump_hiduke_1986_10_4_2
        $ min1 = 0
        $ min2 = 1391
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_16
    elif BtnRes == 17:
        call scenario_jump_hiduke_1986_10_4_2
        $ min1 = 0
        $ min2 = 1427
        $ clock_speed = (min2 / 180.0)
        call scenario_jump_clock
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_17
    elif BtnRes == 18:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_18
    elif BtnRes == 19:
        call scenario_jump_exit_efe1
        $ renpy.block_rollback()
        jump umi4_19


label scenario_jump_hiduke_1986_10_4:
    scene black with t2
    $ se1(se29)
    scene oct_4_1986 with t2
    with Pause(1.0)
    scene black with t2
    return
    
label scenario_jump_hiduke_1986_10_4_2:
    scene black with t2
    $ se1(se28)
    scene oct_4_1986 with t2
    with Pause(1.0)
    scene black with t2
    return

label scenario_jump_hiduke_1986_10_5:
    scene black with t2
    $ se1(se28)
    scene oct_5_1986 with t2
    with Pause(1.0)
    scene black with t2
    return

label scenario_jump_hiduke_1998:
    $ E_A()
    scene black with t2
    $ se1v(se29,0.7)
    scene oct_1998 with t80
    with Pause(4.0)
    scene black with t22
    return
    
label scenario_jump_hiduke_enj_mirai:
    $ E_A()
    $ se1v(se29,0.7)
    scene ENJ_mirai01 with t80
    with Pause(4.0)
    scene black with t22
    return
    
label scenario_jump_exit_efe1:
    $ E_A()
    stop se9
    stop se10
    stop se20
    with Pause(1.0)
#    show dim onlayer cinema2
    show ware onlayer cinema2
    with None
    $ seplay(9,se1100.pick())
    with Pause(1.0)
    scene black
    scene onlayer cinema2
    hide screen clock
    with t2
#    $ _game_menu_screen = "save"
    return

label scenario_jump_clock:
    show screen clock
    with t2
    with Pause(1.0)
    play me5 me1050
#    $ min3 = clock_speed
#    $ min1 += min2
    with Pause(clock_speed)
    stop me5
    return

label exit_chapters:
    scene chess1 with None
    with Pause(0.3)
    show black with t42
    $ renpy.full_restart()
    
screen demo:
    tag menu
    add "background/efe/black.png"
    timer 1.0 action Start("demo")
label demo:
    $ E_A()
    stop se10
    stop se9
    stop se20
    scene black with None
    
    if persistent.op_demo == 1 and (renpy.seen_label('umi1_op2') or renpy.seen_label('umi2_op2') or renpy.seen_label('umi3_op2')):
        $ renpy.movie_cutscene("movie/umineko_op1.mkv")
        $ persistent.op_demo += 1
        jump demo_end
    elif persistent.op_demo == 1:
        $ persistent.op_demo += 1
    
    if persistent.op_demo == 2 and renpy.seen_label('umi4_op2'):
        $ renpy.movie_cutscene("movie/umineko_op3.mkv")
        $ persistent.op_demo += 1
        jump demo_end
    elif persistent.op_demo == 2:
        $ persistent.op_demo += 1
    
    if persistent.op_demo == 3:
        $ persistent.op_demo = 0
    
    if persistent.op_demo == 0:
        $ renpy.movie_cutscene("movie/umineko_op.mkv")
        $ persistent.op_demo += 1
label demo_end:
    scene black with t22
    return
    
init -2:
    transform title:
        alpha 0.0
        delay 0.3 alpha 1.0
    transform logo:
        xanchor 1.0 xpos (1870.0/1920.0) ypos (50.0/1080.0)
    transform ep_start(x,y):
        xpos (x/1920.0) ypos (y/1080.0)
    transform ep_move(x=0,y=0,y2=0):
        xpos (x/1920.0) ypos (y/1080.0)
        linear 0.3 ypos (y2/1080.0)
    transform ep_button(x=0,y=0,z=0):
        xpos (x/1920.0) ypos y alpha 0.0
        pause z alpha 1.0
    transform new_title(x,y):
        xpos ((x + 20.0)/1920.0) ypos ((y+8.0)/1080.0)
    transform new_ep(x=0,y=0,z=0):
        xpos (x/1920.0) ypos (y/1080.0) alpha 0.0
        pause z alpha 1.0
    
    transform tea_button:
        alpha 0.0
        pause 0.3 alpha 1.0
    transform chp_fadeout:
        alpha 1.0
        pause 5.0
        linear 1.0 alpha 0.0
    transform chp_fadein:
        alpha 0.0
        pause 4.0
        linear 1.0 alpha 1.0
    transform chp_fadein2:
        alpha 0.0
        pause 5.0
        linear 0.5 alpha 1.0
    transform choice_caption:
#        pause 5.0
#        alpha 0.0 xpos (541.0/1920.0) ypos (348.0/1080.0)
        xcenter (929.0/1920.0) ycenter (425.0/1080.0)
#        linear 1.0 alpha 1.0
    transform choice_yes:
        pause 5.0
        alpha 0.0
        linear 1.0 alpha 1.0
    transform choice_no:
        pause 5.0
        alpha 0.0
        linear 1.0 alpha 1.0
    transform m_btn_trs:
        alpha 0.15
        linear 1.0 alpha 0.5
        linear 0.8 alpha 0.15
        repeat





## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    
screen m_glow:
    #add "murderer/input_mode/white.png" xpos (m_btn_x/1920.0) ypos (m_btn_y/1080.0) at m_btn_trs
    if (r_hyouji_side == 0 and persistent.cha_new[scenario_Number][1][r_hyouji_cha][r[r_hyouji_cha][condition]] == 1) or (r_hyouji_side == 1 and persistent.cha_new[scenario_Number][2][r_hyouji_cha_ma][r_ma[r_hyouji_cha_ma][condition]] == 1) or (r_hyouji_side == 2 and persistent.cha_new[scenario_Number][3][r_hyouji_cha_enj][r_enj_ma[r_hyouji_cha_enj][condition]] == 1):
        add "r_click/chars/btn/white_new.png" xpos m_btn_x ypos m_btn_y at m_btn_trs
    else:
        add "r_click/chars/btn/white.png" xpos m_btn_x ypos m_btn_y at m_btn_trs
    
    
    
    
label main_menu:
    $ load_title = 1
    
#    renpy.predict_screen("main_menu")
    
    jump main_menu_screen
#    $ renpy.show_screen("main_menu_custom")
#    $ ui.interact()
    
init python:
    
    start_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,2,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,2,520,56)))
    start_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,2,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,2,520,56)))
    
    tea_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,182,520,56)))
    tea_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,182,520,56)))
    
    ura_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,242,520,56)))
    ura_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,242,520,56)))
    
    continue1_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    continue1_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    continue2_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    continue2_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    continue3_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    continue3_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    
    load1_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    load1_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    load2_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    load2_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    load3_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    load3_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    
    chars_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,302,520,56)))
    chars_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,302,520,56)))
    
    tips_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,362,520,56)))
    tips_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,362,520,56)))
    
    config1_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config1_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config2_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config2_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config3_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config3_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config4_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config4_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config5_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    config5_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    
    picture1_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    picture1_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    picture2_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    picture2_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    picture3_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,482,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    picture3_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,482,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    
    music1_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    music1_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    music2_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    music2_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    music3_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,542,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    music3_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,542,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    
    exit1_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit1_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit2_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit2_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit3_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit3_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit4_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,482,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit4_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,482,520,56)), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit5_i = LiveComposite((520,56), (0,0), im.MatrixColor(im.Flip(im.Crop("title/plate.png", (0,542,520,56)), vertical=True), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    exit5_h = LiveComposite((520,56), (0,0), im.MatrixColor(im.Flip(im.Crop("title/plate.png", (0,542,520,56)), vertical=True), im.matrix.colorize("#000","#ff2929")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    
    episode1_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,2,256,44)))
    episode1_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,2,256,44)))
    
    episode2_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,50,256,44)))
    episode2_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,50,256,44)))
    episode2_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,50,256,44)))
    
    episode3_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,98,256,44)))
    episode3_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,98,256,44)))
    episode3_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,98,256,44)))
    
    episode4_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,146,256,44)))
    episode4_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,146,256,44)))
    episode4_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,146,256,44)))
    
    episode5_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,194,256,44)))
    episode5_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,194,256,44)))
    episode5_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,194,256,44)))
    
    episode6_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,242,256,44)))
    episode6_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,242,256,44)))
    episode6_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,242,256,44)))
    
    episode7_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,290,256,44)))
    episode7_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,290,256,44)))
    episode7_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,290,256,44)))
    
    episode8_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,338,256,44)))
    episode8_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,338,256,44)))
    episode8_l = LiveComposite((280,44), (0,0), Solid("#252525"), (24,0), im.Crop("title/menu2.png", (0,338,256,44)))
    
    ep_back_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,386,256,44)))
    ep_back_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,386,256,44)))
    
    unlock_all_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,434,256,44)))
    unlock_all_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,434,256,44)))
    
    unlock_i = LiveComposite((160,44), (0,0), Solid("#371b1b"), (0,0), im.Crop("title/menu2.png", (67,434,128,44)))
    unlock_h = LiveComposite((160,44), (0,0), Solid("#ff2929"), (0,0), im.Crop("title/menu2.png", (67,434,128,44)))
    
    trailer_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,482,256,44)))
    trailer_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,482,256,44)))
    
    tsubasa_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,530,256,44)))
    tsubasa_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,530,256,44)))
    
    hane_i = LiveComposite((280,44), (0,0), Solid("#371b1b"), (24,0), im.Crop("title/menu2.png", (0,578,256,44)))
    hane_h = LiveComposite((280,44), (0,0), Solid("#ff2929"), (24,0), im.Crop("title/menu2.png", (0,578,256,44)))
    
    exit_i = ConditionSwitch("_preferences.language == None", LiveComposite((128,60), (0,0), Solid("#371b1b"), (0,0), im.Crop("title/menu.png", (390,600,128,60))), "_preferences.language == 'japanese'", LiveComposite((128,60), (0,0), Solid("#371b1b"), (0,0), Image("exit.png")))          # for use with all screens
    exit_h = ConditionSwitch("_preferences.language == None", LiveComposite((128,60), (0,0), Solid("#ff2929"), (0,0), im.Crop("title/menu.png", (390,600,128,60))), "_preferences.language == 'japanese'", LiveComposite((128,60), (0,0), Solid("#ff2929"), (0,0), Image("exit.png")))
    
image title_new = im.Crop("title/new.png", (0,0,104,40))
    
image title_start = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,2,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,2,520,56)))
    
image title_tea = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,182,520,56)))
    
image title_ura = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,242,520,56)))
    
image title_continue1 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
image title_continue2 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
image title_continue3 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,62,520,56)))
    
image title_load1 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
image title_load2 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
image title_load3 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,122,520,56)))
    
image title_chars = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,302,520,56)))
    
image title_tips = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,362,520,56)))
    
image title_config1 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,62,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
image title_config2 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,182,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
image title_config3 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
image title_config4 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
image title_config5 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,422,520,56)))
    
image title_picture1 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,302,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
image title_picture2 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
image title_picture3 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,482,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,482,520,56)))
    
image title_music1 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,362,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
image title_music2 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
image title_music3 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,542,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,542,520,56)))
    
image title_exit1 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,122,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
image title_exit2 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,242,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
image title_exit3 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,422,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
image title_exit4 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Crop("title/plate.png", (0,482,520,56)), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
image title_exit5 = LiveComposite((520,56), (0,0), im.MatrixColor(im.Flip(im.Crop("title/plate.png", (0,542,520,56)), vertical=True), im.matrix.colorize("#000","#371b1b")), (0,0), im.Crop("title/menu.png", (0,602,520,56)))
    
image title1 = "title/bg1.png"
image title2 = "title/bg2.png"
image title3 = "title/bg3.png"
image title4 = "title/bg4.png"
image title5 = "title/bg5.png"
image title6 = "title/bg6.png"
image title7 = "title/bg7.png"
image title_logo = "title/logo.png"
