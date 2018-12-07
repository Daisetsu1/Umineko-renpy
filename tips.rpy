init:
    
    python:
        condition = 9
        condition_end = 10
        tmp2 = 0
        def execres(exeres,var1):
            global r
            global condition
            global condition_end
            if exeres == "+":
                if r[var1][condition] >= r[var1][condition_end]:
                    pass
                else:
                    r[var1][condition] += 1
            elif exeres == "-":
                if r[var1][condition] <= 1:
                    pass
                else:
                    r[var1][condition] -= 1
            if rmenu_text == 1:
                cha_chk(scenario_Number,1,var1,r[var1][condition],r[var1][condition_end])
            renpy.restart_interaction()
        execresur = renpy.curry(execres)
        
        def execres_ma4(exeres,var1):
            global r_ma
            global condition
            global condition_end
            if exeres == "+":
                if r_ma[var1][condition] >= r_ma[var1][condition_end]:
                    pass
                else:
                    r_ma[var1][condition] += 1
            elif exeres == "-":
                if r_ma[var1][condition] <= 1:
                    pass
                else:
                    r_ma[var1][condition] -= 1
            if rmenu_text == 1:
                cha_chk(scenario_Number,2,var1,r_ma[var1][condition],r_ma[var1][condition_end])
            renpy.restart_interaction()
        execresur_ma4 = renpy.curry(execres_ma4)
        
        def execres_enj(exeres,var1):
            global r_enj_ma
            global condition
            global condition_end
            if exeres == "+":
                if r_enj_ma[var1][condition] >= r_enj_ma[var1][condition_end]:
                    pass
                else:
                    r_enj_ma[var1][condition] += 1
            elif exeres == "-":
                if r_enj_ma[var1][condition] <= 1:
                    pass
                else:
                    r_enj_ma[var1][condition] -= 1
            if rmenu_text == 1:
                cha_chk(scenario_Number,3,var1,r_enj_ma[var1][condition],r_enj_ma[var1][condition_end])
            renpy.restart_interaction()
        execresur_enj = renpy.curry(execres_enj)
        
        def execres_alt():
            global r
            global r_hyouji_cha
            global condition
            global condition_end
            if r[r_hyouji_cha][condition] >= r[r_hyouji_cha][condition_end]:
                r[r_hyouji_cha][condition] = 1
                renpy.music.set_volume(default_vol, 0, channel="se9")
                renpy.music.play(se1021,channel='se9')
                renpy.with_statement(t22, always=True)
            else:
                r[r_hyouji_cha][condition] += 1
                renpy.music.set_volume(default_vol, 0, channel="se9")
                renpy.music.play(se1100.pick(),channel='se9')
            renpy.restart_interaction()
        execresur_alt = renpy.curry(execres_alt)
        
        def execres_alt_ma():
            global r_ma
            global r_hyouji_cha_ma
            global condition
            global condition_end
            if r_ma[r_hyouji_cha_ma][condition] >= r_ma[r_hyouji_cha_ma][condition_end]:
                r_ma[r_hyouji_cha_ma][condition] = 1
                renpy.music.set_volume(default_vol, 0, channel="se9")
                renpy.music.play(se1021.pick(),channel='se9')
                renpy.with_statement(t22, always=True)
            else:
                r_ma[r_hyouji_cha_ma][condition] += 1
                renpy.music.set_volume(default_vol, 0, channel="se9")
                renpy.music.play(se1100.pick(),channel='se9')
            renpy.restart_interaction()
        execresur_alt_ma = renpy.curry(execres_alt_ma)
        
        def execres0(exeres):
            global r
            global condition
            global condition_end
            if exeres == "+":
                for tmp2 in range(1,56):
                    if r[tmp2][condition] >= r[tmp2][condition_end] or r[tmp2][condition] <= 0:
                        pass
                    else:
                        r[tmp2][condition] += 1
            elif exeres == "-":
                for tmp2 in range(1,56):
                    if r[tmp2][condition] <= 1:
                        pass
                    else:
                        r[tmp2][condition] -= 1
            if rmenu_text == 1:
                cha_chk(scenario_Number,1,r_hyouji_cha,r[r_hyouji_cha][condition],r[r_hyouji_cha][condition_end])
            renpy.restart_interaction()
        execresur0 = renpy.curry(execres0)
        
        def execres1(exeres):
            global r_ma
            global condition
            global condition_end
            if exeres == "+":
                for tmp2 in range(1,56):
                    if r_ma[tmp2][condition] >= r_ma[tmp2][condition_end] or r_ma[tmp2][condition] <= 0:
                        pass
                    else:
                        r_ma[tmp2][condition] += 1
            elif exeres == "-":
                for tmp2 in range(1,56):
                    if r_ma[tmp2][condition] <= 1:
                        pass
                    else:
                        r_ma[tmp2][condition] -= 1
            if rmenu_text == 1:
                cha_chk(scenario_Number,2,r_hyouji_cha_ma,r_ma[r_hyouji_cha_ma][condition],r_ma[r_hyouji_cha_ma][condition_end])
            renpy.restart_interaction()
        execresur1 = renpy.curry(execres1)
        
        def execres2(exeres):
            global r_enj_ma
            global condition
            global condition_end
            if exeres == "+":
                for tmp2 in range(1,56):
                    if r_enj_ma[tmp2][condition] >= r_enj_ma[tmp2][condition_end] or r_enj_ma[tmp2][condition] <= 0:
                        pass
                    else:
                        r_enj_ma[tmp2][condition] += 1
            elif exeres == "-":
                for tmp2 in range(1,56):
                    if r_enj_ma[tmp2][condition] <= 1:
                        pass
                    else:
                        r_enj_ma[tmp2][condition] -= 1
            if rmenu_text == 1:
                cha_chk(scenario_Number,3,r_hyouji_cha_enj,r_enj_ma[r_hyouji_cha_enj][condition],r_enj_ma[r_hyouji_cha_enj][condition_end])
            renpy.restart_interaction()
        execresur2 = renpy.curry(execres2)
        
        def ishou():
            global r
            global r_ishou
            global r_hyouji_cha
#            if var:
            if r[r_hyouji_cha][r_ishou] == 1:
                r[r_hyouji_cha][r_ishou] = 2
            elif r[r_hyouji_cha][r_ishou] == 2:
                r[r_hyouji_cha][r_ishou] = 1
#                var = False
            renpy.restart_interaction()
        r_ishou_lsp = renpy.curry(ishou)
        
        def ishou2():
            global r_ma
            global r_ishou
            global r_hyouji_cha_ma
            if r_ma[r_hyouji_cha_ma][r_ishou] == 1:
                r_ma[r_hyouji_cha_ma][r_ishou] = 2
            elif r_ma[r_hyouji_cha_ma][r_ishou] == 2:
                r_ma[r_hyouji_cha_ma][r_ishou] = 1
            renpy.restart_interaction()
        r_ishou2_lsp = renpy.curry(ishou2)
        
        def ishou3():
            global r_enj_ma
            global r_ishou
            global r_hyouji_cha_enj
            if r_enj_ma[r_hyouji_cha_enj][r_ishou] == 1:
                r_enj_ma[r_hyouji_cha_enj][r_ishou] = 2
            elif r_enj_ma[r_hyouji_cha_enj][r_ishou] == 2:
                r_enj_ma[r_hyouji_cha_enj][r_ishou] = 1
            renpy.restart_interaction()
        r_ishou3_lsp = renpy.curry(ishou3)
        
        
    
        tips = [[0 for x in range(0,5)] for x in range(0,11)]
        grim = [[0 for x in range(0,9)] for x in range(0,15)]
        r = [[0 for x in range(0,16)] for x in range(0,60)]
        r_cha_text = [[[0 for x in range(0,5)] for x in range(0,50)] for x in range(0,8)]
        r_ma = [[0 for x in range(0,16)] for x in range(0,60)]
        r_enj_ma = [[0 for x in range(0,16)] for x in range(0,60)]
    
    $ r_enj_enj = 0
    $ m_temp1 = False
    $ cha_text_page = 1
    $ r_for_title = 1
    $ r_u_tea_flg = 0
    $ r_hyouji_side = 0
    $ r_hyouji_cha = 0
    $ r_hyouji_cha_ma = 0
    $ r_hyouji_cha_enj = 0
    $ r_ber_flg = 0
    $ r_tea_bea = 0
    
    $ side_flg = 0
    $ rmenu_ep5_oneshot = 0
    $ rmenu_text = 0
    $ r_tips_text = _(" ")
    $ r_hyouji = 1              ## 0 is char, 1 is tips, 2 is grim : 0 is not used
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 0
    $ tips_page = 1
    $ tips_page_max = 0
    $ tips_flg = 1
    $ tips_file = 2
    $ grim_page = 1
    $ grim_page_max = 0
    $ grim_flg = 1
    $ grim_file = 2
    $ grim_scene = 0
    $ tati_pages = 6            ## used to be tati_x
    $ itiran_x = 7
    $ itiran_y = 8
#    $ condition = 9
#    $ condition_end = 10
    $ r_ishou = 11
    $ tati_new_flg = 12
    $ cha_kazu = 21
    $ cha_kazu_ep2 = 22
    $ cha_kazu_ep3 = 23
    $ cha_kazu_ep4 = 23
#    $ r_ma_side = 2348
    
    $ r_kin = 1
    $ r_kla = 2
    $ r_nat = 3
    $ r_jes = 4
    $ r_eva = 5
    $ r_hid = 6
    $ r_geo = 7
    $ r_rud = 8
    $ r_kir = 9
    $ r_but = 10
    $ r_ros = 11
    $ r_mar = 12
    $ r_nan = 13
    $ r_gen = 14
    $ r_kum = 15
    $ r_goh = 16
    $ r_sha = 17
    $ r_kan = 18
    $ r_bea = 19
    $ r_ber = 20
    $ r_lam = 21
    $ r_enj = 22
    $ r_wal = 23
    $ r_ev2 = 24
    $ r_ron = 25
    
    $ ma_bea = 1
    $ ma_ber = 2
    $ ma_lam = 3
    $ ma_rg1 = 4
    $ ma_kin = 5
    $ ma_gen = 6
    $ ma_sha = 7
    $ ma_kan = 8
    $ ma_mar = 9
    $ ma_but = 10
    $ ma_rg2 = 11
    $ ma_rg3 = 12
    $ ma_rg4 = 13
    $ ma_rg5 = 14
    $ ma_rg6 = 15
    $ ma_rg7 = 16
    
    $ cha_kazu_ep2_2 = 17
    
    $ ma3_bea = 1
    $ ma3_ber = 2
    $ ma3_lam = 3
    $ ma3_rg1 = 4
    $ ma3_goa = 5
    $ ma3_wal = 6
    $ ma3_ron = 7
    $ ma3_ev2 = 8
    $ ma3_enj = 9
    $ ma3_s41 = 10
    $ ma3_rg2 = 11
    $ ma3_rg3 = 12
    $ ma3_rg4 = 13
    $ ma3_rg5 = 14
    $ ma3_rg6 = 15
    $ ma3_rg7 = 16
    $ ma3_s45 = 17
    
    $ cha_kazu_ep3_2 = 18
    
    $ r_s_hyouji = 2351
    $ r_s556_flg = 0
    
    $ ma4_lam = 1
    $ ma4_ber = 2
    $ ma4_bea = 3
    $ ma4_mar = 4
    $ ma4_enj = 5
    $ ma4_kin = 6
    $ ma4_sak = 7
    $ ma4_wal = 8
    $ ma4_ron = 9
    $ ma4_gap = 10
    $ ma4_s00 = 11
    $ ma4_rg1 = 12
    $ ma4_goa = 13
    $ ma4_rg2 = 14
    $ ma4_rg3 = 15
    $ ma4_rg4 = 16
    $ ma4_rg5 = 17
    $ ma4_rg6 = 18
    $ ma4_rg7 = 19
    $ ma4_s41 = 20
    $ ma4_s45 = 21
    $ ma4_s55 = 22
    
    $ cha_kazu_ep4_2 = 23
    
    $ enj_eva = 1
    $ enj_oko = 2
    $ enj_kas = 3
    $ enj_enj = 4
    $ enj_ama = 5
    $ enj_sak = 6
    $ enj_mar = 7
    $ enj_rg1 = 8
    $ enj_pro = 9
    $ enj_mas = 10
    $ enj_sab = 11
    $ enj_kwa = 12
    $ enj_ber = 13
    $ enj_rg2 = 14
    $ enj_rg3 = 15
    $ enj_rg4 = 16
    $ enj_rg5 = 17
    $ enj_rg6 = 18
    $ enj_rg7 = 19
    
    $ cha_kazu_ep4_3 = 20
    
    ## vv old stuff vv
    
    $ tips_r_click = 0
    $ chars_r_click = 0
    $ r_u_tea_flg = 0
    $ chars_text = 0
    $ chars_scenario = 0
    $ chars_start = 1
    $ cha_tati = 0
    $ exec_res = 0
    $ is_unlocked = False
    $ bgm_page = 1
    $ bgm_text = 0
    $ bgm_bg = 0
    
    #EP1
#    $ r_bea = r_ber = r_but = r_eva = r_gen = r_geo = r_goh = r_hid = r_jes = r_kan = r_kin = r_kir = r_kla = r_kum = r_mar = r_nan = r_nat = r_ros = r_rud = r_sha = 0
    #EP2
#    $ r_lam = 0
    
label rmenu_tips():
    $ r_for_title = 1
    $ r_hyouji = 1
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 0
    $ _game_menu_screen = None
    
    python:
        for tmp in range(1,10):
            tips[tmp][tips_flg] = 1
            if not persistent.tips_new[1][tmp]:
                persistent.tips_new[1][tmp] = 1
            if persistent.UMINEKOEND >=30:
                if not persistent.tips_new[2][tmp]:
                    persistent.tips_new[2][tmp] = 1
            if persistent.UMINEKOEND >=40:
                if not persistent.tips_new[3][tmp]:
                    persistent.tips_new[3][tmp] = 1
            if persistent.UMINEKOEND >=50:
                if not persistent.tips_new[4][tmp]:
                    persistent.tips_new[4][tmp] = 1
        for tmp in range(1,15):
            grim[tmp][grim_flg] = 1
            if not persistent.grim_new[1][tmp]:
                persistent.grim_new[1][tmp] = 1
            if persistent.UMINEKOEND >=30:
                if not persistent.grim_new[2][tmp]:
                    persistent.grim_new[2][tmp] = 1
            if persistent.UMINEKOEND >=40:
                if not persistent.grim_new[3][tmp]:
                    persistent.grim_new[3][tmp] = 1
            if persistent.UMINEKOEND >=50:
                if not persistent.grim_new[4][tmp]:
                    persistent.grim_new[4][tmp] = 1
        
    if scenario_Number == 1:
        if persistent.UMINEKOEND_TIPS1_flg == 1:
            $ persistent.UMINEKOEND_TIPS1_flg = 0
        jump tips_t1
#        $ renpy.show_screen('rmenu_tips_1')
#        $ ui.interact()
#        jump _noisy_return
    elif scenario_Number == 2:
        if persistent.UMINEKOEND_TIPS2_flg == 1:
            $ persistent.UMINEKOEND_TIPS2_flg = 0
        jump tips_t2
#        $ renpy.show_screen('rmenu_tips_2')
#        $ ui.interact()
#        jump _noisy_return
    elif scenario_Number == 3:
        if persistent.UMINEKOEND_TIPS3_flg == 1:
            $ persistent.UMINEKOEND_TIPS3_flg = 0
        jump tips_t3
#        $ renpy.show_screen('rmenu_tips_3')
#        $ ui.interact()
#        jump _noisy_return
    elif scenario_Number == 4:
        if persistent.UMINEKOEND_TIPS4_flg == 1:
            $ persistent.UMINEKOEND_TIPS4_flg = 0
        jump tips_t4
#        $ renpy.show_screen('rmenu_tips_4')
#        $ ui.interact()
#        jump _noisy_return
    return

label tips_t1:
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 0
    
    if scenario_Number == 2:
        hide screen rmenu_tips_2
    elif scenario_Number == 3:
        hide screen rmenu_tips_3
    elif scenario_Number == 4:
        hide screen rmenu_tips_4
    $ scenario_Number = 1
    $ renpy.show_screen('rmenu_tips_1')
    with t22
    $ ui.interact()
    jump _noisy_return
    return

label tips_t2:
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 0
    
    if scenario_Number == 1:
        hide screen rmenu_tips_1
    elif scenario_Number == 3:
        hide screen rmenu_tips_3
    elif scenario_Number == 4:
        hide screen rmenu_tips_4
    $ renpy.show_screen('rmenu_tips_2')
    $ scenario_Number = 2
    with t22
    $ ui.interact()
    jump _noisy_return
    return

label tips_t3:
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 0
    
    if scenario_Number == 2:
        hide screen rmenu_tips_2
    elif scenario_Number == 1:
        hide screen rmenu_tips_1
    elif scenario_Number == 4:
        hide screen rmenu_tips_4
    $ renpy.show_screen('rmenu_tips_3')
    $ scenario_Number = 3
    with t22
    $ ui.interact()
    jump _noisy_return
    return

label tips_t4:
    $ r_hyouji_tips = 0
    $ r_hyouji_grim = 0
    
    if scenario_Number == 2:
        hide screen rmenu_tips_2
    elif scenario_Number == 3:
        hide screen rmenu_tips_3
    elif scenario_Number == 1:
        hide screen rmenu_tips_1
    $ renpy.show_screen('rmenu_tips_4')
    $ scenario_Number = 4
    with t22
    $ ui.interact()
    jump _noisy_return
    return

style tips_btn:
        size 45
#        drop_shadow (2, 2)
#        drop_shadow_color "#000"
        color "#525252"
        hover_color "#ffffff"
        insensitive_color (82, 82, 82, 255)
        outlines [(2, "#000000", 2, 2)]
        selected_color "#eeeeee"
        selected_hover_color "#ffffff"
        font "times.ttf"
        xalign 0.0
        text_align 0.0

screen tips():
    tag menu
    
    if r_for_title == 0:                                  ##in-game
        add "background/efe/black.png" alpha 0.7
        key "game_menu" action [Play("se9", se1100.pick()), Return()]
        use all_pause
    elif r_for_title == 1:                                ##title screen
        use title_background
        add "background/efe/black.png" alpha (120.0/255.0)
        
#    add "r_click/tips/caption.png" at caption
    add "r_click/tips/left.png" xpos (164.0/1920.0) ypos (164.0/1080.0)
    add "r_click/tips/right.png" xpos (838.0/1920.0) ypos (164.0/1080.0)
    add "r_click/sysmenu/fg.png" yalign 1.0
    
    if r_for_title == 1:                                ##title screen
        $ tips_x = 220.0
        $ tips_y = 860.0
        
        if scenario_Number == 1:
            add im.Crop("r_click/tips/button_tips.png", (0,128,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0)
        else:
            imagebutton idle im.MatrixColor(im.Crop("r_click/tips/button_tips.png", (0,128,100,48)), im.matrix.brightness(-0.5)) hover im.Crop("r_click/tips/button_tips.png", (0,128,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0) focus_mask None action [ Play ("se9", se1010), Jump('tips_t1'), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        $ tips_x += 140.0
        if persistent.UMINEKOEND >= 30:
            if scenario_Number == 2:
                add im.Crop("r_click/tips/button_tips.png", (0,176,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0)
            else:
                imagebutton idle im.MatrixColor(im.Crop("r_click/tips/button_tips.png", (0,176,100,48)), im.matrix.brightness(-0.5)) hover im.Crop("r_click/tips/button_tips.png", (0,176,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0) focus_mask None action [ Play ("se9", se1010), Jump('tips_t2'), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        $ tips_x += 140.0
        if persistent.UMINEKOEND >= 40:
            if scenario_Number == 3:
                add im.Crop("r_click/tips/button_tips.png", (0,224,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0)
            else:
                imagebutton idle im.MatrixColor(im.Crop("r_click/tips/button_tips.png", (0,224,100,48)), im.matrix.brightness(-0.5)) hover im.Crop("r_click/tips/button_tips.png", (0,224,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0) focus_mask None action [ Play ("se9", se1010), Jump('tips_t3'), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        $ tips_x += 140.0
        if persistent.UMINEKOEND >= 50:
            if scenario_Number == 4:
                add im.Crop("r_click/tips/button_tips.png", (0,272,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0)
            else:
                imagebutton idle im.MatrixColor(im.Crop("r_click/tips/button_tips.png", (0,272,100,48)), im.matrix.brightness(-0.5)) hover im.Crop("r_click/tips/button_tips.png", (0,272,100,48)) xpos (tips_x/1920.0) ypos (tips_y/1080.0) focus_mask None action [ Play ("se9", se1010), Jump('tips_t4'), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
    
    if scenario_Number < 5:
        if r_hyouji == 1:
            imagebutton idle im.MatrixColor(im.Crop("r_click/tips/button_tips.png", (0,64,240,64)), im.matrix.brightness(-0.5)) hover im.Crop("r_click/tips/button_tips.png", (0,64,240,64)) xpos (224.0/1920.0) ypos (988.0/1080.0) focus_mask None action [ SetVariable("r_hyouji", 2), Play ("se9", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        elif r_hyouji == 2:
            if not r_for_title == 1 and scenario_Number == 4:
                pass
            else:
                imagebutton idle im.MatrixColor(im.Crop("r_click/tips/button_tips.png", (0,0,120,64)), im.matrix.brightness(-0.5)) hover im.Crop("r_click/tips/button_tips.png", (0,0,120,64)) xpos (224.0/1920.0) ypos (988.0/1080.0) focus_mask None action [ SetVariable("r_hyouji", 1), Play ("se9", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
    if r_for_title == 0:                                  ##in-game
        imagebutton idle exit_i hover exit_h xanchor 1.0 yanchor 1.0 xpos (1873.0/1920.0) ypos (1057.0/1080.0) focus_mask None action [ Play ("se9", se1100.pick()), Return() ] hovered Play ("se20", "sys_se/zyosys0.ogg")
    elif r_for_title == 1:                                ##title screen
        imagebutton idle exit_i hover exit_h xanchor 1.0 yanchor 1.0 xpos (1873.0/1920.0) ypos (1057.0/1080.0) focus_mask None action [ SetVariable("r_for_title", 0), SetVariable("r_hyouji_tips", 0), Play ("se9", "sys_se/zyosys3.ogg"), Return() ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
screen rmenu_tips_1():
    tag menu
    
    use tips
    
    $ bt_tips_ep1_def()
    
    if r_for_title == 0:
        $ tips_ep1()
    
    if r_hyouji == 1:
        
        use tips_text_ep1
        
        add "r_click/tips/caption.png" at caption
#        imagebutton auto "r_click/tips/grim_%s.png" xpos (720.0/1920.0) ypos (70.0/1080.0) focus_mask True action [ SetVariable("r_hyouji", 2), Play ("se9", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        $ tmp_y = 80.0
        $ tip_y = 184.0
        
        for tmp2 in range(1,tips_kazu):
            if config.developer == True:
                text "%s" % (tips[tmp2][tips_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
#                text "%s" % (tips[tmp2][tips_flg]) xpos (1880.0/1920.0) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not tips[tmp2][tips_flg] == 0:
                textbutton tips[tmp2][tips_file] text_style style.tips_btn xpos (204.0/1920.0) ypos (tip_y/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_tips", tmp2), tips_chk("tips",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
#                textbutton "Halabalough" style style.button_text['tips'] xpos (88.0/1920.0) ypos (tip_y/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_tips", tmp2), SetVariable("tips_page", 1) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.tips_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos (204.0/1920.0) ypos ((tip_y+40.0)/1080.0)
            else:
                pass
            $ tip_y += 90.0
        
    elif r_hyouji == 2:
        
        use grim_text_ep1
        
        add "r_click/tips/caption2.png" at caption
#        imagebutton auto "r_click/tips/tips_%s.png" xpos (720.0/1920.0) ypos (70.0/1080.0) focus_mask True action [ SetVariable("r_hyouji", 1), Play ("se9", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        $ tmp_y = 80.0
        
        for tmp2 in range(1,grim_kazu):
            if config.developer == True:
                text "%s" % (grim[tmp2][grim_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
#                text "%s" % (grim[tmp2][grim_flg]) xpos (1880.0/1920.0) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not grim[tmp2][grim_flg] == 0:
                imagebutton idle grim[tmp2][3] hover grim[tmp2][grim_file] selected_idle grim[tmp2][grim_file] xpos (grim[tmp2][itiran_x]/1920.0) ypos (grim[tmp2][itiran_y]/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_grim", tmp2), tips_chk("grim",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
#                imagebutton auto grim[tmp2][grim_file] xpos (grim[tmp2][itiran_x]/1920.0) ypos (grim[tmp2][itiran_y]/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_grim", tmp2), SetVariable("grim_page", 1) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.grim_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos ((grim[tmp2][itiran_x]+60.0)/1920.0) ypos ((grim[tmp2][itiran_y]+44.0)/1080.0)
            else:
                pass
            
    
screen rmenu_tips_2():
    tag menu
    
    use tips
    
    $ bt_tips_ep2_def()
    
    if r_for_title == 0:
        $ tips_ep2()
    
    if r_hyouji == 1:
        
        use tips_text_ep2
        
        add "r_click/tips/caption.png" at caption
        
        $ tmp_y = 80.0
        $ tip_y = 184.0
        
        for tmp2 in range(1,tips_kazu):
            if config.developer == True:
                text "%s" % (tips[tmp2][tips_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not tips[tmp2][tips_flg] == 0:
                textbutton tips[tmp2][tips_file] text_style style.tips_btn xpos (204.0/1920.0) ypos (tip_y/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_tips", tmp2), tips_chk("tips",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.tips_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos (204.0/1920.0) ypos ((tip_y+40.0)/1080.0)
            else:
                pass
            $ tip_y += 90.0
        
    elif r_hyouji == 2:
        
        use grim_text_ep2
        
        add "r_click/tips/caption2.png" at caption
        
        $ tmp_y = 80.0
        
        for tmp2 in range(1,grim_kazu):
            if config.developer == True:
                text "%s" % (grim[tmp2][grim_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not grim[tmp2][grim_flg] == 0:
                imagebutton idle grim[tmp2][3] hover grim[tmp2][grim_file] selected_idle grim[tmp2][grim_file] xpos (grim[tmp2][itiran_x]/1920.0) ypos (grim[tmp2][itiran_y]/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_grim", tmp2), tips_chk("grim",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.grim_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos ((grim[tmp2][itiran_x]+60.0)/1920.0) ypos ((grim[tmp2][itiran_y]+44.0)/1080.0)
            else:
                pass
            
    
screen rmenu_tips_3():
    tag menu
    
    use tips
    
    $ bt_tips_ep3_def()
    
    if r_for_title == 0:
        $ tips_ep3()
    
    if r_hyouji == 1:
        
        use tips_text_ep3
        
        add "r_click/tips/caption.png" at caption
        
        $ tmp_y = 80.0
        $ tip_y = 184.0
        
        for tmp2 in range(1,tips_kazu):
            if config.developer == True:
                text "%s" % (tips[tmp2][tips_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not tips[tmp2][tips_flg] == 0:
                textbutton tips[tmp2][tips_file] text_style style.tips_btn xpos (204.0/1920.0) ypos (tip_y/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_tips", tmp2), tips_chk("tips",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.tips_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos (204.0/1920.0) ypos ((tip_y+40.0)/1080.0)
            else:
                pass
            $ tip_y += 90.0
        
    elif r_hyouji == 2:
        
        use grim_text_ep3
        
        add "r_click/tips/caption2.png" at caption
        
        $ tmp_y = 80.0
        
        for tmp2 in range(1,grim_kazu):
            if config.developer == True:
                text "%s" % (grim[tmp2][grim_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not grim[tmp2][grim_flg] == 0:
                imagebutton idle grim[tmp2][3] hover grim[tmp2][grim_file] selected_idle grim[tmp2][grim_file] xpos (grim[tmp2][itiran_x]/1920.0) ypos (grim[tmp2][itiran_y]/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_grim", tmp2), tips_chk("grim",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.grim_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos ((grim[tmp2][itiran_x]+60.0)/1920.0) ypos ((grim[tmp2][itiran_y]+44.0)/1080.0)
            else:
                pass
            
    
screen rmenu_tips_4():
    tag menu
    
    use tips
    
    $ bt_tips_ep4_def()
    
    if r_for_title == 0:
        $ tips_ep4()
    
    if r_hyouji == 1:
        
        use tips_text_ep4
        
        add "r_click/tips/caption.png" at caption
        
        $ tmp_y = 80.0
        $ tip_y = 184.0
        
        for tmp2 in range(1,tips_kazu):
            if config.developer == True:
                text "%s" % (tips[tmp2][tips_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not tips[tmp2][tips_flg] == 0:
                textbutton tips[tmp2][tips_file] text_style style.tips_btn xpos (204.0/1920.0) ypos (tip_y/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_tips", tmp2), tips_chk("tips",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.tips_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos (204.0/1920.0) ypos ((tip_y+40.0)/1080.0)
            else:
                pass
            $ tip_y += 90.0
        
    elif r_hyouji == 2:
        
        use grim_text_ep4
        
        add "r_click/tips/caption2.png" at caption
        
        $ tmp_y = 80.0
        
        for tmp2 in range(1,grim_kazu):
            if config.developer == True:
                text "%s" % (grim[tmp2][grim_flg]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
            $ tmp_y += 20.0
            if not grim[tmp2][grim_flg] == 0:
                imagebutton idle grim[tmp2][3] hover grim[tmp2][grim_file] selected_idle grim[tmp2][grim_file] xpos (grim[tmp2][itiran_x]/1920.0) ypos (grim[tmp2][itiran_y]/1080.0) focus_mask None action [ Play ("se9", se1010), SetVariable("r_hyouji_grim", tmp2), tips_chk("grim",scenario_Number,tmp2) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
                if persistent.grim_new[scenario_Number][tmp2] == 1:
                    add "r_click/tips/new.png" xpos ((grim[tmp2][itiran_x]+60.0)/1920.0) ypos ((grim[tmp2][itiran_y]+44.0)/1080.0)
            else:
                pass
            
    
label rmenu_chars():
    $ r_for_title = 1
    $ _game_menu_screen = None
    $ r_hyouji_cha = r_but
    $ r_enj_enj = 1
    $ side_flg = 1
    $ play_scene = 0
    
    python:
        for tmp in range(1,19):
            r[tmp][r_ishou] = 1
            r[tmp][condition] = 1
            for tmp2 in range(1,5):
                for tmp3 in range(1,5):
                    if not persistent.cha_new[tmp2][1][tmp][tmp3]:
                        persistent.cha_new[tmp2][1][tmp][tmp3] = 1
        
    if scenario_Number == 1:
        if persistent.UMINEKOEND_CHARS1_flg == 1:
            $ persistent.UMINEKOEND_CHARS1_flg = 0
        $ r_hyouji_cha = 0
        $ r_hyouji_cha_ma = ma_bea
        $ r_hana = h_hana
        $ r_cha_back = cha_back
        $ ma_cha_back = cha_back3
        $ cha_kazu_x = 3
        python:
            r[r_bea][condition] = 1
            r[r_ber][condition] = -1
            r_ma[ma_bea][condition] = 1
            r_ma[ma_ber][condition] = 1
            r_ma[ma_bea][r_ishou] = 1
            r_ma[ma_ber][r_ishou] = 1
            for tmp3 in range(1,3):
                if not persistent.cha_new[1][1][r_bea][tmp3]:
                    persistent.cha_new[1][1][r_bea][tmp3] = 1
            for tmp2 in range(1,3):
                for tmp3 in range(1,3):
                    if not persistent.cha_new[1][2][tmp2][tmp3]:
                        persistent.cha_new[1][2][tmp2][tmp3] = 1
        $ renpy.show_screen('rmenu_main_ep1')
        $ ui.interact()
        jump _noisy_return
    elif scenario_Number == 2:
        if persistent.UMINEKOEND_CHARS2_flg == 1:
            $ persistent.UMINEKOEND_CHARS2_flg = 0
        $ r_hyouji_cha_ma = ma_bea
        $ r_cha_back = cha_back
        $ ma_cha_back = cha_back_ma
        $ cha_kazu_x = cha_kazu_ep2_2
        python:
            r[r_bea][condition] = 1
            r[r_ber][condition] = -1
            r[r_lam][condition] = -1
            for tmp in range(1,cha_kazu_ep2_2):
                r_ma[tmp][condition] = 1
                r_ma[tmp][r_ishou] = 1
            
            for tmp in range(1,cha_kazu_ep2):
                r[tmp][r_ishou] = 1                   ## used for change button
            
            for tmp3 in range(1,4):
                if not persistent.cha_new[2][1][r_bea][tmp3]:
                    persistent.cha_new[2][1][r_bea][tmp3] = 1
            for tmp2 in range(1,cha_kazu_ep2_2):
                if not persistent.cha_new[2][2][tmp2][1]:
                    persistent.cha_new[2][2][tmp2][1] = 1
        $ renpy.show_screen('rmenu_main_ep2')
        $ ui.interact()
        jump _noisy_return
    elif scenario_Number == 3:
        if persistent.UMINEKOEND_CHARS3_flg == 1:
            $ persistent.UMINEKOEND_CHARS3_flg = 0
        $ r_hyouji_cha = r_enj
        $ r_hyouji_cha_ma = ma3_enj
        $ r_cha_back = cha_back4
        $ ma_cha_back = cha_back15
        $ cha_kazu_x = cha_kazu_ep3_2
        python:
            for tmp in range(1,cha_kazu_ep3_2):
                r_ma[tmp][condition] = 1
                r_ma[tmp][r_ishou] = 1
            r[r_bea][condition] = 1
            r[r_ber][condition] = -1
            r[r_lam][condition] = -1
            r[r_enj][condition] = 1
            for tmp3 in range(1,3):
                if not persistent.cha_new[3][1][r_bea][tmp3]:
                    persistent.cha_new[3][1][r_bea][tmp3] = 1
                if not persistent.cha_new[3][1][r_enj][tmp3]:
                    persistent.cha_new[3][1][r_enj][tmp3] = 1
            for tmp2 in range(1,cha_kazu_ep3_2):
                for tmp3 in range(1,3):
                    if not persistent.cha_new[3][2][tmp2][tmp3]:
                        persistent.cha_new[3][2][tmp2][tmp3] = 1
            
            for tmp in range(1,cha_kazu_ep3):
                r[tmp][r_ishou] = 1                   ## used for change button
        $ renpy.show_screen('rmenu_main_ep3')
        $ ui.interact()
        jump _noisy_return
    elif scenario_Number == 4:
        if persistent.UMINEKOEND_CHARS4_flg == 1:
            $ persistent.UMINEKOEND_CHARS4_flg = 0
        $ r_hyouji_cha_ma = ma4_bea
        $ r_hyouji_cha_enj = enj_enj
        $ r_cha_back = cha_back
        $ ma_cha_back = ba4_2_7_2
        $ enj_cha_back = ba4_3_7
        $ cha_kazu_x = cha_kazu_ep4_2
        python:
            for tmp in range(1,cha_kazu_ep4_2):
                r_ma[tmp][condition] = 1
                r_ma[tmp][r_ishou] = 1
            for tmp in range(1,cha_kazu_ep4_3):
                r_enj_ma[tmp][condition] = 1
                r_enj_ma[tmp][r_ishou] = 1
            r[r_bea][condition] = 1
            r[r_ber][condition] = -1
            r[r_lam][condition] = -1
            r[r_enj][condition] = -1
            r_ma[ma4_s55][condition] = 2
            for tmp in range(1,cha_kazu_ep4):
                r[tmp][r_ishou] = 1
            for tmp3 in range(1,3):
                if not persistent.cha_new[4][1][r_bea][tmp3]:
                    persistent.cha_new[4][1][r_bea][tmp3] = 1
            for tmp2 in range(1,cha_kazu_ep4_2):
                for tmp3 in range(1,3):
                    if not persistent.cha_new[4][2][tmp2][tmp3]:
                        persistent.cha_new[4][2][tmp2][tmp3] = 1
            for tmp2 in range(1,cha_kazu_ep4_3):
                for tmp3 in range(1,3):
                    if not persistent.cha_new[4][3][tmp2][tmp3]:
                        persistent.cha_new[4][3][tmp2][tmp3] = 1
            
        $ renpy.show_screen('rmenu_main_ep4')
        $ ui.interact()
        jump _noisy_return
    return

screen chars():
    
    tag menu
    
    add "r_click/sysmenu/fg.png" yalign 1.0
    
    if r_for_title == 0:                                  ##in-game
        imagebutton idle exit_i hover exit_h xpos (1739.0/1920.0) ypos (997.0/1080.0) focus_mask None action [ Play ("se9", se1100.pick()), SetVariable("rmenu_text", 0), Return(), With(t80) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        key "game_menu" action [Play("se9", se1100.pick()), SetVariable("rmenu_text", 0), Return()]
        use all_pause
        if rmenu_text == 1:
            imagebutton auto "r_click/chars/back_%s.png" xpos (996.0/1920.0) ypos (989.0/1080.0) focus_mask True action [ Play ("se9", se1005), SetVariable("rmenu_text", 0) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
#            vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1200.0/1920.0) ypos (180.0/1080.0)
    elif r_for_title == 1:                                ##title screen
        
        key "game_menu" action NullAction()
        
        use execute_resurrection
        
        if rmenu_text == 0:
            $ ep_x = 1010.0
            $ ep_y = 989.0
            if scenario_Number == 1:
                add btn_char_ep1_h xpos (ep_x/1920.0) ypos (ep_y/1080.0)
            else:
                imagebutton idle btn_char_ep1_i hover btn_char_ep1_h xpos (ep_x/1920.0) ypos (ep_y/1080.0) focus_mask None action [ Play ("se10", se1010), Jump('chars_t1') ] hovered Play ("se20", "sys_se/zyosys0.ogg")
            $ ep_x += 128.0
            if persistent.UMINEKOEND >= 30:
                if scenario_Number == 2:
                    add btn_char_ep2_h xpos (ep_x/1920.0) ypos (ep_y/1080.0)
                else:
                    imagebutton idle btn_char_ep2_i hover btn_char_ep2_h xpos (ep_x/1920.0) ypos (ep_y/1080.0) focus_mask None action [ Play ("se10", se1010), Jump('chars_t2') ] hovered Play ("se20", "sys_se/zyosys0.ogg")
            $ ep_x += 128.0
            if persistent.UMINEKOEND >= 40:
                if scenario_Number == 3:
                    add btn_char_ep3_h xpos (ep_x/1920.0) ypos (ep_y/1080.0)
                else:
                    imagebutton idle btn_char_ep3_i hover btn_char_ep3_h xpos (ep_x/1920.0) ypos (ep_y/1080.0) focus_mask None action [ Play ("se10", se1010), Jump('chars_t3') ] hovered Play ("se20", "sys_se/zyosys0.ogg")
            $ ep_x += 128.0
            if persistent.UMINEKOEND >= 50:
                if scenario_Number == 4:
                    add btn_char_ep4_h xpos (ep_x/1920.0) ypos (ep_y/1080.0)
                else:
                    imagebutton idle btn_char_ep4_i hover btn_char_ep4_h xpos (ep_x/1920.0) ypos (ep_y/1080.0) focus_mask None action [ Play ("se10", se1010), Jump('chars_t4') ] hovered Play ("se20", "sys_se/zyosys0.ogg")
            
        elif rmenu_text == 1:
            imagebutton auto "r_click/chars/back_%s.png" xpos (996.0/1920.0) ypos (989.0/1080.0) focus_mask True action [ Play ("se9", se1005), SetVariable("rmenu_text", 0) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
#            vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
        imagebutton idle exit_i hover exit_h xpos (1739.0/1920.0) ypos (997.0/1080.0) focus_mask None action [ SetVariable("r_for_title", 0), SetVariable("rmenu_text", 0), Play ("se9", "sys_se/zyosys3.ogg"), MainMenu(confirm=False) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        if scenario_Number == 2 and r[r_geo][condition] == 1 and r_hyouji_cha == r_geo and r_hyouji_side == 0:
            imagebutton idle btn_char_change_i hover btn_char_change_h xpos (636.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ Play ("se9", se1001), r_ishou_lsp() ] #hovered Play ("se20", "sys_se/zyosys0.ogg")
        if scenario_Number == 2 and r[r_sha][condition] == 1 and r_hyouji_cha == r_sha and r_hyouji_side == 0:
            imagebutton idle btn_char_change_i hover btn_char_change_h xpos (636.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ Play ("se9", se1001), r_ishou_lsp() ] #hovered Play ("se20", "sys_se/zyosys0.ogg")
        if scenario_Number == 2 and r[r_kan][condition] == 1 and r_hyouji_cha == r_kan and r_hyouji_side == 0:
            imagebutton idle btn_char_change_i hover btn_char_change_h xpos (636.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ Play ("se9", se1001), r_ishou_lsp() ] #hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        if scenario_Number == 3 and r_hyouji_cha_ma == ma3_ev2 and r_hyouji_side == 1:
            imagebutton idle btn_char_change_i hover btn_char_change_h xpos (636.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ Play ("se9", se1001), r_ishou2_lsp() ] #hovered Play ("se20", "sys_se/zyosys0.ogg")
        
        if scenario_Number == 4 and r_hyouji_cha_enj == enj_enj and r_hyouji_side == 2:
            imagebutton idle btn_char_change_i hover btn_char_change_h xpos (636.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ Play ("se9", se1001), r_ishou3_lsp() ] #hovered Play ("se20", "sys_se/zyosys0.ogg")
    
    
    
    
    
    
    add "r_click/chars/caption.png" at caption
#    add "r_click/chars/left.png" at chars_back
#    add "r_click/chars/right.png" at chars_text_page
#    add r_hana xpos 1164 ypos 205
#    add r_cha_back at chars_back
    
    if config.developer == True:
        text "Debug:" xanchor 1.0 xpos (config.screen_width - 15) ypos (105.0/1080.0)
        text "r_hyouji_cha %s" % (r_hyouji_cha) xanchor 1.0 xpos (config.screen_width - 15) ypos (30.0/1080.0)
        text "r_hyouji_cha_ma %s" % (r_hyouji_cha_ma) xanchor 1.0 xpos (config.screen_width - 15) ypos (55.0/1080.0)
        text "r_hyouji_cha_enj %s" % (r_hyouji_cha_enj) xanchor 1.0 xpos (config.screen_width - 15) ypos (80.0/1080.0)
    
    
screen rmenu_main_ep1():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS1_flg == 1:
#            $ persistent.UMINEKOEND_CHARS1_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep1_def()
    
    if not r_for_title == 1:
        $ chars_ep1()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        if r_for_title == 1:
            add btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0)
            imagebutton idle btn_char_side_1_i hover btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep1_2'), Hide('rmenu_main_ep1'), Hide('m_glow'), SetVariable("r_hyouji_side", 1), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        use r_cha_botann_ep5        ## intentional
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep1_text
    
    add r_hana at hana
    use r_cha_hyouji_ep1
    
    use chars
    
screen rmenu_main_ep1_2():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS1_flg == 1:
#            $ persistent.UMINEKOEND_CHARS1_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep1_def()
    
    if not r_for_title == 1:
        $ chars_ep1()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        imagebutton idle btn_char_side_0_i hover btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep1'), Hide('rmenu_main_ep1_2'), Hide('m_glow'), SetVariable("r_hyouji_side", 0), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        add btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0)
        use r_cha_botann_ep5_2
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep1_2_text
    
    add w_hana at hana
    use r_cha_hyouji_ep1_2
    
    use chars
    
screen rmenu_main_ep2():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS2_flg == 1:
#            $ persistent.UMINEKOEND_CHARS2_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep2_def()
    
    if not r_for_title == 1:
        $ chars_ep2()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        if r_for_title == 1:
            add btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0)
            imagebutton idle btn_char_side_1_i hover btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep2_2'), Hide('rmenu_main_ep2'), Hide('m_glow'), SetVariable("r_hyouji_side", 1), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        use r_cha_botann_ep5        ## intentional
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep2_text
    
    add h_hana at hana
    use r_cha_hyouji_ep2
    
    use chars
    
screen rmenu_main_ep2_2():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS2_flg == 1:
#            $ persistent.UMINEKOEND_CHARS2_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep2_def()
    
    if not r_for_title == 1:
        $ chars_ep2()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        if not r_u_tea_flg == 1:
            imagebutton idle btn_char_side_0_i hover btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep2'), Hide('rmenu_main_ep2_2'), Hide('m_glow'), SetVariable("r_hyouji_side", 0), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
            add btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0)
        use r_cha_botann_ep5_2
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep2_2_text
    
    add w_hana at hana
    use r_cha_hyouji_ep2_2
    
    use chars
    
screen rmenu_main_ep3():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS3_flg == 1:
#            $ persistent.UMINEKOEND_CHARS3_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep3_def()
    
    if not r_for_title == 1:
        $ chars_ep3()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        add btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0)
        imagebutton idle btn_char_side_1_i hover btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep3_2'), Hide('rmenu_main_ep3'), Hide('m_glow'), SetVariable("r_hyouji_side", 1), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        use r_cha_botann_ep5        ## intentional
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep3_text
    
    add h_hana at hana
    use r_cha_hyouji_ep3
    
    use chars
    
screen rmenu_main_ep3_2():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS3_flg == 1:
#            $ persistent.UMINEKOEND_CHARS3_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep3_def()
    
    if not r_for_title == 1:
        $ chars_ep3()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        imagebutton idle btn_char_side_0_i hover btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep3'), Hide('rmenu_main_ep3_2'), Hide('m_glow'), SetVariable("r_hyouji_side", 0), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        add btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0)
        use r_cha_botann_ep5_2
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep3_2_text
    
    add w_hana at hana
    use r_cha_hyouji_ep3_2
    
    use chars
    
screen rmenu_main_ep4():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS4_flg == 1:
#            $ persistent.UMINEKOEND_CHARS4_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep4_def()
    
    if not r_for_title == 1:
        $ chars_ep4()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        add btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0)
        imagebutton idle btn_char_side_1_i hover btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4_2'), Hide('rmenu_main_ep4'), Hide('m_glow'), SetVariable("r_hyouji_side", 1), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        if r_enj_enj == 1:
            imagebutton idle btn_char_side_2_i hover btn_char_side_2_h xpos (636.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4_3'), Hide('rmenu_main_ep4'), Hide('m_glow'), SetVariable("r_hyouji_side", 2), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        use r_cha_botann_ep5        ## intentional
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep4_text
    
    add h_hana at hana
    use r_cha_hyouji_ep4
    
    use chars
    
screen rmenu_main_ep4_2():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS4_flg == 1:
#            $ persistent.UMINEKOEND_CHARS4_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep4_def()
    
    if not r_for_title == 1:
        $ chars_ep4()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        if not m_temp1:
            imagebutton idle btn_char_side_0_i hover btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4'), Hide('rmenu_main_ep4_2'), Hide('m_glow'), SetVariable("r_hyouji_side", 0), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        add btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0)
        if not r_for_title == 1:
            if r_enj_enj == 1:
                if not m_temp1:
                    imagebutton idle btn_char_side_2_i hover btn_char_side_2_h xpos (636.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4_3'), Hide('rmenu_main_ep4_2'), Hide('m_glow'), SetVariable("r_hyouji_side", 2), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        else:
            imagebutton idle btn_char_side_2_i hover btn_char_side_2_h xpos (636.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4_3'), Hide('rmenu_main_ep4_2'), Hide('m_glow'), SetVariable("r_hyouji_side", 2), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        use r_cha_botann_ep5_2
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep4_2_text
    
    add w_hana at hana
    use r_cha_hyouji_ep4_2
    
    use chars
    
screen rmenu_main_ep4_3():
    
    tag menu
    
    if r_for_title == 1:
        
#        if persistent.UMINEKOEND_CHARS4_flg == 1:
#            $ persistent.UMINEKOEND_CHARS4_flg = 0
        use title_background
    add "background/efe/black.png" alpha (150.0/255.0)
    
    $ bt_ep4_def()
    
    if not r_for_title == 1:
        $ chars_ep4()
    
    
#    add "r_click/chars/left.png" at chars_back
#    add r_cha_back at chars_back
    
    
    if rmenu_text == 0:
        add "r_click/chars/left.png" at chars_back
        imagebutton idle btn_char_side_0_i hover btn_char_side_0_h xpos (196.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4'), Hide('rmenu_main_ep4_3'), Hide('m_glow'), SetVariable("r_hyouji_side", 0), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        imagebutton idle btn_char_side_1_i hover btn_char_side_1_h xpos (426.0/1920.0) ypos (874.0/1080.0) focus_mask None action [ Show('rmenu_main_ep4_2'), Hide('rmenu_main_ep4_3'), Hide('m_glow'), SetVariable("r_hyouji_side", 1), Play ("se10", se1010), With(t22) ] hovered Play ("se20", "sys_se/zyosys0.ogg")
        add btn_char_side_2_h xpos (636.0/1920.0) ypos (874.0/1080.0)
        use r_cha_botann_ep4_3
    else:
        add "r_click/chars/right.png" at chars_back
        use r_hyouji_cha_ep4_3_text
    
    add f_hana at hana
    use r_cha_hyouji_ep4_3
    
    use chars
    
screen r_cha_botann_ep5():
    
    $ tmp_y = 130.0
    
    add r_cha_back at chars_back
    
    for tmp2 in range(1,19):
        if config.developer == True:
            text "%s" % (r[tmp2][condition]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
        $ tmp_y += 20.0
        if not r[tmp2][condition] == -1:
            if not r[tmp2][condition] == 0:
                if r_for_title == 1:
                    imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r[tmp2][itiran_x]/1920.0) ypos (r[tmp2][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,1,tmp2,r[tmp2][condition],r[tmp2][condition_end]), Hide("m_glow") ] alternate execresur_alt() hovered [ Play("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha", tmp2), Show("m_glow",m_btn_x=(r[tmp2][itiran_x]/1920.0),m_btn_y=(r[tmp2][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
                else:
                    imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r[tmp2][itiran_x]/1920.0) ypos (r[tmp2][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,1,tmp2,r[tmp2][condition],r[tmp2][condition_end]), Hide("m_glow") ] hovered [ Play("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha", tmp2), Show("m_glow",m_btn_x=(r[tmp2][itiran_x]/1920.0),m_btn_y=(r[tmp2][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
                add r[tmp2][r[tmp2][condition]] xpos (r[tmp2][itiran_x]/1920.0) ypos (r[tmp2][itiran_y]/1080.0)
                if persistent.cha_new[scenario_Number][1][tmp2][r[tmp2][condition]] == 1:
                    add "r_click/chars/new.png" xpos ((r[tmp2][itiran_x] + 96.0)/1920.0) ypos ((r[tmp2][itiran_y] + 108.0)/1080.0) anchor (1.0,1.0)
            else:
                add "r_click/chars/btn/non.png" xpos (r[tmp2][itiran_x]/1920.0) ypos (r[tmp2][itiran_y]/1080.0)
                #$ tmp2 +=1
    
    if not r[r_bea][condition] <= 0:
        imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r[r_bea][itiran_x]/1920.0) ypos (r[r_bea][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,1,r_bea,r[r_bea][condition],r[r_bea][condition_end]), Hide("m_glow") ] hovered [ Play ("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha", r_bea), Show("m_glow",m_btn_x=(r[r_bea][itiran_x]/1920.0),m_btn_y=(r[r_bea][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
        add r[r_bea][r[r_bea][condition]] xpos (r[r_bea][itiran_x]/1920.0) ypos (r[r_bea][itiran_y]/1080.0)
        if persistent.cha_new[scenario_Number][1][r_bea][r[r_bea][condition]] == 1:
            add "r_click/chars/new.png" xpos ((r[r_bea][itiran_x] + 96.0)/1920.0) ypos ((r[r_bea][itiran_y] + 108.0)/1080.0) anchor (1.0,1.0)
    if not r[r_ber][condition] <= 0:
        imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r[r_ber][itiran_x]/1920.0) ypos (r[r_ber][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,1,r_ber,r[r_ber][condition],r[r_ber][condition_end]), Hide("m_glow") ] hovered [ Play ("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha", r_ber), Show("m_glow",m_btn_x=(r[r_ber][itiran_x]/1920.0),m_btn_y=(r[r_ber][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
        add r[r_ber][r[r_ber][condition]] xpos (r[r_ber][itiran_x]/1920.0) ypos (r[r_ber][itiran_y]/1080.0)
        if persistent.cha_new[scenario_Number][1][r_ber][r[r_ber][condition]] == 1:
            add "r_click/chars/new.png" xpos ((r[r_ber][itiran_x] + 96.0)/1920.0) ypos ((r[r_ber][itiran_y] + 108.0)/1080.0) anchor (1.0,1.0)
    if not r[r_enj][condition] <= 0:
        imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r[r_enj][itiran_x]/1920.0) ypos (r[r_enj][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,1,r_enj,r[r_enj][condition],r[r_enj][condition_end]), Hide("m_glow") ] hovered [ Play ("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha", r_enj), Show("m_glow",m_btn_x=(r[r_enj][itiran_x]/1920.0),m_btn_y=(r[r_enj][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
        add r[r_enj][r[r_enj][condition]] xpos (r[r_enj][itiran_x]/1920.0) ypos (r[r_enj][itiran_y]/1080.0)
        if persistent.cha_new[scenario_Number][1][r_enj][r[r_enj][condition]] == 1:
            add "r_click/chars/new.png" xpos ((r[r_enj][itiran_x] + 96.0)/1920.0) ypos ((r[r_enj][itiran_y] + 108.0)/1080.0) anchor (1.0,1.0)
    
    
screen r_cha_botann_ep5_2():
    
    add ma_cha_back at chars_back
    
    $ tmp_y = 130.0
    
    for tmp2 in range(1,cha_kazu_x):
        if config.developer == True:
            text "%s" % (r_ma[tmp2][condition]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
        $ tmp_y += 20.0
        if not r_ma[tmp2][condition] == -1:
            if not r_ma[tmp2][condition] == 0:
                if r_for_title == 1:
                    imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r_ma[tmp2][itiran_x]/1920.0) ypos (r_ma[tmp2][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,2,tmp2,r_ma[tmp2][condition],r_ma[tmp2][condition_end]), Hide("m_glow") ] alternate execresur_alt_ma() hovered [ Play("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha_ma", tmp2), Show("m_glow",m_btn_x=(r_ma[tmp2][itiran_x]/1920.0),m_btn_y=(r_ma[tmp2][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
                else:
                    imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r_ma[tmp2][itiran_x]/1920.0) ypos (r_ma[tmp2][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,2,tmp2,r_ma[tmp2][condition],r_ma[tmp2][condition_end]), Hide("m_glow") ] hovered [ Play("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha_ma", tmp2), Show("m_glow",m_btn_x=(r_ma[tmp2][itiran_x]/1920.0),m_btn_y=(r_ma[tmp2][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
                add r_ma[tmp2][r_ma[tmp2][condition]] xpos (r_ma[tmp2][itiran_x]/1920.0) ypos (r_ma[tmp2][itiran_y]/1080.0)
                if persistent.cha_new[scenario_Number][2][tmp2][r_ma[tmp2][condition]] == 1:
                    add "r_click/chars/new.png" xpos ((r_ma[tmp2][itiran_x] + 96.0)/1920.0) ypos ((r_ma[tmp2][itiran_y] + 108.0)/1080.0) anchor (1.0,1.0)
            else:
                add "r_click/chars/btn/non.png" xpos (r_ma[tmp2][itiran_x]/1920.0) ypos (r_ma[tmp2][itiran_y]/1080.0)
                #$ tmp2 +=1
    
    
    
screen r_cha_botann_ep4_3():
    
    add enj_cha_back at chars_back
    
    $ tmp_y = 130.0
    
    for tmp2 in range(1,cha_kazu_ep4_3):
        if config.developer == True:
            text "%s" % (r_enj_ma[tmp2][condition]) xanchor 1.0 xpos (config.screen_width - 15) ypos (tmp_y/1080.0)
        $ tmp_y += 20.0
        if not r_enj_ma[tmp2][condition] == -1:
            if not r_enj_ma[tmp2][condition] == 0:
                if r_for_title == 1:
                    imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r_enj_ma[tmp2][itiran_x]/1920.0) ypos (r_enj_ma[tmp2][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,3,tmp2,r_enj_ma[tmp2][condition],r_enj_ma[tmp2][condition_end]), Hide("m_glow") ] alternate execresur_alt_ma() hovered [ Play("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha_enj", tmp2), Show("m_glow",m_btn_x=(r_enj_ma[tmp2][itiran_x]/1920.0),m_btn_y=(r_enj_ma[tmp2][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
                    add r_enj_ma[tmp2][r_enj_ma[tmp2][condition]] xpos (r_enj_ma[tmp2][itiran_x]/1920.0) ypos (r_enj_ma[tmp2][itiran_y]/1080.0)
                else:
                    imagebutton idle "r_click/chars/btn/non.png" hover "r_click/chars/btn/non.png" xpos (r_enj_ma[tmp2][itiran_x]/1920.0) ypos (r_enj_ma[tmp2][itiran_y]/1080.0) focus_mask True action [ Play ("se9", se1001), SetVariable("rmenu_text", 1), cha_chk(scenario_Number,3,tmp2,r_enj_ma[tmp2][condition],r_enj_ma[tmp2][condition_end]), Hide("m_glow") ] hovered [ Play("se20", "sys_se/zyosys0.ogg"), SetVariable("r_hyouji_cha_enj", tmp2), Show("m_glow",m_btn_x=(r_enj_ma[tmp2][itiran_x]/1920.0),m_btn_y=(r_enj_ma[tmp2][itiran_y]/1080.0)) ] unhovered Hide("m_glow")
                    add r_enj_ma[tmp2][r_enj_ma[tmp2][condition]] xpos (r_enj_ma[tmp2][itiran_x]/1920.0) ypos (r_enj_ma[tmp2][itiran_y]/1080.0)
                if persistent.cha_new[scenario_Number][3][tmp2][r_enj_ma[tmp2][condition]] == 1:
                    add "r_click/chars/new.png" xpos ((r_enj_ma[tmp2][itiran_x] + 96.0)/1920.0) ypos ((r_enj_ma[tmp2][itiran_y] + 108.0)/1080.0) anchor (1.0,1.0)
            else:
                add "r_click/chars/btn/non.png" xpos (r_enj_ma[tmp2][itiran_x]/1920.0) ypos (r_enj_ma[tmp2][itiran_y]/1080.0)
                #$ tmp2 +=1
    
    
    
label chars_t1:
    
    $ r_cha_back = cha_back
    $ ma_cha_back = cha_back3
    $ cha_kazu_x = 3
        
    python:
        for tmp in range(1,30):
            r[tmp][condition] = -1
            r_ma[tmp][condition] = -1
        
        for tmp3 in range(1,3):
            if not persistent.cha_new[1][1][r_bea][tmp3]:
                persistent.cha_new[1][1][r_bea][tmp3] = 1
        for tmp2 in range(1,3):
            for tmp3 in range(1,3):
                if not persistent.cha_new[1][2][tmp2][tmp3]:
                    persistent.cha_new[1][2][tmp2][tmp3] = 1
        
    if persistent.UMINEKOEND_CHARS1_flg == 1:
        $ persistent.UMINEKOEND_CHARS1_flg = 0
    $ r_hyouji_cha_ma = ma_bea
    $ r_hyouji_cha = 0
    python:
        for tmp in range(1,19):
            r[tmp][r_ishou] = 1
        for tmp in range(1,19):
            r[tmp][condition] = 1
        r[r_bea][r_ishou] = 1
        r[r_bea][condition] = 1
        r_ma[ma_bea][r_ishou] = 1
        r_ma[ma_ber][r_ishou] = 1
        r_ma[ma_bea][condition] = 1
        r_ma[ma_ber][condition] = 1
    if scenario_Number == 2:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep2_2')
            $ renpy.show_screen('rmenu_main_ep1_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep2')
            $ renpy.show_screen('rmenu_main_ep1')
    elif scenario_Number == 3:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep3_2')
            $ renpy.show_screen('rmenu_main_ep1_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep3')
            $ renpy.show_screen('rmenu_main_ep1')
    elif scenario_Number == 4:
        if r_hyouji_side == 2:
            $ renpy.hide_screen('rmenu_main_ep4_3')
            $ renpy.show_screen('rmenu_main_ep1_2')
        elif r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep4_2')
            $ renpy.show_screen('rmenu_main_ep1_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep4')
            $ renpy.show_screen('rmenu_main_ep1')
    $ scenario_Number = 1
    with t22
    $ ui.interact()
    jump _noisy_return
    return

label chars_t2:
    
    $ r_cha_back = cha_back
    $ ma_cha_back = cha_back_ma
    $ cha_kazu_x = cha_kazu_ep2_2
        
    python:
        for tmp in range(1,30):
            r[tmp][condition] = -1
            r_ma[tmp][condition] = -1
        
        for tmp3 in range(1,4):
            if not persistent.cha_new[2][1][r_bea][tmp3]:
                persistent.cha_new[2][1][r_bea][tmp3] = 1
            for tmp2 in range(1,cha_kazu_ep2_2):
                if not persistent.cha_new[2][2][tmp2][tmp3]:
                    persistent.cha_new[2][2][tmp2][tmp3] = 1
        
    if persistent.UMINEKOEND_CHARS2_flg == 1:
        $ persistent.UMINEKOEND_CHARS2_flg = 0
    $ r_hyouji_cha = r_but
    $ r_hyouji_cha_ma = ma_bea
    python:
        for tmp in range(1,19):
            r[tmp][r_ishou] = 1
        for tmp in range(1,19):
            r[tmp][condition] = 1
        r[r_bea][r_ishou] = 1
        r[r_bea][condition] = 1
        for tmp in range(1,cha_kazu_ep2_2):
            r_ma[tmp][r_ishou] = 1
        for tmp in range(1,cha_kazu_ep2_2):
            r_ma[tmp][condition] = 1
    if scenario_Number == 1:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep1_2')
            $ renpy.show_screen('rmenu_main_ep2_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep1')
            $ renpy.show_screen('rmenu_main_ep2')
    elif scenario_Number == 3:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep3_2')
            $ renpy.show_screen('rmenu_main_ep2_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep3')
            $ renpy.show_screen('rmenu_main_ep2')
    elif scenario_Number == 4:
        if r_hyouji_side == 2:
            $ renpy.hide_screen('rmenu_main_ep4_3')
            $ renpy.show_screen('rmenu_main_ep2_2')
        elif r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep4_2')
            $ renpy.show_screen('rmenu_main_ep2_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep4')
            $ renpy.show_screen('rmenu_main_ep2')
    $ scenario_Number = 2
    with t22
    $ ui.interact()
    jump _noisy_return
    return

label chars_t3:
    
    $ r_cha_back = cha_back4
    $ ma_cha_back = cha_back15
    $ cha_kazu_x = cha_kazu_ep3_2
        
    python:
        for tmp in range(1,30):
            r[tmp][condition] = -1
            r_ma[tmp][condition] = -1
        
        for tmp3 in range(1,3):
            if not persistent.cha_new[3][1][r_bea][tmp3]:
                persistent.cha_new[3][1][r_bea][tmp3] = 1
            if not persistent.cha_new[3][1][r_enj][tmp3]:
                persistent.cha_new[3][1][r_enj][tmp3] = 1
            for tmp2 in range(1,cha_kazu_ep3_2):
                if not persistent.cha_new[3][2][tmp2][tmp3]:
                    persistent.cha_new[3][2][tmp2][tmp3] = 1
        
    if persistent.UMINEKOEND_CHARS3_flg == 1:
        $ persistent.UMINEKOEND_CHARS3_flg = 0
    $ r_hyouji_cha = r_enj
    $ r_hyouji_cha_ma = ma3_enj
    python:
        for tmp in range(1,19):
            r[tmp][r_ishou] = 1
        for tmp in range(1,19):
            r[tmp][condition] = 1
        r[r_bea][r_ishou] = 1
        r[r_bea][condition] = 1
        r[r_enj][r_ishou] = 1
        r[r_enj][condition] = 1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][r_ishou] = 1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = 1
    if scenario_Number == 1:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep1_2')
            $ renpy.show_screen('rmenu_main_ep3_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep1')
            $ renpy.show_screen('rmenu_main_ep3')
    elif scenario_Number == 2:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep2_2')
            $ renpy.show_screen('rmenu_main_ep3_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep2')
            $ renpy.show_screen('rmenu_main_ep3')
    elif scenario_Number == 4:
        if r_hyouji_side == 2:
            $ renpy.hide_screen('rmenu_main_ep4_3')
            $ renpy.show_screen('rmenu_main_ep3_2')
        elif r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep4_2')
            $ renpy.show_screen('rmenu_main_ep3_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep4')
            $ renpy.show_screen('rmenu_main_ep3')
    $ scenario_Number = 3
    with t22
    $ ui.interact()
    jump _noisy_return
    return

label chars_t4:
    
    $ r_cha_back = cha_back
    $ ma_cha_back = ba4_2_7_2
    $ enj_cha_back = ba4_3_7
    $ cha_kazu_x = cha_kazu_ep4_2
        
    python:
        for tmp in range(1,30):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep4_2):
            r_ma[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        
        for tmp3 in range(1,3):
            if not persistent.cha_new[4][1][r_bea][tmp3]:
                persistent.cha_new[4][1][r_bea][tmp3] = 1
        for tmp2 in range(1,cha_kazu_ep4_2):
            if not persistent.cha_new[4][2][tmp2][tmp3]:
                persistent.cha_new[4][2][tmp2][tmp3] = 1
        for tmp2 in range(1,cha_kazu_ep4_3):
            if not persistent.cha_new[4][3][tmp2][1]:
               persistent.cha_new[4][3][tmp2][1] = 1
        
    if persistent.UMINEKOEND_CHARS4_flg == 1:
        $ persistent.UMINEKOEND_CHARS4_flg = 0
    $ r_hyouji_cha = r_enj
    $ r_hyouji_cha_ma = ma4_bea
    python:
        for tmp in range(1,19):
            r[tmp][r_ishou] = 1
        for tmp in range(1,19):
            r[tmp][condition] = 1
        r[r_bea][r_ishou] = 1
        r[r_bea][condition] = 1
        for tmp in range(1,cha_kazu_ep4_2):
            r_ma[tmp][r_ishou] = 1
        for tmp in range(1,cha_kazu_ep4_2):
            r_ma[tmp][condition] = 1
    if scenario_Number == 1:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep1_2')
            $ renpy.show_screen('rmenu_main_ep4_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep1')
            $ renpy.show_screen('rmenu_main_ep4')
    elif scenario_Number == 2:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep2_2')
            $ renpy.show_screen('rmenu_main_ep4_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep2')
            $ renpy.show_screen('rmenu_main_ep4')
    elif scenario_Number == 3:
        if r_hyouji_side == 1:
            $ renpy.hide_screen('rmenu_main_ep3_2')
            $ renpy.show_screen('rmenu_main_ep4_2')
        else:
            $ renpy.hide_screen('rmenu_main_ep3')
            $ renpy.show_screen('rmenu_main_ep4')
    $ scenario_Number = 4
    with t22
    $ ui.interact()
    jump _noisy_return
    return



style tips_text:
    size 40
    outlines [(1, "#000000", 0, 0)]
    #drop_shadow (2, 2)
    font "times.ttf"
    color "#ffffff"
    hover_color "#ffffff"
    insensitive_color (255, 255, 255, 255)

style hyperlink_text:
    size 40
    outlines [(1, "#000000", 0, 0)]
    #drop_shadow (2, 2)
    font "times.ttf"
    color "#86bbff"            #0ff in base renpy
    hover_color "#86ffff"      #08f in base renpy
    insensitive_color (255, 255, 255, 255)



screen execute_resurrection():
    
    if not r_hyouji_cha == 0 or not r_hyouji_cha_ma == 0 or not r_hyouji_cha_enj == 0:
        if r_hyouji_side == 0 and r[r_hyouji_cha][condition_end] > 1:
            imagebutton idle btn_char_exec_i hover btn_char_exec_h xpos (196.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ execresur("+",r_hyouji_cha), Play ("se9", se1100.pick()) ] alternate [ execresur0("+"), Play ("se9", se1100.pick()) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
            imagebutton idle btn_char_resur_i hover btn_char_resur_h xpos (396.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ execresur("-",r_hyouji_cha), Play ("se9", se1021), With(t22) ] alternate [ execresur0("-"), Play ("se9", se1023), With(t22) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        elif r_hyouji_side == 1 and r_ma[r_hyouji_cha_ma][condition_end] > 1:
            imagebutton idle btn_char_exec_i hover btn_char_exec_h xpos (196.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ execresur_ma4("+",r_hyouji_cha_ma), Play ("se9", se1100.pick()) ] alternate [ execresur1("+"), Play ("se9", se1100.pick()) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
            imagebutton idle btn_char_resur_i hover btn_char_resur_h xpos (396.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ execresur_ma4("-",r_hyouji_cha_ma), Play ("se9", se1021), With(t22) ] alternate [ execresur1("-"), Play ("se9", se1023), With(t22) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        elif r_hyouji_side == 2 and r_enj_ma[r_hyouji_cha_enj][condition_end] > 1:
            imagebutton idle btn_char_exec_i hover btn_char_exec_h xpos (196.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ execresur_enj("+",r_hyouji_cha_enj), Play ("se9", se1100.pick()) ] alternate [ execresur2("+"), Play ("se9", se1100.pick()) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
            imagebutton idle btn_char_resur_i hover btn_char_resur_h xpos (396.0/1920.0) ypos (989.0/1080.0) focus_mask None action [ execresur_enj("-",r_hyouji_cha_enj), Play ("se9", se1021), With(t22) ] alternate [ execresur2("-"), Play ("se9", se1023), With(t22) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
        
        else:
            imagebutton idle btn_char_exec_i hover btn_char_exec_i xpos (196.0/1920.0) ypos (989.0/1080.0) focus_mask None action Play ("se9", "sys_se/zyosys5.ogg") hovered Play ("se10", "sys_se/zyosys0.ogg")
            imagebutton idle btn_char_resur_i hover btn_char_resur_i xpos (396.0/1920.0) ypos (989.0/1080.0) focus_mask None action Play ("se9", "sys_se/zyosys5.ogg") hovered Play ("se10", "sys_se/zyosys0.ogg")
    
init python:
    
    def bt_tips_ep1_def():
        global tips
        global grim
        global tips_kazu
        global grim_kazu
        
        tips_kazu = 8
        grim_kazu = 12
        
        tips[1][tips_file] = _("Epitaph on the Portrait")
        tips[2][tips_file] = _("The Witch's Letter")
        tips[3][tips_file] = _("The Witch's Letter II")
        tips[4][tips_file] = _("The Witch's Letter III")
        tips[5][tips_file] = _("The Witch's Game Record")
        tips[6][tips_file] = _("Winchester M1894 Sawed off")
        tips[7][tips_file] = _("The Seven Stakes of Purgatory")
    
        grim[1][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,0,160,80))
        grim[2][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,0,160,80))
        grim[3][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,0,160,80))
        grim[4][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,80,160,80))
        grim[5][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,80,160,80))
        grim[6][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,80,160,80))
        grim[7][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,160,160,80))
        grim[8][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,160,160,80))
        grim[9][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,160,160,80))
        grim[10][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,240,160,80))
        grim[11][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,240,160,80))
    
        grim[1][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,0,160,80)), im.matrix.brightness(-0.68))
        grim[2][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,0,160,80)), im.matrix.brightness(-0.68))
        grim[3][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,0,160,80)), im.matrix.brightness(-0.68))
        grim[4][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,80,160,80)), im.matrix.brightness(-0.68))
        grim[5][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,80,160,80)), im.matrix.brightness(-0.68))
        grim[6][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,80,160,80)), im.matrix.brightness(-0.68))
        grim[7][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,160,160,80)), im.matrix.brightness(-0.68))
        grim[8][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,160,160,80)), im.matrix.brightness(-0.68))
        grim[9][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,160,160,80)), im.matrix.brightness(-0.68))
        grim[10][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,240,160,80)), im.matrix.brightness(-0.68))
        grim[11][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,240,160,80)), im.matrix.brightness(-0.68))
    
        grim[1][itiran_x] = grim[4][itiran_x] = grim[7][itiran_x] = grim[10][itiran_x] = grim[13][itiran_x] = 198.0
        grim[2][itiran_x] = grim[5][itiran_x] = grim[8][itiran_x] = grim[11][itiran_x] = grim[14][itiran_x] = 398.0
        grim[3][itiran_x] = grim[6][itiran_x] = grim[9][itiran_x] = grim[12][itiran_x] = 598.0
    
        grim[1][itiran_y] = grim[2][itiran_y] = grim[3][itiran_y] = 188.0
        grim[4][itiran_y] = grim[5][itiran_y] = grim[6][itiran_y] = 288.0
        grim[7][itiran_y] = grim[8][itiran_y] = grim[9][itiran_y] = 388.0
        grim[10][itiran_y] = grim[11][itiran_y] = grim[12][itiran_y] = 488.0
        grim[13][itiran_y] = grim[14][itiran_y] = 588.0
    

    def bt_tips_ep2_def():
        global tips
        global grim
        global tips_kazu
        global grim_kazu
        
        tips_kazu = 8
        grim_kazu = 8
    
        tips[1][tips_file] = _("Epitaph on the Portrait")
        tips[2][tips_file] = _("The Witch's Letter")
        tips[3][tips_file] = _("The Witch's Letter II")
        tips[4][tips_file] = _("The Witch's Letter III")
        tips[5][tips_file] = _("The Witch's Letter IV")
        tips[6][tips_file] = _("The Witch's Game Record")
        tips[7][tips_file] = _("Golden Butterfly Brooch")
    
        grim[1][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,0,160,80))
        grim[2][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,0,160,80))
        grim[3][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,0,160,80))
        grim[4][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,80,160,80))
        grim[5][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,80,160,80))
        grim[6][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,80,160,80))
        grim[7][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,160,160,80))
    
        grim[1][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,0,160,80)), im.matrix.brightness(-0.68))
        grim[2][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,0,160,80)), im.matrix.brightness(-0.68))
        grim[3][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,0,160,80)), im.matrix.brightness(-0.68))
        grim[4][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,80,160,80)), im.matrix.brightness(-0.68))
        grim[5][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,80,160,80)), im.matrix.brightness(-0.68))
        grim[6][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,80,160,80)), im.matrix.brightness(-0.68))
        grim[7][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,160,160,80)), im.matrix.brightness(-0.68))
    
        grim[1][itiran_x] = grim[4][itiran_x] = grim[7][itiran_x] = grim[10][itiran_x] = grim[13][itiran_x] = 198.0
        grim[2][itiran_x] = grim[5][itiran_x] = grim[8][itiran_x] = grim[11][itiran_x] = grim[14][itiran_x] = 398.0
        grim[3][itiran_x] = grim[6][itiran_x] = grim[9][itiran_x] = grim[12][itiran_x] = 598.0
    
        grim[1][itiran_y] = grim[2][itiran_y] = grim[3][itiran_y] = 188.0
        grim[4][itiran_y] = grim[5][itiran_y] = grim[6][itiran_y] = 288.0
        grim[7][itiran_y] = grim[8][itiran_y] = grim[9][itiran_y] = 388.0
        grim[10][itiran_y] = grim[11][itiran_y] = grim[12][itiran_y] = 488.0
        grim[13][itiran_y] = grim[14][itiran_y] = 588.0
    

    def bt_tips_ep3_def():
        global tips
        global grim
        global tips_kazu
        global grim_kazu
        
        tips_kazu = 7
        grim_kazu = 14
    
        tips[1][tips_file] = _("Epitaph on the Portrait")
        tips[2][tips_file] = _("The Witch's Letter")
        tips[3][tips_file] = _("The Witch's Game Record")
        tips[4][tips_file] = _("Chiester Sisters Imperial Guard Corps")
        tips[5][tips_file] = _("The Chiesters' Golden Bow")
        tips[6][tips_file] = _("Regarding the Succession of the Witch")
    
        grim[1][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,0,160,80))
        grim[2][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,0,160,80))
        grim[3][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,0,160,80))
        grim[4][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,80,160,80))
        grim[5][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,80,160,80))
        grim[6][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,80,160,80))
        grim[7][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,160,160,80))
        grim[8][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,160,160,80))
        grim[9][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,160,160,80))
        grim[10][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,240,160,80))
        grim[11][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,240,160,80))
        grim[12][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,240,160,80))
        grim[13][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,320,160,80))
    
        grim[1][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,0,160,80)), im.matrix.brightness(-0.68))
        grim[2][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,0,160,80)), im.matrix.brightness(-0.68))
        grim[3][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,0,160,80)), im.matrix.brightness(-0.68))
        grim[4][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,80,160,80)), im.matrix.brightness(-0.68))
        grim[5][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,80,160,80)), im.matrix.brightness(-0.68))
        grim[6][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,80,160,80)), im.matrix.brightness(-0.68))
        grim[7][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,160,160,80)), im.matrix.brightness(-0.68))
        grim[8][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,160,160,80)), im.matrix.brightness(-0.68))
        grim[9][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,160,160,80)), im.matrix.brightness(-0.68))
        grim[10][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,240,160,80)), im.matrix.brightness(-0.68))
        grim[11][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,240,160,80)), im.matrix.brightness(-0.68))
        grim[12][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,240,160,80)), im.matrix.brightness(-0.68))
        grim[13][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,320,160,80)), im.matrix.brightness(-0.68))
    
        grim[1][itiran_x] = grim[4][itiran_x] = grim[7][itiran_x] = grim[10][itiran_x] = grim[13][itiran_x] = 198.0
        grim[2][itiran_x] = grim[5][itiran_x] = grim[8][itiran_x] = grim[11][itiran_x] = grim[14][itiran_x] = 398.0
        grim[3][itiran_x] = grim[6][itiran_x] = grim[9][itiran_x] = grim[12][itiran_x] = 598.0
    
        grim[1][itiran_y] = grim[2][itiran_y] = grim[3][itiran_y] = 188.0
        grim[4][itiran_y] = grim[5][itiran_y] = grim[6][itiran_y] = 288.0
        grim[7][itiran_y] = grim[8][itiran_y] = grim[9][itiran_y] = 388.0
        grim[10][itiran_y] = grim[11][itiran_y] = grim[12][itiran_y] = 488.0
        grim[13][itiran_y] = grim[14][itiran_y] = 588.0
    

    def bt_tips_ep4_def():
        global tips
        global grim
        global tips_kazu
        global grim_kazu
        
        tips_kazu = 8
        grim_kazu = 13
    
        tips[1][tips_file] = _("Mariage Sorcière")
        tips[2][tips_file] = _("Magical Compendium")
        tips[3][tips_file] = _("Grimoire")
        tips[4][tips_file] = _("Beatrice's Titles")
        tips[5][tips_file] = _("Regarding Witches")
        tips[6][tips_file] = _("Regarding Voyagers")
        tips[7][tips_file] = _("Regarding Creators")
    
        grim[1][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,0,160,80))
        grim[2][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,0,160,80))
        grim[3][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,0,160,80))
        grim[4][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,80,160,80))
        grim[5][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,80,160,80))
        grim[6][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,80,160,80))
        grim[7][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,160,160,80))
        grim[8][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,160,160,80))
        grim[9][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,160,160,80))
        grim[10][grim_file] = im.Crop("r_click/tips/button_grim.png", (0,240,160,80))
        grim[11][grim_file] = im.Crop("r_click/tips/button_grim.png", (160,240,160,80))
        grim[12][grim_file] = im.Crop("r_click/tips/button_grim.png", (320,240,160,80))
    
        grim[1][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,0,160,80)), im.matrix.brightness(-0.68))
        grim[2][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,0,160,80)), im.matrix.brightness(-0.68))
        grim[3][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,0,160,80)), im.matrix.brightness(-0.68))
        grim[4][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,80,160,80)), im.matrix.brightness(-0.68))
        grim[5][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,80,160,80)), im.matrix.brightness(-0.68))
        grim[6][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,80,160,80)), im.matrix.brightness(-0.68))
        grim[7][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,160,160,80)), im.matrix.brightness(-0.68))
        grim[8][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,160,160,80)), im.matrix.brightness(-0.68))
        grim[9][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,160,160,80)), im.matrix.brightness(-0.68))
        grim[10][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (0,240,160,80)), im.matrix.brightness(-0.68))
        grim[11][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (160,240,160,80)), im.matrix.brightness(-0.68))
        grim[12][3] = im.MatrixColor(im.Crop("r_click/tips/button_grim.png", (320,240,160,80)), im.matrix.brightness(-0.68))
    
        grim[1][itiran_x] = grim[4][itiran_x] = grim[7][itiran_x] = grim[10][itiran_x] = grim[13][itiran_x] = 198.0
        grim[2][itiran_x] = grim[5][itiran_x] = grim[8][itiran_x] = grim[11][itiran_x] = grim[14][itiran_x] = 398.0
        grim[3][itiran_x] = grim[6][itiran_x] = grim[9][itiran_x] = grim[12][itiran_x] = 598.0
    
        grim[1][itiran_y] = grim[2][itiran_y] = grim[3][itiran_y] = 188.0
        grim[4][itiran_y] = grim[5][itiran_y] = grim[6][itiran_y] = 288.0
        grim[7][itiran_y] = grim[8][itiran_y] = grim[9][itiran_y] = 388.0
        grim[10][itiran_y] = grim[11][itiran_y] = grim[12][itiran_y] = 488.0
        grim[13][itiran_y] = grim[14][itiran_y] = 588.0
    
    
    
    
    
    def bt_ep1_def():
        global r
        global r_ma
        
        r[r_kin][condition_end] = 3
        r[r_kin][0] = Null()
        r[r_kin][1] = "r_click/chars/btn/kin0.png"
        r[r_kin][2] = im.Grayscale("r_click/chars/btn/kin0.png")
        r[r_kin][3] = im.MatrixColor("r_click/chars/btn/kin0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kla][condition_end] = 2
        r[r_kla][0] = Null()
        r[r_kla][1] = "r_click/chars/btn/kla0.png"
        r[r_kla][2] = im.MatrixColor("r_click/chars/btn/kla0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nat][condition_end] = 2
        r[r_nat][0] = Null()
        r[r_nat][1] = "r_click/chars/btn/nat0.png"
        r[r_nat][2] = im.MatrixColor("r_click/chars/btn/nat0.png", im.matrix.tint(1.0,0,0))
    
        r[r_jes][condition_end] = 2
        r[r_jes][0] = Null()
        r[r_jes][1] = "r_click/chars/btn/jes0.png"
        r[r_jes][2] = im.MatrixColor("r_click/chars/btn/jes0.png", im.matrix.tint(1.0,0,0))
    
        r[r_eva][condition_end] = 2
        r[r_eva][0] = Null()
        r[r_eva][1] = "r_click/chars/btn/eva0.png"
        r[r_eva][2] = im.MatrixColor("r_click/chars/btn/eva0.png", im.matrix.tint(1.0,0,0))
    
        r[r_hid][condition_end] = 2
        r[r_hid][0] = Null()
        r[r_hid][1] = "r_click/chars/btn/hid0.png"
        r[r_hid][2] = im.MatrixColor("r_click/chars/btn/hid0.png", im.matrix.tint(1.0,0,0))
    
        r[r_geo][condition_end] = 2
        r[r_geo][0] = Null()
        r[r_geo][1] = "r_click/chars/btn/geo0.png"
        r[r_geo][2] = im.MatrixColor("r_click/chars/btn/geo0.png", im.matrix.tint(1.0,0,0))
    
        r[r_rud][condition_end] = 2
        r[r_rud][0] = Null()
        r[r_rud][1] = "r_click/chars/btn/rud0.png"
        r[r_rud][2] = im.MatrixColor("r_click/chars/btn/rud0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kir][condition_end] = 2
        r[r_kir][0] = Null()
        r[r_kir][1] = "r_click/chars/btn/kir0.png"
        r[r_kir][2] = im.MatrixColor("r_click/chars/btn/kir0.png", im.matrix.tint(1.0,0,0))
    
        r[r_but][condition_end] = 2
        r[r_but][0] = Null()
        r[r_but][1] = "r_click/chars/btn/but0.png"
        r[r_but][2] = im.MatrixColor("r_click/chars/btn/but0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ros][condition_end] = 2
        r[r_ros][0] = Null()
        r[r_ros][1] = "r_click/chars/btn/ros0.png"
        r[r_ros][2] = im.MatrixColor("r_click/chars/btn/ros0.png", im.matrix.tint(1.0,0,0))
    
        r[r_mar][condition_end] = 2
        r[r_mar][0] = Null()
        r[r_mar][1] = "r_click/chars/btn/mar0.png"
        r[r_mar][2] = im.MatrixColor("r_click/chars/btn/mar0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nan][condition_end] = 2
        r[r_nan][0] = Null()
        r[r_nan][1] = "r_click/chars/btn/nan0.png"
        r[r_nan][2] = im.MatrixColor("r_click/chars/btn/nan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_gen][condition_end] = 2
        r[r_gen][0] = Null()
        r[r_gen][1] = "r_click/chars/btn/gen0.png"
        r[r_gen][2] = im.MatrixColor("r_click/chars/btn/gen0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kum][condition_end] = 2
        r[r_kum][0] = Null()
        r[r_kum][1] = "r_click/chars/btn/kum0.png"
        r[r_kum][2] = im.MatrixColor("r_click/chars/btn/kum0.png", im.matrix.tint(1.0,0,0))
    
        r[r_goh][condition_end] = 2
        r[r_goh][0] = Null()
        r[r_goh][1] = "r_click/chars/btn/goh0.png"
        r[r_goh][2] = im.MatrixColor("r_click/chars/btn/goh0.png", im.matrix.tint(1.0,0,0))
    
        r[r_sha][condition_end] = 2
        r[r_sha][0] = Null()
        r[r_sha][1] = "r_click/chars/btn/sha0.png"
        r[r_sha][2] = im.MatrixColor("r_click/chars/btn/sha0.png", im.matrix.tint(1.0,0,0))
        
        r[r_kan][condition_end] = 2
        r[r_kan][0] = Null()
        r[r_kan][1] = "r_click/chars/btn/kan0.png"
        r[r_kan][2] = im.MatrixColor("r_click/chars/btn/kan0.png", im.matrix.tint(1.0,0,0))
        
        r[r_bea][condition_end] = 2
        r[r_bea][0] = Null()
        r[r_bea][1] = "r_click/chars/btn/bea0.png"
        r[r_bea][2] = im.MatrixColor("r_click/chars/btn/bea0.png", im.matrix.tint(1.0,0,0))
        
        r[r_ber][condition_end] = 2
        r[r_ber][0] = Null()
        r[r_ber][1] = "r_click/chars/btn/ber0.png"
        r[r_ber][2] = im.MatrixColor("r_click/chars/btn/ber0.png", im.matrix.tint(1.0,0,0))
        
        r[r_kin][itiran_x] = r[r_nan][itiran_x] = r[r_gen][itiran_x] = r[r_bea][itiran_x] = r[r_ber][itiran_x] = 276.0
        r[r_kla][itiran_x] = r[r_eva][itiran_x] = r[r_rud][itiran_x] = r[r_ros][itiran_x] = r[r_sha][itiran_x] = 404.0
        r[r_nat][itiran_x] = r[r_hid][itiran_x] = r[r_kir][itiran_x] = r[r_kan][itiran_x] = 532.0
        r[r_jes][itiran_x] = r[r_geo][itiran_x] = r[r_but][itiran_x] = r[r_mar][itiran_x] = r[r_goh][itiran_x] = 660.0
        r[r_kum][itiran_x] = 788.0
        
        r[r_kin][itiran_y] = r[r_kla][itiran_y] = r[r_nat][itiran_y] = r[r_jes][itiran_y] = 180.0
        r[r_bea][itiran_y] = r[r_eva][itiran_y] = r[r_hid][itiran_y] = r[r_geo][itiran_y] = 324.0
        r[r_rud][itiran_y] = r[r_kir][itiran_y] = r[r_but][itiran_y] = r[r_ber][itiran_y] = 468.0
        r[r_nan][itiran_y] = r[r_ros][itiran_y] = r[r_mar][itiran_y] = 612.0
        r[r_gen][itiran_y] = r[r_sha][itiran_y] = r[r_kan][itiran_y] = r[r_goh][itiran_y] = r[r_kum][itiran_y] = 756.0
        
        r_ma[ma_bea][condition_end] = 2
        r_ma[ma_bea][0] = Null()
        r_ma[ma_bea][1] = "r_click/chars/btn/bea0.png"
        r_ma[ma_bea][2] = im.MatrixColor("r_click/chars/btn/bea0.png", im.matrix.tint(1.0,0,0))
        
        r_ma[ma_ber][condition_end] = 2
        r_ma[ma_ber][0] = Null()
        r_ma[ma_ber][1] = "r_click/chars/btn/ber0.png"
        r_ma[ma_ber][2] = im.MatrixColor("r_click/chars/btn/ber0.png", im.matrix.tint(1.0,0,0))
        
        r_ma[ma_bea][itiran_x] = 468.0
        r_ma[ma_ber][itiran_x] = 596.0
        
        r_ma[ma_bea][itiran_y] = r_ma[ma_ber][itiran_y] = 468.0
        
    def bt_ep2_def():
        global r
        global r_ma
        
        r[r_kin][condition_end] = 2
        r[r_kin][0] = Null()
        r[r_kin][1] = "r_click/chars/btn/kin0.png"
        r[r_kin][2] = im.MatrixColor("r_click/chars/btn/kin0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kla][condition_end] = 2
        r[r_kla][0] = Null()
        r[r_kla][1] = "r_click/chars/btn/kla0.png"
        r[r_kla][2] = im.MatrixColor("r_click/chars/btn/kla0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nat][condition_end] = 2
        r[r_nat][0] = Null()
        r[r_nat][1] = "r_click/chars/btn/nat0.png"
        r[r_nat][2] = im.MatrixColor("r_click/chars/btn/nat0.png", im.matrix.tint(1.0,0,0))
    
        r[r_jes][condition_end] = 2
        r[r_jes][0] = Null()
        r[r_jes][1] = "r_click/chars/btn/jes0.png"
        r[r_jes][2] = im.MatrixColor("r_click/chars/btn/jes0.png", im.matrix.tint(1.0,0,0))
    
        r[r_eva][condition_end] = 2
        r[r_eva][0] = Null()
        r[r_eva][1] = "r_click/chars/btn/eva0.png"
        r[r_eva][2] = im.MatrixColor("r_click/chars/btn/eva0.png", im.matrix.tint(1.0,0,0))
    
        r[r_hid][condition_end] = 2
        r[r_hid][0] = Null()
        r[r_hid][1] = "r_click/chars/btn/hid0.png"
        r[r_hid][2] = im.MatrixColor("r_click/chars/btn/hid0.png", im.matrix.tint(1.0,0,0))
    
        r[r_geo][condition_end] = 2
        r[r_geo][0] = Null()
        if r[r_geo][r_ishou] == 2:
            r[r_geo][1] = "r_click/chars/btn/geo1.png"
        else:
            r[r_geo][1] = "r_click/chars/btn/geo0.png"
        r[r_geo][2] = im.MatrixColor("r_click/chars/btn/geo0.png", im.matrix.tint(1.0,0,0))
    
        r[r_rud][condition_end] = 2
        r[r_rud][0] = Null()
        r[r_rud][1] = "r_click/chars/btn/rud0.png"
        r[r_rud][2] = im.MatrixColor("r_click/chars/btn/rud0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kir][condition_end] = 2
        r[r_kir][0] = Null()
        r[r_kir][1] = "r_click/chars/btn/kir0.png"
        r[r_kir][2] = im.MatrixColor("r_click/chars/btn/kir0.png", im.matrix.tint(1.0,0,0))
    
        r[r_but][condition_end] = 2
        r[r_but][0] = Null()
        r[r_but][1] = "r_click/chars/btn/but0.png"
        r[r_but][2] = im.MatrixColor("r_click/chars/btn/but0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ros][condition_end] = 2
        r[r_ros][0] = Null()
        r[r_ros][1] = "r_click/chars/btn/ros0.png"
        r[r_ros][2] = im.MatrixColor("r_click/chars/btn/ros0.png", im.matrix.tint(1.0,0,0))
    
        r[r_mar][condition_end] = 2
        r[r_mar][0] = Null()
        r[r_mar][1] = "r_click/chars/btn/mar0.png"
        r[r_mar][2] = im.MatrixColor("r_click/chars/btn/mar0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nan][condition_end] = 3
        r[r_nan][0] = Null()
        r[r_nan][1] = "r_click/chars/btn/nan0.png"
        r[r_nan][2] = im.MatrixColor("r_click/chars/btn/nan0.png", im.matrix.tint(1.0,0,0))
        r[r_nan][3] = im.MatrixColor("r_click/chars/btn/nan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_gen][condition_end] = 2
        r[r_gen][0] = Null()
        r[r_gen][1] = "r_click/chars/btn/gen0.png"
        r[r_gen][2] = im.MatrixColor("r_click/chars/btn/gen0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kum][condition_end] = 3
        r[r_kum][0] = Null()
        r[r_kum][1] = "r_click/chars/btn/kum0.png"
        r[r_kum][2] = im.MatrixColor("r_click/chars/btn/kum0.png", im.matrix.tint(1.0,0,0))
        r[r_kum][3] = im.MatrixColor("r_click/chars/btn/kum0.png", im.matrix.tint(1.0,0,0))
    
        r[r_goh][condition_end] = 2
        r[r_goh][0] = Null()
        r[r_goh][1] = "r_click/chars/btn/goh0.png"
        r[r_goh][2] = im.MatrixColor("r_click/chars/btn/goh0.png", im.matrix.tint(1.0,0,0))
    
        r[r_sha][condition_end] = 2
        r[r_sha][0] = Null()
        if r[r_sha][r_ishou] == 2:
            r[r_sha][1] = "r_click/chars/btn/sha1.png"
        else:
            r[r_sha][1] = "r_click/chars/btn/sha0.png"
        r[r_sha][2] = im.MatrixColor("r_click/chars/btn/sha0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kan][condition_end] = 3
        r[r_kan][0] = Null()
        if r[r_kan][r_ishou] == 2:
            r[r_kan][1] = "r_click/chars/btn/kan1.png"
        else:
            r[r_kan][1] = "r_click/chars/btn/kan0.png"
        r[r_kan][2] = im.Grayscale("r_click/chars/btn/kan0.png")
        r[r_kan][3] = im.MatrixColor("r_click/chars/btn/kan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_bea][condition_end] = 3
        r[r_bea][0] = Null()
        if r[r_bea][r_ishou] == 2:
            r[r_bea][1] = "r_click/chars/btn/bea1.png"
        else:
            r[r_bea][1] = "r_click/chars/btn/bea0.png"
        r[r_bea][2] = "r_click/chars/btn/bea1.png"
        r[r_bea][3] = im.MatrixColor("r_click/chars/btn/bea0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ber][condition_end] = 2
        r[r_ber][0] = Null()
        r[r_ber][1] = "r_click/chars/btn/ber0.png"
        r[r_ber][2] = im.MatrixColor("r_click/chars/btn/ber0.png", im.matrix.tint(1.0,0,0))
    
        r[r_lam][condition_end] = 1
        r[r_lam][0] = Null()
        r[r_lam][1] = "r_click/chars/btn/lam0.png"
        r[r_lam][2] = im.MatrixColor("r_click/chars/btn/lam0.png", im.matrix.tint(1.0,0,0))
        
        r[r_kin][itiran_x] = r[r_nan][itiran_x] = r[r_gen][itiran_x] = r[r_bea][itiran_x] = r[r_ber][itiran_x] = 276.0
        r[r_kla][itiran_x] = r[r_eva][itiran_x] = r[r_rud][itiran_x] = r[r_ros][itiran_x] = r[r_sha][itiran_x] = 404.0
        r[r_nat][itiran_x] = r[r_hid][itiran_x] = r[r_kir][itiran_x] = r[r_kan][itiran_x] = 532.0
        r[r_jes][itiran_x] = r[r_geo][itiran_x] = r[r_but][itiran_x] = r[r_mar][itiran_x] = r[r_goh][itiran_x] = 660.0
        r[r_kum][itiran_x] = 788.0
        
        r[r_kin][itiran_y] = r[r_kla][itiran_y] = r[r_nat][itiran_y] = r[r_jes][itiran_y] = 180.0
        r[r_bea][itiran_y] = r[r_eva][itiran_y] = r[r_hid][itiran_y] = r[r_geo][itiran_y] = 324.0
        r[r_rud][itiran_y] = r[r_kir][itiran_y] = r[r_but][itiran_y] = r[r_ber][itiran_y] = 468.0
        r[r_nan][itiran_y] = r[r_ros][itiran_y] = r[r_mar][itiran_y] = 612.0
        r[r_gen][itiran_y] = r[r_sha][itiran_y] = r[r_kan][itiran_y] = r[r_goh][itiran_y] = r[r_kum][itiran_y] = 756.0
        
        
#    def bt_ep2_2_def():
        
        r_ma[ma_kin][condition_end] = 1
        r_ma[ma_kin][1] = "r_click/chars/btn/kin0.png"
        
        r_ma[ma_but][condition_end] = 1
        r_ma[ma_but][1] = "r_click/chars/btn/but0.png"
        
        r_ma[ma_mar][condition_end] = 1
        r_ma[ma_mar][1] = "r_click/chars/btn/mar0.png"
    
        r_ma[ma_gen][condition_end] = 1
        r_ma[ma_gen][1] = "r_click/chars/btn/gen0.png"
    
        r_ma[ma_sha][condition_end] = 1
        r_ma[ma_sha][1] = "r_click/chars/btn/sha0.png"
    
        r_ma[ma_kan][condition_end] = 1
        r_ma[ma_kan][1] = "r_click/chars/btn/kan0.png"
    
        r_ma[ma_bea][condition_end] = 1
        r_ma[ma_bea][1] = "r_click/chars/btn/bea0.png"
    
        r_ma[ma_ber][condition_end] = 1
        r_ma[ma_ber][1] = "r_click/chars/btn/ber0.png"
    
        r_ma[ma_lam][condition_end] = 1
        r_ma[ma_lam][1] = "r_click/chars/btn/lam0.png"
    
        r_ma[ma_rg1][condition_end] = 1
        r_ma[ma_rg1][1] = "r_click/chars/btn/rgk0.png"
    
        r_ma[ma_rg2][condition_end] = 1
        r_ma[ma_rg2][1] = "r_click/chars/btn/rgk1.png"
    
        r_ma[ma_rg3][condition_end] = 1
        r_ma[ma_rg3][1] = "r_click/chars/btn/rgk2.png"
    
        r_ma[ma_rg4][condition_end] = 1
        r_ma[ma_rg4][1] = "r_click/chars/btn/rgk3.png"
    
        r_ma[ma_rg5][condition_end] = 1
        r_ma[ma_rg5][1] = "r_click/chars/btn/rgk4.png"
    
        r_ma[ma_rg6][condition_end] = 1
        r_ma[ma_rg6][1] = "r_click/chars/btn/rgk5.png"
    
        r_ma[ma_rg7][condition_end] = 1
        r_ma[ma_rg7][1] = "r_click/chars/btn/rgk6.png"
        
        r_ma[ma_bea][itiran_x] = r_ma[ma_rg1][itiran_x] = r_ma[ma_rg5][itiran_x] = 196.0
        r_ma[ma_ber][itiran_x] = 324.0
        r_ma[ma_lam][itiran_x] = 452.0
        r_ma[ma_kin][itiran_x] = r_ma[ma_gen][itiran_x] = r_ma[ma_sha][itiran_x] = r_ma[ma_kan][itiran_x] = 612.0
        r_ma[ma_but][itiran_x] = 740.0
        r_ma[ma_mar][itiran_x] = 868.0
        r_ma[ma_rg2][itiran_x] = r_ma[ma_rg6][itiran_x] = 292
        r_ma[ma_rg3][itiran_x] = r_ma[ma_rg7][itiran_x] = 388.0
        r_ma[ma_rg4][itiran_x] = 484.0
    
        r_ma[ma_bea][itiran_y] = r_ma[ma_ber][itiran_y] = r_ma[ma_lam][itiran_y] = r_ma[ma_kin][itiran_y] = r_ma[ma_but][itiran_y] = r_ma[ma_mar][itiran_y] = 252.0
        r_ma[ma_rg1][itiran_y] = r_ma[ma_rg2][itiran_y] = r_ma[ma_rg3][itiran_y] = r_ma[ma_rg4][itiran_y] = r_ma[ma_gen][itiran_y] = 396.0
        r_ma[ma_rg5][itiran_y] = r_ma[ma_rg6][itiran_y] = r_ma[ma_rg7][itiran_y] = 504.0
        r_ma[ma_sha][itiran_y] = 540.0
        r_ma[ma_kan][itiran_y] = 684.0
    

    def bt_ep3_def():
        global r
        global r_ma
        
        r[r_kin][condition_end] = 2
        r[r_kin][0] = Null()
        r[r_kin][1] = "r_click/chars/btn/kin0.png"
        r[r_kin][2] = im.MatrixColor("r_click/chars/btn/kin0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kla][condition_end] = 2
        r[r_kla][0] = Null()
        r[r_kla][1] = "r_click/chars/btn/kla0.png"
        r[r_kla][2] = im.MatrixColor("r_click/chars/btn/kla0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nat][condition_end] = 2
        r[r_nat][0] = Null()
        r[r_nat][1] = "r_click/chars/btn/nat0.png"
        r[r_nat][2] = im.MatrixColor("r_click/chars/btn/nat0.png", im.matrix.tint(1.0,0,0))
    
        r[r_jes][condition_end] = 2
        r[r_jes][0] = Null()
        r[r_jes][1] = "r_click/chars/btn/jes0.png"
        r[r_jes][2] = im.MatrixColor("r_click/chars/btn/jes0.png", im.matrix.tint(1.0,0,0))
    
        r[r_eva][condition_end] = 1
        r[r_eva][0] = Null()
        r[r_eva][1] = "r_click/chars/btn/eva0.png"
        r[r_eva][2] = im.MatrixColor("r_click/chars/btn/eva0.png", im.matrix.tint(1.0,0,0))
    
        r[r_hid][condition_end] = 2
        r[r_hid][0] = Null()
        r[r_hid][1] = "r_click/chars/btn/hid0.png"
        r[r_hid][2] = im.MatrixColor("r_click/chars/btn/hid0.png", im.matrix.tint(1.0,0,0))
    
        r[r_geo][condition_end] = 2
        r[r_geo][0] = Null()
        r[r_geo][1] = "r_click/chars/btn/geo0.png"
        r[r_geo][2] = im.MatrixColor("r_click/chars/btn/geo0.png", im.matrix.tint(1.0,0,0))
    
        r[r_rud][condition_end] = 2
        r[r_rud][0] = Null()
        r[r_rud][1] = "r_click/chars/btn/rud0.png"
        r[r_rud][2] = im.MatrixColor("r_click/chars/btn/rud0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kir][condition_end] = 2
        r[r_kir][0] = Null()
        r[r_kir][1] = "r_click/chars/btn/kir0.png"
        r[r_kir][2] = im.MatrixColor("r_click/chars/btn/kir0.png", im.matrix.tint(1.0,0,0))
    
        r[r_but][condition_end] = 2
        r[r_but][0] = Null()
        r[r_but][1] = "r_click/chars/btn/but0.png"
        r[r_but][2] = im.MatrixColor("r_click/chars/btn/but0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ros][condition_end] = 2
        r[r_ros][0] = Null()
        r[r_ros][1] = "r_click/chars/btn/ros0.png"
        r[r_ros][2] = im.MatrixColor("r_click/chars/btn/ros0.png", im.matrix.tint(1.0,0,0))
    
        r[r_mar][condition_end] = 2
        r[r_mar][0] = Null()
        r[r_mar][1] = "r_click/chars/btn/mar0.png"
        r[r_mar][2] = im.MatrixColor("r_click/chars/btn/mar0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nan][condition_end] = 2
        r[r_nan][0] = Null()
        r[r_nan][1] = "r_click/chars/btn/nan0.png"
        r[r_nan][2] = im.MatrixColor("r_click/chars/btn/nan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_gen][condition_end] = 2
        r[r_gen][0] = Null()
        r[r_gen][1] = "r_click/chars/btn/gen0.png"
        r[r_gen][2] = im.MatrixColor("r_click/chars/btn/gen0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kum][condition_end] = 2
        r[r_kum][0] = Null()
        r[r_kum][1] = "r_click/chars/btn/kum0.png"
        r[r_kum][2] = im.MatrixColor("r_click/chars/btn/kum0.png", im.matrix.tint(1.0,0,0))
    
        r[r_goh][condition_end] = 2
        r[r_goh][0] = Null()
        r[r_goh][1] = "r_click/chars/btn/goh0.png"
        r[r_goh][2] = im.MatrixColor("r_click/chars/btn/goh0.png", im.matrix.tint(1.0,0,0))
    
        r[r_sha][condition_end] = 2
        r[r_sha][0] = Null()
        r[r_sha][1] = "r_click/chars/btn/sha0.png"
        r[r_sha][2] = im.MatrixColor("r_click/chars/btn/sha0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kan][condition_end] = 2
        r[r_kan][0] = Null()
        r[r_kan][1] = "r_click/chars/btn/kan0.png"
        r[r_kan][2] = im.MatrixColor("r_click/chars/btn/kan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_bea][condition_end] = 2
        r[r_bea][0] = Null()
        r[r_bea][1] = "r_click/chars/btn/bea0.png"
        r[r_bea][2] = im.MatrixColor("r_click/chars/btn/bea0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ber][condition_end] = 2
        r[r_ber][0] = Null()
        r[r_ber][1] = "r_click/chars/btn/ber0.png"
        r[r_ber][2] = im.MatrixColor("r_click/chars/btn/ber0.png", im.matrix.tint(1.0,0,0))
    
        r[r_lam][condition_end] = 1
        r[r_lam][0] = Null()
        r[r_lam][1] = "r_click/chars/btn/lam0.png"
        r[r_lam][2] = im.MatrixColor("r_click/chars/btn/lam0.png", im.matrix.tint(1.0,0,0))
    
        r[r_enj][condition_end] = 1
        r[r_enj][0] = Null()
        r[r_enj][1] = "r_click/chars/btn/enj0.png"
        
#    def bt_ep3_pos_def():
        r[r_kin][itiran_x] = r[r_nan][itiran_x] = r[r_gen][itiran_x] = r[r_bea][itiran_x] = r[r_ber][itiran_x] = 276.0
        r[r_kla][itiran_x] = r[r_eva][itiran_x] = r[r_rud][itiran_x] = r[r_ros][itiran_x] = r[r_sha][itiran_x] = 404.0
        r[r_nat][itiran_x] = r[r_hid][itiran_x] = r[r_kir][itiran_x] = r[r_kan][itiran_x] = 532.0
        r[r_jes][itiran_x] = r[r_geo][itiran_x] = r[r_but][itiran_x] = r[r_mar][itiran_x] = r[r_goh][itiran_x] = 660.0
        r[r_kum][itiran_x] = r[r_enj][itiran_x] = 788.0
        
        r[r_kin][itiran_y] = r[r_kla][itiran_y] = r[r_nat][itiran_y] = r[r_jes][itiran_y] = 180.0
        r[r_bea][itiran_y] = r[r_eva][itiran_y] = r[r_hid][itiran_y] = r[r_geo][itiran_y] = 324.0
        r[r_rud][itiran_y] = r[r_kir][itiran_y] = r[r_but][itiran_y] = r[r_ber][itiran_y] = r[r_enj][itiran_y] = 468.0
        r[r_nan][itiran_y] = r[r_ros][itiran_y] = r[r_mar][itiran_y] = 612.0
        r[r_gen][itiran_y] = r[r_sha][itiran_y] = r[r_kan][itiran_y] = r[r_goh][itiran_y] = r[r_kum][itiran_y] = 756.0
        
        
        r_ma[ma3_bea][condition_end] = 1
        r_ma[ma3_bea][1] = "r_click/chars/btn/bea0.png"
    
        r_ma[ma3_ber][condition_end] = 1
        r_ma[ma3_ber][1] = "r_click/chars/btn/ber0.png"
    
        r_ma[ma3_lam][condition_end] = 1
        r_ma[ma3_lam][1] = "r_click/chars/btn/lam0.png"
    
        r_ma[ma3_rg1][condition_end] = 1
        r_ma[ma3_rg1][1] = "r_click/chars/btn/rgk0.png"
    
        r_ma[ma3_rg2][condition_end] = 1
        r_ma[ma3_rg2][1] = "r_click/chars/btn/rgk1.png"
    
        r_ma[ma3_rg3][condition_end] = 1
        r_ma[ma3_rg3][1] = "r_click/chars/btn/rgk2.png"
    
        r_ma[ma3_rg4][condition_end] = 1
        r_ma[ma3_rg4][1] = "r_click/chars/btn/rgk3.png"
    
        r_ma[ma3_rg5][condition_end] = 1
        r_ma[ma3_rg5][1] = "r_click/chars/btn/rgk4.png"
    
        r_ma[ma3_rg6][condition_end] = 1
        r_ma[ma3_rg6][1] = "r_click/chars/btn/rgk5.png"
    
        r_ma[ma3_rg7][condition_end] = 1
        r_ma[ma3_rg7][1] = "r_click/chars/btn/rgk6.png"
    
        r_ma[ma3_goa][condition_end] = 1
        r_ma[ma3_goa][1] = "r_click/chars/btn/goa0.png"
    
        r_ma[ma3_wal][condition_end] = 1
        r_ma[ma3_wal][1] = "r_click/chars/btn/wal0.png"
    
        r_ma[ma3_ron][condition_end] = 1
        r_ma[ma3_ron][1] = "r_click/chars/btn/ron0.png"
    
        r_ma[ma3_ev2][condition_end] = 1
        if r_ma[ma3_ev2][r_ishou] == 2:
            r_ma[ma3_ev2][1] = "r_click/chars/btn/evb1.png"
        else:
            r_ma[ma3_ev2][1] = "r_click/chars/btn/evb0.png"
    
        r_ma[ma3_enj][condition_end] = 1
        r_ma[ma3_enj][1] = "r_click/chars/btn/enj0.png"
    
        r_ma[ma3_s41][condition_end] = 1
        r_ma[ma3_s41][1] = "r_click/chars/btn/sie1.png"
        
        r_ma[ma3_s45][condition_end] = 1
        r_ma[ma3_s45][1] = "r_click/chars/btn/sie2.png"
    
#    def bt_ep3_2_pos_def():
        r_ma[ma3_wal][itiran_x] = r_ma[ma3_ber][itiran_x] = 276.0        # base all these on cha_back14 but ma3_enj on cha_back15
        r_ma[ma3_goa][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_lam][itiran_x] = 404.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 532.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 628.0
        r_ma[ma3_s45][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 724.0
        r_ma[ma3_s41][itiran_x] = 756.0
        r_ma[ma3_enj][itiran_x] = 788.0
        
        r_ma[ma3_wal][itiran_y] = r_ma[ma3_bea][itiran_y] = r_ma[ma3_ev2][itiran_y] = r_ma[ma3_enj][itiran_y] = 198.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        r_ma[ma3_lam][itiran_y] = r_ma[ma3_ber][itiran_y] = 738.0
        

    def bt_ep4_def():
        global r
        global r_ma
        global r_enj_ma
        
        r[r_kin][condition_end] = 2
        r[r_kin][0] = Null()
        r[r_kin][1] = "r_click/chars/btn/kin0.png"
        r[r_kin][2] = im.MatrixColor("r_click/chars/btn/kin0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kla][condition_end] = 2
        r[r_kla][0] = Null()
        r[r_kla][1] = "r_click/chars/btn/kla0.png"
        r[r_kla][2] = im.MatrixColor("r_click/chars/btn/kla0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nat][condition_end] = 2
        r[r_nat][0] = Null()
        r[r_nat][1] = "r_click/chars/btn/nat0.png"
        r[r_nat][2] = im.MatrixColor("r_click/chars/btn/nat0.png", im.matrix.tint(1.0,0,0))
    
        r[r_jes][condition_end] = 2
        r[r_jes][0] = Null()
        r[r_jes][1] = "r_click/chars/btn/jes0.png"
        r[r_jes][2] = im.MatrixColor("r_click/chars/btn/jes0.png", im.matrix.tint(1.0,0,0))
    
        r[r_eva][condition_end] = 2
        r[r_eva][0] = Null()
        r[r_eva][1] = "r_click/chars/btn/eva0.png"
        r[r_eva][2] = im.MatrixColor("r_click/chars/btn/eva0.png", im.matrix.tint(1.0,0,0))
    
        r[r_hid][condition_end] = 2
        r[r_hid][0] = Null()
        r[r_hid][1] = "r_click/chars/btn/hid0.png"
        r[r_hid][2] = im.MatrixColor("r_click/chars/btn/hid0.png", im.matrix.tint(1.0,0,0))
    
        r[r_geo][condition_end] = 2
        r[r_geo][0] = Null()
        r[r_geo][1] = "r_click/chars/btn/geo0.png"
        r[r_geo][2] = im.MatrixColor("r_click/chars/btn/geo0.png", im.matrix.tint(1.0,0,0))
    
        r[r_rud][condition_end] = 2
        r[r_rud][0] = Null()
        r[r_rud][1] = "r_click/chars/btn/rud0.png"
        r[r_rud][2] = im.MatrixColor("r_click/chars/btn/rud0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kir][condition_end] = 2
        r[r_kir][0] = Null()
        r[r_kir][1] = "r_click/chars/btn/kir0.png"
        r[r_kir][2] = im.MatrixColor("r_click/chars/btn/kir0.png", im.matrix.tint(1.0,0,0))
    
        r[r_but][condition_end] = 2
        r[r_but][0] = Null()
        r[r_but][1] = "r_click/chars/btn/but0.png"
        r[r_but][2] = im.MatrixColor("r_click/chars/btn/but0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ros][condition_end] = 2
        r[r_ros][0] = Null()
        r[r_ros][1] = "r_click/chars/btn/ros0.png"
        r[r_ros][2] = im.MatrixColor("r_click/chars/btn/ros0.png", im.matrix.tint(1.0,0,0))
    
        r[r_mar][condition_end] = 2
        r[r_mar][0] = Null()
        r[r_mar][1] = "r_click/chars/btn/mar0.png"
        r[r_mar][2] = im.MatrixColor("r_click/chars/btn/mar0.png", im.matrix.tint(1.0,0,0))
    
        r[r_nan][condition_end] = 2
        r[r_nan][0] = Null()
        r[r_nan][1] = "r_click/chars/btn/nan0.png"
        r[r_nan][2] = im.MatrixColor("r_click/chars/btn/nan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_gen][condition_end] = 2
        r[r_gen][0] = Null()
        r[r_gen][1] = "r_click/chars/btn/gen0.png"
        r[r_gen][2] = im.MatrixColor("r_click/chars/btn/gen0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kum][condition_end] = 2
        r[r_kum][0] = Null()
        r[r_kum][1] = "r_click/chars/btn/kum0.png"
        r[r_kum][2] = im.MatrixColor("r_click/chars/btn/kum0.png", im.matrix.tint(1.0,0,0))
    
        r[r_goh][condition_end] = 2
        r[r_goh][0] = Null()
        r[r_goh][1] = "r_click/chars/btn/goh0.png"
        r[r_goh][2] = im.MatrixColor("r_click/chars/btn/goh0.png", im.matrix.tint(1.0,0,0))
    
        r[r_sha][condition_end] = 2
        r[r_sha][0] = Null()
        r[r_sha][1] = "r_click/chars/btn/sha0.png"
        r[r_sha][2] = im.MatrixColor("r_click/chars/btn/sha0.png", im.matrix.tint(1.0,0,0))
    
        r[r_kan][condition_end] = 2
        r[r_kan][0] = Null()
        r[r_kan][1] = "r_click/chars/btn/kan0.png"
        r[r_kan][2] = im.MatrixColor("r_click/chars/btn/kan0.png", im.matrix.tint(1.0,0,0))
    
        r[r_bea][condition_end] = 2
        r[r_bea][0] = Null()
        r[r_bea][1] = "r_click/chars/btn/bea0.png"
        r[r_bea][2] = im.MatrixColor("r_click/chars/btn/bea0.png", im.matrix.tint(1.0,0,0))
    
        r[r_ber][condition_end] = 2
        r[r_ber][0] = Null()
        r[r_ber][1] = "r_click/chars/btn/ber0.png"
        r[r_ber][2] = im.MatrixColor("r_click/chars/btn/ber0.png", im.matrix.tint(1.0,0,0))
    
        r[r_lam][condition_end] = 1
        r[r_lam][0] = Null()
        r[r_lam][1] = "r_click/chars/btn/lam0.png"
        r[r_lam][2] = im.MatrixColor("r_click/chars/btn/lam0.png", im.matrix.tint(1.0,0,0))
    
        r[r_enj][condition_end] = 1
        r[r_enj][0] = Null()
        r[r_enj][1] = "r_click/chars/btn/enj0.png"
    
#    def bt_ep4_pos_def():
        r[r_kin][itiran_x] = r[r_nan][itiran_x] = r[r_gen][itiran_x] = r[r_bea][itiran_x] = r[r_ber][itiran_x] = 276.0
        r[r_kla][itiran_x] = r[r_eva][itiran_x] = r[r_rud][itiran_x] = r[r_ros][itiran_x] = r[r_sha][itiran_x] = 404.0
        r[r_nat][itiran_x] = r[r_hid][itiran_x] = r[r_kir][itiran_x] = r[r_kan][itiran_x] = 532.0
        r[r_jes][itiran_x] = r[r_geo][itiran_x] = r[r_but][itiran_x] = r[r_mar][itiran_x] = r[r_goh][itiran_x] = 660.0
        r[r_kum][itiran_x] = 788.0
        
        r[r_kin][itiran_y] = r[r_kla][itiran_y] = r[r_nat][itiran_y] = r[r_jes][itiran_y] = 180.0
        r[r_bea][itiran_y] = r[r_eva][itiran_y] = r[r_hid][itiran_y] = r[r_geo][itiran_y] = 324.0
        r[r_rud][itiran_y] = r[r_kir][itiran_y] = r[r_but][itiran_y] = r[r_ber][itiran_y] = 468.0
        r[r_nan][itiran_y] = r[r_ros][itiran_y] = r[r_mar][itiran_y] = 612.0
        r[r_gen][itiran_y] = r[r_sha][itiran_y] = r[r_kan][itiran_y] = r[r_goh][itiran_y] = r[r_kum][itiran_y] = 756.0
        

        r_ma[ma4_lam][condition_end] = 1
        r_ma[ma4_lam][1] = "r_click/chars/btn/lam0.png"
    
        r_ma[ma4_ber][condition_end] = 1
        r_ma[ma4_ber][1] = "r_click/chars/btn/ber0.png"
    
        r_ma[ma4_bea][condition_end] = 2
        r_ma[ma4_bea][1] = "r_click/chars/btn/bea0.png"
        r_ma[ma4_bea][2] = "r_click/chars/btn/bea0.png"
    
        r_ma[ma4_mar][condition_end] = 2
        r_ma[ma4_mar][1] = "r_click/chars/btn/mar0.png"
        r_ma[ma4_mar][2] = "r_click/chars/btn/mar1.png"
    
        r_ma[ma4_enj][condition_end] = 1
        r_ma[ma4_enj][1] = "r_click/chars/btn/enj0.png"
    
        r_ma[ma4_kin][condition_end] = 1
        r_ma[ma4_kin][1] = "r_click/chars/btn/kin0.png"
    
        r_ma[ma4_sak][condition_end] = 2
        r_ma[ma4_sak][1] = "r_click/chars/btn/sak0.png"
        r_ma[ma4_sak][2] = im.MatrixColor("r_click/chars/btn/sak0.png", im.matrix.tint(1.0,0,0))
    
        r_ma[ma4_wal][condition_end] = 1
        r_ma[ma4_wal][1] = "r_click/chars/btn/wal0.png"
    
        r_ma[ma4_ron][condition_end] = 1
        r_ma[ma4_ron][1] = "r_click/chars/btn/ron0.png"
    
        r_ma[ma4_gap][condition_end] = 1
        r_ma[ma4_gap][1] = "r_click/chars/btn/gap0.png"
    
        r_ma[ma4_s00][condition_end] = 1
        r_ma[ma4_s00][1] = "r_click/chars/btn/sie0.png"
    
        r_ma[ma4_s41][condition_end] = 1
        r_ma[ma4_s41][1] = "r_click/chars/btn/sie1.png"
    
        r_ma[ma4_s45][condition_end] = 1
        r_ma[ma4_s45][1] = "r_click/chars/btn/sie2.png"
    
        r_ma[ma4_s55][condition_end] = 2
        r_ma[ma4_s55][1] = "r_click/chars/btn/sie3.png"
        r_ma[ma4_s55][2] = im.MatrixColor("r_click/chars/btn/sie3.png", im.matrix.tint(1.0,0,0))
    
        r_ma[ma4_rg1][condition_end] = 1
        r_ma[ma4_rg1][1] = "r_click/chars/btn/rgk0.png"
    
        r_ma[ma4_rg2][condition_end] = 1
        r_ma[ma4_rg2][1] = "r_click/chars/btn/rgk1.png"
    
        r_ma[ma4_rg3][condition_end] = 1
        r_ma[ma4_rg3][1] = "r_click/chars/btn/rgk2.png"
    
        r_ma[ma4_rg4][condition_end] = 1
        r_ma[ma4_rg4][1] = "r_click/chars/btn/rgk3.png"
    
        r_ma[ma4_rg5][condition_end] = 1
        r_ma[ma4_rg5][1] = "r_click/chars/btn/rgk4.png"
    
        r_ma[ma4_rg6][condition_end] = 1
        r_ma[ma4_rg6][1] = "r_click/chars/btn/rgk5.png"
    
        r_ma[ma4_rg7][condition_end] = 1
        r_ma[ma4_rg7][1] = "r_click/chars/btn/rgk6.png"
        
        r_ma[ma4_goa][condition_end] = 1
        r_ma[ma4_goa][1] = "r_click/chars/btn/goa0.png"
    
#    def bt_ep4_2_pos_def():
        r_ma[ma4_wal][itiran_x] = r_ma[ma4_goa][itiran_x] = 180.0
        r_ma[ma4_ron][itiran_x] = r_ma[ma4_rg1][itiran_x] = 308.0
        r_ma[ma4_rg2][itiran_x] = 404.0
        r_ma[ma4_lam][itiran_x] = r_ma[ma4_bea][itiran_x] = r_ma[ma4_kin][itiran_x] = r_ma[ma4_gap][itiran_x] = 436.0
        r_ma[ma4_rg3][itiran_x] = 500.0
        r_ma[ma4_sak][itiran_x] = r_ma[ma4_mar][itiran_x] = r_ma[ma4_s45][itiran_x] = 564.0
        r_ma[ma4_rg4][itiran_x] = 596.0
        r_ma[ma4_s41][itiran_x] = 660.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = r_ma[ma4_rg5][itiran_x] = 692.0
        r_ma[ma4_s00][itiran_x] = 756.0
        r_ma[ma4_rg6][itiran_x] = 788.0
        r_ma[ma4_s55][itiran_x] = 852.0
        r_ma[ma4_rg7][itiran_x] = 884.0
        
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 180.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 324.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 468.0
        r_ma[ma4_wal][itiran_y] = r_ma[ma4_ron][itiran_y] = r_ma[ma4_gap][itiran_y] = r_ma[ma4_s45][itiran_y] = r_ma[ma4_s41][itiran_y] = r_ma[ma4_s00][itiran_y] = r_ma[ma4_s55][itiran_y] = 612.0
        r_ma[ma4_goa][itiran_y] = r_ma[ma4_rg1][itiran_y] = r_ma[ma4_rg2][itiran_y] = r_ma[ma4_rg3][itiran_y] = r_ma[ma4_rg4][itiran_y] = r_ma[ma4_rg5][itiran_y] = r_ma[ma4_rg6][itiran_y] = r_ma[ma4_rg7][itiran_y] = 756.0
        

        r_enj_ma[enj_eva][condition_end] = 1
        r_enj_ma[enj_eva][1] = im.MatrixColor("r_click/chars/btn/eva0.png", im.matrix.tint(1.0,0,0))
    
        r_enj_ma[enj_oko][condition_end] = 1
        r_enj_ma[enj_oko][1] = "r_click/chars/btn/oko0.png"
    
        r_enj_ma[enj_kas][condition_end] = 1
        r_enj_ma[enj_kas][1] = "r_click/chars/btn/kas0.png"
    
        r_enj_ma[enj_enj][condition_end] = 1
        if r_enj_ma[enj_enj][r_ishou] == 2:
            r_enj_ma[enj_enj][1] = "r_click/chars/btn/enj1.png"
        else:
            r_enj_ma[enj_enj][1] = "r_click/chars/btn/enj0.png"
    
        r_enj_ma[enj_ama][condition_end] = 1
        r_enj_ma[enj_ama][1] = "r_click/chars/btn/ama0.png"
    
        r_enj_ma[enj_sak][condition_end] = 1
        r_enj_ma[enj_sak][1] = "r_click/chars/btn/sak0.png"
    
        r_enj_ma[enj_mar][condition_end] = 1
        r_enj_ma[enj_mar][1] = "r_click/chars/btn/mar1.png"
    
        r_enj_ma[enj_rg1][condition_end] = 1
        r_enj_ma[enj_rg1][1] = "r_click/chars/btn/rgk0.png"
    
        r_enj_ma[enj_rg2][condition_end] = 1
        r_enj_ma[enj_rg2][1] = "r_click/chars/btn/rgk1.png"
    
        r_enj_ma[enj_rg3][condition_end] = 1
        r_enj_ma[enj_rg3][1] = "r_click/chars/btn/rgk2.png"
    
        r_enj_ma[enj_rg4][condition_end] = 1
        r_enj_ma[enj_rg4][1] = "r_click/chars/btn/rgk3.png"
    
        r_enj_ma[enj_rg5][condition_end] = 1
        r_enj_ma[enj_rg5][1] = "r_click/chars/btn/rgk4.png"
    
        r_enj_ma[enj_rg6][condition_end] = 1
        r_enj_ma[enj_rg6][1] = "r_click/chars/btn/rgk5.png"
    
        r_enj_ma[enj_rg7][condition_end] = 1
        r_enj_ma[enj_rg7][1] = "r_click/chars/btn/rgk6.png"
    
        r_enj_ma[enj_pro][condition_end] = 1
        r_enj_ma[enj_pro][1] = "r_click/chars/btn/pro0.png"
    
        r_enj_ma[enj_mas][condition_end] = 1
        r_enj_ma[enj_mas][1] = "r_click/chars/btn/mas0.png"
    
        r_enj_ma[enj_sab][condition_end] = 1
        r_enj_ma[enj_sab][1] = "r_click/chars/btn/sab0.png"
    
        r_enj_ma[enj_kwa][condition_end] = 1
        r_enj_ma[enj_kwa][1] = "r_click/chars/btn/kwa0.png"
        
        r_enj_ma[enj_ber][condition_end] = 1
        r_enj_ma[enj_ber][1] = "r_click/chars/btn/ber0.png"
    
#    def bt_ep4_3_pos_def():
        r_enj_ma[enj_ber][itiran_x] = r_enj_ma[enj_mar][itiran_x] = r_enj_ma[enj_pro][itiran_x] = 260.0
        r_enj_ma[enj_kas][itiran_x] = 324.0
        r_enj_ma[enj_sak][itiran_x] = r_enj_ma[enj_mas][itiran_x] = 388.0
        r_enj_ma[enj_rg1][itiran_x] = r_enj_ma[enj_rg5][itiran_x] = r_enj_ma[enj_sab][itiran_x] = 516.0
        r_enj_ma[enj_eva][itiran_x] = r_enj_ma[enj_enj][itiran_x] = 580.0
        r_enj_ma[enj_rg2][itiran_x] = r_enj_ma[enj_rg6][itiran_x] = 612.0
        r_enj_ma[enj_kwa][itiran_x] = 644.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = r_enj_ma[enj_rg3][itiran_x] = r_enj_ma[enj_rg7][itiran_x] = 708.0
        r_enj_ma[enj_rg4][itiran_x] = 804.0
        
        
        r_enj_ma[enj_ber][itiran_y] = r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 198.0
        r_enj_ma[enj_kas][itiran_y] = r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_ama][itiran_y] = 342.0
        r_enj_ma[enj_mar][itiran_y] = r_enj_ma[enj_sak][itiran_y] = r_enj_ma[enj_rg1][itiran_y] = r_enj_ma[enj_rg2][itiran_y] = r_enj_ma[enj_rg3][itiran_y] = r_enj_ma[enj_rg4][itiran_y] = 486.0
        r_enj_ma[enj_rg5][itiran_y] = r_enj_ma[enj_rg6][itiran_y] = r_enj_ma[enj_rg7][itiran_y] = 594.0
        r_enj_ma[enj_pro][itiran_y] = r_enj_ma[enj_mas][itiran_y] = r_enj_ma[enj_sab][itiran_y] = r_enj_ma[enj_kwa][itiran_y] = 738.0
        
    
    def chars_ep1():
        global r
        global r_ma
        global r_cha_back
        global r_hana
        
        if play_scene == 0:
            return
        
        for tmp in range(1,3):
            r_ma[tmp][r_ishou] = 1
            r_ma[tmp][condition] = -1
        for tmp in range(1,19):
            r[tmp][condition] = 1
        r[r_bea][condition] = -1
        r[r_ber][condition] = -1
        r_cha_back = cha_back
        r_hana = h_hana
        
        if play_scene == 10000:
            rmenu_main_ep1_scene_10000()
        elif play_scene == 10010:
            rmenu_main_ep1_scene_10010()
        elif play_scene == 10020:
            rmenu_main_ep1_scene_10020()
        elif play_scene == 10030:
            rmenu_main_ep1_scene_10030()
        elif play_scene == 10040:
            rmenu_main_ep1_scene_10040()
        elif play_scene == 10050:
            rmenu_main_ep1_scene_10050()
        elif play_scene == 10060:
            rmenu_main_ep1_scene_10060()
        elif play_scene == 10070:
            rmenu_main_ep1_scene_10070()
        elif play_scene == 10080:
            rmenu_main_ep1_scene_10080()
        elif play_scene == 10090:
            rmenu_main_ep1_scene_10090()
        elif play_scene == 10100:
            rmenu_main_ep1_scene_10100()
        elif play_scene == 10110:
            rmenu_main_ep1_scene_10110()
        elif play_scene == 10120:
            rmenu_main_ep1_scene_10120()
        elif play_scene == 10130:
            rmenu_main_ep1_scene_10130()
        elif play_scene == 10140:
            rmenu_main_ep1_scene_10140()
        elif play_scene == 10150:
            rmenu_main_ep1_scene_10150()
        elif play_scene == 10160:
            rmenu_main_ep1_scene_10160()
        elif play_scene == 10170:
            rmenu_main_ep1_scene_10170()
        elif play_scene >= 10180 and play_scene < 10200:
            rmenu_main_ep1_scene_10180()
        elif play_scene == 10200:
            rmenu_main_ep1_scene_10200()
        elif play_scene == 10210:
            rmenu_main_ep1_scene_10210()
        elif play_scene == 10220:
            rmenu_main_ep1_scene_10220()
        elif play_scene == 10230:
            rmenu_main_ep1_scene_10230()
        elif play_scene == 10240:
            rmenu_main_ep1_scene_10240()
        elif play_scene == 10250:
            rmenu_main_ep1_scene_10250()
        elif play_scene == 10260:
            rmenu_main_ep1_scene_10260()
        elif play_scene >= 10270 and play_scene < 10280:
            rmenu_main_ep1_scene_10270()
        elif play_scene == 10280:
            rmenu_main_ep1_scene_10280()
        elif play_scene == 10290:
            rmenu_main_ep1_scene_10290()
        elif play_scene == 11000:
            rmenu_main_ep1_scene_11000()
        elif play_scene == 11010:
            rmenu_main_ep1_scene_11010()
        elif play_scene == 12000:
            rmenu_main_ep1_scene_12000()
        elif play_scene == 12010:
            rmenu_main_ep1_scene_12010()
        
        for tmp in range(1,19):
            for y in range(1,r[tmp][condition_end]+1):
                if r[tmp][condition] == y and not persistent.cha_new[1][1][tmp][y]:
                    persistent.cha_new[1][1][tmp][y] = 1
        for tmp in range(1,3):
            for y in range(1,r[tmp][condition_end]+1):
                if r[tmp][condition] == y and not persistent.cha_new[1][2][tmp][y]:
                    persistent.cha_new[1][2][tmp][y] = 1
        
    
    def chars_ep2():
        global r
        global r_ma
#        global r_hyouji_side
        global r_for_title
        global load_title
        global chars_r_click
        global cha_kazu_x
        
        if play_scene == 0:
            return
        
        cha_kazu_x = cha_kazu_ep2_2
        
    #    if play_scene < 30000:             ## what does this do?
    #        pass
        
        if scenario_Number == 2:
            
            for tmp in range(1,cha_kazu_ep2):
                r[tmp][r_ishou] = 1
            for tmp in range(1,cha_kazu_ep2_2):
                r[tmp][r_ishou] = 1
            
            if play_scene == 10:
                rmenu_main_ep2_scene_10()
            elif play_scene == 20:
                rmenu_main_ep2_scene_20()
            elif play_scene == 30:
                rmenu_main_ep2_scene_30()
            elif play_scene == 40:
                rmenu_main_ep2_scene_40()
            elif play_scene == 41:
                rmenu_main_ep2_scene_41()
            elif play_scene == 45:
                rmenu_main_ep2_scene_45()
            elif play_scene == 50:
                rmenu_main_ep2_scene_50()
            elif play_scene == 51:
                rmenu_main_ep2_scene_51()
            elif play_scene == 52:
                rmenu_main_ep2_scene_52()
            elif play_scene == 60:
                rmenu_main_ep2_scene_60()
            elif play_scene == 70:
                rmenu_main_ep2_scene_70()
            elif play_scene == 71:
                rmenu_main_ep2_scene_71()
            elif play_scene == 80:
                rmenu_main_ep2_scene_80()
            elif play_scene == 90:
                rmenu_main_ep2_scene_90()
            elif play_scene == 100:
                rmenu_main_ep2_scene_100()
            elif play_scene == 101:
                rmenu_main_ep2_scene_101()
            elif play_scene == 102:
                rmenu_main_ep2_scene_102()
            elif play_scene == 110:
                rmenu_main_ep2_scene_110()
            elif play_scene == 120:
                rmenu_main_ep2_scene_120()
            elif play_scene == 130:
                rmenu_main_ep2_scene_130()
            elif play_scene == 140:
                rmenu_main_ep2_scene_140()
            elif play_scene == 150:
                rmenu_main_ep2_scene_150()
            elif play_scene == 160:
                rmenu_main_ep2_scene_160()
            elif play_scene == 170:
                rmenu_main_ep2_scene_170()
            elif play_scene == 180:
                rmenu_main_ep2_scene_180()
            elif play_scene == 1010:
                rmenu_main_ep2_scene_1010()
            elif play_scene == 1020:
                rmenu_main_ep2_scene_1020()
            elif play_scene == 2010:
                rmenu_main_ep2_scene_2010()
            elif play_scene == 2020:
                rmenu_main_ep2_scene_2020()
        
        for tmp in range(1,cha_kazu_ep2):
            for y in range(1,r[tmp][condition_end]+1):
                if r[tmp][condition] == y and not persistent.cha_new[2][1][tmp][y]:
                    persistent.cha_new[2][1][tmp][y] = 1
        for tmp in range(1,cha_kazu_ep2_2):
            for y in range(1,r_ma[tmp][condition_end]+1):
                if r_ma[tmp][condition] == y and not persistent.cha_new[2][2][tmp][y]:
                    persistent.cha_new[2][2][tmp][y] = 1
        
    def chars_ep3():
        global r
        global r_ma
        global r_hyouji_side
        global r_for_title
        global load_title
        global chars_r_click
        global cha_kazu_x
        
        if play_scene == 0:
            return
        
        cha_kazu_x = cha_kazu_ep3_2
        
        if scenario_Number == 3:
            
            for tmp in range(1,cha_kazu_ep3):
                r[tmp][r_ishou] = 1
            for tmp in range(1,cha_kazu_ep3_2):
                r[tmp][r_ishou] = 1
            
            if play_scene == 30010:
                rmenu_main_ep3_scene_30010()
            elif play_scene == 30020:
                rmenu_main_ep3_scene_30020()
            elif play_scene == 30021:
                rmenu_main_ep3_scene_30021()
            elif play_scene == 30022:
                rmenu_main_ep3_scene_30022()
            elif play_scene == 30030:
                rmenu_main_ep3_scene_30030()
            elif play_scene == 30031:
                rmenu_main_ep3_scene_30031()
            elif play_scene == 30032:
                rmenu_main_ep3_scene_30032()
            elif play_scene == 30035:
                rmenu_main_ep3_scene_30035()
            elif play_scene == 30040:
                rmenu_main_ep3_scene_30040()
            elif play_scene == 30045:
                rmenu_main_ep3_scene_30045()
            elif play_scene == 30050:
                rmenu_main_ep3_scene_30050()
            elif play_scene == 30060:
                rmenu_main_ep3_scene_30060()
            elif play_scene == 30070:
                rmenu_main_ep3_scene_30070()
            elif play_scene == 30071:
                rmenu_main_ep3_scene_30071()
            elif play_scene == 30080:
                rmenu_main_ep3_scene_30080()
            elif play_scene == 30090:
                rmenu_main_ep3_scene_30090()
            elif play_scene == 30100:
                rmenu_main_ep3_scene_30100()
            elif play_scene == 30110:
                rmenu_main_ep3_scene_30110()
            elif play_scene == 30120:
                rmenu_main_ep3_scene_30120()
            elif play_scene == 30130:
                rmenu_main_ep3_scene_30130()
            elif play_scene == 30140:
                rmenu_main_ep3_scene_30140()
            elif play_scene == 30150:
                rmenu_main_ep3_scene_30150()
            elif play_scene == 30160:
                rmenu_main_ep3_scene_30160()
            elif play_scene == 30170:
                rmenu_main_ep3_scene_30170()
            elif play_scene == 30180:
                rmenu_main_ep3_scene_30180()
            elif play_scene == 30181:
                rmenu_main_ep3_scene_30181()
            elif play_scene == 30190:
                rmenu_main_ep3_scene_30190()
            elif play_scene == 30200:
                rmenu_main_ep3_scene_30200()
            elif play_scene == 30210:
                rmenu_main_ep3_scene_30210()
            elif play_scene == 30220:
                rmenu_main_ep3_scene_30220()
            elif play_scene == 30230:
                rmenu_main_ep3_scene_30230()
            elif play_scene == 30240:
                rmenu_main_ep3_scene_30240()
            elif play_scene == 30250:
                rmenu_main_ep3_scene_30250()
            elif play_scene == 30260:
                rmenu_main_ep3_scene_30260()
            elif play_scene == 30270:
                rmenu_main_ep3_scene_30270()
            elif play_scene == 30280:
                rmenu_main_ep3_scene_30280()
            elif play_scene == 30281:
                rmenu_main_ep3_scene_30281()
            elif play_scene == 30282:
                rmenu_main_ep3_scene_30282()
            elif play_scene == 30283:
                rmenu_main_ep3_scene_30283()
            
            elif play_scene == 30290:
                rmenu_main_ep3_scene_30290()
            elif play_scene == 30300:
                rmenu_main_ep3_scene_30300()
            
            elif play_scene == 31010:
                rmenu_main_ep3_scene_31010()
            elif play_scene == 31011:
                rmenu_main_ep3_scene_31011()
            elif play_scene == 31020:
                rmenu_main_ep3_scene_31020()
            elif play_scene == 31030:
                rmenu_main_ep3_scene_31030()
            
            elif play_scene == 32010:
                rmenu_main_ep3_scene_32010()
            elif play_scene == 32020:
                rmenu_main_ep3_scene_32020()
            elif play_scene == 32030:
                rmenu_main_ep3_scene_32030()
            elif play_scene == 32040:
                rmenu_main_ep3_scene_32040()
            if not play_scene >= 32020:
                r[r_enj][condition] = -1
        
        for tmp in range(1,cha_kazu_ep3):
            for y in range(1,r[tmp][condition_end]+1):
                if r[tmp][condition] == y and not persistent.cha_new[3][1][tmp][y]:
                    persistent.cha_new[3][1][tmp][y] = 1
        for tmp in range(1,cha_kazu_ep3_2):
            for y in range(1,r_ma[tmp][condition_end]+1):
                if r_ma[tmp][condition] == y and not persistent.cha_new[3][2][tmp][y]:
                    persistent.cha_new[3][2][tmp][y] = 1
        
        
    def chars_ep4():
        global r
        global r_ma
        global r_enj_ma
        global r_cha_back
        global ma_cha_back
        global enj_cha_back
        global r_enj_enj
        global r_u_tea_flg
        global cha_kazu_x
        
        if play_scene == 0:
            return
        
        cha_kazu_x = cha_kazu_ep4_2
        
        for tmp in range(1,19):
            r[tmp][condition] = 1
        for tmp in range(19,cha_kazu_ep4):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep4):
            r[tmp][r_ishou] = 1
            
        r_cha_back = cha_back
        
        for tmp in range(1,cha_kazu_ep4_2):
            r_ma[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep4_2):
            r_ma[tmp][r_ishou] = 1
        
        ma_cha_back = "saveload/load_null.png"
        
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][r_ishou] = 1
        
        enj_cha_back = "saveload/load_null.png"
        
        if play_scene < 40030:
            r_enj_enj = 0
        else:
            r_enj_enj = 1
        
        ## 4_1
        
        if play_scene >= 40190 and play_scene <= 40300:
            rmenu_main_ep4_scene_40190()
        if play_scene == 40260:
            rmenu_main_ep4_scene_40260()
        if play_scene >= 40270 and play_scene <= 40330:
            rmenu_main_ep4_scene_40270()
        if play_scene == 40335:
            rmenu_main_ep4_scene_40260()
        if play_scene == 40340:
            rmenu_main_ep4_scene_40260()
        if play_scene == 40350:
            rmenu_main_ep4_scene_40350()
        if play_scene == 40360:
            rmenu_main_ep4_scene_40360()
        if play_scene == 40370:
            rmenu_main_ep4_scene_40370()
        if play_scene == 40380:
            rmenu_main_ep4_scene_40380()
        if play_scene == 40390:
            rmenu_main_ep4_scene_40390()
        if play_scene == 40400:
            rmenu_main_ep4_scene_40400()
        if play_scene == 40410:
            rmenu_main_ep4_scene_40410()
        if play_scene == 40420:
            rmenu_main_ep4_scene_40420()
        if play_scene == 40430:
            rmenu_main_ep4_scene_40430()
        if play_scene == 40440:
            rmenu_main_ep4_scene_40440()
        if play_scene == 40450:
            rmenu_main_ep4_scene_40450()
        
        ## 4_2
        
        if play_scene == 40001:
            rmenu_main_ep4_scene_40001()
        if play_scene == 40005:
            rmenu_main_ep4_scene_40005()
        if play_scene < 40090 and play_scene >= 40010:
            rmenu_main_ep4_scene_40005()
        if play_scene == 40090:
            rmenu_main_ep4_scene_40090()
        if play_scene == 40100:
            rmenu_main_ep4_scene_40100()
        if play_scene >= 40110 and play_scene <= 40140:
            rmenu_main_ep4_scene_40110()
        if play_scene == 40150:
            rmenu_main_ep4_scene_40150()
        if play_scene == 40160:
            rmenu_main_ep4_scene_40160()
        if play_scene == 40170:
            rmenu_main_ep4_scene_40170()
        if play_scene == 40175:
            rmenu_main_ep4_scene_40175()
        if play_scene == 40180:
            rmenu_main_ep4_scene_40180()
        if play_scene == 40190:
            rmenu_main_ep4_scene_40180()
        if play_scene == 40200:
            rmenu_main_ep4_scene_40200()
        if play_scene == 40210:
            rmenu_main_ep4_scene_40210()
        if play_scene >= 40220 and play_scene <= 40270:
            rmenu_main_ep4_scene_40220()
        if play_scene == 40280:
            rmenu_main_ep4_scene_40280()
        if play_scene == 40290:
            rmenu_main_ep4_scene_40290()
        if play_scene == 40300:
            rmenu_main_ep4_scene_40300()
        if play_scene == 40310:
            rmenu_main_ep4_scene_40310()
        if play_scene == 40320:
            rmenu_main_ep4_scene_40320()
        if play_scene >= 40330 and play_scene <= 40440:
            rmenu_main_ep4_scene_40330()
        if play_scene == 40450:
            rmenu_main_ep4_scene_40450()
        
        ## 4_3
        
        if play_scene == 40000:
            rmenu_main_ep4_scene_40000()
        if play_scene > 40000 and play_scene < 40010:
            rmenu_main_ep4_scene_40000()
        if play_scene == 40030:
            rmenu_main_ep4_scene_40030()
        if play_scene == 40040:
            rmenu_main_ep4_scene_40040()
        if play_scene == 40050:
            rmenu_main_ep4_scene_40050()
        if play_scene == 40060:
            rmenu_main_ep4_scene_40060()
        if play_scene == 40070:
            rmenu_main_ep4_scene_40070()
        if play_scene >= 40080 and play_scene <= 40110:
            rmenu_main_ep4_scene_40080()
        if play_scene == 40120:
            rmenu_main_ep4_scene_40120()
        if play_scene == 40130:
            rmenu_main_ep4_scene_40130()
        if play_scene >= 40140 and play_scene <= 40170:
            rmenu_main_ep4_scene_40140()
        if play_scene >= 40175 and play_scene <= 40220:
            rmenu_main_ep4_scene_40175()
        if play_scene == 40230:
            rmenu_main_ep4_scene_40230()
        if play_scene == 40240:
            rmenu_main_ep4_scene_40240()
        if play_scene >= 40250 and play_scene <= 40280:
            rmenu_main_ep4_scene_40250()
        if play_scene == 40290:
            rmenu_main_ep4_scene_40290()
        if play_scene >= 40300 and play_scene <= 40500:
            rmenu_main_ep4_scene_40250()
        if play_scene == 40450:
            r_u_tea_flg = 1
        
        for tmp in range(1,cha_kazu_ep4):
            for y in range(1,r[tmp][condition_end]+1):
                if r[tmp][condition] == y and not persistent.cha_new[4][1][tmp][y]:
                    persistent.cha_new[4][1][tmp][y] = 1
        for tmp in range(1,cha_kazu_ep4_2):
            for y in range(1,r_ma[tmp][condition_end]+1):
                if r_ma[tmp][condition] == y and not persistent.cha_new[4][2][tmp][y]:
                    persistent.cha_new[4][2][tmp][y] = 1
        for tmp in range(1,cha_kazu_ep4_3):
            for y in range(1,r_enj_ma[tmp][condition_end]+1):
                if r_enj_ma[tmp][condition] == y and not persistent.cha_new[4][3][tmp][y]:
                    persistent.cha_new[4][3][tmp][y] = 1
        
        
    

    def rmenu_main_ep1_scene_10000():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        return

    def rmenu_main_ep1_scene_10010():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10020():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10030():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10040():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10050():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10060():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10070():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        r[r_mar][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10080():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        r[r_mar][condition] = 1
        r[r_ros][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10090():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        r[r_mar][condition] = 1
        r[r_ros][condition] = 1
        r[r_jes][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10100():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        r[r_mar][condition] = 1
        r[r_ros][condition] = 1
        r[r_jes][condition] = 1
        r[r_kum][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10110():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        r[r_mar][condition] = 1
        r[r_ros][condition] = 1
        r[r_jes][condition] = 1
        r[r_kum][condition] = 1
        r[r_goh][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10120():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 0
        
        r[r_but][condition] = 1
        r[r_geo][condition] = 1
        r[r_hid][condition] = 1
        r[r_eva][condition] = 1
        r[r_kir][condition] = 1
        r[r_rud][condition] = 1
        r[r_mar][condition] = 1
        r[r_ros][condition] = 1
        r[r_jes][condition] = 1
        r[r_kum][condition] = 1
        r[r_goh][condition] = 1
        r[r_kan][condition] = 1
        
        return

    def rmenu_main_ep1_scene_10130():
        global r
        
        r[r_gen][condition] = 0
        r[r_nat][condition] = 0
        r[r_kin][condition] = 0
        r[r_kla][condition] = 0
        r[r_nan][condition] = 0
        
        return

    def rmenu_main_ep1_scene_10140():
        global r
        
        r[r_nat][condition] = 0
        r[r_kin][condition] = 0
        r[r_kla][condition] = 0
        r[r_nan][condition] = 0
        
        return

    def rmenu_main_ep1_scene_10150():
        global r
        
        r[r_kin][condition] = 0
        r[r_kla][condition] = 0
        r[r_nan][condition] = 0
        
        return

    def rmenu_main_ep1_scene_10160():
        global r
        
        r[r_kla][condition] = 0
        r[r_nan][condition] = 0
        
        return

    def rmenu_main_ep1_scene_10170():
        global r
        
        r[r_nan][condition] = 0
        
        return

    def rmenu_main_ep1_scene_10180():
        global r
        
        return

    def rmenu_main_ep1_scene_10200():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10210():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10220():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        r[r_kin][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10230():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        r[r_kin][condition] = 2
        r[r_eva][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10240():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        r[r_kin][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10250():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        r[r_kin][condition] = 3
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10260():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        r[r_kin][condition] = 3
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_kan][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10270():
        global r
        
        r[r_kla][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_ros][condition] = 2
        r[r_goh][condition] = 2
        r[r_sha][condition] = 2
        r[r_kin][condition] = 3
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_kan][condition] = 2
        
        return

    def rmenu_main_ep1_scene_10280():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 2
        
        r[r_nat][condition] = 1
        r[r_jes][condition] = 1
        r[r_geo][condition] = 1
        r[r_but][condition] = 1
        r[r_mar][condition] = 1
        r[r_kin][condition] = 3
        
        return

    def rmenu_main_ep1_scene_10290():
        global r
        for tmp in range(1,19):
            r[tmp][condition] = 2
        
        r[r_jes][condition] = 1
        r[r_geo][condition] = 1
        r[r_but][condition] = 1
        r[r_mar][condition] = 1
        r[r_kin][condition] = 3
        
        return

    def rmenu_main_ep1_scene_11000():
        global r
        global r_hana
        for tmp in range(1,19):
            r[tmp][condition] = 2
        
        r[r_kin][condition] = 3
        r_hana = w_hana
        
        return

    def rmenu_main_ep1_scene_11010():
        global r
        global r_hana
        for tmp in range(1,19):
            r[tmp][condition] = 2
        
        r[r_kin][condition] = 3
        r[r_bea][condition] = 1
        r_hana = w_hana
        
        return

    def rmenu_main_ep1_scene_12000():
        global r
        global r_cha_back
        global r_hana
        for tmp in range(1,21):
            r[tmp][condition] = -1
        
        r[r_bea][condition] = 1
        r[r_bea][itiran_x] = 532.0
        r[r_bea][itiran_y] = 468.0
        r_cha_back = "saveload/load_null.png"
        r_hana = w_hana
        
        return

    def rmenu_main_ep1_scene_12010():
        global r
        global r_cha_back
        global r_hana
        for tmp in range(1,21):
            r[tmp][condition] = -1
        
        r[r_bea][condition] = 1
        r[r_ber][condition] = 1
        r[r_bea][itiran_x] = 468.0
        r[r_bea][itiran_y] = 468.0
        r[r_ber][itiran_x] = 596.0
        r[r_ber][itiran_y] = 468.0
        r_cha_back = "saveload/load_null.png"
        r_hana = w_hana
        
        return




    def rmenu_main_ep2_scene_10():
        global r
        global r_cha_back
        global r_hyouji_cha
        for tmp in range(1,cha_kazu_ep2):
            r[tmp][condition] = -1
        
        r[r_geo][condition] = r[r_sha][condition] = 1
        r[r_geo][r_ishou] = r[r_sha][r_ishou] = 2
        r[r_geo][itiran_x] = 468.0
        r[r_sha][itiran_x] = 596.0
        r[r_geo][itiran_y] = r[r_sha][itiran_y] = 468.0
        r_hyouji_cha = r_sha
        r_cha_back = "saveload/load_null.png"
        return

    def rmenu_main_ep2_scene_20():
        global r
        global r_cha_back
        for tmp in range(1,19):
            r[tmp][condition] = 1
        for tmp in range(19,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        return

    def rmenu_main_ep2_scene_30():
        global r
        global r_cha_back
        for tmp in range(1,19):
            r[tmp][condition] = 1
        for tmp in range(19,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        return

    def rmenu_main_ep2_scene_40():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 1
        
        return

    def rmenu_main_ep2_scene_41():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 1
        
        return

    def rmenu_main_ep2_scene_45():
        global r
        global r_cha_back
        global r_hyouji_cha
        for tmp in range(1,cha_kazu_ep2):
            r[tmp][condition] = -1
        
        r[r_jes][condition] = 1
        
        r[r_jes][itiran_x] = 580.0
        r[r_jes][itiran_y] = 468.0
        r_hyouji_cha = r_jes
        r_cha_back = "saveload/load_null.png"
        
        return

    def rmenu_main_ep2_scene_46():
        global r
        global r_cha_back
        global r_hyouji_cha
        for tmp in range(1,cha_kazu_ep2):
            r[tmp][condition] = -1
        
        r[r_jes][condition] = 1
        
        r[r_jes][itiran_x] = 580.0
        r[r_jes][itiran_y] = 468.0
        r_hyouji_cha = r_jes
        r_cha_back = "saveload/load_null.png"
        
        return

    def rmenu_main_ep2_scene_50():
        global r
        global r_cha_back
        global r_hyouji_cha
        for tmp in range(1,cha_kazu_ep2):
            r[tmp][condition] = -1
        
        r[r_jes][condition] = 1
        r[r_kan][condition] = 1
        
    #    r[r_jes][r_ishou] = 2
        r[r_kan][r_ishou] = 2
        
        r[r_jes][itiran_x] = 468.0
        r[r_kan][itiran_x] = 596.0
        r[r_jes][itiran_y] = r[r_kan][itiran_y] = 468.0
        r_hyouji_cha = r_jes
        r_cha_back = "saveload/load_null.png"
        
        return

    def rmenu_main_ep2_scene_51():
        global r
        global r_cha_back
        global r_hyouji_cha
        for tmp in range(1,cha_kazu_ep2):
            r[tmp][condition] = -1
        
        r[r_jes][condition] = 1
        r[r_kan][condition] = 1
        
    #    r[r_jes][r_ishou] = 2
        r[r_kan][r_ishou] = 2
        
        r[r_jes][itiran_x] = 468.0
        r[r_kan][itiran_x] = 596.0
        r[r_jes][itiran_y] = r[r_kan][itiran_y] = 468.0
        r_hyouji_cha = r_jes
        r_cha_back = "saveload/load_null.png"
        
        return

    def rmenu_main_ep2_scene_52():
        global r
        global r_cha_back
        global r_hyouji_cha
        for tmp in range(1,cha_kazu_ep2):
            r[tmp][condition] = -1
        
        r[r_jes][condition] = 1
        r[r_kan][condition] = 1
        
    #    r[r_jes][r_ishou] = 2
        r[r_kan][r_ishou] = 2
        
        r[r_jes][itiran_x] = 468.0
        r[r_kan][itiran_x] = 596.0
        r[r_jes][itiran_y] = r[r_kan][itiran_y] = 468.0
        r_hyouji_cha = r_jes
        r_cha_back = "saveload/load_null.png"
        
        return

    def rmenu_main_ep2_scene_60():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        return

    def rmenu_main_ep2_scene_70():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        return

    def rmenu_main_ep2_scene_71():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        return

    def rmenu_main_ep2_scene_80():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        return

    def rmenu_main_ep2_scene_90():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        return

    def rmenu_main_ep2_scene_100():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        return

    def rmenu_main_ep2_scene_101():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        return

    def rmenu_main_ep2_scene_102():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        return

    def rmenu_main_ep2_scene_110():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        return

    def rmenu_main_ep2_scene_120():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 2
        return

    def rmenu_main_ep2_scene_130():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 3
        return

    def rmenu_main_ep2_scene_140():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 3
        r[r_nan][condition] = 2
        r[r_kum][condition] = 2
        return

    def rmenu_main_ep2_scene_150():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 3
        r[r_nan][condition] = 2
        r[r_kum][condition] = 2
        return

    def rmenu_main_ep2_scene_160():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 3
        r[r_nan][condition] = 3
        r[r_kum][condition] = 3
        return

    def rmenu_main_ep2_scene_170():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 3
        r[r_nan][condition] = 3
        r[r_kum][condition] = 3
        r[r_geo][condition] = 2
        r[r_sha][condition] = 2
        r[r_goh][condition] = 2
        return

    def rmenu_main_ep2_scene_180():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_eva][condition] = 2
        r[r_hid][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_jes][condition] = 2
        r[r_kan][condition] = 3
        r[r_nan][condition] = 3
        r[r_kum][condition] = 3
        r[r_geo][condition] = 2
        r[r_sha][condition] = 2
        r[r_goh][condition] = 2
        return

    def rmenu_main_ep2_scene_1010():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 2
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 0
        r[r_but][condition] = 0
        r[r_kan][condition] = 3
        r[r_nan][condition] = 3
        r[r_kum][condition] = 3
        return

    def rmenu_main_ep2_scene_1020():
        global r
        global r_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 2
        for tmp in range(20,22):
            r[tmp][condition] = -1
        r_cha_back = cha_back
        
        r[r_bea][condition] = 1
        r[r_but][condition] = 0
        r[r_kan][condition] = 3
        r[r_nan][condition] = 3
        r[r_kum][condition] = 3
        return

    def rmenu_main_ep2_scene_2010():
        global r_ma
        global ma_cha_back
        global r_hyouji_cha_ma
        for tmp in range(1,cha_kazu_ep2_2):
            r_ma[tmp][condition] = -1
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma_bea][condition] = 1
        r_ma[ma_ber][condition] = 1
        
        r_ma[ma_bea][itiran_x] = 468.0
        r_ma[ma_ber][itiran_x] = 596.0
        r_ma[ma_bea][itiran_y] = r_ma[ma_ber][itiran_y] = 468.0
        r_hyouji_cha_ma = ma_bea
        return

    def rmenu_main_ep2_scene_2020():
        global r_ma
        global ma_cha_back
        global r_hyouji_cha_ma
        for tmp in range(1,cha_kazu_ep2_2):
            r_ma[tmp][condition] = -1
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma_bea][condition] = 1
        r_ma[ma_ber][condition] = 1
        r_ma[ma_lam][condition] = 1
        
        r_ma[ma_bea][itiran_x] = 404.0
        r_ma[ma_ber][itiran_x] = 532.0
        r_ma[ma_lam][itiran_x] = 660.0
        r_ma[ma_bea][itiran_y] = r_ma[ma_ber][itiran_y] = r_ma[ma_lam][itiran_y] = 468.0
        r_hyouji_cha_ma = ma_lam
        return

    def rmenu_main_ep3_scene_30000():
        global r
        global r_ma
        global tips
        global grim
        global ma_cha_back
        global r_cha_back
        for tmp in range(1,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        for tmp in range(1,11):
            tips[tmp][tips_flg] = 0
        for tmp in range(1,15):
            grim[tmp][grim_flg] = 0
        ma_cha_back = "saveload/load_null.png"
        r_cha_back = "saveload/load_null.png"
        return
        
    def rmenu_main_ep3_scene_30010():
        rmenu_main_ep3_scene_30030()
    def rmenu_main_ep3_scene_30020():
        rmenu_main_ep3_scene_30030()
    def rmenu_main_ep3_scene_30030():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,19):
            r[tmp][condition] = 1
        for tmp in range(19,23):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back10
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        
        return

    def rmenu_main_ep3_scene_30021():
        rmenu_main_ep3_scene_30031()
    def rmenu_main_ep3_scene_30031():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,19):
            r[tmp][condition] = 1
        for tmp in range(19,23):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back10
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        
        return

    def rmenu_main_ep3_scene_30022():
        rmenu_main_ep3_scene_30032()
    def rmenu_main_ep3_scene_30032():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,19):
            r[tmp][condition] = 1
        for tmp in range(19,23):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back10
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        
        return

    def rmenu_main_ep3_scene_30035():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back10
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        
        return

    def rmenu_main_ep3_scene_30040():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back10
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        
        return

    def rmenu_main_ep3_scene_30050():
        rmenu_main_ep3_scene_30060()
    def rmenu_main_ep3_scene_30060():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back11
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30070():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back12
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 420.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30071():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back12
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 420.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30080():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back12
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 420.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30090():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back12
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 420.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30100():
        rmenu_main_ep3_scene_30110()
    def rmenu_main_ep3_scene_30110():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back12
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 420.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30120():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30130():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13_2
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_lam][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = r_ma[ma3_lam][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 198.0
        r_ma[ma3_ron][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        r_ma[ma3_lam][itiran_y] = 738.0
        
        return

    def rmenu_main_ep3_scene_30140():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13_2
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_lam][condition] = 1
        r_ma[ma3_ber][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = r_ma[ma3_ber][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = r_ma[ma3_lam][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 198.0
        r_ma[ma3_ron][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        r_ma[ma3_lam][itiran_y] = r_ma[ma3_ber][itiran_y] = 738.0
        
        return

    def rmenu_main_ep3_scene_30150():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30160():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30170():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30180():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30181():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back13
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 308.0
        r_ma[ma3_bea][itiran_x] = 436.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 564.0
        r_ma[ma3_goa][itiran_x] = 340.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 468.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 660.0
        r_ma[ma3_rg4][itiran_x] = 756.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30190():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30200():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30210():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30220():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30230():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30240():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30250():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30260():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30270():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30280():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30281():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30282():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_30283():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_31010():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = "saveload/load_null.png"
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_ber][condition] = 1
        r_ma[ma3_lam][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = 404.0
        r_ma[ma3_ber][itiran_x] = 532.0
        r_ma[ma3_lam][itiran_x] = 660.0
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_ber][itiran_y] = r_ma[ma3_lam][itiran_y] = 468.0
        
        return

    def rmenu_main_ep3_scene_31011():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = "saveload/load_null.png"
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_ber][condition] = 1
        r_ma[ma3_lam][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = 404.0
        r_ma[ma3_ber][itiran_x] = 532.0
        r_ma[ma3_lam][itiran_x] = 660.0
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_ber][itiran_y] = r_ma[ma3_lam][itiran_y] = 468.0
        
        return

    def rmenu_main_ep3_scene_31020():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = "r_click/chars/btn/cha_back.png"
        ma_cha_back = "saveload/load_null.png"
        
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_lam][condition] = 1
        
        r_ma[ma3_bea][itiran_x] = 468.0
        r_ma[ma3_lam][itiran_x] = 596.0
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_lam][itiran_y] = 468.0
        
        return

    def rmenu_main_ep3_scene_32010():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back
        ma_cha_back = cha_back14
        
        r[r_bea][condition] = -1
        r[r_eva][condition] = 1
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_32020():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back4
        ma_cha_back = cha_back14
        
        r[r_bea][condition] = -1
        r[r_eva][condition] = 1
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        r[r_enj][condition] = 1
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 270.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 414.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 558.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 666.0
        
        return

    def rmenu_main_ep3_scene_32030():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back4
        ma_cha_back = cha_back14_2
        
        r[r_bea][condition] = -1
        r[r_eva][condition] = 1
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        r[r_enj][condition] = 1
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        r_ma[ma3_ber][condition] = 1
        
        r_ma[ma3_wal][itiran_x] = r_ma[ma3_ber][itiran_x] = 292.0
        r_ma[ma3_bea][itiran_x] = 420.0
        r_ma[ma3_ev2][itiran_x] = r_ma[ma3_ron][itiran_x] = r_ma[ma3_rg2][itiran_x] = r_ma[ma3_rg6][itiran_x] = 548.0
        r_ma[ma3_goa][itiran_x] = 324.0
        r_ma[ma3_rg1][itiran_x] = r_ma[ma3_rg5][itiran_x] = 452.0
        r_ma[ma3_rg3][itiran_x] = r_ma[ma3_rg7][itiran_x] = 644.0
        r_ma[ma3_rg4][itiran_x] = 740.0
        r_ma[ma3_s45][itiran_x] = 676.0
        r_ma[ma3_s41][itiran_x] = 772.0
        
        r_ma[ma3_bea][itiran_y] = r_ma[ma3_wal][itiran_y] = r_ma[ma3_ev2][itiran_y] = 198.0
        r_ma[ma3_ron][itiran_y] = r_ma[ma3_s45][itiran_y] = r_ma[ma3_s41][itiran_y] = 342.0
        r_ma[ma3_goa][itiran_y] = r_ma[ma3_rg1][itiran_y] = r_ma[ma3_rg2][itiran_y] = r_ma[ma3_rg3][itiran_y] = r_ma[ma3_rg4][itiran_y] = 486.0
        r_ma[ma3_rg5][itiran_y] = r_ma[ma3_rg6][itiran_y] = r_ma[ma3_rg7][itiran_y] = 594.0
        r_ma[ma3_lam][itiran_y] = r_ma[ma3_ber][itiran_y] = 738.0
        
        return

    def rmenu_main_ep3_scene_32040():
        global r
        global r_ma
        global r_cha_back
        global ma_cha_back
        for tmp in range(1,20):
            r[tmp][condition] = 1
        for tmp in range(20,cha_kazu_ep3):
            r[tmp][condition] = -1
        for tmp in range(1,cha_kazu_ep3_2):
            r_ma[tmp][condition] = -1
        r_cha_back = cha_back4
        ma_cha_back = cha_back15
        
        r[r_bea][condition] = -1
        r[r_eva][condition] = 1
        r[r_kin][condition] = 2
        r[r_gen][condition] = 2
        r[r_sha][condition] = 2
        r[r_kan][condition] = 2
        r[r_goh][condition] = 2
        r[r_kum][condition] = 2
        r[r_ros][condition] = 2
        r[r_mar][condition] = 2
        r[r_rud][condition] = 2
        r[r_kir][condition] = 2
        r[r_hid][condition] = 2
        r[r_kla][condition] = 2
        r[r_nat][condition] = 2
        r[r_geo][condition] = 2
        r[r_nan][condition] = 2
        r[r_but][condition] = 2
        r[r_jes][condition] = 2
        r[r_enj][condition] = 1
        
        r_ma[ma3_bea][condition] = 1
        r_ma[ma3_rg1][condition] = 1
        r_ma[ma3_rg2][condition] = 1
        r_ma[ma3_rg3][condition] = 1
        r_ma[ma3_rg4][condition] = 1
        r_ma[ma3_rg5][condition] = 1
        r_ma[ma3_rg6][condition] = 1
        r_ma[ma3_rg7][condition] = 1
        r_ma[ma3_goa][condition] = 1
        r_ma[ma3_ron][condition] = 1
        r_ma[ma3_wal][condition] = 1
        r_ma[ma3_ev2][condition] = 1
        r_ma[ma3_s41][condition] = 1
        r_ma[ma3_s45][condition] = 1
        r_ma[ma3_ber][condition] = 1
        r_ma[ma3_enj][condition] = 1
        
        return

    def rmenu_main_ep4_scene_40000():
        global r_enj_ma
        global enj_cha_back
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_enj][condition] = 1
        
        enj_cha_back = ba4_3_0
        return

    def rmenu_main_ep4_scene_40001():
        global r_ma
        global ma_cha_back
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_ber][condition] = 1
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_enj][itiran_x] = 468.0
        r_ma[ma4_ber][itiran_x] = 596.0
        r_ma[ma4_enj][itiran_y] = r_ma[ma4_ber][itiran_y] = 468.0
        return

    def rmenu_main_ep4_scene_40005():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 1
        r_ma[ma4_bea][condition] = 1
        
        ma_cha_back = ba4_2_0
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = 404.0
        r_ma[ma4_mar][itiran_x] = 532.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 660.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 396.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 540.0
        return

    def rmenu_main_ep4_scene_40030():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        
        enj_cha_back = ba4_3_0
        
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 532.0
        r_enj_ma[enj_enj][itiran_y] = 540.0
        r_enj_ma[enj_eva][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40040():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        
        enj_cha_back = ba4_3_1
        
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 468.0
        r_enj_ma[enj_oko][itiran_x] = 596.0
        r_enj_ma[enj_enj][itiran_y] = 540.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40050():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        
        enj_cha_back = ba4_3_2
        
        r_enj_ma[enj_kas][itiran_x] = 340.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 596.0
        r_enj_ma[enj_oko][itiran_x] = 724.0
        r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_kas][itiran_y] = 540.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40060():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = 1
        
        enj_cha_back = ba4_3_3
        
        r_enj_ma[enj_kas][itiran_x] = 340.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 596.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = 724.0
        r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_kas][itiran_y] = r_enj_ma[enj_ama][itiran_y] = 540.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40070():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = 1
        r_enj_ma[enj_ber][condition] = 1
        
        enj_cha_back = ba4_3_3
        
        r_enj_ma[enj_kas][itiran_x] = r_enj_ma[enj_ber][itiran_x] = 340.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 596.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = 724.0
        r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_kas][itiran_y] = r_enj_ma[enj_ama][itiran_y] = 540.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = r_enj_ma[enj_ber][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40080():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = 1
        
        enj_cha_back = ba4_3_3
        
        r_enj_ma[enj_kas][itiran_x] = 340.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 596.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = 724.0
        r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_kas][itiran_y] = r_enj_ma[enj_ama][itiran_y] = 540.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40090():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 1
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        
        ma_cha_back = ba4_2_1
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = 404.0
        r_ma[ma4_mar][itiran_x] = 532.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 660.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 324.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        r_ma[ma4_kin][itiran_y] = 612.0
        return

    def rmenu_main_ep4_scene_40100():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 1
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 1
        
        ma_cha_back = ba4_2_2
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = 404.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = 532.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 660.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 324.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 612.0
        return

    def rmenu_main_ep4_scene_40110():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 1
        
        ma_cha_back = ba4_2_2
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = 404.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = 532.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 660.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 324.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 612.0
        return

    def rmenu_main_ep4_scene_40120():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = 1
        r_enj_ma[enj_pro][condition] = 1
        
        enj_cha_back = ba4_3_3_2
        
        r_enj_ma[enj_kas][itiran_x] = r_enj_ma[enj_pro][itiran_x] = 340.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = 596.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = 724.0
        r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_kas][itiran_y] = r_enj_ma[enj_ama][itiran_y] = 468.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 324.0
        r_enj_ma[enj_pro][itiran_y] = 612.0
        return

    def rmenu_main_ep4_scene_40130():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = 1
        r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = 1
        
        enj_cha_back = ba4_3_5
        
        r_enj_ma[enj_kas][itiran_x] = r_enj_ma[enj_pro][itiran_x] = 340.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = r_enj_ma[enj_mar][itiran_x] = 596.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = 724.0
        r_enj_ma[enj_enj][itiran_y] = r_enj_ma[enj_kas][itiran_y] = r_enj_ma[enj_ama][itiran_y] = 396.0
        r_enj_ma[enj_eva][itiran_y] = r_enj_ma[enj_oko][itiran_y] = 252.0
        r_enj_ma[enj_mar][itiran_y] = 540.0
        r_enj_ma[enj_pro][itiran_y] = 684.0
        return

    def rmenu_main_ep4_scene_40140():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = 1
        r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = 1
        r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = 1
        r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = 1
        r_enj_ma[enj_rg1][condition] = 1
        r_enj_ma[enj_rg2][condition] = 1
        r_enj_ma[enj_rg3][condition] = 1
        r_enj_ma[enj_rg4][condition] = 1
        r_enj_ma[enj_rg5][condition] = 1
        r_enj_ma[enj_rg6][condition] = 1
        r_enj_ma[enj_rg7][condition] = 1
        
        enj_cha_back = ba4_3_6
        
        r_enj_ma[enj_kas][itiran_x] = r_enj_ma[enj_pro][itiran_x] = 308.0
        r_enj_ma[enj_mar][itiran_x] = 340.0
        r_enj_ma[enj_rg1][itiran_x] = r_enj_ma[enj_rg5][itiran_x] = 468.0
        r_enj_ma[enj_enj][itiran_x] = r_enj_ma[enj_eva][itiran_x] = r_enj_ma[enj_rg2][itiran_x] = r_enj_ma[enj_rg6][itiran_x] = 564.0
        r_enj_ma[enj_rg3][itiran_x] = r_enj_ma[enj_rg7][itiran_x] = 660.0
        r_enj_ma[enj_oko][itiran_x] = r_enj_ma[enj_ama][itiran_x] = 692.0
        r_enj_ma[enj_rg4][itiran_x] = 756.0
        return

    def rmenu_main_ep4_scene_40150():
        global r_ma
        global ma_cha_back
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_lam][itiran_x] = 468.0
        r_ma[ma4_enj][itiran_x] = 596.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        return

    def rmenu_main_ep4_scene_40160():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 1
        
        ma_cha_back = ba4_2_2
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = 404.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = 532.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 660.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 324.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 612.0
        return

    def rmenu_main_ep4_scene_40170():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 2
        
        ma_cha_back = ba4_2_2
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = 404.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = 532.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 660.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 324.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 612.0
        return

    def rmenu_main_ep4_scene_40175():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = r_enj_ma[enj_rg1][condition] = 1
        r_enj_ma[enj_rg2][condition] = r_enj_ma[enj_rg3][condition] = 1
        r_enj_ma[enj_rg4][condition] = r_enj_ma[enj_rg5][condition] = 1
        r_enj_ma[enj_rg6][condition] = r_enj_ma[enj_rg7][condition] = 1
        r_enj_ma[enj_sak][condition] = 1
        
        enj_cha_back = ba4_3_7
        return

    def rmenu_main_ep4_scene_40180():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 2
        r_ma[ma4_s41][condition] = 1
        r_ma[ma4_s45][condition] = 1
        r_ma[ma4_s00][condition] = 1
        
        ma_cha_back = ba4_2_4
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = r_ma[ma4_s41][itiran_x] = 452.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = 580.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 708.0
        r_ma[ma4_s45][itiran_x] = 356.0
        r_ma[ma4_s00][itiran_x] = 548.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 252.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 396.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 540.0
        r_ma[ma4_s41][itiran_y] = r_ma[ma4_s45][itiran_y] = r_ma[ma4_s00][itiran_y] = 684.0
        return

    def rmenu_main_ep4_scene_40190():
        return

    def rmenu_main_ep4_scene_40200():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 2
        r_ma[ma4_s41][condition] = 1
        r_ma[ma4_s45][condition] = 1
        r_ma[ma4_s00][condition] = 1
        r_ma[ma4_ron][condition] = 1
        
        ma_cha_back = ba4_2_5
        
        r_ma[ma4_bea][itiran_x] = r_ma[ma4_lam][itiran_x] = r_ma[ma4_kin][itiran_x] = r_ma[ma4_ron][itiran_x] = 372.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = r_ma[ma4_s45][itiran_x] = 500.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = 628.0
        r_ma[ma4_s41][itiran_x] = 596.0
        r_ma[ma4_s00][itiran_x] = 692.0
        r_ma[ma4_lam][itiran_y] = r_ma[ma4_ber][itiran_y] = 252.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = r_ma[ma4_enj][itiran_y] = 396.0
        r_ma[ma4_kin][itiran_y] = r_ma[ma4_sak][itiran_y] = 540.0
        r_ma[ma4_ron][itiran_y] = r_ma[ma4_s41][itiran_y] = r_ma[ma4_s45][itiran_y] = r_ma[ma4_s00][itiran_y] = 684.0
        return

    def rmenu_main_ep4_scene_40210():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = 1
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_kin][condition] = 1
        r_ma[ma4_sak][condition] = 2
        r_ma[ma4_s41][condition] = 1
        r_ma[ma4_s45][condition] = 1
        r_ma[ma4_s00][condition] = 1
        r_ma[ma4_ron][condition] = 1
        r_ma[ma4_wal][condition] = 1
        r_ma[ma4_goa][condition] = 1
        r_ma[ma4_rg1][condition] = r_ma[ma4_rg2][condition] = r_ma[ma4_rg3][condition] = r_ma[ma4_rg4][condition] = 1
        r_ma[ma4_rg5][condition] = r_ma[ma4_rg6][condition] = r_ma[ma4_rg7][condition] = 1
        
        ma_cha_back = ba4_2_6
        
        r_ma[ma4_wal][itiran_x] = 308.0
        r_ma[ma4_ron][itiran_x] = 436.0
        return

    def rmenu_main_ep4_scene_40220():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = r_ma[ma4_lam][condition] = r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = r_ma[ma4_sak][condition] = 2
        r_ma[ma4_bea][condition] = r_ma[ma4_kin][condition] = r_ma[ma4_s41][condition] = 1
        r_ma[ma4_s45][condition] = r_ma[ma4_s00][condition] = r_ma[ma4_ron][condition] = 1
        r_ma[ma4_wal][condition] = r_ma[ma4_goa][condition] = 1
        r_ma[ma4_rg1][condition] = r_ma[ma4_rg2][condition] = r_ma[ma4_rg3][condition] = r_ma[ma4_rg4][condition] = 1
        r_ma[ma4_rg5][condition] = r_ma[ma4_rg6][condition] = r_ma[ma4_rg7][condition] = 1
        r_ma[ma4_gap][condition] = 1
        
        ma_cha_back = ba4_2_7
        
        r_ma[ma4_wal][itiran_x] = 244.0
        r_ma[ma4_lam][itiran_x] = r_ma[ma4_bea][itiran_x] = r_ma[ma4_kin][itiran_x] = r_ma[ma4_ron][itiran_x] = 372.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = r_ma[ma4_gap][itiran_x] = 500.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = r_ma[ma4_s45][itiran_x] = 628.0
        r_ma[ma4_s41][itiran_x] = 724.0
        r_ma[ma4_s00][itiran_x] = 820.0
        return

    def rmenu_main_ep4_scene_40230():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = r_enj_ma[enj_rg1][condition] = 1
        r_enj_ma[enj_rg2][condition] = r_enj_ma[enj_rg3][condition] = 1
        r_enj_ma[enj_rg4][condition] = r_enj_ma[enj_rg5][condition] = 1
        r_enj_ma[enj_rg6][condition] = r_enj_ma[enj_rg7][condition] = 1
        r_enj_ma[enj_sak][condition] = r_enj_ma[enj_mas][condition] = 1
        
        enj_cha_back = ba4_3_7
        return

    def rmenu_main_ep4_scene_40240():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = r_enj_ma[enj_rg1][condition] = 1
        r_enj_ma[enj_rg2][condition] = r_enj_ma[enj_rg3][condition] = 1
        r_enj_ma[enj_rg4][condition] = r_enj_ma[enj_rg5][condition] = 1
        r_enj_ma[enj_rg6][condition] = r_enj_ma[enj_rg7][condition] = 1
        r_enj_ma[enj_sak][condition] = r_enj_ma[enj_mas][condition] = 1
        r_enj_ma[enj_sab][condition] = 1
        
        enj_cha_back = ba4_3_7
        return

    def rmenu_main_ep4_scene_40250():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = r_enj_ma[enj_rg1][condition] = 1
        r_enj_ma[enj_rg2][condition] = r_enj_ma[enj_rg3][condition] = 1
        r_enj_ma[enj_rg4][condition] = r_enj_ma[enj_rg5][condition] = 1
        r_enj_ma[enj_rg6][condition] = r_enj_ma[enj_rg7][condition] = 1
        r_enj_ma[enj_sak][condition] = r_enj_ma[enj_mas][condition] = 1
        r_enj_ma[enj_sab][condition] = r_enj_ma[enj_kwa][condition] = 1
        
        enj_cha_back = ba4_3_7
        return

    def rmenu_main_ep4_scene_40260():
        global r
        r[r_geo][condition] = 2
        return

    def rmenu_main_ep4_scene_40270():
        global r
        global r_cha_back
        r[r_geo][condition] = 2
        r[r_but][condition] = -1
        r_cha_back = cha_back16
        return

    def rmenu_main_ep4_scene_40280():
        global r_ma
        global ma_cha_back
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_mar][condition] = 2
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_mar][itiran_x] = 468.0
        r_ma[ma4_bea][itiran_x] = 596.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = 468.0
        return

    def rmenu_main_ep4_scene_40290():
        global r_enj_ma
        global enj_cha_back
        for tmp in range(1,cha_kazu_ep4_3):
            r_enj_ma[tmp][condition] = -1
        r_enj_ma[enj_enj][condition] = r_enj_ma[enj_eva][condition] = 1
        r_enj_ma[enj_oko][condition] = r_enj_ma[enj_kas][condition] = 1
        r_enj_ma[enj_ama][condition] = r_enj_ma[enj_pro][condition] = 1
        r_enj_ma[enj_mar][condition] = r_enj_ma[enj_rg1][condition] = 1
        r_enj_ma[enj_rg2][condition] = r_enj_ma[enj_rg3][condition] = 1
        r_enj_ma[enj_rg4][condition] = r_enj_ma[enj_rg5][condition] = 1
        r_enj_ma[enj_rg6][condition] = r_enj_ma[enj_rg7][condition] = 1
        r_enj_ma[enj_sak][condition] = r_enj_ma[enj_mas][condition] = 1
        r_enj_ma[enj_sab][condition] = r_enj_ma[enj_kwa][condition] = 1
        r_enj_ma[enj_ber][condition] = 1
        
        enj_cha_back = ba4_3_7
        return

    def rmenu_main_ep4_scene_40300():
        global r_ma
        global ma_cha_back
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_mar][condition] = 2
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_enj][itiran_x] = 340.0
        r_ma[ma4_mar][itiran_x] = 596.0
        r_ma[ma4_bea][itiran_x] = 724.0
        r_ma[ma4_enj][itiran_y] = r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = 468.0
        return

    def rmenu_main_ep4_scene_40310():
        global r_ma
        global ma_cha_back
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_sak][condition] = 1
        r_ma[ma4_bea][condition] = 1
        r_ma[ma4_mar][condition] = 2
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_enj][itiran_x] = 340.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = 468.0
        r_ma[ma4_bea][itiran_x] = 724.0
        r_ma[ma4_enj][itiran_y] = r_ma[ma4_bea][itiran_y] = r_ma[ma4_mar][itiran_y] = 540.0
        r_ma[ma4_sak][itiran_y] = 396.0
        return

    def rmenu_main_ep4_scene_40320():
        global r_ma
        global ma_cha_back
        r_ma[ma4_enj][condition] = 1
        r_ma[ma4_bea][condition] = 1
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_enj][itiran_x] = 468.0
        r_ma[ma4_bea][itiran_x] = 596.0
        r_ma[ma4_bea][itiran_y] = r_ma[ma4_enj][itiran_y] = 468.0
        return

    def rmenu_main_ep4_scene_40330():
        global r_ma
        global ma_cha_back
        r_ma[ma4_ber][condition] = r_ma[ma4_lam][condition] = r_ma[ma4_enj][condition] = 1
        r_ma[ma4_mar][condition] = 2
        r_ma[ma4_bea][condition] = r_ma[ma4_kin][condition] = r_ma[ma4_s41][condition] = 1
        r_ma[ma4_s45][condition] = r_ma[ma4_s00][condition] = r_ma[ma4_ron][condition] = 1
        r_ma[ma4_wal][condition] = r_ma[ma4_goa][condition] = r_ma[ma4_sak][condition] = 1
        r_ma[ma4_rg1][condition] = r_ma[ma4_rg2][condition] = r_ma[ma4_rg3][condition] = r_ma[ma4_rg4][condition] = 1
        r_ma[ma4_rg5][condition] = r_ma[ma4_rg6][condition] = r_ma[ma4_rg7][condition] = 1
        r_ma[ma4_gap][condition] = 1
        
        ma_cha_back = ba4_2_7
        
        r_ma[ma4_wal][itiran_x] = 244.0
        r_ma[ma4_lam][itiran_x] = r_ma[ma4_bea][itiran_x] = r_ma[ma4_kin][itiran_x] = r_ma[ma4_ron][itiran_x] = 372.0
        r_ma[ma4_mar][itiran_x] = r_ma[ma4_sak][itiran_x] = r_ma[ma4_gap][itiran_x] = 500.0
        r_ma[ma4_ber][itiran_x] = r_ma[ma4_enj][itiran_x] = r_ma[ma4_s45][itiran_x] = 628.0
        r_ma[ma4_s41][itiran_x] = 724.0
        r_ma[ma4_s00][itiran_x] = 820.0
        return

    def rmenu_main_ep4_scene_40350():
        global r
        r[r_geo][condition] = 2
        r[r_eva][condition] = 2
        r[r_rud][condition] = 2
        r[r_ros][condition] = 2
        r[r_nat][condition] = 2
        r[r_hid][condition] = 2
        r[r_gen][condition] = 2
        return

    def rmenu_main_ep4_scene_40360():
        global r
        r[r_geo][condition] = 2
        r[r_eva][condition] = 2
        r[r_rud][condition] = 2
        r[r_ros][condition] = 2
        r[r_nat][condition] = 2
        r[r_hid][condition] = 2
        r[r_gen][condition] = 2
        r[r_mar][condition] = 2
        return

    def rmenu_main_ep4_scene_40370():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = 2
        return

    def rmenu_main_ep4_scene_40380():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        return

    def rmenu_main_ep4_scene_40390():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        r[r_kla][condition] = 2
        return

    def rmenu_main_ep4_scene_40400():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        r[r_kla][condition] = 2
        r[r_nan][condition] = r[r_sha][condition] = 2
        return

    def rmenu_main_ep4_scene_40410():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        r[r_kla][condition] = r[r_sha][condition] = 2
        r[r_nan][condition] = r[r_kin][condition] = 2
        return

    def rmenu_main_ep4_scene_40420():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        r[r_kla][condition] = r[r_sha][condition] = 2
        r[r_nan][condition] = r[r_kin][condition] = 2
        r[r_goh][condition] = r[r_kum][condition] = 2
        return

    def rmenu_main_ep4_scene_40430():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        r[r_kla][condition] = r[r_sha][condition] = 2
        r[r_nan][condition] = r[r_kin][condition] = 2
        r[r_goh][condition] = r[r_kum][condition] = 2
        r[r_kan][condition] = 2
        return

    def rmenu_main_ep4_scene_40440():
        global r
        r[r_geo][condition] = r[r_eva][condition] = 2
        r[r_rud][condition] = r[r_ros][condition] = 2
        r[r_nat][condition] = r[r_hid][condition] = 2
        r[r_gen][condition] = r[r_mar][condition] = 2
        r[r_jes][condition] = r[r_kir][condition] = 2
        r[r_kla][condition] = r[r_sha][condition] = 2
        r[r_nan][condition] = r[r_kin][condition] = 2
        r[r_goh][condition] = r[r_kum][condition] = 2
        r[r_kan][condition] = 2
        r[r_but][condition] = 1
        r[r_bea][condition] = 1
        
        r[r_bea][itiran_x] = 276.0
        r[r_bea][itiran_y] = 324.0
        return

    def rmenu_main_ep4_scene_40450():
        global r_ma
        global ma_cha_back
        r_ma[ma4_lam][condition] = 1
        r_ma[ma4_ber][condition] = 1
        
        ma_cha_back = "saveload/load_null.png"
        
        r_ma[ma4_lam][itiran_x] = 468.0
        r_ma[ma4_ber][itiran_x] = 596.0
        r_ma[ma4_ber][itiran_y] = r_ma[ma4_lam][itiran_y] = 468.0
        return


    def tips_ep1():
        global tips
        global grim
        
        for tmp in range(1,tips_kazu):
            tips[tmp][tips_flg] = 0
        for tmp in range(1,grim_kazu):
            grim[tmp][grim_flg] = 0
        
        tmp2 = (grim_scene-100)
        if tmp2 > 10:
            tmp2 = 10
        tmp2 += 2
        
        for tmp in range(1,tmp2):
            grim[tmp][grim_flg] = 1
            if not persistent.grim_new[1][tmp]:
                persistent.grim_new[1][tmp] = 1
        
        if play_scene < 10190:
            rtips_main_ep1_scene_10000()
        elif play_scene == 10190:
            rtips_main_ep1_scene_10190()
        elif play_scene >= 10191 and play_scene < 10270:
            rtips_main_ep1_scene_10191()
        elif play_scene == 10270:
            rtips_main_ep1_scene_10270()
        elif play_scene >= 10271 and play_scene < 11000:
            rtips_main_ep1_scene_10271()
        elif play_scene >= 11000:
            rtips_main_ep1_scene_11000()
        
    
      
    def rtips_main_ep1_scene_10000():
        global tips
        
        
    def rtips_main_ep1_scene_10190():
        global tips
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[1][1]:
            persistent.tips_new[1][1] = 1
        
    def rtips_main_ep1_scene_10191():
        global tips
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        if not persistent.tips_new[1][1]:
            persistent.tips_new[1][1] = 1
        if not persistent.tips_new[1][2]:
            persistent.tips_new[1][2] = 1
        
    def rtips_main_ep1_scene_10270():
        global tips
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        if not persistent.tips_new[1][1]:
            persistent.tips_new[1][1] = 1
        if not persistent.tips_new[1][2]:
            persistent.tips_new[1][2] = 1
        if not persistent.tips_new[1][3]:
            persistent.tips_new[1][3] = 1
        
    def rtips_main_ep1_scene_10271():
        global tips
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        tips[4][tips_flg] = 1
        if not persistent.tips_new[1][1]:
            persistent.tips_new[1][1] = 1
        if not persistent.tips_new[1][2]:
            persistent.tips_new[1][2] = 1
        if not persistent.tips_new[1][3]:
            persistent.tips_new[1][3] = 1
        if not persistent.tips_new[1][4]:
            persistent.tips_new[1][4] = 1
        
    def rtips_main_ep1_scene_11000():
        global tips
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        tips[4][tips_flg] = 1
        tips[5][tips_flg] = 1
        if not persistent.tips_new[1][1]:
            persistent.tips_new[1][1] = 1
        if not persistent.tips_new[1][2]:
            persistent.tips_new[1][2] = 1
        if not persistent.tips_new[1][3]:
            persistent.tips_new[1][3] = 1
        if not persistent.tips_new[1][4]:
            persistent.tips_new[1][4] = 1
        if not persistent.tips_new[1][5]:
            persistent.tips_new[1][5] = 1
        
    
    def tips_ep2():
        global tips
        global grim
        
        for tmp in range(1,tips_kazu):
            tips[tmp][tips_flg] = 0
        for tmp in range(1,grim_kazu):
            grim[tmp][grim_flg] = 0
        
#        tmp2 = (grim_scene-200)
#        if tmp2 > 6:
#            tmp2 = 6
#        tmp2 += 2
        
#        for tmp in range(1,tmp2):
#            grim[tmp][grim_flg] = 1
        
        if play_scene < 41:
            rtips_main_ep2_scene_10()
        elif play_scene >= 41 and play_scene < 51:
            rtips_main_ep2_scene_41()
        elif play_scene == 51:
            rtips_main_ep2_scene_51()
        elif play_scene >= 52 and play_scene < 71:
            rtips_main_ep2_scene_52()
        elif play_scene >= 71 and play_scene < 90:
            rtips_main_ep2_scene_71()
        elif play_scene == 90:
            rtips_main_ep2_scene_90()
        elif play_scene == 100:
            rtips_main_ep2_scene_100()
        elif play_scene == 101:
            rtips_main_ep2_scene_101()
        elif play_scene >= 102 and play_scene < 150:
            rtips_main_ep2_scene_102()
        elif play_scene >= 150 and play_scene < 180:
            rtips_main_ep2_scene_150()
        elif play_scene >= 180:
            rtips_main_ep2_scene_180()
        
    
      
    def rtips_main_ep2_scene_10():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        
        grim[1][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        
    def rtips_main_ep2_scene_41():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        
    def rtips_main_ep2_scene_51():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        
    def rtips_main_ep2_scene_52():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        
    def rtips_main_ep2_scene_71():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        
    def rtips_main_ep2_scene_90():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        if not persistent.tips_new[2][2]:
            persistent.tips_new[2][2] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        
    def rtips_main_ep2_scene_100():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        if not persistent.tips_new[2][2]:
            persistent.tips_new[2][2] = 1
        if not persistent.tips_new[2][3]:
            persistent.tips_new[2][3] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        
    def rtips_main_ep2_scene_101():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        if not persistent.tips_new[2][2]:
            persistent.tips_new[2][2] = 1
        if not persistent.tips_new[2][3]:
            persistent.tips_new[2][3] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        grim[6][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        if not persistent.grim_new[2][6]:
            persistent.grim_new[2][6] = 1
        
    def rtips_main_ep2_scene_102():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        if not persistent.tips_new[2][2]:
            persistent.tips_new[2][2] = 1
        if not persistent.tips_new[2][3]:
            persistent.tips_new[2][3] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        grim[6][grim_flg] = 1
        grim[7][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        if not persistent.grim_new[2][6]:
            persistent.grim_new[2][6] = 1
        if not persistent.grim_new[2][7]:
            persistent.grim_new[2][7] = 1
        
    def rtips_main_ep2_scene_150():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        tips[4][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        if not persistent.tips_new[2][2]:
            persistent.tips_new[2][2] = 1
        if not persistent.tips_new[2][3]:
            persistent.tips_new[2][3] = 1
        if not persistent.tips_new[2][4]:
            persistent.tips_new[2][4] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        grim[6][grim_flg] = 1
        grim[7][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        if not persistent.grim_new[2][6]:
            persistent.grim_new[2][6] = 1
        if not persistent.grim_new[2][7]:
            persistent.grim_new[2][7] = 1
        
    def rtips_main_ep2_scene_180():
        global tips
        global grim
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        tips[3][tips_flg] = 1
        tips[4][tips_flg] = 1
        tips[5][tips_flg] = 1
        if not persistent.tips_new[2][1]:
            persistent.tips_new[2][1] = 1
        if not persistent.tips_new[2][2]:
            persistent.tips_new[2][2] = 1
        if not persistent.tips_new[2][3]:
            persistent.tips_new[2][3] = 1
        if not persistent.tips_new[2][4]:
            persistent.tips_new[2][4] = 1
        if not persistent.tips_new[2][5]:
            persistent.tips_new[2][5] = 1
        
        grim[1][grim_flg] = 1
        grim[2][grim_flg] = 1
        grim[3][grim_flg] = 1
        grim[4][grim_flg] = 1
        grim[5][grim_flg] = 1
        grim[6][grim_flg] = 1
        grim[7][grim_flg] = 1
        if not persistent.grim_new[2][1]:
            persistent.grim_new[2][1] = 1
        if not persistent.grim_new[2][2]:
            persistent.grim_new[2][2] = 1
        if not persistent.grim_new[2][3]:
            persistent.grim_new[2][3] = 1
        if not persistent.grim_new[2][4]:
            persistent.grim_new[2][4] = 1
        if not persistent.grim_new[2][5]:
            persistent.grim_new[2][5] = 1
        if not persistent.grim_new[2][6]:
            persistent.grim_new[2][6] = 1
        if not persistent.grim_new[2][7]:
            persistent.grim_new[2][7] = 1
        
    def tips_ep3():
        global tips
        global grim
        
        for tmp in range(1,tips_kazu):
            tips[tmp][tips_flg] = 0
        for tmp in range(1,grim_kazu):
            grim[tmp][grim_flg] = 0
        
        tmp2 = (grim_scene-300)
        if tmp2 > 12:
            tmp2 = 12
        tmp2 += 2
        
        for tmp in range(1,tmp2):
            grim[tmp][grim_flg] = 1
            if not persistent.grim_new[3][tmp]:
                persistent.grim_new[3][tmp] = 1
        
        if play_scene < 30100:
            rtips_main_ep3_scene_30010()
        elif play_scene >= 30100:
            rtips_main_ep3_scene_30100()
        
    
      
    def rtips_main_ep3_scene_30010():
        global tips
        
        tips[1][tips_flg] = 1
        if not persistent.tips_new[3][1]:
            persistent.tips_new[3][1] = 1
        
    def rtips_main_ep3_scene_30100():
        global tips
        
        tips[1][tips_flg] = 1
        tips[2][tips_flg] = 1
        if not persistent.tips_new[3][1]:
            persistent.tips_new[3][1] = 1
        if not persistent.tips_new[3][2]:
            persistent.tips_new[3][2] = 1
        
    def tips_ep4():
        global tips
        global grim
        
        for tmp in range(1,tips_kazu):
            tips[tmp][tips_flg] = 0
        for tmp in range(1,grim_kazu):
            grim[tmp][grim_flg] = 0
        
        tmp2 = (grim_scene-400)
        if tmp2 > 11:
            tmp2 = 11
        tmp2 += 2
        
        for tmp in range(1,tmp2):
            grim[tmp][grim_flg] = 1
            if not persistent.grim_new[4][tmp]:
                persistent.grim_new[4][tmp] = 1
        
    

style chr_text:
    size 50
    #drop_shadow (2, 2)
    font "times.ttf"
    color "#ffffff"
    hover_color "#ffffff"
    insensitive_color (255, 255, 255, 255)
    outlines [(1, "#000000", 0, 0)]
    
style tip_text:
    size 34
    #drop_shadow (2, 2)
    font "times.ttf"
    color "#ffffff"
    hover_color "#ffffff"
    insensitive_color (255, 255, 255, 255)
    outlines [(1, "#000000", 0, 0)]
    

init -2:
    transform text_page:
        xpos (960.0/1920.0) ypos (112.0/1080.0)
#        xpos (960+18) ypos (112+20)
    transform chars_text_page:
        xpos (680.0/1920.0) ypos (128.0/1080.0)
    transform chars_back:
#        xpos (62.0/1920.0) ypos (128.0/1080.0)
        xpos (164.0/1920.0) ypos (164.0/1080.0)
    transform chars_tati:
#        xpos (1410.0/1920.0) ypos 0.0 alpha 0.0 events True
        xpos 1.0 ypos 0.0 alpha 0.0 events True
        linear 0.5 xpos (1200.0/1920.0) alpha 1.0
