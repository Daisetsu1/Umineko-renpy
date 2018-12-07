
## https://github.com/OlegWock/Roselia-achievements (for instructions)
## https://lemmasoft.renai.us/forums/viewtopic.php?t=39890 (for help?)


transform achievement_transform:
    on show:
        alpha 0.0
        linear 0.1 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.1 alpha 0.0

screen scr_achievement_get(title, a_text, icon, trans=achievement_transform):
    on "show" action Play("achmnt", "sys_se/trophy.ogg")
    timer 5.0 action Hide("scr_achievement_get")
    fixed:
        at trans
        add "trophies/bg.png"
        xalign 0.5
        ycenter (65.0/1080.0)
        xysize (700, 110)
        image icon zoom (5.0/12.0) xpos (55.0/700.0) yalign 0.5
        text "Achievement Unlocked!":
#        text title:
            font "micross.ttf"
            size 28
            id title
            xpos (165.0/700.0)
            ypos (10.0/110.0)
        text title:
#        text a_text:
            font "micross.ttf"
            size 22
            id a_text
            xpos (165.0/700.0)
            ycenter (75.0/110.0)

screen scr_achievement_get_plt(title, a_text, icon, trans=achievement_transform):
    timer 7.0 action [Hide("scr_achievement_get_plt"), Show("scr_achievement_get", title=title, a_text=a_text, icon=icon)]

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    on "show" action Play("achmnt", "sys_se/trophy.ogg")
    timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
                image icon zoom (1.0/3.0)
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text "Achievement Unlocked!":
#                text title:
                    size 28
                    id title
                text title:
#                text a_text:
                    size 22
                    id a_text


                

init python:
    renpy.music.register_channel("achmnt", "sfx", False)
    
    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        platinum = 1
        achievement.grant(ach_id)
        for i, a in persistent.achievements_dict.items():
            if achievement.has(i):
                platinum += 1
        if platinum == len(persistent.achievements_dict):
            achievement.grant(0)
        if persistent.ach_toggle:
            renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                              a_text=ach['text'], icon=ach['icon'], trans=trans)
            if platinum == len(persistent.achievements_dict):
                ach = persistent.achievements_dict[0]
                renpy.show_screen(_screen_name='scr_achievement_get_plt', title=ach['title'],
                                  a_text=ach['text'], icon=ach['icon'], trans=trans)

    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog']:
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]

        if persistent.ach_toggle:
            renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                              icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)





    # Define your achievements here
    if not persistent.achievements_dict:
        persistent.achievements_dict = {0: {"type": 0, # One time achievement
                                                             "title": "Witch Hunter", # Also neame for steam
                                                             "text": "Collected all achievements.", # description
                                                             "icon": "trophies/TROP000.png", # 96x96 image
                                                             "hidden": "yes",
                                                             },
                                        1: {"type": 0, # One time achievement
                                                             "title": "Welcome to Rokkenjima",    ##this is unlocked when textbox shows up?
                                                             "text": "Began Episode 1.",
                                                             "icon": "trophies/TROP001.png",
                                                             "hidden": "no",
                                                             },
                                        2: {"type": 0, # One time achievement
                                                             "title": "Episode 1 Tips Hunter",
                                                             "text": "Looked at all of the Episode 1 tips.",
                                                             "icon": "trophies/TROP002.png",
                                                             "hidden": "yes",
                                                             },
                                        3: {"type": 0, # One time achievement
                                                             "title": "Episode 1 Characters Hunter",
                                                             "text": "Looked at all of the Episode 1 characters.",
                                                             "icon": "trophies/TROP003.png",
                                                             "hidden": "yes",
                                                             },
                                        4: {"type": 0, # One time achievement
                                                             "title": "Episode 2 Tips Hunter",
                                                             "text": "Looked at all of the Episode 2 tips.",
                                                             "icon": "trophies/TROP004.png",
                                                             "hidden": "yes",
                                                             },
                                        5: {"type": 0, # One time achievement
                                                             "title": "Episode 2 Characters Hunter",
                                                             "text": "Looked at all of the Episode 2 characters.",
                                                             "icon": "trophies/TROP005.png",
                                                             "hidden": "yes",
                                                             },
                                        6: {"type": 0, # One time achievement
                                                             "title": "Episode 3 Tips Hunter",
                                                             "text": "Looked at all of the Episode 3 tips.",
                                                             "icon": "trophies/TROP006.png",
                                                             "hidden": "yes",
                                                             },
                                        7: {"type": 0, # One time achievement
                                                             "title": "Episode 3 Characters Hunter",
                                                             "text": "Looked at all of the Episode 3 characters.",
                                                             "icon": "trophies/TROP007.png",
                                                             "hidden": "yes",
                                                             },
                                        8: {"type": 0, # One time achievement
                                                             "title": "Episode 4 Tips Hunter",
                                                             "text": "Looked at all of the Episode 4 tips.",
                                                             "icon": "trophies/TROP008.png",
                                                             "hidden": "yes",
                                                             },
                                        9: {"type": 0, # One time achievement
                                                             "title": "Episode 4 Characters Hunter",
                                                             "text": "Looked at all of the Episode 4 characters.",
                                                             "icon": "trophies/TROP009.png",
                                                             "hidden": "yes",
                                                             },
                                        10: {"type": 0, # One time achievement
                                                             "title": "Change setting",
                                                             "text": "Changed a setting in Config.",
                                                             "icon": "trophies/TROP010.png",
                                                             "hidden": "no",
                                                             },
                                        11: {"type": 0, # One time achievement
                                                             "title": "Episode 1 Tea Party",
                                                             "text": "Finished Episode 1 Tea Party.",
                                                             "icon": "trophies/TROP011.png",
                                                             "hidden": "yes",
                                                             },
                                        12: {"type": 0, # One time achievement
                                                             "title": "Episode 1 Reverse Tea Party",
                                                             "text": "Finished Episode 1 Reverse (????) Tea Party.",
                                                             "icon": "trophies/TROP012.png",
                                                             "hidden": "yes",
                                                             },
                                        13: {"type": 0, # One time achievement
                                                             "title": "Episode 2 Tea Party",
                                                             "text": "Finished Episode 2 Tea Party.",
                                                             "icon": "trophies/TROP013.png",
                                                             "hidden": "yes",
                                                             },
                                        14: {"type": 0, # One time achievement
                                                             "title": "Episode 2 Reverse Tea Party",
                                                             "text": "Finished Episode 2 Reverse (????) Tea Party.",
                                                             "icon": "trophies/TROP014.png",
                                                             "hidden": "yes",
                                                             },
                                        15: {"type": 0, # One time achievement
                                                             "title": "Episode 3 Tea Party",
                                                             "text": "Finished Episode 3 Tea Party.",
                                                             "icon": "trophies/TROP015.png",
                                                             "hidden": "yes",
                                                             },
                                        16: {"type": 0, # One time achievement
                                                             "title": "Episode 3 Reverse Tea Party",
                                                             "text": "Finished Episode 3 Reverse (????) Tea Party.",
                                                             "icon": "trophies/TROP016.png",
                                                             "hidden": "yes",
                                                             },
                                        17: {"type": 0, # One time achievement
                                                             "title": "Episode 4 Tea Party",
                                                             "text": "Finished Episode 4 Tea Party.",
                                                             "icon": "trophies/TROP017.png",
                                                             "hidden": "yes",
                                                             },
                                        18: {"type": 0, # One time achievement
                                                             "title": "Episode 4 Reverse Tea Party",
                                                             "text": "Finished Episode 4 Reverse (????) Tea Party.",
                                                             "icon": "trophies/TROP018.png",
                                                             "hidden": "yes",
                                                             },
                                        19: {"type": 0, # One time achievement
                                                             "title": "A Force to be Reckoned With",
                                                             "text": "You have played for 50 hours.\nRemember to take a break!",
                                                             "icon": "trophies/TROP019.png",
                                                             "hidden": "yes",
                                                             },
                                        20: {"type": 0, # One time achievement
                                                             "title": "Unbelieveable Clicking",  ## "There's No Reason to Click This Much"
                                                             "text": "You've seen 30,000 lines.\nKinzo-san could do it.",
                                                             "icon": "trophies/TROP020.png",
                                                             "hidden": "yes",
                                                             },
                                        21: {"type": 0, # One time achievement
                                                             "title": "Rosa Unrivaled",    ## unlocked just after Rosa's scream at end of main part (before 023 is unlocked)
                                                             "text": "\"UWOOOOOOOHHHhHHHhH!!!\"\nGive me a Golden Dream.",
                                                             "icon": "trophies/TROP021.png",
                                                             "hidden": "yes",
                                                             },
                                        22: {"type": 0, # One time achievement
                                                             "title": "Legend of the Golden Witch",    ## these are unlocked at beginning of text004 block
                                                             "text": "Finished Episode 1.",
                                                             "icon": "trophies/TROP022.png",
                                                             "hidden": "yes",
                                                             },
                                        23: {"type": 0, # One time achievement
                                                             "title": "Turn of the Golden Witch",
                                                             "text": "Finished Episode 2.",
                                                             "icon": "trophies/TROP023.png",
                                                             "hidden": "yes",
                                                             },
                                        24: {"type": 0, # One time achievement
                                                             "title": "Banquet of the Golden Witch",
                                                             "text": "Finished Episode 3.",
                                                             "icon": "trophies/TROP024.png",
                                                             "hidden": "yes",
                                                             },
                                        25: {"type": 0, # One time achievement
                                                             "title": "Alliance of the Golden Witch",
                                                             "text": "Finished Episode 4.",
                                                             "icon": "trophies/TROP025.png",
                                                             "hidden": "yes",
                                                             },
                                        26: {"type": 0, # One time achievement
                                                             "title": "CG Hunter",
                                                             "text": "Unlocked 100% of the Picture Box.\nA true witch hunter shall be rewarded.",
                                                             "icon": "trophies/TROP026.png",
                                                             "hidden": "yes",
                                                             },
                                        27: {"type": 0, # One time achievement
                                                             "title": "Music Hunter",
                                                             "text": "Unlocked 100% of the Music Box.",
                                                             "icon": "trophies/TROP027.png",
                                                             "hidden": "yes",
                                                             },
                                        28: {"type": 0, # One time achievement
                                                             "title": "Anime Music Hunter",
                                                             "text": "Unlocked 100% of the Anime's Music Box.",
                                                             "icon": "trophies/TROP028.png",
                                                             "hidden": "yes",
                                                             },
#                                        "0": {"type": 1, # Progress achievement
#                                                             "title": "",
#                                                             "text": "",
#                                                             "icon": "trophies/TROP0.png",
#                                                             "cur_prog": , # current progress 
#                                                             "max_prog": # maximal progress
#                                                             }
                                        }
                                        

        for i, a in persistent.achievements_dict.items():
            if a['type'] == 0:
                achievement.register(i, steam=a['title'])
            if a['type'] == 1:
                achievement.register(i, steam=a['title'], stat_max=a['max_prog'], stat_modulo=a['cur_prog'])

screen achievements:
    tag menu
    use title_background
    add "background/efe/black.png" alpha 0.5
    
    vpgrid id "ach":
        cols 2
        draggable True
        mousewheel True
        spacing 10
        
        xpos 30
        xsize 1810
        ypos -50
        ysize 1252
        fixed:
            xmaximum 900
            ymaximum 240
            add Null()
        fixed:
            xmaximum 900
            ymaximum 240
            add Null()
        
        for i, a in persistent.achievements_dict.items():
            if not a['hidden'] == "no":
                $ ach_ico = "trophies/locked.png"
            else:
                $ ach_ico = im.Grayscale(a['icon'])
            $ ach_title = a['title']
            $ ach_text = a['text']
            fixed:
                xmaximum 900
                ymaximum 240
                if achievement.has(i):
                    add a['icon']
                    text "[ach_title]" xpos 272 ypos 120 yanchor 1.0 size 50 font "micross.ttf" outlines [(1, "#000000", 0, 0)]
                    text "[ach_text]" xpos 272 ypos 138 size 40 font "micross.ttf" outlines [(1, "#000000", 0, 0)]
                else:
                    add ach_ico
                    text "????" xpos 272 ypos 120 yanchor 0.5 size 50 font "micross.ttf" outlines [(1, "#000000", 0, 0)]
        
        fixed:
            xmaximum 900
            ymaximum 240
            add Null()
        fixed:
            xmaximum 900
            ymaximum 240
            add Null()
        
    
    add "trophies/caption.png" at caption
    add "config/vscrollbar.png" xcenter (1876.0/1920.0) yanchor 0.5 ypos (580.0/1080.0)  ## murderer for chiru & saveload for portable
    vbar value YScrollValue("ach") style style.c_vbar thumb "saveload/vscrollbar_thumb.png"
    add "r_click/sysmenu/fg.png" yalign 1.0
    imagebutton idle exit_i hover exit_h xpos (1856.0/1920.0) ypos (1064.0/1080.0) xanchor 1.0 yanchor 1.0 focus_mask None action [ Play ("se20", "sys_se/zyosys3.ogg"), Return(), With(t23) ] hovered Play ("se10", "sys_se/zyosys0.ogg")
