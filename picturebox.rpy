init python:
    
    g = Gallery()
    
    g.locked_button = "cgmode/logo.png"
    g.navigation = True
    g.idle_border = "cgmode/border.png"
    g.transition = dissolve
    g.unlocked_advance = True
    
    g.button("c0101")
    g.unlock_image("c0101_a")
    g.unlock_image("c0101_b")
    g.unlock_image("c0101_c")
    
    g.button("c0201")
    g.unlock_image("c0201_a")
    g.unlock_image("c0201_b")
    g.unlock_image("c0201_c")
    g.unlock_image("c0201_d")
    g.unlock_image("c0201_e")
    g.unlock_image("c0201_f")
    
    g.button("c0202")
    g.unlock_image("c0202_a")
    g.unlock_image("c0202_b")
    
    g.button("c0301")
    g.unlock_image("c0301")
    
    g.button("c0302")
    g.unlock_image("c0302_a")
    g.unlock_image("c0302_b")
    
    g.button("c0303")
    g.unlock_image("c0303")
    
    g.button("c0406")
    g.unlock_image("c0406")
    
    g.button("e0104")
    g.unlock_image("e0104_a")
    g.unlock_image("e0104_b")
    g.unlock_image("e0104_c")
    g.unlock_image("e0104_d")
    g.condition("renpy.seen_image('e0104_a') or renpy.seen_image('e0104_b') or renpy.seen_image('e0104_c') or renpy.seen_image('e0104_d')")
    
    g.button("e0201")
    g.unlock_image("e0201")
    
    g.button("e0404")
    g.unlock_image("e0404")
    
    g.button("e0903")
    g.unlock_image("e0903_a")
    g.unlock_image("e0903_b")
    g.unlock_image("e0903_c")
    
    g.button("e0904")
    g.unlock_image("e0904_a")
    g.unlock_image("e0904_b")
    
    #
    
    g.button("e0301_a")
    g.unlock_image("e0301_a")
    
    g.button("e0301_b")
    g.unlock_image("e0301_b")
    
    g.button("e0301_c")
    g.unlock_image("e0301_c")
    
    g.button("e0401_a")
    g.unlock_image("e0401_a")
    
    g.button("e0401_b")
    g.unlock_image("e0401_b")
    
    g.button("e0405")
    g.unlock_image("e0405")
    
    g.button("e0406")
    g.unlock_image("e0406")
    
    g.button("e0407")
    g.unlock_image("e0407")
    
    g.button("e0901_a")
    g.unlock_image("e0901_a")
    g.unlock_image("e0901_b")
    
    g.button("e0901_c")
    g.unlock_image("e0901_c")
    
    g.button("e0902")
    g.unlock_image("e0902")
    
    g.button("no55")
    g.unlock_image("no55_00059")
    
    #
    
    g.button("g0101")
    g.unlock_image("g0101")
    
    g.button("g0102")
    g.unlock_image("g0102")
    
    g.button("g0103")
    g.unlock_image("g0103")
    
    g.button("g0201")
    g.unlock_image("g0201")
    
    g.button("g0202")
    g.unlock_image("g0202")
    
    g.button("g0203")
    g.unlock_image("g0203_a")
    g.unlock_image("g0203_b")
    
    g.button("g0301")
    g.unlock_image("g0301")
    
    g.button("g0302")
    g.unlock_image("g0302")
    
    g.button("g0401")
    g.unlock_image("g0401")
    
    g.button("no01")
    g.unlock_image("no01_00119")
    
    g.button("no60")
    g.unlock_image("no60_00179")
    g.unlock_image("no61_00089")
    
    g.button("no64")
    g.unlock_image("no64_00000")
    
    #
    
    g.button("g0402")
    g.unlock_image("g0402")
    
    g.button("g0403")
    g.unlock_image("g0403")
    
    g.button("g0404")
    g.unlock_image("g0404")
    
    g.button("cg_c0203")
    g.condition("renpy.seen_image('c0203_cwall') or renpy.seen_image('c0203_lwall') or renpy.seen_image('ep2_c0203_2')")
    g.image("cg_c0203_la")
    g.condition("renpy.seen_image('c0203 ca') or renpy.seen_image('c0203 la')")
    g.image("cg_c0203_lb")
    g.condition("renpy.seen_image('c0203 cb') or renpy.seen_image('c0203 lb')")
    g.image("cg_c0203_lc")
    g.condition("renpy.seen_image('ep2_c0203_2')")
    
    g.button("cg_c0204")
    g.unlock_image("c0204 a")
    g.unlock_image("c0204 b")
    g.unlock_image("c0204 c")
    g.unlock_image("c0204 d")
    
    g.button("cg_c0205")
    g.condition("renpy.seen_image('c0205 a') or renpy.seen_image('c0205 b') or renpy.seen_image('c0205 c')")
    g.image("cg_c0205_a")
    g.condition("renpy.seen_image('c0205 a')")
    g.image("cg_c0205_b")
    g.condition("renpy.seen_image('c0205 b')")
    g.image("cg_c0205_c")
    g.condition("renpy.seen_image('c0205 c')")
    
    g.button("cg_c0401")
    g.condition("renpy.seen_image('c_c0401 a') or renpy.seen_image('c_c0401 b') or renpy.seen_image('c_c0401 la') or renpy.seen_image('c_c0401 lb') or renpy.seen_image('ep4_c0401 1') or renpy.seen_image('ep4_c0401 2') or renpy.seen_image('ep4_c0401 3')")
    g.image("cg_c0401_la")
    g.condition("renpy.seen_image('c_c0401 a') or renpy.seen_image('c_c0401 la') or renpy.seen_image('ep4_c0401 1') or renpy.seen_image('ep4_c0401 2')")
    g.image("cg_c0401_lb")
    g.condition("renpy.seen_image('c_c0401 b') or renpy.seen_image('c_c0401 lb') or renpy.seen_image('ep4_c0401 3')")
    
    g.button("cg_c0402")
    g.condition("renpy.seen_image('c_c0402_wall') or renpy.seen_image('c_c0402_lwall') or renpy.seen_image('ep4_c0402 2') or renpy.seen_image('ep4_c0402 4') or renpy.seen_image('ep4_c0402 5') or renpy.seen_image('ep4_c0402 6')")
    g.image("cg_c0402_la")
    g.condition("renpy.seen_image('c_c0402 a') or renpy.seen_image('c_c0402 la') or renpy.seen_image('ep4_c0402_4')")
    g.image("cg_c0402_lb")
    g.condition("renpy.seen_image('c_c0402 b') or renpy.seen_image('c_c0402 lb')")
    g.image("cg_c0402_lc")
    g.condition("renpy.seen_image('c_c0402 lc') or renpy.seen_image('ep4_c0402 5')")
    g.image("cg_c0402_ld")
    g.condition("renpy.seen_image('c_c0402 ld') or renpy.seen_image('ep4_c0402 2') or renpy.seen_image('ep4_c0402 6')")
    g.image("cg_c0402_le")
    g.condition("renpy.seen_image('c_c0402 le')")
    
    g.button("cg_c0403")
    g.condition("renpy.seen_image('c_c0403 a') or renpy.seen_image('c_c0403 c') or renpy.seen_image('c_c0403 f') or renpy.seen_image('ep4_c0403 4') or renpy.seen_image('ep4_c0403 5') or renpy.seen_image('ep4_c0403 6') or renpy.seen_image('ep4_c0403 2')")
    g.image("cg_c0403_a")
    g.condition("renpy.seen_image('c_c0403 a') or renpy.seen_image('ep4_c0403 1') or renpy.seen_image('ep4_c0403 7')")
    g.image("cg_c0403_b")
    g.condition("renpy.seen_image('ep4_c0403 2') or renpy.seen_image('ep4_c0403 6')")
    g.image("cg_c0403_c")
    g.condition("renpy.seen_image('c_c0403 c') or renpy.seen_image('ep4_c0403 3')")
    g.image("cg_c0403_d")
    g.condition("renpy.seen_image('ep4_c0403 5')")
    g.image("cg_c0403_e")
    g.condition("renpy.seen_image('ep4_c0403 4')")
    g.image("cg_c0403_f")
    g.condition("renpy.seen_image('c_c0403 f')")
    
    g.button("cg_c0404")
    g.condition("renpy.seen_image('c_c0404 a') or renpy.seen_image('c_c0404 b') or renpy.seen_image('c_c0404 lc') or renpy.seen_image('c_c0404 d') or renpy.seen_image('c_c0404 e') or renpy.seen_image('ep4_c0404 1') or renpy.seen_image('ep4_c0404 2') or renpy.seen_image('ep4_c0404 3')")
    g.image("cg_c0404_a")
    g.condition("renpy.seen_image('c_c0404 a')")
    g.image("cg_c0404_b")
    g.condition("renpy.seen_image('c_c0404 b') or renpy.seen_image('ep4_c0404 1')")
    g.image("cg_c0404_c")
    g.condition("renpy.seen_image('c_c0404 lc')")
    g.image("cg_c0404_d")
    g.condition("renpy.seen_image('c_c0404 d')")
    g.image("cg_c0404_e")
    g.condition("renpy.seen_image('c_c0404 e') or renpy.seen_image('ep4_c0404 2')")
    g.image("cg_c0404_f")
    g.condition("renpy.seen_image('ep4_c0404 3')")
    
    g.button("cg_c0901")
    g.condition("renpy.seen_image('c_c0901_a') or renpy.seen_image('c_c0901_b') or renpy.seen_image('ep3_c0901 4') or renpy.seen_image('ep3_c0901 5') or renpy.seen_image('c_c0901 ca')")
    g.image("cg_c0901_a")
    g.condition("renpy.seen_image('c_c0901_a') or renpy.seen_image('ep3_c0901 4') or renpy.seen_image('ep3_c0901 5') or renpy.seen_image('c_c0901 ca')")
    g.image("cg_c0901_b")
    g.condition("renpy.seen_image('c_c0901_b')")
    
    g.button("cg_c0902")
    g.condition("renpy.seen_image('c_c0902_a') or renpy.seen_image('ep3_c0902 2') or renpy.seen_image('ep3_c0902 4') or renpy.seen_image('ep3_c0902_7') or renpy.seen_image('ep3_c0902 8')")
    g.image("cg_c0902_a")
    
    #
    
    g.button("cg_e0101")
    g.condition("renpy.seen_image('e0101_wall')")
    g.image("cg_e0101_a")
    g.condition("renpy.seen_image('e0101 a')")
    g.image("cg_e0101_b")
    g.condition("renpy.seen_image('e0101 b')")
    g.image("cg_e0101_c")
    g.condition("renpy.seen_image('e0101 c')")
    
    g.button("cg_e0102")
    g.condition("renpy.seen_image('e0102_wall')")
    g.image("cg_e0102_a")
    g.condition("renpy.seen_image('e0102 a')")
    g.image("cg_e0102_b")
    g.condition("renpy.seen_image('e0102 b')")
    g.image("cg_e0102_c")
    g.condition("renpy.seen_image('e0102 c')")
    g.image("cg_e0102_d")
    g.condition("renpy.seen_image('e0102 d')")
    
    g.button("cg_e0103")
    g.condition("renpy.seen_image('e0103_wall') or renpy.seen_image('c_e0103_la')")
    g.image("cg_e0103_a")
    g.condition("renpy.seen_image('e0103 a') or renpy.seen_image('c_e0103_la')")
    g.image("cg_e0103_b")
    g.condition("renpy.seen_image('e0103 b')")
    g.image("cg_e0103_c")
    g.condition("renpy.seen_image('e0103 c')")
    g.image("cg_e0103_d")
    g.condition("renpy.seen_image('e0103 d')")
    
    g.button("cg_e0305")
    g.condition("renpy.seen_image('c_e0305_a') or renpy.seen_image('c_e0305_c') or renpy.seen_image('c_e0305_d') or renpy.seen_image('c_e0305_la') or renpy.seen_image('c_e0305_lc') or renpy.seen_image('c_e0305_ld')")
    g.image("cg_e0305_la")
    g.condition("renpy.seen_image('c_e0305_a') or renpy.seen_image('c_e0305_la')")
    g.image("cg_e0305_lc")
    g.condition("renpy.seen_image('c_e0305_c') or renpy.seen_image('c_e0305_lc')")
    g.image("cg_e0305_ld")
    g.condition("renpy.seen_image('c_e0305_d') or renpy.seen_image('c_e0305_ld')")
    
    g.button("cg_e0406")
    g.condition("renpy.seen_image('ep4_e0406 a') or renpy.seen_image('ep4_e0406 b') or renpy.seen_image('ep4_e0406 c') or renpy.seen_image('ep4_e0406 d') or renpy.seen_image('ep4_e0406 f')")
    g.image("cg_e0406_a")
    g.condition("renpy.seen_image('ep4_e0406 a')")
    g.image("cg_e0406_b")
    g.condition("renpy.seen_image('ep4_e0406 b')")
    g.image("cg_e0406_c")
    g.condition("renpy.seen_image('ep4_e0406 c')")
    g.image("cg_e0406_d")
    g.condition("renpy.seen_image('ep4_e0406 d')")
    g.image("cg_e0406_f")
    g.condition("renpy.seen_image('ep4_e0406 f')")
    
    g.button("cg_e0903")
    g.condition("renpy.seen_image('c_e0903_wall')")
    g.image("cg_e0903_a")
    g.condition("renpy.seen_image('e0903a')")
    g.image("cg_e0903_b")
    g.condition("renpy.seen_image('c_e0903 b')")
#    g.image("cg_e0903_c")
#    g.condition("renpy.seen_image('c_e0903 c') or renpy.seen_image('c_e0305_ld')")
    g.image("cg_e0903_d")
    g.condition("renpy.seen_image('e0903d')")
    
    g.button("congra")
    g.image("congra")
    g.condition("achievement.has(0)")
    g.image("package02")
#    g.condition("achievement.has(3) and achievement.has(5) and achievement.has(7) and achievement.has(9)")
    g.condition("renpy.seen_label('ura_teatime_1b') and renpy.seen_label('ura_teatime_2b') and renpy.seen_label('ura_teatime_3b') and renpy.seen_label('ura_teatime_4b')")
    
    g.button("package01")               ## unlock after all tips? chars for 02?
    g.image("package01")
    g.condition("achievement.has(2) and achievement.has(4) and achievement.has(6) and achievement.has(8)")
    
    g.button("portrait_ep1")               ## unlock after all EP1 music?
    g.image("portrait_ep1")
    g.condition("renpy.seen_label('ura_teatime_1b')")
    
    g.button("portrait_ep2")               ## unlock after all EP2 music?
    g.image("portrait_ep2")
    g.condition("renpy.seen_label('ura_teatime_2b')")
    
    g.button("portrait_ep3")               ## unlock after all EP3 music?
    g.image("portrait_ep3")
    g.condition("renpy.seen_label('ura_teatime_3b')")
    
    g.button("portrait_ep4")               ## unlock after all EP4 music?
    g.image("portrait_ep4")
    g.condition("renpy.seen_label('ura_teatime_4b')")
    
    cg_list = ['c0101_a', 'c0101_b', 'c0101_c',
                'c0201_a', 'c0201_b', 'c0201_c', 'c0201_d', 'c0201_e', 'c0201_f',
                'c0202_a', 'c0202_b', 'c0301',
                'c0302_a', 'c0302_b', 'c0303', 'c0406',
                'e0104_a', 'e0104_b', 'e0104_c', 'e0104_d', #'e0104_e',
                'e0201', 'e0404',
                'e0903_a', 'e0903_b', 'e0903_c',
                'e0904_a', 'e0904_b',
                'e0301_a', 'e0301_b', 'e0301_c',
                'e0401_a', 'e0401_b',
                'e0405', 'e0406', 'e0407',
                'e0901_a', 'e0901_b', 'e0901_c', 'e0902', 'no55_00059',
                'g0101', 'g0102', 'g0103',
                'g0201', 'g0202', 'g0203_a', 'g0203_b',
                'g0301', 'g0302', 'g0401',
                'no01_00119', 'no60_00179', 'no61_00089', 'no64_00000',
                'g0402', 'g0403', 'g0404',
                'c0203 ca', 'c0203 cb', 'ep2_c0203_2',
                'c0204 a', 'c0204 b', 'c0204 c', 'c0204 d',
                'c0205 a', 'c0205 b', 'c0205 c',
                'c_c0401 a', 'c_c0401 b',
                'c_c0402 a', 'c_c0402 b', 'c_c0402 lc', 'c_c0402 ld', 'c_c0402 le',
                'c_c0403 a', 'ep4_c0403 2', 'c_c0403 c', 'ep4_c0403 5', 'ep4_c0403 4', 'c_c0403 f',
                'c_c0404 a', 'c_c0404 b', 'c_c0404 d', 'c_c0404 e', 'ep4_c0404 1c', 'ep4_c0404 3',
                'c_c0901_a', 'c_c0901_b', 'c_c0902_a',
                'e0101 a', 'e0101 b', 'e0101 c',
                'e0102 a', 'e0102 b', 'e0102 c', 'e0102 d',
                'e0103 a', 'e0103 b', 'e0103 c', 'e0103 d',
                'c_e0305_a', 'c_e0305_c', 'c_e0305_d',
                'ep4_e0406 a', 'ep4_e0406 b', 'ep4_e0406 c', 'ep4_e0406 d', 'ep4_e0406 f',
                'e0903a', 'c_e0903 b', 'e0903d']
    
    cg_label_list = ['ura_teatime_1b', 'ura_teatime_2b', 'ura_teatime_3b', 'ura_teatime_4b', 'ura_teatime_4b']                # , 'ura_teatime_5b'
    
    def cg_counter():
        global cg_per
        global cg_count
        global label_count
        global cg_list
        global cg_label_list
        cg_count = 0.0              ## 121 total
        label_count = 0.0           ## 6   total
        for cg_name in cg_list:
            if renpy.seen_image(cg_name):
                cg_count += 1.0
        
        for cg_label in cg_label_list:
            if renpy.seen_label(cg_label):
                label_count += 1.0
        
        cg_per = round(((cg_count + label_count)/(len(cg_list) + len(cg_label_list)))*100,2)
        
        if cg_per >= 100.00 and not achievement.has(26):
            get_achievement(26)
    
    def cg_page(exeres):
        global cg_screen
        cg_screen += 1
        cg_screen2 = 5        # number of pages
        renpy.music.set_volume(default_vol, 0, channel="se9")
        renpy.music.play(se1010, channel="se9")
        if exeres == "+":
            if cg_screen >= cg_screen2:
                cg_screen = 0
            else:
                pass
            renpy.transition(t24)
        elif exeres == "-":
            if cg_screen <= 1:
                cg_screen = cg_screen2 - 1
            else:
                cg_screen -= 2
            renpy.transition(t23)
        renpy.restart_interaction()
    cg_pg = renpy.curry(cg_page)
    
default cg_screen = 0
    
screen cg():
    
    $ cg_counter()
    $ cg_screen2 = cg_screen + 1
    
    tag menu
    
    use title_background
    
#    add "cgmode/bg.png"
    add "background/efe/black.png" alpha 0.5
    add "cgmode/caption.png" at caption
    add "r_click/sysmenu/fg.png" yalign 1.0
    text "[cg_per]% Unlocked" style style.bgm_per_text xpos (80.0/1920.0) ypos (1060.0/1080.0) yalign 1.0
    
    imagebutton idle exit_i hover exit_h xpos (1722.0/1920.0) ypos (988.0/1080.0) focus_mask None action [ Play ("se9", se1005), Hide('cg_check'), Return() ] hovered Play ("se10", se1002)
    
    imagebutton auto "cgmode/prv_pg_%s.png" xpos (1414.0/1920.0) ypos (39.0/1080.0) focus_mask None action [cg_pg("-")] hovered Play ("se10", se1002)
    imagebutton auto "cgmode/nxt_pg_%s.png" xpos (1803.0/1920.0) ypos (39.0/1080.0) focus_mask None action [cg_pg("+")] hovered Play ("se10", se1002)
    text "Page: [cg_screen2]/5" style style.cg_text xpos (1500.0/1920.0) ypos (32.0/1080.0)
    
    if cg_screen == 0:
        use cg_000
    elif cg_screen == 1:
        use cg_001
    elif cg_screen == 2:
        use cg_002
    elif cg_screen == 3:
        use cg_003
    elif cg_screen == 4:
        use cg_004
    
style cg_text:
        size 70
        outlines [(1, "#000000", 0, 0)]
        #drop_shadow (2, 2)
        font "timesbd.ttf"
        color "#ffffff"
        hover_color "#ffffff"
        insensitive_color (255, 255, 255, 255)

transform cg_btn:
    xanchor 0.5 yanchor 0.5
    on idle:
        easein 0.2 zoom 1.0
    on hover:
        easein 0.2 zoom 1.11
    
screen cg_00():
    imagebutton auto "cgmode/prv_pg_%s.png" xpos (1414.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "04"), With(t23) ] hovered Play ("se10", se1002)
    imagebutton auto "cgmode/nxt_pg_%s.png" xpos (1803.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "01"), With(t24) ] hovered Play ("se10", se1002)
    text "Page: 1/5" style style.cg_text xpos (1500.0/1920.0) ypos (32.0/1080.0)
    $ g_x = 260.0
    $ g_y = 303.0
    
    add g.make_button("c0101", "cgmode/thumb/00/C0101_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0104", "cgmode/thumb/00/E0104_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("c0202", "cgmode/thumb/00/C0202_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("c0201", "cgmode/thumb/00/C0201_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    add g.make_button("e0201", "cgmode/thumb/00/E0201.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("c0301", "cgmode/thumb/00/C0301.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("c0302", "cgmode/thumb/00/C0302_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0903", "cgmode/thumb/00/E0903_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    add g.make_button("c0303", "cgmode/thumb/00/C0303.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("c0406", "cgmode/thumb/00/C0406.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0904", "cgmode/thumb/00/E0904_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0404", "cgmode/thumb/00/E0404.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
screen cg_01():
    imagebutton auto "cgmode/prv_pg_%s.png" xpos (1414.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "00"), With(t23) ] hovered Play ("se10", se1002)
    imagebutton auto "cgmode/nxt_pg_%s.png" xpos (1803.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "02"), With(t24) ] hovered Play ("se10", se1002)
    text "Page: 2/5" style style.cg_text xpos (1500.0/1920.0) ypos (32.0/1080.0)
    
    $ g_x = 260.0
    $ g_y = 303.0
    
    add g.make_button("e0405", "cgmode/thumb/01/E0405.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0406", "cgmode/thumb/01/E0406.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0407", "cgmode/thumb/01/E0407.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0901_a", "cgmode/thumb/01/E0901_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    add g.make_button("e0901_c", "cgmode/thumb/01/E0901_c.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0902", "cgmode/thumb/01/E0902.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0301_a", "cgmode/thumb/01/E0301_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0301_b", "cgmode/thumb/01/E0301_b.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    add g.make_button("e0301_c", "cgmode/thumb/01/E0301_c.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0401_a", "cgmode/thumb/01/E0401_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("e0401_b", "cgmode/thumb/01/E0401_b.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("no55", "cgmode/thumb/01/no55_00059.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
screen cg_02():
    imagebutton auto "cgmode/prv_pg_%s.png" xpos (1414.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "01"), With(t23) ] hovered Play ("se10", se1002)
    imagebutton auto "cgmode/nxt_pg_%s.png" xpos (1803.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "03"), With(t24) ] hovered Play ("se10", se1002)
    text "Page: 3/5" style style.cg_text xpos (1500.0/1920.0) ypos (32.0/1080.0)
    
    $ g_x = 260.0
    $ g_y = 303.0
    
    add g.make_button("no01", "cgmode/thumb/02/no01_00119.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("no60", "cgmode/thumb/02/no60_00179.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("no64", "cgmode/thumb/02/no64_00000.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0101", "cgmode/thumb/02/G0101.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    add g.make_button("g0102", "cgmode/thumb/02/G0102.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0103", "cgmode/thumb/02/G0103.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0201", "cgmode/thumb/02/G0201.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0202", "cgmode/thumb/02/G0202.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    add g.make_button("g0203", "cgmode/thumb/02/G0203_a.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0301", "cgmode/thumb/02/G0301.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0302", "cgmode/thumb/02/G0302.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0401", "cgmode/thumb/02/G0401.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
screen cg_03():
    imagebutton auto "cgmode/prv_pg_%s.png" xpos (1414.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "02"), With(t23) ] hovered Play ("se10", se1002)
    imagebutton auto "cgmode/nxt_pg_%s.png" xpos (1803.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "04"), With(t24) ] hovered Play ("se10", se1002)
    text "Page: 4/5" style style.cg_text xpos (1500.0/1920.0) ypos (32.0/1080.0)
    
    $ g_x = 260.0
    $ g_y = 303.0
    
    add g.make_button("g0402", "cgmode/thumb/03/G0402.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0403", "cgmode/thumb/03/G0403.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("g0404", "cgmode/thumb/03/G0404.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0203", "cgmode/thumb/03/CG_C0203_LA.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    add g.make_button("cg_c0204", "cgmode/thumb/03/CG_C0204_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0205", "cgmode/thumb/03/CG_C0205_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0401", "cgmode/thumb/03/CG_C0401_LA.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0402", "cgmode/thumb/03/CG_C0402_LA.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    add g.make_button("cg_c0403", "cgmode/thumb/03/CG_C0403_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0404", "cgmode/thumb/03/CG_C0404_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0901", "cgmode/thumb/03/CG_C0901_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_c0902", "cgmode/thumb/03/CG_C0902_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
screen cg_04():
    imagebutton auto "cgmode/prv_pg_%s.png" xpos (1414.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "03"), With(t23) ] hovered Play ("se10", se1002)
    imagebutton auto "cgmode/nxt_pg_%s.png" xpos (1803.0/1920.0) ypos (39.0/1080.0) focus_mask None action [ Play ("se9", se1010), SetScreenVariable("cg_screen", "00"), With(t24) ] hovered Play ("se10", se1002)
    text "Page: 5/5" style style.cg_text xpos (1500.0/1920.0) ypos (32.0/1080.0)
    
    $ g_x = 260.0
    $ g_y = 303.0
    
    add g.make_button("cg_e0101", "cgmode/thumb/04/CG_E0101_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_e0102", "cgmode/thumb/04/CG_E0102_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_e0103", "cgmode/thumb/04/CG_E0103_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_e0305", "cgmode/thumb/04/CG_E0305_LA.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    add g.make_button("cg_e0406", "cgmode/thumb/04/CG_E0406_t.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("cg_e0903", "cgmode/thumb/04/CG_E0903_A.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("portrait_ep1", "cgmode/thumb/04/PORTRAIT_EP1.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("portrait_ep2", "cgmode/thumb/04/PORTRAIT_EP2.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    add g.make_button("portrait_ep3", "cgmode/thumb/04/PORTRAIT_EP3.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("portrait_ep4", "cgmode/thumb/04/PORTRAIT_EP4.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("package01", "cgmode/thumb/04/PACKAGE01.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    $ g_x += 442.0
    add g.make_button("congra", "cgmode/thumb/04/congra_t.png", locked="cgmode/logox.png", xpos=(g_x/1920.0), ypos=(g_y/1080.0), hover_sound=se1002, activate_sound=se1001) at cg_btn
    


screen cg_000():
    $ g_x = 260.0
    $ g_y = 303.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0101_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0101_a.png" action g.Action("c0101") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0101'), Show('cg_check', None, 'c0101'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/E0104_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/E0104_a.png" action g.Action("e0104") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0104'), Show('cg_check', None, 'e0104'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0202_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0202_a.png" action g.Action("c0202") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0202'), Show('cg_check', None, 'c0202'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0201_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0201_a.png" action g.Action("c0201") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0201'), Show('cg_check', None, 'c0201'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/E0201.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/E0201.png" action g.Action("e0201") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0201'), Show('cg_check', None, 'e0201'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0301.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0301.png" action g.Action("c0301") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0301'), Show('cg_check', None, 'c0301'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0302_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0302_a.png" action g.Action("c0302") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0302'), Show('cg_check', None, 'c0302'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/E0903_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/E0903_a.png" action g.Action("e0903") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0903'), Show('cg_check', None, 'e0903'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0303.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0303.png" action g.Action("c0303") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0303'), Show('cg_check', None, 'c0303'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/C0406.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/C0406.png" action g.Action("c0406") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'c0406'), Show('cg_check', None, 'c0406'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/E0904_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/E0904_a.png" action g.Action("e0904") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0904'), Show('cg_check', None, 'e0904'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/00/E0404.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/00/E0404.png" action g.Action("e0404") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0404'), Show('cg_check', None, 'e0404'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
screen cg_001():
    $ g_x = 260.0
    $ g_y = 303.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0405.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0405.png" action g.Action("e0405") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0405'), Show('cg_check', None, 'e0405'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0406.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0406.png" action g.Action("e0406") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0406'), Show('cg_check', None, 'e0406'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0407.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0407.png" action g.Action("e0407") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0407'), Show('cg_check', None, 'e0407'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0901_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0901_a.png" action g.Action("e0901_a") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0901_a'), Show('cg_check', None, 'e0901_a'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0901_c.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0901_c.png" action g.Action("e0901_c") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0901_c'), Show('cg_check', None, 'e0901_c'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0902.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0902.png" action g.Action("e0902") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0902'), Show('cg_check', None, 'e0902'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0301_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0301_a.png" action g.Action("e0301_a") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0301_a'), Show('cg_check', None, 'e0301_a'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0301_b.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0301_b.png" action g.Action("e0301_b") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0301_b'), Show('cg_check', None, 'e0301_b'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0301_c.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0301_c.png" action g.Action("e0301_c") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0301_c'), Show('cg_check', None, 'e0301_c'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0401_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0401_a.png" action g.Action("e0401_a") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0401_a'), Show('cg_check', None, 'e0401_a'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/E0401_b.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/E0401_b.png" action g.Action("e0401_b") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'e0401_b'), Show('cg_check', None, 'e0401_b'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/no55_00059.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/no55_00059.png" action g.Action("no55") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'no55'), Show('cg_check', None, 'no55'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
#    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/01/tower2r.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/01/tower2r.png" action g.Action("tower") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'tower'), Show('cg_check', None, 'tower'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
screen cg_002():
    $ g_x = 260.0
    $ g_y = 303.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/no01_00119.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/no01_00119.png" action g.Action("no01") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'no01'), Show('cg_check', None, 'no01'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/no60_00179.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/no60_00179.png" action g.Action("no60") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'no60'), Show('cg_check', None, 'no60'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/no64_00000.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/no64_00000.png" action g.Action("no64") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'no64'), Show('cg_check', None, 'no64'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0101.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0101.png" action g.Action("g0101") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0101'), Show('cg_check', None, 'g0101'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0102.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0102.png" action g.Action("g0102") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0102'), Show('cg_check', None, 'g0102'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0103.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0103.png" action g.Action("g0103") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0103'), Show('cg_check', None, 'g0103'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0201.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0201.png" action g.Action("g0201") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0201'), Show('cg_check', None, 'g0201'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0202.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0202.png" action g.Action("g0202") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0202'), Show('cg_check', None, 'g0202'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0203_a.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0203_a.png" action g.Action("g0203") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0203'), Show('cg_check', None, 'g0203'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0301.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0301.png" action g.Action("g0301") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0301'), Show('cg_check', None, 'g0301'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0302.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0302.png" action g.Action("g0302") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0302'), Show('cg_check', None, 'g0302'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/02/G0401.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/02/G0401.png" action g.Action("g0401") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0401'), Show('cg_check', None, 'g0401'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
screen cg_003():
    $ g_x = 260.0
    $ g_y = 303.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/G0402.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/G0402.png" action g.Action("g0402") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0402'), Show('cg_check', None, 'g0402'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/G0403.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/G0403.png" action g.Action("g0403") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0403'), Show('cg_check', None, 'g0403'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/G0404.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/G0404.png" action g.Action("g0404") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'g0404'), Show('cg_check', None, 'g0404'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0203_LA.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0203_LA.png" action g.Action("cg_c0203") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0203'), Show('cg_check', None, 'cg_c0203'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0204_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0204_A.png" action g.Action("cg_c0204") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0204'), Show('cg_check', None, 'cg_c0204'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0205_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0205_A.png" action g.Action("cg_c0205") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0205'), Show('cg_check', None, 'cg_c0205'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0401_LA.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0401_LA.png" action g.Action("cg_c0401") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0401'), Show('cg_check', None, 'cg_c0401'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0402_LA.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0402_LA.png" action g.Action("cg_c0402") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0402'), Show('cg_check', None, 'cg_c0402'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0403_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0403_A.png" action g.Action("cg_c0403") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0403'), Show('cg_check', None, 'cg_c0403'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0404_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0404_A.png" action g.Action("cg_c0404") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0404'), Show('cg_check', None, 'cg_c0404'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0901_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0901_A.png" action g.Action("cg_c0901") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0901'), Show('cg_check', None, 'cg_c0901'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/03/CG_C0902_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/03/CG_C0902_A.png" action g.Action("cg_c0902") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_c0902'), Show('cg_check', None, 'cg_c0902'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
screen cg_004():
    $ g_x = 260.0
    $ g_y = 303.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/CG_E0101_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/CG_E0101_A.png" action g.Action("cg_e0101") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_e0101'), Show('cg_check', None, 'cg_e0101'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/CG_E0102_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/CG_E0102_A.png" action g.Action("cg_e0102") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_e0102'), Show('cg_check', None, 'cg_e0102'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/CG_E0103_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/CG_E0103_A.png" action g.Action("cg_e0103") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_e0103'), Show('cg_check', None, 'cg_e0103'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/CG_E0305_LA.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/CG_E0305_LA.png" action g.Action("cg_e0305") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_e0305'), Show('cg_check', None, 'cg_e0305'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 300.0
    $ g_y = 548.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/CG_E0406_t.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/CG_E0406_t.png" action g.Action("cg_e0406") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_e0406'), Show('cg_check', None, 'cg_e0406'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/CG_E0903_A.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/CG_E0903_A.png" action g.Action("cg_e0903") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'cg_e0903'), Show('cg_check', None, 'cg_e0903'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/PORTRAIT_EP1.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/PORTRAIT_EP1.png" action g.Action("portrait_ep1") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'portrait_ep1'), Show('cg_check', None, 'portrait_ep1'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/PORTRAIT_EP2.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/PORTRAIT_EP2.png" action g.Action("portrait_ep2") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'portrait_ep2'), Show('cg_check', None, 'portrait_ep2'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
    $ g_x = 340.0
    $ g_y = 793.0
    
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/PORTRAIT_EP3.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/PORTRAIT_EP3.png" action g.Action("portrait_ep3") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'portrait_ep3'), Show('cg_check', None, 'portrait_ep3'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/PORTRAIT_EP4.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/PORTRAIT_EP4.png" action g.Action("portrait_ep4") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'portrait_ep4'), Show('cg_check', None, 'portrait_ep4'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive g.locked_button idle im.MatrixColor("cgmode/thumb/04/PACKAGE01.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/PACKAGE01.png" action g.Action("package01") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'package01'), Show('cg_check', None, 'package01'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    $ g_x += 442.0
    imagebutton insensitive "cgmode/logox.png" idle im.MatrixColor("cgmode/thumb/04/congra_t.png", im.matrix.tint(0.65,0.65,0.65)) hover "cgmode/thumb/04/congra_t.png" action g.Action("congra") xpos (g_x/1920.0) ypos (g_y/1080.0) hovered [SetVariable('cg_btn2', 'congra'), Show('cg_check', None, 'congra'), Play ("se20", se1002)] unhovered Hide('cg_check') at cg_btn
    
default cg_btn2=0

screen cg_check(cg_btn2=None):
    if len(g.buttons[cg_btn2].images) > 1:
        hbox:
            xpos (1864.0/1920.0) xanchor 1.0 ypos (940.0/1080.0)
            for x in range(0,len(g.buttons[cg_btn2].images)):
                if not g.buttons[cg_btn2].images[x].check_unlock(True):
                    add im.MatrixColor("cgmode/check.png", im.matrix.brightness(-0.5)) #xpos x1 ypos 940
                else:
                    add "cgmode/check.png" #xpos x1 ypos 940
    
#init:
#    $ cg_screen = "00"
init -1500:

    # Displays a set of images in the gallery, or indicates that the images
    # are locked. This is given the following arguments:
    #
    # locked
    #     True if the image is locked.
    # displayables
    #     A list of transformed displayables that should be shown to the user.
    # index
    #     A 1-based index of the image being shown.
    # count
    #     The number of images attached to the current button.
    # gallery
    #     The image gallery object.
    screen _gallery:

        if locked:
            add "#000"
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
#            for d in displayables:
#                add d
            
            viewport:
                draggable True
                mousewheel True
                
                for d in displayables:
                    add d

        if count > 1:
            hbox:
                xpos (1864.0/1920.0) xanchor 1.0 ypos (940.0/1080.0)
                for x in range(0,count):
                    if (index-1) == x:
                        add im.MatrixColor("cgmode/check.png", im.matrix.tint(0,1,0)) #xpos x1 ypos 940
                    else:
                        if not g.buttons[cg_btn2].images[x].check_unlock(True):
                            add im.MatrixColor("cgmode/check.png", im.matrix.brightness(-0.5)) #xpos x1 ypos 940
                        else:
                            add "cgmode/check.png" #xpos x1 ypos 940
#                    $ x1-=30
            
        if gallery.slideshow:
            timer gallery.slideshow_delay action Return("next")

        key "game_menu" action [SetVariable('cg_btn2',0), Play ("sound", se1001), gallery.Return(), Hide('cg_check')]

        if gallery.navigation:

            imagebutton auto "cgmode/prev_%s.png" xpos (1600.0/1920.0) ypos (1008.0/1080.0) focus_mask None action [ Play ("sound", se1001), gallery.Previous() ]
            imagebutton auto "cgmode/next_%s.png" xpos (1696.0/1920.0) ypos (1008.0/1080.0) focus_mask None action [ Play ("sound", se1001), gallery.Next() ]
#                imagebutton auto "cgmode/slide_%s.png" xpos 1600 ypos 1008 focus_mask None action gallery.ToggleSlideshow()
            imagebutton auto "cgmode/back_%s.png" xpos (1808.0/1920.0) ypos (1008.0/1080.0) focus_mask None action [ Play ("sound", se1001), gallery.Return() ]
#                textbutton _("prev") action gallery.Previous()
#                textbutton _("next") action gallery.Next()
#                textbutton _("slideshow") action gallery.ToggleSlideshow()
#                textbutton _("return") action gallery.Return()
