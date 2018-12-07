    
image ctc_animation = Animation("ctc_12.png", 0.2, "ctc_22.png", 0.2, "ctc_32.png", 0.2, "ctc_22.png", 0.2, xpos=0.99, ypos=0.99, xanchor=1.0, yanchor=1.0)
image keywait:
    "keywait.png"
    alpha 1.0
    pause 0.5
    linear 1.0 alpha 0.4
    linear 1.0 alpha 1.0
    repeat
image keywait2:
    "keywait2.png"
    linear 1.5 alpha 0.0
    linear 1.5 alpha 1.0
    repeat
    
image auto2 = im.MatrixColor("auto1.png", im.matrix.desaturate() * im.matrix.tint(0.525, 0.937, 0.612))
image auto3 = im.MatrixColor("auto1.png", im.matrix.desaturate() * im.matrix.tint(0.157, 0.157, 0.157))         ## disabled variant
image auto_arrow:
    contains:
        "auto1.png"
    contains:
        "auto2"
        linear 0.5 alpha 1.0
        pause 0.25
        linear 0.5 alpha 0.0
        repeat
    contains:
        "auto.png"

#image fast2 = im.MatrixColor("fast1.png", im.matrix.desaturate() * im.matrix.tint(0.188, 0.302, 1.0))
image fast2 = im.MatrixColor("fast1.png", im.matrix.desaturate() * im.matrix.tint(0.2901, 0.353, 0.937))
image fast3 = im.MatrixColor("fast1.png", im.matrix.desaturate() * im.matrix.tint(0.157, 0.157, 0.157))         ## disabled variant
image fast_forward_arrow:
    contains:
        "fast1.png"
    contains:
        "fast2"
        linear 0.5 alpha 1.0
        pause 0.25
        linear 0.5 alpha 0.0
        repeat
    contains:
        "fast.png"

image fast_forward_disabled_arrow:
    contains:
        "fast3"
    contains:
        "fast.png"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#image rainback scroll = Snow("efe/rain_bg1.png")
#image rainfront scroll = Snow("efe/rain_fg.png")

image rainback:
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_small.png", count=100, border=128, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                        "rain_static == 1", Image("efe/rain_bg_static.png"))
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg1.png", count=100, border=161, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg2.png", count=100, border=214, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_small.png", count=100, border=128, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg1.png", count=100, border=161, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg2.png", count=100, border=214, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                        "rain_static == 1", Null())
image rainfront:
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_fg.png", count=100, border=268, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                                "rain_static == 1", Image("efe/rain_fg_static.png"))
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_medium.png", count=100, border=256, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                                "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_large.png", count=100, border=384, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                                "rain_static == 1", Null())

image rainback static = "efe/rain_bg_static.png"
image rainfront static = "efe/rain_fg_static.png"

image rainback 2:
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_small.png", count=100, border=128, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                        "rain_static == 1", Image("efe/rain_bg_static.png"))
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg1.png", count=100, border=161, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg2.png", count=100, border=214, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                        "rain_static == 1", Null())

#Background images
image splash = "title/alchemist.png"
#image splash2 = "title/circle_logo.png"
image splash2 = "title/07th.png"
#image splash3 = im.Scale("title/circle_logo.png", config.screen_width,config.screen_height, bilinear=True)
image splash3 = "title/circle_logo.png"
image splash4 = im.Scale("title/renpy.png", config.screen_width,config.screen_height, bilinear=True)

image flg_0 = Image("efe/number/0.png", xanchor=0.0, yanchor=0.0)
image flg_1 = Image("efe/number/1.png", xanchor=0.0, yanchor=0.0)
image flg_2 = Image("efe/number/2.png", xanchor=0.0, yanchor=0.0)
image flg_3 = Image("efe/number/3.png", xanchor=0.0, yanchor=0.0)
image flg_4 = Image("efe/number/4.png", xanchor=0.0, yanchor=0.0)
image flg_5 = Image("efe/number/5.png", xanchor=0.0, yanchor=0.0)
image flg_6 = Image("efe/number/6.png", xanchor=0.0, yanchor=0.0)
image flg_7 = Image("efe/number/7.png", xanchor=0.0, yanchor=0.0)
image flg_8 = Image("efe/number/8.png", xanchor=0.0, yanchor=0.0)
image flg_9 = Image("efe/number/9.png", xanchor=0.0, yanchor=0.0)

image cinema logo = "efe/cinema_logo.png"
image cinema logo 2 = "efe/cinema_logo2.png"
image ware = "efe/ware.png"
image data1 = "efe/data1.png"
image dim = Image("efe/untitled.png", xalign=0.5, yalign=0.5)
#image dim = Image("background/efe/black.png", xalign=0.5, yalign=0.5, alpha=0.7)
image boiler_dark:
    "efe/untitled2.png"
#    "background/efe/black.png"
    xalign 0.5
    yalign 0.5
    alpha 0.1
image chain1r_sp = "efe/chain1r_sp.png"
image chain2r_sp = "efe/chain2r_sp.png"
image chain3r_sp = "efe/chain3r_sp.png"
image chain4r_sp = "efe/chain4r_sp.png"
image chain5r_sp = "efe/chain5r_sp.png"
image chain6r_sp = "efe/chain6r_sp.png"
image chain7r_sp = "efe/chain7r_sp.png"

image movie = Movie(channel="movie", size=(config.screen_width, config.screen_height), xpos=0, ypos=0, xanchor=0, yanchor=0)
image no03 = Movie(channel="movie_efe", play="movie/no03.mkv", mask="movie/no03_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no04 = Movie(channel="movie_efe", play="movie/no04.mkv", mask="movie/no04_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no05 = Movie(channel="movie_efe", play="movie/no05.mkv", mask="movie/no05_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no06 = Movie(channel="movie_efe", play="movie/no06.mkv", mask="movie/no06_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no07 = Movie(channel="movie_efe", play="movie/no07.mkv", mask="movie/no07_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no08 = Movie(channel="movie_efe", play="movie/no08.mkv", mask="movie/no08_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no09 = Movie(channel="movie_efe", play="movie/no09.mkv", mask="movie/no09_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no10 = Movie(channel="movie_efe", play="movie/no10.mkv", mask="movie/no10_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no19 = Movie(channel="movie_efe", play="movie/no19.mkv", mask="movie/no19_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no20 = Movie(channel="movie_efe", play="movie/no20.mkv", mask="movie/no20_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no21 = Movie(channel="movie_efe", play="movie/no21.mkv", mask="movie/no21_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no22 = Movie(channel="movie_efe", play="movie/no22.mkv", mask="movie/no22_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no23 = Movie(channel="movie_efe", play="movie/no23.mkv", mask="movie/no23_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no23a = Movie(channel="movie_efe", play="movie/no23a.mkv", mask="movie/no23a_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no24 = Movie(channel="movie_efe", play="movie/no24.mkv", mask="movie/no24_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no26 = Movie(channel="movie_efe", play="movie/no26.mkv", mask="movie/no26_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no29 = Movie(channel="movie_efe", play="movie/no29.mkv", mask="movie/no29_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no29a = Movie(channel="movie_efe", play="movie/no29a.mkv", mask="movie/no29a_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no33 = Movie(channel="movie_efe", play="movie/no33.mkv", mask="movie/no33_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no33_gray = Movie(channel="movie_efe", play="movie/no33_gray.mkv", mask="movie/no33_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no33a = Movie(channel="movie_efe", play="movie/no33a.mkv", mask="movie/no33a_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no34 = Movie(channel="movie_efe", play="movie/no34.mkv", mask="movie/no34_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no34a = Movie(channel="movie_efe", play="movie/no34a.mkv", mask="movie/no34a_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no35 = Movie(channel="movie_efe", play="movie/no35.mkv", mask="movie/no35_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no36 = Movie(channel="movie_efe", play="movie/no36.mkv", mask="movie/no36_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no37 = Movie(channel="movie_efe", play="movie/no37.mkv", mask="movie/no37_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no42 = Movie(channel="movie_efe", play="movie/no42.mkv", mask="movie/no42_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no64 = Movie(channel="movie_efe", play="movie/no64.mkv", xalign=0.5, yalign=0.5)
image no80 = Movie(channel="movie_efe", play="movie/no80.mkv", mask="movie/no80_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no81 = Movie(channel="movie_efe", play="movie/no81.mkv", mask="movie/no81_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no82 = Movie(channel="movie_efe", play="movie/no82.mkv", mask="movie/no82_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no83 = Movie(channel="movie_efe", play="movie/no83.mkv", mask="movie/no83_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no84 = Movie(channel="movie_efe", play="movie/no84.mkv", mask="movie/no84_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)
image no85 = Movie(channel="movie_efe", play="movie/no85.mkv", mask="movie/no85_mask.mkv", xpos=0, ypos=0, xanchor=0, yanchor=0)

image anm_no0018a = Image("anime/anm_no0018a.png", xalign=0.5, yalign=0.5)
image anm_no0018c = Image("anime/anm_no0018c.png", xalign=0.5, yalign=0.5)
image anm_no0019a = Image("anime/anm_no0019a.png", xalign=0.5, yalign=0.5)
image anm_no0019b = Image("anime/anm_no0019b.png", xalign=0.5, yalign=0.5)
image anm_no0020a = Image("anime/anm_no0020a.png", xalign=0.5, yalign=0.5)
image door_00096 = Image("anime/door_00096.png", xalign=0.5, yalign=0.5)
image no3_00000 = Image("anime/no3_00000.png", xalign=0.5, yalign=0.5)
image no3_00059 = Image("anime/no3_00059.png", xalign=0.5, yalign=0.5)
image no5_00000 = Image("anime/no5_00000.png", xalign=0.5, yalign=0.5)
image no5_00012 = Image("anime/no5_00012.png", xalign=0.5, yalign=0.5)
image no5_00039 = Image("anime/no5_00039.png", xalign=0.5, yalign=0.5)
image no6_00000 = Image("anime/no6_00000.png", xalign=0.5, yalign=0.5)
image no6_00039 = Image("anime/no6_00039.png", xalign=0.5, yalign=0.5)
image no9_00000 = Image("anime/no9_00000.png", xalign=0.5, yalign=0.5)
image no9_00039 = Image("anime/no9_00039.png", xalign=0.5, yalign=0.5)
image no01_00000 = Image("anime/no01_00000.png", xalign=0.5, yalign=0.5)
image no01_00119 = Image("anime/no01_00119.png", xalign=0.5, yalign=0.5)
image no01_00209 = Image("anime/no01_00209.png", xalign=0.5, yalign=0.5)
image no02_00000 = Image("anime/no02_00000.png", xalign=0.5, yalign=0.5)
image no02_00178 = Image("anime/no02_00178.png", xalign=0.5, yalign=0.5)
image no04_00000 = Image("anime/no04_00000.png", xalign=0.5, yalign=0.5)
image no04_00059 = Image("anime/no04_00059.png", xalign=0.5, yalign=0.5)
image no07_00000 = Image("anime/no07_00000.png", xalign=0.5, yalign=0.5)
image no07_00059 = Image("anime/no07_00059.png", xalign=0.5, yalign=0.5)
image no08_00000 = Image("anime/no08_00000.png", xalign=0.5, yalign=0.5)
image no08_00059 = Image("anime/no08_00059.png", xalign=0.5, yalign=0.5)
image no10_00000 = Image("anime/no10_00000.png", xalign=0.5, yalign=0.5)
image no10_00039 = Image("anime/no10_00039.png", xalign=0.5, yalign=0.5)
image no11_00000 = Image("anime/no11_00000.png", xalign=0.5, yalign=0.5)
image no11_00001 = Image("anime/no11_00001.png", xalign=0.5, yalign=0.5)
image no11_00002 = Image("anime/no11_00002.png", xalign=0.5, yalign=0.5)
image no11_00003 = Image("anime/no11_00003.png", xalign=0.5, yalign=0.5)
image no11_00004 = Image("anime/no11_00004.png", xalign=0.5, yalign=0.5)
image no11_00006 = Image("anime/no11_00006.png", xalign=0.5, yalign=0.5)
image no11_00059 = Image("anime/no11_00059.png", xalign=0.5, yalign=0.5)
image no12_00000 = Image("anime/no12_00000.png", xalign=0.5, yalign=0.5)
image no12_00059 = Image("anime/no12_00059.png", xalign=0.5, yalign=0.5)
image no13_00000 = Image("anime/no13_00000.png", xalign=0.5, yalign=0.5)
image no13_00039 = Image("anime/no13_00039.png", xalign=0.5, yalign=0.5)
image no14_00000 = Image("anime/no14_00000.png", xalign=0.5, yalign=0.5)
image no14_00039 = Image("anime/no14_00039.png", xalign=0.5, yalign=0.5)
image no15_00000 = Image("anime/no15_00000.png", xalign=0.5, yalign=0.5)
image no15_00059 = Image("anime/no15_00059.png", xalign=0.5, yalign=0.5)
image no16_00000 = Image("anime/no16_00000.png", xalign=0.5, yalign=0.5)
image no16_00059 = Image("anime/no16_00059.png", xalign=0.5, yalign=0.5)
image no17_00000 = Image("anime/no17_00000.png", xalign=0.5, yalign=0.5)
image no17_00039 = Image("anime/no17_00039.png", xalign=0.5, yalign=0.5)
image no18_00000 = Image("anime/no18_00000.png", xalign=0.5, yalign=0.5)
image no18_00039 = Image("anime/no18_00039.png", xalign=0.5, yalign=0.5)
image no19_00000 = Image("anime/no19_00000.png", xalign=0.5, yalign=0.5)
image no19_00060 = Image("anime/no19_00060.png", xalign=0.5, yalign=0.5)
image no20_00000 = Image("anime/no20_00000.png", xalign=0.5, yalign=0.5)
image no20_00059 = Image("anime/no20_00059.png", xalign=0.5, yalign=0.5)
image no0021c_hook_slow_00060 = Image("anime/no0021c_hook_slow_00060.png", xalign=0.5, yalign=0.5)
image no21_00000 = Image("anime/no21_00000.png", xalign=0.5, yalign=0.5)
image no21_00059 = Image("anime/no21_00059.png", xalign=0.5, yalign=0.5)
image no22_00000 = Image("anime/no22_00000.png", xalign=0.5, yalign=0.5)
image no22_00059 = Image("anime/no22_00059.png", xalign=0.5, yalign=0.5)
image no23_00000 = Image("anime/no23_00000.png", xalign=0.5, yalign=0.5)
image no23_00059 = Image("anime/no23_00059.png", xalign=0.5, yalign=0.5)
image no24_00000 = Image("anime/no24_00000.png", xalign=0.5, yalign=0.5)
image no24_00059 = Image("anime/no24_00059.png", xalign=0.5, yalign=0.5)
image no25_00000 = Image("anime/no25_00000.png", xalign=0.5, yalign=0.5)
image no25_00059 = Image("anime/no25_00059.png", xalign=0.5, yalign=0.5)
image no26_00000 = Image("anime/no26_00000.png", xalign=0.5, yalign=0.5)
image no26_00179 = Image("anime/no26_00179.png", xalign=0.5, yalign=0.5)
image no27_00000 = Image("anime/no27_00000.png", xalign=0.5, yalign=0.5)
image no27_00179 = Image("anime/no27_00179.png", xalign=0.5, yalign=0.5)
image no28_00000 = Image("anime/no28_00000.png", xalign=0.5, yalign=0.5)
image no28_00179 = Image("anime/no28_00179.png", xalign=0.5, yalign=0.5)
image no29_00000 = Image("anime/no29_00000.png", xalign=0.5, yalign=0.5)
image no29_00023 = Image("anime/no29_00023.png", xalign=0.5, yalign=0.5)
image no29_00179 = Image("anime/no29_00179.png", xalign=0.5, yalign=0.5)
image no30_00000 = Image("anime/no30_00000.png", xalign=0.5, yalign=0.5)
image no30_00006 = Image("anime/no30_00006.png", xalign=0.5, yalign=0.5)
image no30_00025 = Image("anime/no30_00025.png", xalign=0.5, yalign=0.5)
image no30_00059 = Image("anime/no30_00059.png", xalign=0.5, yalign=0.5)
image no31_00000 = Image("anime/no31_00000.png", xalign=0.5, yalign=0.5)
image no31_00059 = Image("anime/no31_00059.png", xalign=0.5, yalign=0.5)
image no32_00000 = Image("anime/no32_00000.png", xalign=0.5, yalign=0.5)
image no32_00059 = Image("anime/no32_00059.png", xalign=0.5, yalign=0.5)
image no33_00000 = Image("anime/no33_00000.png", xalign=0.5, yalign=0.5)
image no33_00068 = Image("anime/no33_00068.png", xalign=0.5, yalign=0.5)
image no33_00069 = Image("anime/no33_00069.png", xalign=0.5, yalign=0.5)
image no34_00000 = Image("anime/no34_00000.png", xalign=0.5, yalign=0.5)
image no34_00068 = Image("anime/no34_00068.png", xalign=0.5, yalign=0.5)
image no34_00069 = Image("anime/no34_00069.png", xalign=0.5, yalign=0.5)
image no35_00000 = Image("anime/no35_00000.png", xalign=0.5, yalign=0.5)
image no35_00039 = Image("anime/no35_00039.png", xalign=0.5, yalign=0.5)
image no36_00000 = Image("anime/no36_00000.png", xalign=0.5, yalign=0.5)
image no36_00039 = Image("anime/no36_00039.png", xalign=0.5, yalign=0.5)
image no37_00000 = Image("anime/no37_00000.png", xalign=0.5, yalign=0.5)
image no37_00039 = Image("anime/no37_00039.png", xalign=0.5, yalign=0.5)
image no38_00000 = Image("anime/no38_00000.png", xalign=0.5, yalign=0.5)
image no38_00149 = Image("anime/no38_00149.png", xalign=0.5, yalign=0.5)
image no38b_00149 = Image("anime/no38b_00149.png", xalign=0.5, yalign=0.5)
image no39_00000 = Image("anime/no39_00000.png", xalign=0.5, yalign=0.5)
image no39_00044 = Image("anime/no39_00044.png", xalign=0.5, yalign=0.5)
image no40_00000 = Image("anime/no40_00000.png", xalign=0.5, yalign=0.5)
image no40_00059 = Image("anime/no40_00059.png", xalign=0.5, yalign=0.5)
image no40b_00059 = Image("anime/no40b_00059.png", xalign=0.5, yalign=0.5)
image no41_00000 = Image("anime/no41_00000.png", xalign=0.5, yalign=0.5)
image no41_00119 = Image("anime/no41_00119.png", xalign=0.5, yalign=0.5)
image no42_00000 = Image("anime/no42_00000.png", xalign=0.5, yalign=0.5)
image no42_00039 = Image("anime/no42_00039.png", xalign=0.5, yalign=0.5)
image no43_00000 = Image("anime/no43_00000.png", xalign=0.5, yalign=0.5)
image no43_00089 = Image("anime/no43_00089.png", xalign=0.5, yalign=0.5)
image no44_00000 = Image("anime/no44_00000.png", xalign=0.5, yalign=0.5)
image no44_00119 = Image("anime/no44_00119.png", xalign=0.5, yalign=0.5)
image no45_00000 = Image("anime/no45_00000.png", xalign=0.5, yalign=0.5)
image no45_00150 = Image("anime/no45_00150.png", xalign=0.5, yalign=0.5)
image no46_00000 = Image("anime/no46_00000.png", xalign=0.5, yalign=0.5)
image no46_00089 = Image("anime/no46_00089.png", xalign=0.5, yalign=0.5)
image no47_00000 = Image("anime/no47_00000.png", xalign=0.5, yalign=0.5)
image no47_00119 = Image("anime/no47_00119.png", xalign=0.5, yalign=0.5)
image no48_00000 = Image("anime/no48_00000.png", xalign=0.5, yalign=0.5)
image no48_00179 = Image("anime/no48_00179.png", xalign=0.5, yalign=0.5)
image no49_00000 = Image("anime/no49_00000.png", xalign=0.5, yalign=0.5)
image no49_00119 = Image("anime/no49_00119.png", xalign=0.5, yalign=0.5)
image no50_00000 = Image("anime/no50_00000.png", xalign=0.5, yalign=0.5)
image no50_00089 = Image("anime/no50_00089.png", xalign=0.5, yalign=0.5)
image no51_00000 = Image("anime/no51_00000.png", xalign=0.5, yalign=0.5)
image no51_00119 = Image("anime/no51_00119.png", xalign=0.5, yalign=0.5)
image no52_00000 = Image("anime/no52_00000.png", xalign=0.5, yalign=0.5)
image no52_00089 = Image("anime/no52_00089.png", xalign=0.5, yalign=0.5)
image no53_00000 = Image("anime/no53_00000.png", xalign=0.5, yalign=0.5)
image no53_00209 = Image("anime/no53_00209.png", xalign=0.5, yalign=0.5)
image no54_00000 = Image("anime/no54_00000.png", xalign=0.5, yalign=0.5)
image no54_00059 = Image("anime/no54_00059.png", xalign=0.5, yalign=0.5)
image no55_00000 = Image("anime/no55_00000.png", xalign=0.5, yalign=0.5)
image no55_00059 = Image("anime/no55_00059.png", xalign=0.5, yalign=0.5)
image no56_00000 = Image("anime/no56_00000.png", xalign=0.5, yalign=0.5)
image no56_00119 = Image("anime/no56_00119.png", xalign=0.5, yalign=0.5)
image no57_00000 = Image("anime/no57_00000.png", xalign=0.5, yalign=0.5)
image no57_00119 = Image("anime/no57_00119.png", xalign=0.5, yalign=0.5)
image no58_00000 = Image("anime/no58_00000.png", xalign=0.5, yalign=0.5)
image no58_00059 = Image("anime/no58_00059.png", xalign=0.5, yalign=0.5)
image no59_00000 = Image("anime/no59_00000.png", xalign=0.5, yalign=0.5)
image no59_00073 = Image("anime/no59_00073.png", xalign=0.5, yalign=0.5)
image no59_00089 = Image("anime/no59_00089.png", xalign=0.5, yalign=0.5)
image no60_00000 = Image("anime/no60_00000.png", xalign=0.5, yalign=0.5)
image no60_00179 = Image("anime/no60_00179.png", xalign=0.5, yalign=0.5)
image no61_00000 = Image("anime/no61_00000.png", xalign=0.5, yalign=0.5)
image no61_00089 = Image("anime/no61_00089.png", xalign=0.5, yalign=0.5)
image no62_00000 = Image("anime/no62_00000.png", xalign=0.5, yalign=0.5)
#image no62_00149 = Image("anime/no62_00149.png", xalign=0.5, yalign=0.5)
image no62_00149 = Image("anime/no62_00149.png", xalign=0.5, yalign=0.5)
image no63_00000 = Image("anime/no63_00000.png", xalign=0.5, yalign=0.5)
image no63_00089 = Image("anime/no63_00089.png", xalign=0.5, yalign=0.5)
image no64_00000 = Image("anime/no64_00000.png", xalign=0.5, yalign=0.5)
image no64_00119 = Image("anime/no64_00119.png", xalign=0.5, yalign=0.5)
image no65_00000 = Image("anime/no65_00000.png", xalign=0.5, yalign=0.5)
image no65_00159 = Image("anime/no65_00159.png", xalign=0.5, yalign=0.5)
image no66_00000 = Image("anime/no66_00000.png", xalign=0.5, yalign=0.5)
image no66_00239 = Image("anime/no66_00239.png", xalign=0.5, yalign=0.5)
image no80_0001 = Image("anime/no80_0001.png", xalign=0.5, yalign=0.5)
image no80_0045 = Image("anime/no80_0045.png", xalign=0.5, yalign=0.5)
image no81_0001 = Image("anime/no81_0001.png", xalign=0.5, yalign=0.5)
image no81_0048 = Image("anime/no81_0048.png", xalign=0.5, yalign=0.5)
image no82_0001 = Image("anime/no82_0001.png", xalign=0.5, yalign=0.5)
image no82_0057 = Image("anime/no82_0057.png", xalign=0.5, yalign=0.5)
image no83_0001 = Image("anime/no83_0001.png", xalign=0.5, yalign=0.5)
image no83_0051 = Image("anime/no83_0051.png", xalign=0.5, yalign=0.5)
image no84_0001 = Image("anime/no84_0001.png", xalign=0.5, yalign=0.5)
image no84_0086 = Image("anime/no84_0086.png", xalign=0.5, yalign=0.5)
image no85_0001 = Image("anime/no85_0001.png", xalign=0.5, yalign=0.5)
image no85_0074 = Image("anime/no85_0074.png", xalign=0.5, yalign=0.5)

image c_c0401 a = "cg/c_c0401_a.png"
image c_c0401 b = "cg/c_c0401_b.png"
image c_c0401_wall = "cg/c_c0401_wall.png"
image c_c0401 la = "cg/c_c0401_la.png"
image c_c0401 lb = "cg/c_c0401_lb.png"
image c_c0401_lwall = "cg/c_c0401_lwall.png"
image c_c0402 a = "cg/c_c0402_a.png"
image c_c0402 b = "cg/c_c0402_b.png"
image c_c0402 c = "cg/c_c0402_c.png"
image c_c0402 d = "cg/c_c0402_d.png"
image c_c0402 e = "cg/c_c0402_e.png"
image c_c0402_wall = "cg/c_c0402_wall.png"
image c_c0402 la = "cg/c_c0402_la.png"
image c_c0402 lb = "cg/c_c0402_lb.png"
image c_c0402 lc = "cg/c_c0402_lc.png"
image c_c0402 ld = "cg/c_c0402_ld.png"
image c_c0402 le = "cg/c_c0402_le.png"
image c_c0402_lwall = "cg/c_c0402_lwall.png"
image c_c0403 a = "cg/c_c0403_a.png"
image c_c0403 b = "cg/c_c0403_b.png"
image c_c0403 c = "cg/c_c0403_c.png"
image c_c0403 d = "cg/c_c0403_d.png"
image c_c0403 e = "cg/c_c0403_e.png"
image c_c0403 f = "cg/c_c0403_f.png"
image c_c0403 la = "cg/c_c0403_la.png"
image c_c0403 lb = "cg/c_c0403_lb.png"
image c_c0403 lc = "cg/c_c0403_lc.png"
image c_c0403 ld = "cg/c_c0403_ld.png"
image c_c0403 le = "cg/c_c0403_le.png"
image c_c0403 lf = "cg/c_c0403_lf.png"
image c_c0404 a = "cg/c_c0404_a.png"
image c_c0404 b = "cg/c_c0404_b.png"
image c_c0404 c = "cg/c_c0404_c.png"
image c_c0404 d = "cg/c_c0404_d.png"
image c_c0404 e = "cg/c_c0404_e.png"
image c_c0404 f = "cg/c_c0404_f.png"
image c_c0404 la = "cg/c_c0404_la.png"
image c_c0404 lb = "cg/c_c0404_lb.png"
image c_c0404 lc = "cg/c_c0404_lc.png"
image c_c0404 ld = "cg/c_c0404_ld.png"
image c_c0404 le = "cg/c_c0404_le.png"
image c_c0404 lf = "cg/c_c0404_lf.png"
image c_c0901_a = "cg/c_c0901_a.png"
image c_c0901_b = "cg/c_c0901_b.png"
image c_c0901 ca = "cg/c_c0901_ca.png"
image c_c0901 cb = "cg/c_c0901_cb.png"
image c_c0902_a = "cg/c_c0902_a.png"
image c_e0103_la = "cg/c_e0103_la.png"
image c_e0305_a = "cg/c_e0305_a.png"
image c_e0305_b = "cg/c_e0305_b.png"
image c_e0305_c = "cg/c_e0305_c.png"
image c_e0305_d = "cg/c_e0305_d.png"
image c_e0305_la = "cg/c_e0305_la.png"
image c_e0305_lb = "cg/c_e0305_lb.png"
image c_e0305_lc = "cg/c_e0305_lc.png"
image c_e0305_ld = "cg/c_e0305_ld.png"
image c_e0406_a = "cg/c_e0406_a.png"
image c_e0406_b = "cg/c_e0406_b.png"
image c_e0406_c = "cg/c_e0406_c.png"
image c_e0406_d = "cg/c_e0406_d.png"
image c_e0406_e = "cg/c_e0406_e.png"
image c_e0406_f = "cg/c_e0406_f.png"
image c_e0903 a = "cg/c_e0903_a.png"
image c_e0903 b = "cg/c_e0903_b.png"
image c_e0903 c = "cg/c_e0903_c.png"
image c_e0903 d = "cg/c_e0903_d.png"
image c_e0903_wall = "cg/c_e0903_wall.png"
image c0101_a = "cg/c0101_a.png"
image c0101_b = "cg/c0101_b.png"
image c0101_c = "cg/c0101_c.png"
image c0201_a = "cg/c0201_a.png"
image c0201_b = "cg/c0201_b.png"
image c0201_c = "cg/c0201_c.png"
image c0201_d = "cg/c0201_d.png"
image c0201_e = "cg/c0201_e.png"
image c0201_f = "cg/c0201_f.png"
image c0202_a = "pettan/c0202_a.png"
image c0202_b = "pettan/c0202_b.png"
image c0203 ca = "cg/c0203_ca.png"
image c0203 cb = "cg/c0203_cb.png"
image c0203 cc = "cg/c0203_cc.png"
image c0203_cwall = "cg/c0203_cwall.png"
image c0203_cwall2 = "cg/c0203_cwall2.png"
image c0203 la = "cg/c0203_la.png"
image c0203 lb = "cg/c0203_lb.png"
image c0203 lc = "cg/c0203_lc.png"
image c0203_lwall = "cg/c0203_lwall.png"
image c0204 a = "cg/c0204_a.png"
image c0204 b = "cg/c0204_b.png"
image c0204 c = "cg/c0204_c.png"
image c0204 d = "cg/c0204_d.png"
image c0205 a = "cg/c0205_a.png"
image c0205 b = "cg/c0205_b.png"
image c0205 c = "cg/c0205_c.png"
image c0205_wall = "cg/c0205_wall.png"
image c0301 = "cg/c0301.png"
image c0302_a = "cg/c0302_a.png"
image c0302_b = "cg/c0302_b.png"
image c0303 = "cg/c0303.png"
image c0406 = "cg/c0406.png"
image c0901_b2 = Image("cg/c0901_b2.png", xalign=0.5, yalign=0.5)
image c0901_b3 = Image("cg/c0901_b3.png", xalign=0.5, yalign=0.5)
##Use im.Composite to combine wall?
image e0101 a = "cg/e0101_a.png"
image e0101 b = "cg/e0101_b.png"
image e0101 c = "cg/e0101_c.png"
image e0101_wall = "cg/e0101_wall.png"
image e0102 a = "cg/e0102_a.png"
image e0102 b = "cg/e0102_b.png"
image e0102 c = "cg/e0102_c.png"
image e0102 d = "cg/e0102_d.png"
image e0102_wall = "cg/e0102_wall.png"
image e0103 a = "cg/e0103_a.png"
image e0103 b = "cg/e0103_b.png"
image e0103 c = "cg/e0103_c.png"
image e0103 d = "cg/e0103_d.png"
image e0103_wall = "cg/e0103_wall.png"
image e0104_a = "cg/e0104_a.png"
image e0104_b = "cg/e0104_b.png"
image e0104_c = "cg/e0104_c.png"
image e0104_d = "cg/e0104_d.png"
image e0104_e = "cg/e0104_e.png"
image e0201 = "cg/e0201.png"
image e0301_a = "cg/e0301_a.png"
image e0301_b = "cg/e0301_b.png"
image e0301_c = "cg/e0301_c.png"
image e0401_a = "cg/e0401_a.png"
image e0401_b = "cg/e0401_b.png"
image e0404 = "cg/e0404.png"
image e0405 = "cg/e0405.png"
image e0406 = "cg/e0406.png"
image e0407 = "cg/e0407.png"
image e0901_a = "cg/e0901_a.png"
image e0901_b = "cg/e0901_b.png"
image e0901_c = "cg/e0901_c.png"
image e0902 = "cg/e0902.png"
image e0903_a = "cg/e0903_a.png"
image e0903_b = "cg/e0903_b.png"
image e0903_c = "cg/e0903_c.png"
image e0903a = "cg/e0903a.png"
image e0903d = "cg/e0903d.png"
image e0904_a = "cg/e0904_a.png"
image e0904_b = "cg/e0904_b.png"
image g0101 = "cg/g0101.png"
image g0102 = "cg/g0102.png"
image g0103 = "cg/g0103.png"
image g0201 = "cg/g0201.png"
image g0202 = "cg/g0202.png"
image g0203_a = "cg/g0203_a.png"
image g0203_b = "cg/g0203_b.png"
image g0301 = "cg/g0301.png"
image g0302 = "cg/g0302.png"
image g0401 = "cg/g0401.png"
image g0402 = "cg/g0402.png"
image g0403 = "cg/g0403.png"
image g0404 = "cg/g0404.png"

image cg_c0203_la = "cgmode/cg_c0203_la.png"
image cg_c0203_lb = "cgmode/cg_c0203_lb.png"
image cg_c0203_lc = "cgmode/cg_c0203_lc.png"
image cg_c0204_a = "cgmode/cg_c0204_a.png"
image cg_c0204_b = "cgmode/cg_c0204_b.png"
image cg_c0204_c = "cgmode/cg_c0204_c.png"
image cg_c0204_d = "cgmode/cg_c0204_d.png"
image cg_c0205_a = "cgmode/cg_c0205_a.png"
image cg_c0205_b = "cgmode/cg_c0205_b.png"
image cg_c0205_c = "cgmode/cg_c0205_c.png"
image cg_c0401_la = "cgmode/cg_c0401_la.png"
image cg_c0401_lb = "cgmode/cg_c0401_lb.png"
image cg_c0402_la = "cgmode/cg_c0402_la.png"
image cg_c0402_lb = "cgmode/cg_c0402_lb.png"
image cg_c0402_lc = "cgmode/cg_c0402_lc.png"
image cg_c0402_ld = "cgmode/cg_c0402_ld.png"
image cg_c0402_le = "cgmode/cg_c0402_le.png"
image cg_c0403_a = "cgmode/cg_c0403_a.png"
image cg_c0403_b = "cgmode/cg_c0403_b.png"
image cg_c0403_c = "cgmode/cg_c0403_c.png"
image cg_c0403_d = "cgmode/cg_c0403_d.png"
image cg_c0403_e = "cgmode/cg_c0403_e.png"
image cg_c0403_f = "cgmode/cg_c0403_f.png"
image cg_c0404_a = "cgmode/cg_c0404_a.png"
image cg_c0404_b = "cgmode/cg_c0404_b.png"
image cg_c0404_c = "cgmode/cg_c0404_c.png"
image cg_c0404_d = "cgmode/cg_c0404_d.png"
image cg_c0404_e = "cgmode/cg_c0404_e.png"
image cg_c0404_f = "cgmode/cg_c0404_f.png"
image cg_c0901_a = "cgmode/cg_c0901_a.png"
image cg_c0901_b = "cgmode/cg_c0901_b.png"
image cg_c0902_a = "cgmode/cg_c0902_a.png"
image cg_e0101_a = "cgmode/cg_e0101_a.png"
image cg_e0101_b = "cgmode/cg_e0101_b.png"
image cg_e0101_c = "cgmode/cg_e0101_c.png"
image cg_e0102_a = "cgmode/cg_e0102_a.png"
image cg_e0102_b = "cgmode/cg_e0102_b.png"
image cg_e0102_c = "cgmode/cg_e0102_c.png"
image cg_e0102_d = "cgmode/cg_e0102_d.png"
image cg_e0103_a = "cgmode/cg_e0103_a.png"
image cg_e0103_b = "cgmode/cg_e0103_b.png"
image cg_e0103_c = "cgmode/cg_e0103_c.png"
image cg_e0103_d = "cgmode/cg_e0103_d.png"
image cg_e0305_la = "cgmode/cg_e0305_la.png"
image cg_e0305_lb = "cgmode/cg_e0305_lb.png"
image cg_e0305_lc = "cgmode/cg_e0305_lc.png"
image cg_e0305_ld = "cgmode/cg_e0305_ld.png"
image cg_e0406_a = "cgmode/cg_e0406_a.png"
image cg_e0406_b = "cgmode/cg_e0406_b.png"
image cg_e0406_c = "cgmode/cg_e0406_c.png"
image cg_e0406_d = "cgmode/cg_e0406_d.png"
image cg_e0406_e = "cgmode/cg_e0406_e.png"
image cg_e0406_f = "cgmode/cg_e0406_f.png"
image cg_e0903_a = "cgmode/cg_e0903_a.png"
image cg_e0903_b = "cgmode/cg_e0903_b.png"
image cg_e0903_c = "cgmode/cg_e0903_c.png"
image cg_e0903_d = "cgmode/cg_e0903_d.png"
image congra = "cgmode/congra.png"
image package01 = "cgmode/package01.png"
image package02 = "cgmode/package02.png"
image portrait_ep1 = "cgmode/portrait_ep1.png"
image portrait_ep2 = "cgmode/portrait_ep2.png"
image portrait_ep3 = "cgmode/portrait_ep3.png"
image portrait_ep4 = "cgmode/portrait_ep4.png"

image ss_1a = Image("background/efe/1a.png", xalign=0.5, yalign=0.5)
image ss_1b = Image("background/efe/1b.png", xalign=0.5, yalign=0.5)
image ss_1c = Image("background/efe/1c.png", xalign=0.5, yalign=0.5)
image ss_1d = Image("background/efe/1d.png", xalign=0.5, yalign=0.5)
image ss_1e = Image("background/efe/1e.png", xalign=0.5, yalign=0.5)
image ss_1f = Image("background/efe/1f.png", xalign=0.5, yalign=0.5)
image ss_1g = Image("background/efe/1g.png", xalign=0.5, yalign=0.5)
image armor1 = Image("background/efe/armor1.png", xalign=0.5, yalign=0.5)
image armor2 = Image("background/efe/armor2.png", xalign=0.5, yalign=0.5)
image armor3 = Image("background/efe/armor3.png", xalign=0.5, yalign=0.5)
image armor4 = Image("background/efe/armor4.png", xalign=0.5, yalign=0.5)
image armor5 = Image("background/efe/armor5.png", xalign=0.5, yalign=0.5)
image armor6 = Image("background/efe/armor6.png", xalign=0.5, yalign=0.5)
image armor7b = Image("background/efe/armor7b.png", xalign=0.5, yalign=0.5)
image barrier = Image("background/efe/barrier.png", xalign=0.5, yalign=0.5)
image barrier1 = Image("background/efe/barrier1.png", xalign=0.5, yalign=0.5)
image barrier1p = Image("background/efe/barrier1p.png", xalign=0.5, yalign=0.5)
image barrierbrake1 = Image("background/efe/barrierbrake1.png", xalign=0.5, yalign=0.5)
image barrierbrake1p = Image("background/efe/barrierbrake1p.png", xalign=0.5, yalign=0.5)
image barrierbrake1p1 = Image("background/efe/barrierbrake1p1.png", xalign=0.5, yalign=0.5)
image barrierbrake1p2 = Image("background/efe/barrierbrake1p2.png", xalign=0.5, yalign=0.5)
image barrierbrake1p3 = Image("background/efe/barrierbrake1p3.png", xalign=0.5, yalign=0.5)
image barrierbrake1p4 = Image("background/efe/barrierbrake1p4.png", xalign=0.5, yalign=0.5)
image barrierbrake1p6 = Image("background/efe/barrierbrake1p6.png", xalign=0.5, yalign=0.5)
image barrierbrake2 = Image("background/efe/barrierbrake2.png", xalign=0.5, yalign=0.5)
image barrierbrake2p1 = Image("background/efe/barrierbrake2p1.png", xalign=0.5, yalign=0.5)
image barrierbrake2p2 = Image("background/efe/barrierbrake2p2.png", xalign=0.5, yalign=0.5)
image barrierbrake2p3 = Image("background/efe/barrierbrake2p3.png", xalign=0.5, yalign=0.5)
image barrierbrake2p4 = Image("background/efe/barrierbrake2p4.png", xalign=0.5, yalign=0.5)
image barrierbrake2p5 = Image("background/efe/barrierbrake2p5.png", xalign=0.5, yalign=0.5)
image bite = Image("background/efe/bite.png", xalign=0.5, yalign=0.5)
image black = Image("background/efe/black.png", xalign=0.5, yalign=0.5)
image black2 = Image("background/efe/black2.png", xalign=0.5, yalign=0.5)
image black3 = Image("background/efe/black3.png", xalign=0.5, yalign=0.5)
image blade1p = Image("background/efe/blade1p.png", xalign=0.5, yalign=0.5)
image blade1r = Image("background/efe/blade1r.png", xalign=0.5, yalign=0.5)
image blade2p = Image("background/efe/blade2p.png", xalign=0.5, yalign=0.5)
image blade2r = Image("background/efe/blade2r.png", xalign=0.5, yalign=0.5)
image blade3p = Image("background/efe/blade3p.png", xalign=0.5, yalign=0.5)
image blade3r = Image("background/efe/blade3r.png", xalign=0.5, yalign=0.5)
image blade4p = Image("background/efe/blade4p.png", xalign=0.5, yalign=0.5)
image blade4r = Image("background/efe/blade4r.png", xalign=0.5, yalign=0.5)
image blade5p = Image("background/efe/blade5p.png", xalign=0.5, yalign=0.5)
image blade5r = Image("background/efe/blade5r.png", xalign=0.5, yalign=0.5)
image blade6_1p = Image("background/efe/blade6_1p.png", xalign=0.5, yalign=0.5)
image blade6_1r = Image("background/efe/blade6_1r.png", xalign=0.5, yalign=0.5)
image blade6_2p = Image("background/efe/blade6_2p.png", xalign=0.5, yalign=0.5)
image blade6_2r = Image("background/efe/blade6_2r.png", xalign=0.5, yalign=0.5)
image blade7_1r = Image("background/efe/blade7_1r.png", xalign=0.5, yalign=0.5)
image blade7_2r = Image("background/efe/blade7_2r.png", xalign=0.5, yalign=0.5)
image blood_1a = Image("background/efe/blood_1a.png", xalign=0.5, yalign=0.5)
image blood_1ar = Image("background/efe/blood_1ar.png", xalign=0.5, yalign=0.5)
image blood_1b = Image("background/efe/blood_1b.png", xalign=0.5, yalign=0.5)
image blood_2a = Image("background/efe/blood_2a.png", xalign=0.5, yalign=0.5)
image blood_2b = Image("background/efe/blood_2b.png", xalign=0.5, yalign=0.5)
image blood_2c = Image("background/efe/blood_2c.png", xalign=0.5, yalign=0.5)
image blood_2d = Image("background/efe/blood_2d.png", xalign=0.5, yalign=0.5)
image blood_2e = Image("background/efe/blood_2e.png", xalign=0.5, yalign=0.5)
image blue = Image("background/efe/blue.png", xalign=0.5, yalign=0.5)
image book1 = Image("background/efe/book1.png", xalign=0.5, yalign=0.5)
image bul2 = Image("background/efe/bul2.png", xalign=0.5, yalign=0.5)
image bullet_1a = Image("background/efe/bullet_1a.png", xalign=0.5, yalign=0.5)
image bullet_1b = Image("background/efe/bullet_1b.png", xalign=0.5, yalign=0.5)
image bullet_1c = Image("background/efe/bullet_1c.png", xalign=0.5, yalign=0.5)
image bullet_1d = Image("background/efe/bullet_1d.png", xalign=0.5, yalign=0.5)
image bullet_1e = Image("background/efe/bullet_1e.png", xalign=0.5, yalign=0.5)
image bullet1a = Image("background/efe/bullet1a.png", xalign=0.5, yalign=0.5)
image bullet1b = Image("background/efe/bullet1b.png", xalign=0.5, yalign=0.5)
image bullet1c = Image("background/efe/bullet1c.png", xalign=0.5, yalign=0.5)
image bullet2a = Image("background/efe/bullet2a.png", xalign=0.5, yalign=0.5)
image bullet2b = Image("background/efe/bullet2b.png", xalign=0.5, yalign=0.5)
image butterfly_1a = "background/efe/butterfly_1a.png"
image butterfly_2a = "background/efe/butterfly_2a.png"
image butterfly_3a = "background/efe/butterfly_3a.png"
image butterfly_3x = "background/efe/butterfly_3x.png"
image butterfly_4a = "background/efe/butterfly_4a.png"
image butterfly_4sp1 = "background/efe/butterfly_4sp1.png"
image butterfly_4sp1r = "background/efe/butterfly_4sp1r.png"
image butterfly_4sp2 = "background/efe/butterfly_4sp2.png"
image butterfly_4sp2r = "background/efe/butterfly_4sp2r.png"
image different_space_1a = Image("background/efe/different_space_1a.png", xalign=0.5, yalign=0.5)
image different_space_1c = Image("background/efe/different_space_1c.png", xalign=0.5, yalign=0.5)
image different_space_1cf = Image("background/efe/different_space_1cf.png", xalign=0.5, yalign=0.5)
image different_space_p1a = Image("background/efe/different_space_p1a.png", xalign=0.5, yalign=0.5)
image different_space_p1b = Image("background/efe/different_space_p1b.png", xalign=0.5, yalign=0.5)
image different_spiral_1a = Image("background/efe/different_spiral_1a.png", xalign=0.5, yalign=0.5)
image chess1 = Image("background/efe/chess1.png", xalign=0.5, yalign=0.5)
image end_1a = "background/efe/end_1a.png"
image end_1a_1 = "background/efe/end_1a_1.png"
image end_1a_2 = "background/efe/end_1a_2.png"
image end_1a_3 = "background/efe/end_1a_3.png"
image end_1a_4 = "background/efe/end_1a_4.png"
image end_1a_5 = "background/efe/end_1a_5.png"
image end_1a_6 = "background/efe/end_1a_6.png"
image end_1a_7 = "background/efe/end_1a_7.png"
image end_1a_8 = "background/efe/end_1a_8.png"
image end_1b = "background/efe/end_1b.png"
image end_1b_en = "background/efe/end_1b_en.png"
image end_1c = "background/efe/end_1c.png"              ##original
image end_1c2 = "background/efe/end_1c2.png"            ##edited
image end_1d = "background/efe/end_1d.png"
image end_2a = "background/efe/end_2a.png"
image end_2b = "background/efe/end_2b.png"
image end_2c = "background/efe/end_2c.png"
image end_2d = "background/efe/end_2d.png"
image end_3a = "background/efe/end_3a.png"
image end_3b = "background/efe/end_3b.png"
image end_4a = "background/efe/end_4a.png"
image end_4b = "background/efe/end_4b.png"
image enj_mirai01 = "background/efe/enj_mirai01.png"
image ep2_text = "background/efe/ep2_text.png"
image ep4_meta_1 = "background/efe/ep4_meta_1.png"
image ep4_meta_2 = "background/efe/ep4_meta_2.png"
image ep4last00 = "background/efe/ep4last00.png"
image ep4last01 = "background/efe/ep4last01.png"
image ep4last02 = "background/efe/ep4last02.png"
image ep4last03 = "background/efe/ep4last03.png"
image ep4last04 = "background/efe/ep4last04.png"
image ep4last05 = "background/efe/ep4last05.png"
image ep4last06 = "background/efe/ep4last06.png"
image ep4last07 = "background/efe/ep4last07.png"
image ep4last08 = "background/efe/ep4last08.png"
image ep4last09 = "background/efe/ep4last09.png"
image goa_memory1 = "background/efe/goa_memory1.png"
image goa_memory2 = "background/efe/goa_memory2.png"
image goa_memory3 = "background/efe/goa_memory3.png"
image goa_memory4 = "background/efe/goa_memory4.png"
image gold1 = Image("background/efe/gold1.png", xalign=0.5, yalign=0.5)
image gold2 = Image("background/efe/gold2.png", xalign=0.5, yalign=0.5)
image grimoire1 = "background/efe/grimoire1.png"
image hana1 = "background/efe/hana1.png"                ## in-game meta
image hana1_ = "background/efe/hana1_.png"              ## menu/chapter end?/etc.
image homing1 = Image("background/efe/homing1.png", xalign=0.5, yalign=0.5)
image homing1r = Image("background/efe/homing1r.png", xalign=0.5, yalign=0.5)
image homing1s = Image("background/efe/homing1s.png", xalign=0.5, yalign=0.5)
image homing1sr = Image("background/efe/homing1sr.png", xalign=0.5, yalign=0.5)
image homing2 = Image("background/efe/homing2.png", xalign=0.5, yalign=0.5)
image homing2r = Image("background/efe/homing2r.png", xalign=0.5, yalign=0.5)
image homing2s = Image("background/efe/homing2s.png", xalign=0.5, yalign=0.5)
image homing2sr = Image("background/efe/homing2sr.png", xalign=0.5, yalign=0.5)
image homing3 = Image("background/efe/homing3.png", xalign=0.5, yalign=0.5)
image homing3r = Image("background/efe/homing3r.png", xalign=0.5, yalign=0.5)
image homing3s = Image("background/efe/homing3s.png", xalign=0.5, yalign=0.5)
image homing3sr = Image("background/efe/homing3sr.png", xalign=0.5, yalign=0.5)
image homing4 = Image("background/efe/homing4.png", xalign=0.5, yalign=0.5)
image homing4r = Image("background/efe/homing4r.png", xalign=0.5, yalign=0.5)
image homing4s = Image("background/efe/homing4s.png", xalign=0.5, yalign=0.5)
image homing4sr = Image("background/efe/homing4sr.png", xalign=0.5, yalign=0.5)
image homing5 = Image("background/efe/homing5.png", xalign=0.5, yalign=0.5)
image homing5r = Image("background/efe/homing5r.png", xalign=0.5, yalign=0.5)
image homing5s = Image("background/efe/homing5s.png", xalign=0.5, yalign=0.5)
image homing5sr = Image("background/efe/homing5sr.png", xalign=0.5, yalign=0.5)
image homing6 = Image("background/efe/homing6.png", xalign=0.5, yalign=0.5)
image homing6bs = Image("background/efe/homing6bs.png", xalign=0.5, yalign=0.5)
image homing6bsr = Image("background/efe/homing6bsr.png", xalign=0.5, yalign=0.5)
image homing6r = Image("background/efe/homing6r.png", xalign=0.5, yalign=0.5)
image homing6s = Image("background/efe/homing6s.png", xalign=0.5, yalign=0.5)
image homing6sr = Image("background/efe/homing6sr.png", xalign=0.5, yalign=0.5)
image homing7 = Image("background/efe/homing7.png", xalign=0.5, yalign=0.5)
image homing7bs = Image("background/efe/homing7bs.png", xalign=0.5, yalign=0.5)
image homing7bsr = Image("background/efe/homing7bsr.png", xalign=0.5, yalign=0.5)
image homing7r = Image("background/efe/homing7r.png", xalign=0.5, yalign=0.5)
image homing7s = Image("background/efe/homing7s.png", xalign=0.5, yalign=0.5)
image homing7sr = Image("background/efe/homing7sr.png", xalign=0.5, yalign=0.5)
image javelin1a = Image("background/efe/javelin1a.png", xalign=0.5, yalign=0.5)
#image javelin1b = Image("background/efe/javelin1b.png", xalign=0.5, yalign=0.5)         # no38_bgm
image javelin1c = Image("background/efe/javelin1c.png", xalign=0.5, yalign=0.5)
#image javelin1d = Image("background/efe/javelin1d.png", xalign=0.5, yalign=0.5)         # no38_00149
image key1 = Image("background/efe/key1.png", xalign=0.5, yalign=0.5)
image key2 = Image("background/efe/key2.png", xalign=0.5, yalign=0.5)
image letter1 = Image("background/efe/letter1.png", xalign=0.5, yalign=0.5)
image magicsquare_gap = "background/efe/magicsquare_gap.png"
image magicsquare_mars3 = "background/efe/magicsquare_mars3.png"
image magicsquare_mars5 = "background/efe/magicsquare_mars5.png"
image magicsquare_moon1 = "background/efe/magicsquare_moon1.png"
image magicsquare_sun7 = "background/efe/magicsquare_sun7.png"
image map01 = "background/efe/map01.png"
image map02 = "background/efe/map02.png"
image map03 = "background/efe/map03.png"
image map04 = "background/efe/map04.png"
image map05 = "background/efe/map05.png"
image map06 = "background/efe/map06.png"
image map07 = "background/efe/map07.png"
image map08 = "background/efe/map08.png"
image map09 = "background/efe/map09.png"
image map10 = "background/efe/map10.png"
image map10b = "background/efe/map10b.png"
image map10c = "background/efe/map10c.png"
image nails1 = "background/efe/nails1.png"
image note1 = Image("background/efe/note1.png", xalign=0.5, yalign=0.5)
image number = "background/efe/number.png"
image oct_4_1986 = "background/efe/oct_4_1986.png"
image oct_4_1998 = "background/efe/oct_4_1998.png"
image oct_4_1998b = "background/efe/oct_4_1998b.png"
image oct_4_1998c = "background/efe/oct_4_1998c.png"
image oct_5_1986 = "background/efe/oct_5_1986.png"
image oct_1998 = "background/efe/oct_1998.png"
image od = "background/efe/od.png"
image op0101 = "background/efe/op0101.png"
image op0102 = "background/efe/op0102.png"
image op0103 = "background/efe/op0103.png"
image op0104 = "background/efe/op0104.png"
image op0105 = "background/efe/op0105.png"
image op0106 = "background/efe/op0106.png"
image op0107 = "background/efe/op0107.png"
image op0108 = "background/efe/op0108.png"
image op0201 = "background/efe/op0201.png"
image op0202 = "background/efe/op0202.png"
image op0203 = "background/efe/op0203.png"
image op0204 = "background/efe/op0204.png"
image op0205 = "background/efe/op0205.png"
image op0206 = "background/efe/op0206.png"
image op0207 = "background/efe/op0207.png"
image op0208 = "background/efe/op0208.png"
image pumpkin2 = Image("background/efe/pumpkin2.png", xalign=0.5, yalign=0.5)
image purgatorio = "background/efe/purgatorio.png"
image red = Image("background/efe/red.png", xalign=0.5, yalign=0.5)
image red_b = Image("background/efe/red_b.png", xalign=0.5, yalign=0.5)
image sakutaro1a = Image("background/efe/sakutaro1a.png", xalign=0.5, yalign=0.5)
image sakutaro1ab = Image("background/efe/sakutaro1ab.png", xalign=0.5, yalign=0.5)
image sakutaro1b = Image("background/efe/sakutaro1b.png", xalign=0.5, yalign=0.5)
image sakutaro1bb = Image("background/efe/sakutaro1bb.png", xalign=0.5, yalign=0.5)
image sakutaro2a = Image("background/efe/sakutaro2a.png", xalign=0.5, yalign=0.5)
image sakutaro2ab = Image("background/efe/sakutaro2ab.png", xalign=0.5, yalign=0.5)
image sakutaro2b = Image("background/efe/sakutaro2b.png", xalign=0.5, yalign=0.5)
image sakutaro2bb = Image("background/efe/sakutaro2bb.png", xalign=0.5, yalign=0.5)
image sweet1 = Image("background/efe/sweet1.png", xalign=0.5, yalign=0.5)
image sweet2 = Image("background/efe/sweet2.png", xalign=0.5, yalign=0.5)
image system1 = "background/efe/system1.png"
image system2 = "background/efe/system2.png"
image system3 = "background/efe/system3.png"
image system4 = "background/efe/system4.png"
image system5 = "background/efe/system5.png"
image tel1a = Image("background/efe/tel1a.png", xalign=0.5, yalign=0.5)
image text001 = "background/efe/text001.png"
image text002 = "background/efe/text002.png"
image text003 = "background/efe/text003.png"
image text003a = "background/efe/text003a.png"
image text003b = "background/efe/text003b.png"
image text004 = "background/efe/text004.png"
image text005 = "background/efe/text005.png"
image text006 = "background/efe/text006.png"
image text007 = "background/efe/text007.png"
image text010 = "background/efe/text010.png"
image text010a = "background/efe/text010a.png"
image text010b = "background/efe/text010b.png"
image text010c = "background/efe/text010c.png"
image text011 = "background/efe/text011.png"
image text011_r = "background/efe/text011_r.png"
image text011 = "background/efe/text011.png"
image text012 = "background/efe/text012.png"
image text012_r = "background/efe/text012_r.png"
image tower1 = "background/efe/tower1.png"
image tower2 = "background/efe/tower2.png"
image tower2r = "background/efe/tower2r.png"
image tower4 = "background/efe/tower4.png"
image unknown01 = "background/efe/unknown01.png"
image white = Image("background/efe/white.png", xalign=0.5, yalign=0.5)
image white_waku = Image("background/efe/white_waku.png", xalign=0.5, yalign=0.5)

image end_5d = "background/efe/t/end_5d.png"
image ep606_2 = "background/efe/t/ep606_2.png"
image ep606_3 = "background/efe/t/ep606_3.png"
image title_dawn = "background/efe/t/title_dawn.png"
image title_end = "background/efe/t/title_end.png"
image wsan_1a = "background/efe/t/wsan_1a.png"
image wsan_1b = "background/efe/t/wsan_1b.png"

image air_in1a = Image("background/airport/air_in1a.png", xalign=0.5, yalign=0.5)
image air_in1e = Image("background/airport/air_in1e.png", xalign=0.5, yalign=0.5)
image air_in1ec = Image("background/airport/air_in1ec.png", xalign=0.5, yalign=0.5)
image air_in1ec_bg = Image("background/airport/air_in1ec_bg.png", xalign=0.5, yalign=0.5)
image air_t1a = Image("background/airport/air_t1a.png", xalign=0.5, yalign=0.5)
image air_out1a = Image("background/airport/air_out1a.png", xalign=0.5, yalign=0.5)
image air_out2a = Image("background/airport/air_out2a.png", xalign=0.5, yalign=0.5)
image air_out2b = Image("background/airport/air_out2b.png", xalign=0.5, yalign=0.5)
image air_out2bc = Image("background/airport/air_out2bc.png", xalign=0.5, yalign=0.5)
image airp_in1a = Image("background/airport/airp_in1a.png", xalign=0.5, yalign=0.5)
image airp_out1a = Image("background/airport/airp_out1a.png", xalign=0.5, yalign=0.5)
image airp_out2a = Image("background/airport/airp_out2a.png", xalign=0.5, yalign=0.5)
image airp_out2b = Image("background/airport/airp_out2b.png", xalign=0.5, yalign=0.5)
image airp_w1a = Image("background/airport/airp_w1a.png", xalign=0.5, yalign=0.5)
image airp_w1b = Image("background/airport/airp_w1b.png", xalign=0.5, yalign=0.5)
image airp_w1bc = Image("background/airport/airp_w1bc.png", xalign=0.5, yalign=0.5)
image airp_w1bc_bg = Image("background/airport/airp_w1bc_bg.png", xalign=0.5, yalign=0.5)
image airp_w1c = Image("background/airport/airp_w1c.png", xalign=0.5, yalign=0.5)
image airp_w1cc = Image("background/airport/airp_w1cc.png", xalign=0.5, yalign=0.5)
image airp_w1cc_bg = Image("background/airport/airp_w1cc_bg.png", xalign=0.5, yalign=0.5)
image airp_w1d = Image("background/airport/airp_w1d.png", xalign=0.5, yalign=0.5)
image airp_w1j = Image("background/airport/airp_w1j.png", xalign=0.5, yalign=0.5)
image airp_w1k = Image("background/airport/airp_w1k.png", xalign=0.5, yalign=0.5)
image car_i1a = Image("background/airport/car_i1a.png", xalign=0.5, yalign=0.5)
image car_i1ac = Image("background/airport/car_i1ac.png", xalign=0.5, yalign=0.5)
image car_i1ac_bg = Image("background/airport/car_i1ac_bg.png", xalign=0.5, yalign=0.5)
image car_i3b = Image("background/airport/car_i3b.png", xalign=0.5, yalign=0.5)
image car_i3b2 = "background/airport/car_i3b2.png"
image car_i3c = Image("background/airport/car_i3c.png", xalign=0.5, yalign=0.5)
image car_i3c2 = "background/airport/car_i3c2.png"
image car_o2a = Image("background/airport/car_o2a.png", xalign=0.5, yalign=0.5)
image car_o2c = Image("background/airport/car_o2c.png", xalign=0.5, yalign=0.5)

image aqu_i1a = Image("background/aquarium/aqu_i1a.png", xalign=0.5, yalign=0.5)
image aqu_i2a = Image("background/aquarium/aqu_i2a.png", xalign=0.5, yalign=0.5)
image aqu_i2b = Image("background/aquarium/aqu_i2b.png", xalign=0.5, yalign=0.5)
image aqu_i2bg = Image("background/aquarium/aqu_i2bg.png", xalign=0.5, yalign=0.5)

image cha_i1a = Image("background/chapel/cha_i1a.png", xalign=0.5, yalign=0.5)
image cha_i1a_bg = Image("background/chapel/cha_i1a_bg.png", xalign=0.5, yalign=0.5)
image cha_i1af = Image("background/chapel/cha_i1af.png", xalign=0.5, yalign=0.5)
image cha_i1an = Image("background/chapel/cha_i1an.png", xalign=0.5, yalign=0.5)
image cha_i1an_bg = Image("background/chapel/cha_i1an_bg.png", xalign=0.5, yalign=0.5)
image cha_i1ar = Image("background/chapel/cha_i1ar.png", xalign=0.5, yalign=0.5)
image cha_i1ar_bg = Image("background/chapel/cha_i1ar_bg.png", xalign=0.5, yalign=0.5)
image cha_i1d = Image("background/chapel/cha_i1d.png", xalign=0.5, yalign=0.5)
image cha_i1d_bg = Image("background/chapel/cha_i1d_bg.png", xalign=0.5, yalign=0.5)
image cha_i1df = Image("background/chapel/cha_i1df.png", xalign=0.5, yalign=0.5)
image cha_i1dn = Image("background/chapel/cha_i1dn.png", xalign=0.5, yalign=0.5)
image cha_i1dn_bg = Image("background/chapel/cha_i1dn_bg.png", xalign=0.5, yalign=0.5)
image cha_i1dr = Image("background/chapel/cha_i1dr.png", xalign=0.5, yalign=0.5)
image cha_i1dr_bg = Image("background/chapel/cha_i1dr_bg.png", xalign=0.5, yalign=0.5)
image cha_i1e = Image("background/chapel/cha_i1e.png", xalign=0.5, yalign=0.5)
image cha_i1e_bg = Image("background/chapel/cha_i1e_bg.png", xalign=0.5, yalign=0.5)
image cha_i1ef = Image("background/chapel/cha_i1ef.png", xalign=0.5, yalign=0.5)
image cha_i1en = Image("background/chapel/cha_i1en.png", xalign=0.5, yalign=0.5)
image cha_i1en_bg = Image("background/chapel/cha_i1en_bg.png", xalign=0.5, yalign=0.5)
image cha_i1er = Image("background/chapel/cha_i1er.png", xalign=0.5, yalign=0.5)
image cha_i1er_bg = Image("background/chapel/cha_i1er_bg.png", xalign=0.5, yalign=0.5)
image cha_o1a = Image("background/chapel/cha_o1a.png", xalign=0.5, yalign=0.5)
image cha_o1af = Image("background/chapel/cha_o1af.png", xalign=0.5, yalign=0.5)
image cha_o1an = Image("background/chapel/cha_o1an.png", xalign=0.5, yalign=0.5)
image cha_o2a = Image("background/chapel/cha_o2a.png", xalign=0.5, yalign=0.5)
image cha_o2af = Image("background/chapel/cha_o2af.png", xalign=0.5, yalign=0.5)
image cha_o2an = Image("background/chapel/cha_o2an.png", xalign=0.5, yalign=0.5)

image amu_i1a = Image("background/city/amu_i1a.png", xalign=0.5, yalign=0.5)
image bui_inf1a = Image("background/city/bui_inf1a.png", xalign=0.5, yalign=0.5)
image bui_o1a = Image("background/city/bui_o1a.png", xalign=0.5, yalign=0.5)
image bui_o2a = Image("background/city/bui_o2a.png", xalign=0.5, yalign=0.5)
image bui_o2b = Image("background/city/bui_o2b.png", xalign=0.5, yalign=0.5)
image bui_r1a = Image("background/city/bui_r1a.png", xalign=0.5, yalign=0.5)
image bui_r1d = Image("background/city/bui_r1d.png", xalign=0.5, yalign=0.5)
image bui_r1e = Image("background/city/bui_r1e.png", xalign=0.5, yalign=0.5)
image cit_1a = Image("background/city/cit_1a.png", xalign=0.5, yalign=0.5)
image cit_1ar = Image("background/city/cit_1ar.png", xalign=0.5, yalign=0.5)
image cit_2a = Image("background/city/cit_2a.png", xalign=0.5, yalign=0.5)
image cit_2b = Image("background/city/cit_2b.png", xalign=0.5, yalign=0.5)
image cit_3a = Image("background/city/cit_3a.png", xalign=0.5, yalign=0.5)
image cof_1a = Image("background/city/cof_1a.png", xalign=0.5, yalign=0.5)
image con_i1a = Image("background/city/con_i1a.png", xalign=0.5, yalign=0.5)
image hos_p1b = Image("background/city/hos_p1b.png", xalign=0.5, yalign=0.5)
image hos_r1a = Image("background/city/hos_r1a.png", xalign=0.5, yalign=0.5)
image hos_r1am = Image("background/city/hos_r1am.png", xalign=0.5, yalign=0.5)
image hos_r1c = Image("background/city/hos_r1c.png", xalign=0.5, yalign=0.5)
image hos_r1cm = Image("background/city/hos_r1cm.png", xalign=0.5, yalign=0.5)
image hot_r1a = Image("background/city/hot_r1a.png", xalign=0.5, yalign=0.5)
image hot_r1c = Image("background/city/hot_r1c.png", xalign=0.5, yalign=0.5)
image off_1a = Image("background/city/off_1a.png", xalign=0.5, yalign=0.5)
image par_1a = Image("background/city/par_1a.png", xalign=0.5, yalign=0.5)
image par_1c = Image("background/city/par_1c.png", xalign=0.5, yalign=0.5)
image pro_o1a = Image("background/city/pro_o1a.png", xalign=0.5, yalign=0.5)
image sta_1a = Image("background/city/sta_1a.png", xalign=0.5, yalign=0.5)
image tra_1a = Image("background/city/tra_1a.png", xalign=0.5, yalign=0.5)
image tra_1b = Image("background/city/tra_1b.png", xalign=0.5, yalign=0.5)

image fea_r1ap = Image("background/fea/fea_r1ap.png", xalign=0.5, yalign=0.5)
image fea_r1c = Image("background/fea/fea_r1c.png", xalign=0.5, yalign=0.5)

image beach_1a = Image("background/forest/beach_1a.png", xalign=0.5, yalign=0.5)
image beach_1af = Image("background/forest/beach_1af.png", xalign=0.5, yalign=0.5)
image beach_2a = Image("background/forest/beach_2a.png", xalign=0.5, yalign=0.5)
image beach_2af = Image("background/forest/beach_2af.png", xalign=0.5, yalign=0.5)
image beach_l1a = "background/forest/beach_l1a.png"
image beach_l1ac = "background/forest/beach_l1ac.png"
image beach_l1ac2 = "background/forest/beach_l1ac2.png"
image beach_l1an = "background/forest/beach_l1an.png"
image beach_l2a = "background/forest/beach_l2a.png"
image beach_s1a = Image("background/forest/beach_s1a.png", xalign=0.5, yalign=0.5)
image beach_s1af = Image("background/forest/beach_s1af.png", xalign=0.5, yalign=0.5)
image beach_s1an = Image("background/forest/beach_s1an.png", xalign=0.5, yalign=0.5)
image beach_s2a = Image("background/forest/beach_s2a.png", xalign=0.5, yalign=0.5)
image beach_s2af = Image("background/forest/beach_s2af.png", xalign=0.5, yalign=0.5)
image beach_s2an = Image("background/forest/beach_s2an.png", xalign=0.5, yalign=0.5)
image cliff_1a = Image("background/forest/cliff_1a.png", xalign=0.5, yalign=0.5)
image cliff_1b = Image("background/forest/cliff_1b.png", xalign=0.5, yalign=0.5)
image forest_p1a = Image("background/forest/forest_p1a.png", xalign=0.5, yalign=0.5)
image forest_p1af = Image("background/forest/forest_p1af.png", xalign=0.5, yalign=0.5)
image forest_p1an = Image("background/forest/forest_p1an.png", xalign=0.5, yalign=0.5)
image forest_p1ar = Image("background/forest/forest_p1ar.png", xalign=0.5, yalign=0.5)
image forest_p1b = Image("background/forest/forest_p1b.png", xalign=0.5, yalign=0.5)
image forest_p1bf = Image("background/forest/forest_p1bf.png", xalign=0.5, yalign=0.5)
image forest_p1bn = Image("background/forest/forest_p1bn.png", xalign=0.5, yalign=0.5)
image forest_p1br = Image("background/forest/forest_p1br.png", xalign=0.5, yalign=0.5)
image forest_p2a = Image("background/forest/forest_p2a.png", xalign=0.5, yalign=0.5)
image forest_p2af = Image("background/forest/forest_p2af.png", xalign=0.5, yalign=0.5)
image forest_p2an = Image("background/forest/forest_p2an.png", xalign=0.5, yalign=0.5)
image forest_p2ar = Image("background/forest/forest_p2ar.png", xalign=0.5, yalign=0.5)
image forest_s1a = Image("background/forest/forest_s1a.png", xalign=0.5, yalign=0.5)
image forest_s1a_2 = "background/forest/forest_s1a_2.png"
image forest_s1ac = Image("background/forest/forest_s1ac.png", xalign=0.5, yalign=0.5)
image forest_s1af = Image("background/forest/forest_s1af.png", xalign=0.5, yalign=0.5)
image hill_1a = Image("background/forest/hill_1a.png", xalign=0.5, yalign=0.5)
image hill_1af = Image("background/forest/hill_1af.png", xalign=0.5, yalign=0.5)
image hill_1an = Image("background/forest/hill_1an.png", xalign=0.5, yalign=0.5)
image hill_1ar = Image("background/forest/hill_1ar.png", xalign=0.5, yalign=0.5)
image hill_1b = Image("background/forest/hill_1b.png", xalign=0.5, yalign=0.5)
image hill_1bf = Image("background/forest/hill_1bf.png", xalign=0.5, yalign=0.5)
image hill_1bn = Image("background/forest/hill_1bn.png", xalign=0.5, yalign=0.5)
image hill_1br = Image("background/forest/hill_1br.png", xalign=0.5, yalign=0.5)
image moon_1a = Image("background/forest/moon_1a.png", xalign=0.5, yalign=0.5)
image moon_1an = Image("background/forest/moon_1an.png", xalign=0.5, yalign=0.5)
image moon_1b = Image("background/forest/moon_1b.png", xalign=0.5, yalign=0.5)
image moon_1bn = Image("background/forest/moon_1bn.png", xalign=0.5, yalign=0.5)
image moon_2a = Image("background/forest/moon_2a.png", xalign=0.5, yalign=0.5)
image o_beach_1a = Image("background/forest/o_beach_1a.png", xalign=0.5, yalign=0.5)
image o_beach_1ac = Image("background/forest/o_beach_1ac.png", xalign=0.5, yalign=0.5)
image o_sky_1a = Image("background/forest/o_sky_1a.png", xalign=0.5, yalign=0.5)
image o_sky_1ac = Image("background/forest/o_sky_1ac.png", xalign=0.5, yalign=0.5)
image sky_1a = Image("background/forest/sky_1a.png", xalign=0.5, yalign=0.5)
image sky_1b = Image("background/forest/sky_1b.png", xalign=0.5, yalign=0.5)
image sky_1c = Image("background/forest/sky_1c.png", xalign=0.5, yalign=0.5)
image sky_2b = Image("background/forest/sky_2b.png", xalign=0.5, yalign=0.5)
image sky_3a = Image("background/forest/sky_3a.png", xalign=0.5, yalign=0.5)
image sky_4b = Image("background/forest/sky_4b.png", xalign=0.5, yalign=0.5)
image well_1a = Image("background/forest/well_1a.png", xalign=0.5, yalign=0.5)
image well_1af = Image("background/forest/well_1af.png", xalign=0.5, yalign=0.5)
image well_1an = Image("background/forest/well_1an.png", xalign=0.5, yalign=0.5)
image well_1ar = Image("background/forest/well_1ar.png", xalign=0.5, yalign=0.5)
image well_1b = Image("background/forest/well_1b.png", xalign=0.5, yalign=0.5)
image well_1bf = Image("background/forest/well_1bf.png", xalign=0.5, yalign=0.5)
image well_1bn = Image("background/forest/well_1bn.png", xalign=0.5, yalign=0.5)
image well_1br = Image("background/forest/well_1br.png", xalign=0.5, yalign=0.5)

image different_garden1a = Image("background/garden/different_garden1a.png", xalign=0.5, yalign=0.5)
image different_garden1b = Image("background/garden/different_garden1b.png", xalign=0.5, yalign=0.5)
image garden_1a = Image("background/garden/garden_1a.png", xalign=0.5, yalign=0.5)
image garden_1ac = Image("background/garden/garden_1ac.png", xalign=0.5, yalign=0.5)
image garden_1af = Image("background/garden/garden_1af.png", xalign=0.5, yalign=0.5)
image garden_1an = Image("background/garden/garden_1an.png", xalign=0.5, yalign=0.5)
image garden_1ar = Image("background/garden/garden_1ar.png", xalign=0.5, yalign=0.5)
image garden_1c = Image("background/garden/garden_1c.png", xalign=0.5, yalign=0.5)
image garden_1cc = Image("background/garden/garden_1cc.png", xalign=0.5, yalign=0.5)
image garden_1cf = Image("background/garden/garden_1cf.png", xalign=0.5, yalign=0.5)
image garden_1cn = Image("background/garden/garden_1cn.png", xalign=0.5, yalign=0.5)
image garden_1cr = Image("background/garden/garden_1cr.png", xalign=0.5, yalign=0.5)
image garden_r1a = Image("background/garden/garden_r1a.png", xalign=0.5, yalign=0.5)
image garden_r1a_bg = Image("background/garden/garden_r1a_bg.png", xalign=0.5, yalign=0.5)
image garden_r1ac = Image("background/garden/garden_r1ac.png", xalign=0.5, yalign=0.5)
image garden_r1ac_bg = Image("background/garden/garden_r1ac_bg.png", xalign=0.5, yalign=0.5)
image garden_r1af = Image("background/garden/garden_r1af.png", xalign=0.5, yalign=0.5)
image garden_r1an = Image("background/garden/garden_r1an.png", xalign=0.5, yalign=0.5)
image garden_r1an_bg = Image("background/garden/garden_r1an_bg.png", xalign=0.5, yalign=0.5)
image garden_r1ar = Image("background/garden/garden_r1ar.png", xalign=0.5, yalign=0.5)
image garden_r1ar_bg = Image("background/garden/garden_r1ar_bg.png", xalign=0.5, yalign=0.5)
image garden_r1d = Image("background/garden/garden_r1d.png", xalign=0.5, yalign=0.5)
image garden_r1d_bg = Image("background/garden/garden_r1d_bg.png", xalign=0.5, yalign=0.5)
image garden_r1dc = Image("background/garden/garden_r1dc.png", xalign=0.5, yalign=0.5)
image garden_r1dc_bg = Image("background/garden/garden_r1dc_bg.png", xalign=0.5, yalign=0.5)
image garden_r1df = Image("background/garden/garden_r1df.png", xalign=0.5, yalign=0.5)
image garden_r1df_bg = Image("background/garden/garden_r1df_bg.png", xalign=0.5, yalign=0.5)
image garden_r1dn = Image("background/garden/garden_r1dn.png", xalign=0.5, yalign=0.5)
image garden_r1dn_bg = Image("background/garden/garden_r1dn_bg.png", xalign=0.5, yalign=0.5)
image garden_r1dr = Image("background/garden/garden_r1dr.png", xalign=0.5, yalign=0.5)
image garden_r1dr_bg = Image("background/garden/garden_r1dr_bg.png", xalign=0.5, yalign=0.5)
image garden_se1b = Image("background/garden/garden_se1b.png", xalign=0.5, yalign=0.5)
image garden_se2b = Image("background/garden/garden_se2b.png", xalign=0.5, yalign=0.5)
image garden_se4a = Image("background/garden/garden_se4a.png", xalign=0.5, yalign=0.5)
image garden_seaia = Image("background/garden/garden_seaia.png", xalign=0.5, yalign=0.5)
image rose_1a = Image("background/garden/rose_1a.png", xalign=0.5, yalign=0.5)
image rose_1ac = Image("background/garden/rose_1ac.png", xalign=0.5, yalign=0.5)
image rose_1af = Image("background/garden/rose_1af.png", xalign=0.5, yalign=0.5)
image rose_1an = Image("background/garden/rose_1an.png", xalign=0.5, yalign=0.5)
image rose_1ar = Image("background/garden/rose_1ar.png", xalign=0.5, yalign=0.5)
image rose_1c = Image("background/garden/rose_1c.png", xalign=0.5, yalign=0.5)
image rose_1cc = Image("background/garden/rose_1cc.png", xalign=0.5, yalign=0.5)
image rose_1cf = Image("background/garden/rose_1cf.png", xalign=0.5, yalign=0.5)
image rose_1cn = Image("background/garden/rose_1cn.png", xalign=0.5, yalign=0.5)
image rose_1cn2 = Image("background/garden/rose_1cn2.png", xalign=0.5, yalign=0.5)
image rose_1cp = Image("background/garden/rose_1cp.png", xalign=0.5, yalign=0.5)
image rose_1cpr = Image("background/garden/rose_1cpr.png", xalign=0.5, yalign=0.5)
image rose_1cr = Image("background/garden/rose_1cr.png", xalign=0.5, yalign=0.5)
image rose_1e = Image("background/garden/rose_1e.png", xalign=0.5, yalign=0.5)
image rose_1ec = Image("background/garden/rose_1ec.png", xalign=0.5, yalign=0.5)
image rose_1ef = Image("background/garden/rose_1ef.png", xalign=0.5, yalign=0.5)
image rose_1en = Image("background/garden/rose_1en.png", xalign=0.5, yalign=0.5)
image rose_1en2 = Image("background/garden/rose_1en2.png", xalign=0.5, yalign=0.5)
image rose_1ep = Image("background/garden/rose_1ep.png", xalign=0.5, yalign=0.5)
image rose_1epr = Image("background/garden/rose_1epr.png", xalign=0.5, yalign=0.5)
image rose_1er = Image("background/garden/rose_1er.png", xalign=0.5, yalign=0.5)
image rose_2an = Image("background/garden/rose_2an.png", xalign=0.5, yalign=0.5)
image rose_2ap = Image("background/garden/rose_2ap.png", xalign=0.5, yalign=0.5)
image rose_2apr = Image("background/garden/rose_2apr.png", xalign=0.5, yalign=0.5)
image rose_2bn = Image("background/garden/rose_2bn.png", xalign=0.5, yalign=0.5)
image rose_2bp = Image("background/garden/rose_2bp.png", xalign=0.5, yalign=0.5)
image rose_2bpr = Image("background/garden/rose_2bpr.png", xalign=0.5, yalign=0.5)
image rose_3an = Image("background/garden/rose_3an.png", xalign=0.5, yalign=0.5)
image rose_3ap = Image("background/garden/rose_3ap.png", xalign=0.5, yalign=0.5)
image rose_3apr = Image("background/garden/rose_3apr.png", xalign=0.5, yalign=0.5)
image rose_g1a = Image("background/garden/rose_g1a.png", xalign=0.5, yalign=0.5)
image rose_g1ac = Image("background/garden/rose_g1ac.png", xalign=0.5, yalign=0.5)
image rose_g1af = Image("background/garden/rose_g1af.png", xalign=0.5, yalign=0.5)
image rose_g1an = Image("background/garden/rose_g1an.png", xalign=0.5, yalign=0.5)
image rose_g1ar = Image("background/garden/rose_g1ar.png", xalign=0.5, yalign=0.5)
image rose_g1b = Image("background/garden/rose_g1b.png", xalign=0.5, yalign=0.5)
image rose_g1bc = Image("background/garden/rose_g1bc.png", xalign=0.5, yalign=0.5)
image rose_g1bf = Image("background/garden/rose_g1bf.png", xalign=0.5, yalign=0.5)
image rose_g1bn = Image("background/garden/rose_g1bn.png", xalign=0.5, yalign=0.5)
image rose_g1br = Image("background/garden/rose_g1br.png", xalign=0.5, yalign=0.5)
image rose_g1c = Image("background/garden/rose_g1c.png", xalign=0.5, yalign=0.5)
image warehous_i1a = Image("background/garden/warehous_i1a.png", xalign=0.5, yalign=0.5)
image warehous_i1a_bg = Image("background/garden/warehous_i1a_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1an = Image("background/garden/warehous_i1an.png", xalign=0.5, yalign=0.5)
image warehous_i1an_bg = Image("background/garden/warehous_i1an_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1ar = Image("background/garden/warehous_i1ar.png", xalign=0.5, yalign=0.5)
image warehous_i1ar_bg = Image("background/garden/warehous_i1ar_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1ar2 = Image("background/garden/warehous_i1ar2.png", xalign=0.5, yalign=0.5)
image warehous_i1ar2_bg = Image("background/garden/warehous_i1ar2_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1c = Image("background/garden/warehous_i1c.png", xalign=0.5, yalign=0.5)
image warehous_i1c_bg = Image("background/garden/warehous_i1c_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1cn = Image("background/garden/warehous_i1cn.png", xalign=0.5, yalign=0.5)
image warehous_i1cn_bg = Image("background/garden/warehous_i1cn_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1cr = Image("background/garden/warehous_i1cr.png", xalign=0.5, yalign=0.5)
image warehous_i1cr_bg = Image("background/garden/warehous_i1cr_bg.png", xalign=0.5, yalign=0.5)
image warehous_i1e = Image("background/garden/warehous_i1e.png", xalign=0.5, yalign=0.5)
image warehous_i1en = Image("background/garden/warehous_i1en.png", xalign=0.5, yalign=0.5)
image warehous_i1er = Image("background/garden/warehous_i1er.png", xalign=0.5, yalign=0.5)
image warehous_o1a = Image("background/garden/warehous_o1a.png", xalign=0.5, yalign=0.5)
image warehous_o1an = Image("background/garden/warehous_o1an.png", xalign=0.5, yalign=0.5)
image warehous_o2a = Image("background/garden/warehous_o2a.png", xalign=0.5, yalign=0.5)
image warehous_o2an = Image("background/garden/warehous_o2an.png", xalign=0.5, yalign=0.5)
image warehous_o2ar = Image("background/garden/warehous_o2ar.png", xalign=0.5, yalign=0.5)

image g_o1a = Image("background/guesthouse/g_o1a.png", xalign=0.5, yalign=0.5)
image g_o1ac = Image("background/guesthouse/g_o1ac.png", xalign=0.5, yalign=0.5)
image g_o1af = Image("background/guesthouse/g_o1af.png", xalign=0.5, yalign=0.5)
image g_o1an = Image("background/guesthouse/g_o1an.png", xalign=0.5, yalign=0.5)
image g_o1ar = Image("background/guesthouse/g_o1ar.png", xalign=0.5, yalign=0.5)
image g_o1c = Image("background/guesthouse/g_o1c.png", xalign=0.5, yalign=0.5)
image g_o1cc = Image("background/guesthouse/g_o1cc.png", xalign=0.5, yalign=0.5)
image g_o1cf = Image("background/guesthouse/g_o1cf.png", xalign=0.5, yalign=0.5)
image g_o1cn = Image("background/guesthouse/g_o1cn.png", xalign=0.5, yalign=0.5)
image g_o1cr = Image("background/guesthouse/g_o1cr.png", xalign=0.5, yalign=0.5)
image g1f_p1a = Image("background/guesthouse/g1f_p1a.png", xalign=0.5, yalign=0.5)
image g1f_p1a_bg = Image("background/guesthouse/g1f_p1a_bg.png", xalign=0.5, yalign=0.5)
image g1f_p1an = Image("background/guesthouse/g1f_p1an.png", xalign=0.5, yalign=0.5)
image g1f_p1an_bg = Image("background/guesthouse/g1f_p1an_bg.png", xalign=0.5, yalign=0.5)
image g1f_p1ar = Image("background/guesthouse/g1f_p1ar.png", xalign=0.5, yalign=0.5)
image g1f_p1ar_bg = Image("background/guesthouse/g1f_p1ar_bg.png", xalign=0.5, yalign=0.5)
image g1f_p1b = Image("background/guesthouse/g1f_p1b.png", xalign=0.5, yalign=0.5)
image g1f_p1b_bg = Image("background/guesthouse/g1f_p1b_bg.png", xalign=0.5, yalign=0.5)
image g1f_p1bn = Image("background/guesthouse/g1f_p1bn.png", xalign=0.5, yalign=0.5)
image g1f_p1bn_bg = Image("background/guesthouse/g1f_p1bn_bg.png", xalign=0.5, yalign=0.5)
image g1f_p1br = Image("background/guesthouse/g1f_p1br.png", xalign=0.5, yalign=0.5)
image g1f_p1br_bg = Image("background/guesthouse/g1f_p1br_bg.png", xalign=0.5, yalign=0.5)
image g1f_p1c = Image("background/guesthouse/g1f_p1c.png", xalign=0.5, yalign=0.5)
image g1f_p1e = Image("background/guesthouse/g1f_p1e.png", xalign=0.5, yalign=0.5)
image g1f_p1en = Image("background/guesthouse/g1f_p1en.png", xalign=0.5, yalign=0.5)
image g1f_p1er = Image("background/guesthouse/g1f_p1er.png", xalign=0.5, yalign=0.5)
image g1f_r1a = Image("background/guesthouse/g1f_r1a.png", xalign=0.5, yalign=0.5)
image g1f_r1an = Image("background/guesthouse/g1f_r1an.png", xalign=0.5, yalign=0.5)
image g1f_r1ar = Image("background/guesthouse/g1f_r1ar.png", xalign=0.5, yalign=0.5)
image g1f_r2a = Image("background/guesthouse/g1f_r2a.png", xalign=0.5, yalign=0.5)
image g1f_r2a_bg = Image("background/guesthouse/g1f_r2a_bg.png", xalign=0.5, yalign=0.5)
image g1f_r2am = Image("background/guesthouse/g1f_r2am.png", xalign=0.5, yalign=0.5)
image g1f_r2am_bg = Image("background/guesthouse/g1f_r2am_bg.png", xalign=0.5, yalign=0.5)
image g1f_r2an = Image("background/guesthouse/g1f_r2an.png", xalign=0.5, yalign=0.5)
image g1f_r2an_bg = Image("background/guesthouse/g1f_r2an_bg.png", xalign=0.5, yalign=0.5)
image g1f_r2ar = Image("background/guesthouse/g1f_r2ar.png", xalign=0.5, yalign=0.5)
image g1f_r2ar_bg = Image("background/guesthouse/g1f_r2ar_bg.png", xalign=0.5, yalign=0.5)
image g1f_s1a = Image("background/guesthouse/g1f_s1a.png", xalign=0.5, yalign=0.5)
image g1f_s1ap = Image("background/guesthouse/g1f_s1ap.png", xalign=0.5, yalign=0.5)
image g1f_s1bp = Image("background/guesthouse/g1f_s1bp.png", xalign=0.5, yalign=0.5)
image g2f_p1a = Image("background/guesthouse/g2f_p1a.png", xalign=0.5, yalign=0.5)
image g2f_p1a_bg = Image("background/guesthouse/g2f_p1a_bg.png", xalign=0.5, yalign=0.5)
image g2f_p1an = Image("background/guesthouse/g2f_p1an.png", xalign=0.5, yalign=0.5)
image g2f_p1an_bg = Image("background/guesthouse/g2f_p1an_bg.png", xalign=0.5, yalign=0.5)
image g2f_p1ar = Image("background/guesthouse/g2f_p1ar.png", xalign=0.5, yalign=0.5)
image g2f_p1ar_bg = Image("background/guesthouse/g2f_p1ar_bg.png", xalign=0.5, yalign=0.5)
image g2f_r1a = Image("background/guesthouse/g2f_r1a.png", xalign=0.5, yalign=0.5)
image g2f_r1a_bg= Image("background/guesthouse/g2f_r1a_bg.png", xalign=0.5, yalign=0.5)
image g2f_r1am = Image("background/guesthouse/g2f_r1am.png", xalign=0.5, yalign=0.5)
image g2f_r1am_bg = Image("background/guesthouse/g2f_r1am_bg.png", xalign=0.5, yalign=0.5)
image g2f_r1an = Image("background/guesthouse/g2f_r1an.png", xalign=0.5, yalign=0.5)
image g2f_r1an_bg = Image("background/guesthouse/g2f_r1an_bg.png", xalign=0.5, yalign=0.5)
image g2f_r1ar = Image("background/guesthouse/g2f_r1ar.png", xalign=0.5, yalign=0.5)
image g2f_r1ar_bg = Image("background/guesthouse/g2f_r1ar_bg.png", xalign=0.5, yalign=0.5)
image g2f_r1c = Image("background/guesthouse/g2f_r1c.png", xalign=0.5, yalign=0.5)
image g2f_r1cm = Image("background/guesthouse/g2f_r1cm.png", xalign=0.5, yalign=0.5)
image g2f_r1cn = Image("background/guesthouse/g2f_r1cn.png", xalign=0.5, yalign=0.5)
image g2f_r1cr = Image("background/guesthouse/g2f_r1cr.png", xalign=0.5, yalign=0.5)
image gdin_1a = Image("background/guesthouse/gdin_1a.png", xalign=0.5, yalign=0.5)
image gdin_1ad = Image("background/guesthouse/gdin_1ad.png", xalign=0.5, yalign=0.5)
image gdin_1ad2 = Image("background/guesthouse/gdin_1ad2.png", xalign=0.5, yalign=0.5)
image glib_1a = Image("background/guesthouse/glib_1a.png", xalign=0.5, yalign=0.5)
image glib_1an = Image("background/guesthouse/glib_1an.png", xalign=0.5, yalign=0.5)
image glib_1ar = Image("background/guesthouse/glib_1ar.png", xalign=0.5, yalign=0.5)
image glob_1a = Image("background/guesthouse/glob_1a.png", xalign=0.5, yalign=0.5)
image glob_1a_bg = Image("background/guesthouse/glob_1a_bg.png", xalign=0.5, yalign=0.5)
image glob_1an = Image("background/guesthouse/glob_1an.png", xalign=0.5, yalign=0.5)
image glob_1an_bg = Image("background/guesthouse/glob_1an_bg.png", xalign=0.5, yalign=0.5)
image glob_1ar = Image("background/guesthouse/glob_1ar.png", xalign=0.5, yalign=0.5)
image glob_1ar_bg = Image("background/guesthouse/glob_1ar_bg.png", xalign=0.5, yalign=0.5)
image glob_1d = Image("background/guesthouse/glob_1d.png", xalign=0.5, yalign=0.5)
image glob_1d_bg = Image("background/guesthouse/glob_1d_bg.png", xalign=0.5, yalign=0.5)
image glob_1dn = Image("background/guesthouse/glob_1dn.png", xalign=0.5, yalign=0.5)
image glob_1dn_bg = Image("background/guesthouse/glob_1dn_bg.png", xalign=0.5, yalign=0.5)
image glob_1dr = Image("background/guesthouse/glob_1dr.png", xalign=0.5, yalign=0.5)
image glob_1dr_bg = Image("background/guesthouse/glob_1dr_bg.png", xalign=0.5, yalign=0.5)
image glob_1e = Image("background/guesthouse/glob_1e.png", xalign=0.5, yalign=0.5)                      ## originally from PS3 chiru
image glob_1en = Image("background/guesthouse/glob_1en.png", xalign=0.5, yalign=0.5)                    ## originally from PS3 chiru
image glob_1er = Image("background/guesthouse/glob_1er.png", xalign=0.5, yalign=0.5)                    ## originally from PS3 chiru

image kaw_r1a = Image("background/kawhouse/kaw_r1a.png", xalign=0.5, yalign=0.5)
image kaw_r1an = Image("background/kawhouse/kaw_r1an.png", xalign=0.5, yalign=0.5)
image kaw_r1cn = Image("background/kawhouse/kaw_r1cn.png", xalign=0.5, yalign=0.5)
image kaw_r2a = Image("background/kawhouse/kaw_r2a.png", xalign=0.5, yalign=0.5)
image kaw_r2an = Image("background/kawhouse/kaw_r2an.png", xalign=0.5, yalign=0.5)
image kaw_r3b = Image("background/kawhouse/kaw_r3b.png", xalign=0.5, yalign=0.5)
image kaw_r3bn = Image("background/kawhouse/kaw_r3bn.png", xalign=0.5, yalign=0.5)

image kum_r1a = Image("background/kumhouse/kum_r1a.png", xalign=0.5, yalign=0.5)

image m_door1 = Image("background/mainbuilding/m_door1.png", xalign=0.5, yalign=0.5)
image m_door1_2 = Image("background/mainbuilding/m_door1_2.png", xalign=0.5, yalign=0.5)
image m_door1h = Image("background/mainbuilding/m_door1h.png", xalign=0.5, yalign=0.5)
image m_door1k = Image("background/mainbuilding/m_door1k.png", xalign=0.5, yalign=0.5)
image m_door1r = Image("background/mainbuilding/m_door1r.png", xalign=0.5, yalign=0.5)
image m_door1x = Image("background/mainbuilding/m_door1x.png", xalign=0.5, yalign=0.5)
image m_door1x_2 = Image("background/mainbuilding/m_door1x_2.png", xalign=0.5, yalign=0.5)
image m_door2 = Image("background/mainbuilding/m_door2.png", xalign=0.5, yalign=0.5)
image m_door2_2 = Image("background/mainbuilding/m_door2_2.png", xalign=0.5, yalign=0.5)
image m_door2h = Image("background/mainbuilding/m_door2h.png", xalign=0.5, yalign=0.5)
image m_door2k = Image("background/mainbuilding/m_door2k.png", xalign=0.5, yalign=0.5)
image m_door2r = Image("background/mainbuilding/m_door2r.png", xalign=0.5, yalign=0.5)
image m_o1a = Image("background/mainbuilding/m_o1a.png", xalign=0.5, yalign=0.5)
image m_o1a2 = Image("background/mainbuilding/m_o1a2.png", xalign=0.5, yalign=0.5)
image m_o1ac = Image("background/mainbuilding/m_o1ac.png", xalign=0.5, yalign=0.5)
image m_o1af = Image("background/mainbuilding/m_o1af.png", xalign=0.5, yalign=0.5)
image m_o1an = Image("background/mainbuilding/m_o1an.png", xalign=0.5, yalign=0.5)
image m_o1an2 = Image("background/mainbuilding/m_o1an2.png", xalign=0.5, yalign=0.5)
image m_o1anc = Image("background/mainbuilding/m_o1anc.png", xalign=0.5, yalign=0.5)
image m_o1anc_sak = Image("background/mainbuilding/m_o1anc_sak.png", xalign=0.5, yalign=0.5)
image m_o1ar = Image("background/mainbuilding/m_o1ar.png", xalign=0.5, yalign=0.5)
image m_o1ar2 = Image("background/mainbuilding/m_o1ar2.png", xalign=0.5, yalign=0.5)
image m1f_p1b = Image("background/mainbuilding/m1f_p1b.png", xalign=0.5, yalign=0.5)
image m1f_p1b_bg = Image("background/mainbuilding/m1f_p1b_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1bn = Image("background/mainbuilding/m1f_p1bn.png", xalign=0.5, yalign=0.5)
image m1f_p1bn_bg = Image("background/mainbuilding/m1f_p1bn_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1br = Image("background/mainbuilding/m1f_p1br.png", xalign=0.5, yalign=0.5)
image m1f_p1br_bg = Image("background/mainbuilding/m1f_p1br_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1c = Image("background/mainbuilding/m1f_p1c.png", xalign=0.5, yalign=0.5)
image m1f_p1c_bg = Image("background/mainbuilding/m1f_p1c_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1cn = Image("background/mainbuilding/m1f_p1cn.png", xalign=0.5, yalign=0.5)
image m1f_p1cn_bg = Image("background/mainbuilding/m1f_p1cn_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1cr = Image("background/mainbuilding/m1f_p1cr.png", xalign=0.5, yalign=0.5)
image m1f_p1cr_bg = Image("background/mainbuilding/m1f_p1cr_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1d = Image("background/mainbuilding/m1f_p1d.png", xalign=0.5, yalign=0.5)
image m1f_p1d_bg = Image("background/mainbuilding/m1f_p1d_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1dn = Image("background/mainbuilding/m1f_p1dn.png", xalign=0.5, yalign=0.5)
image m1f_p1dn_bg = Image("background/mainbuilding/m1f_p1dn_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1dr = Image("background/mainbuilding/m1f_p1dr.png", xalign=0.5, yalign=0.5)
image m1f_p1dr_bg = Image("background/mainbuilding/m1f_p1dr_bg.png", xalign=0.5, yalign=0.5)
image m1f_p2b = Image("background/mainbuilding/m1f_p2b.png", xalign=0.5, yalign=0.5)
image m1f_p2b_bg = Image("background/mainbuilding/m1f_p2b_bg.png", xalign=0.5, yalign=0.5)
image m1f_p2bn = Image("background/mainbuilding/m1f_p2bn.png", xalign=0.5, yalign=0.5)
image m1f_p2bn_bg = Image("background/mainbuilding/m1f_p2bn_bg.png", xalign=0.5, yalign=0.5)
image m1f_p2br = Image("background/mainbuilding/m1f_p2br.png", xalign=0.5, yalign=0.5)
image m1f_p2br_bg = Image("background/mainbuilding/m1f_p2br_bg.png", xalign=0.5, yalign=0.5)
image m1f_r1a = Image("background/mainbuilding/m1f_r1a.png", xalign=0.5, yalign=0.5)
image m1f_r1a_bg = Image("background/mainbuilding/m1f_r1a_bg.png", xalign=0.5, yalign=0.5)
image m1f_r1an = Image("background/mainbuilding/m1f_r1an.png", xalign=0.5, yalign=0.5)
image m1f_r1an_bg = Image("background/mainbuilding/m1f_r1an_bg.png", xalign=0.5, yalign=0.5)
image m1f_r1ar = Image("background/mainbuilding/m1f_r1ar.png", xalign=0.5, yalign=0.5)
image m1f_r1ar_bg = Image("background/mainbuilding/m1f_r1ar_bg.png", xalign=0.5, yalign=0.5)
image m1f_s1a = Image("background/mainbuilding/m1f_s1a.png", xalign=0.5, yalign=0.5)
image m1f_s1a_bg = Image("background/mainbuilding/m1f_s1a_bg.png", xalign=0.5, yalign=0.5)
image m1f_s1af = Image("background/mainbuilding/m1f_s1af.png", xalign=0.5, yalign=0.5)
image m1f_s1an = Image("background/mainbuilding/m1f_s1an.png", xalign=0.5, yalign=0.5)
image m1f_s1an_bg = Image("background/mainbuilding/m1f_s1an_bg.png", xalign=0.5, yalign=0.5)
image m1f_s1ar = Image("background/mainbuilding/m1f_s1ar.png", xalign=0.5, yalign=0.5)
image m1f_s1ar_bg = Image("background/mainbuilding/m1f_s1ar_bg.png", xalign=0.5, yalign=0.5)
image m1f_s1c = Image("background/mainbuilding/m1f_s1c.png", xalign=0.5, yalign=0.5)
image m1f_s1cn = Image("background/mainbuilding/m1f_s1cn.png", xalign=0.5, yalign=0.5)
image m1f_s1cr = Image("background/mainbuilding/m1f_s1cr.png", xalign=0.5, yalign=0.5)
image m1f_s1d = Image("background/mainbuilding/m1f_s1d.png", xalign=0.5, yalign=0.5)
image m1f_s1d_2 = Image("background/mainbuilding/m1f_s1d_2.png", xalign=0.5, yalign=0.5)
image m1f_s1df = Image("background/mainbuilding/m1f_s1df.png", xalign=0.5, yalign=0.5)
image m1f_s1dn = Image("background/mainbuilding/m1f_s1dn.png", xalign=0.5, yalign=0.5)
image m1f_s1dr = Image("background/mainbuilding/m1f_s1dr.png", xalign=0.5, yalign=0.5)
image m2f_p1a = Image("background/mainbuilding/m2f_p1a.png", xalign=0.5, yalign=0.5)
image m2f_p1a_bg = Image("background/mainbuilding/m2f_p1a_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1af = Image("background/mainbuilding/m2f_p1af.png", xalign=0.5, yalign=0.5)
image m2f_p1an = Image("background/mainbuilding/m2f_p1an.png", xalign=0.5, yalign=0.5)
image m2f_p1an_bg = Image("background/mainbuilding/m2f_p1an_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1ar = Image("background/mainbuilding/m2f_p1ar.png", xalign=0.5, yalign=0.5)
image m2f_p1ar_bg = Image("background/mainbuilding/m2f_p1ar_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1b = Image("background/mainbuilding/m2f_p1b.png", xalign=0.5, yalign=0.5)
image m2f_p1b_bg = Image("background/mainbuilding/m2f_p1b_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1bf = Image("background/mainbuilding/m2f_p1bf.png", xalign=0.5, yalign=0.5)
image m2f_p1bn = Image("background/mainbuilding/m2f_p1bn.png", xalign=0.5, yalign=0.5)
image m2f_p1bn_bg = Image("background/mainbuilding/m2f_p1bn_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1br = Image("background/mainbuilding/m2f_p1br.png", xalign=0.5, yalign=0.5)
image m2f_p1br_bg = Image("background/mainbuilding/m2f_p1br_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1c = Image("background/mainbuilding/m2f_p1c.png", xalign=0.5, yalign=0.5)
image m2f_p1c_bg = Image("background/mainbuilding/m2f_p1c_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1cf = Image("background/mainbuilding/m2f_p1cf.png", xalign=0.5, yalign=0.5)
image m2f_p1cn = Image("background/mainbuilding/m2f_p1cn.png", xalign=0.5, yalign=0.5)
image m2f_p1cn_bg = Image("background/mainbuilding/m2f_p1cn_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1cr = Image("background/mainbuilding/m2f_p1cr.png", xalign=0.5, yalign=0.5)
image m2f_p1cr_bg = Image("background/mainbuilding/m2f_p1cr_bg.png", xalign=0.5, yalign=0.5)
image m2f_r4a = Image("background/mainbuilding/m2f_r4a.png", xalign=0.5, yalign=0.5)
image m2f_r4a_bg = Image("background/mainbuilding/m2f_r4a_bg.png", xalign=0.5, yalign=0.5)
image m2f_r4an = Image("background/mainbuilding/m2f_r4an.png", xalign=0.5, yalign=0.5)
image m2f_r4an_bg = Image("background/mainbuilding/m2f_r4an_bg.png", xalign=0.5, yalign=0.5)
image m2f_r4ar = Image("background/mainbuilding/m2f_r4ar.png", xalign=0.5, yalign=0.5)
image m2f_r4ar_bg = Image("background/mainbuilding/m2f_r4ar_bg.png", xalign=0.5, yalign=0.5)
image mbat_1a = Image("background/mainbuilding/mbat_1a.png", xalign=0.5, yalign=0.5)
image mboi_1a = Image("background/mainbuilding/mboi_1a.png", xalign=0.5, yalign=0.5)
image mboi_1c = Image("background/mainbuilding/mboi_1c.png", xalign=0.5, yalign=0.5)
image mcou_1a = Image("background/mainbuilding/mcou_1a.png", xalign=0.5, yalign=0.5)
image mcou_1an = Image("background/mainbuilding/mcou_1an.png", xalign=0.5, yalign=0.5)
image mcou_1ar = Image("background/mainbuilding/mcou_1ar.png", xalign=0.5, yalign=0.5)
image mcou_2a = Image("background/mainbuilding/mcou_2a.png", xalign=0.5, yalign=0.5)
image mdin_1a = Image("background/mainbuilding/mdin_1a.png", xalign=0.5, yalign=0.5)
image mdin_1an = Image("background/mainbuilding/mdin_1an.png", xalign=0.5, yalign=0.5)
image mdin_1ar = Image("background/mainbuilding/mdin_1ar.png", xalign=0.5, yalign=0.5)
image mdin_1c = Image("background/mainbuilding/mdin_1c.png", xalign=0.5, yalign=0.5)
image mdin_1c_bg = Image("background/mainbuilding/mdin_1c_bg.png", xalign=0.5, yalign=0.5)
image mdin_1cn = Image("background/mainbuilding/mdin_1cn.png", xalign=0.5, yalign=0.5)
image mdin_1cn_bg = Image("background/mainbuilding/mdin_1cn_bg.png", xalign=0.5, yalign=0.5)
image mdin_1cr = Image("background/mainbuilding/mdin_1cr.png", xalign=0.5, yalign=0.5)
image mdin_1cr_bg = Image("background/mainbuilding/mdin_1cr_bg.png", xalign=0.5, yalign=0.5)
image mdin_1e = Image("background/mainbuilding/mdin_1e.png", xalign=0.5, yalign=0.5)
image mdin_1en = Image("background/mainbuilding/mdin_1en.png", xalign=0.5, yalign=0.5)
image mdin_1er = Image("background/mainbuilding/mdin_1er.png", xalign=0.5, yalign=0.5)
image mdin_1f = Image("background/mainbuilding/mdin_1f.png", xalign=0.5, yalign=0.5)
image mdin_1fn = Image("background/mainbuilding/mdin_1fn.png", xalign=0.5, yalign=0.5)
image mdin_1fr = Image("background/mainbuilding/mdin_1fr.png", xalign=0.5, yalign=0.5)
image mdin_1g = Image("background/mainbuilding/mdin_1g.png", xalign=0.5, yalign=0.5)
image mdin_1g_bg = Image("background/mainbuilding/mdin_1g_bg.png", xalign=0.5, yalign=0.5)
image mdin_1gn = Image("background/mainbuilding/mdin_1gn.png", xalign=0.5, yalign=0.5)
image mdin_1gn_bg = Image("background/mainbuilding/mdin_1gn_bg.png", xalign=0.5, yalign=0.5)
image mdin_1gr = Image("background/mainbuilding/mdin_1gr.png", xalign=0.5, yalign=0.5)
image mdin_1gr_bg = Image("background/mainbuilding/mdin_1gr_bg.png", xalign=0.5, yalign=0.5)
image ment_1b = Image("background/mainbuilding/ment_1b.png", xalign=0.5, yalign=0.5)
image ment_1b_bg = Image("background/mainbuilding/ment_1b_bg.png", xalign=0.5, yalign=0.5)
image ment_1bn = Image("background/mainbuilding/ment_1bn.png", xalign=0.5, yalign=0.5)
image ment_1bn_bg = Image("background/mainbuilding/ment_1bn_bg.png", xalign=0.5, yalign=0.5)
image ment_1br = Image("background/mainbuilding/ment_1br.png", xalign=0.5, yalign=0.5)
image ment_1br_bg = Image("background/mainbuilding/ment_1br_bg.png", xalign=0.5, yalign=0.5)
image mhal_1a = Image("background/mainbuilding/mhal_1a.png", xalign=0.5, yalign=0.5)
image mhal_1a_bg = Image("background/mainbuilding/mhal_1a_bg.png", xalign=0.5, yalign=0.5)
image mhal_1a2 = Image("background/mainbuilding/mhal_1a2.png", xalign=0.5, yalign=0.5)
image mhal_1a2_bg = Image("background/mainbuilding/mhal_1a2_bg.png", xalign=0.5, yalign=0.5)
image mhal_1a3 = Image("background/mainbuilding/mhal_1a3.png", xalign=0.5, yalign=0.5)
image mhal_1a3_bg = Image("background/mainbuilding/mhal_1a3_bg.png", xalign=0.5, yalign=0.5)
image mhal_1am = Image("background/mainbuilding/mhal_1am.png", xalign=0.5, yalign=0.5)
image mhal_1am2 = Image("background/mainbuilding/mhal_1am2.png", xalign=0.5, yalign=0.5)
image mhal_1am3 = Image("background/mainbuilding/mhal_1am3.png", xalign=0.5, yalign=0.5)
image mhal_1an = Image("background/mainbuilding/mhal_1an.png", xalign=0.5, yalign=0.5)
image mhal_1an2 = Image("background/mainbuilding/mhal_1an2.png", xalign=0.5, yalign=0.5)
image mhal_1an3 = Image("background/mainbuilding/mhal_1an3.png", xalign=0.5, yalign=0.5)
image mhal_1ar = Image("background/mainbuilding/mhal_1ar.png", xalign=0.5, yalign=0.5)
image mhal_1ar_bg = Image("background/mainbuilding/mhal_1ar_bg.png", xalign=0.5, yalign=0.5)
image mhal_1ar2 = Image("background/mainbuilding/mhal_1ar2.png", xalign=0.5, yalign=0.5)
image mhal_1ar2_bg = Image("background/mainbuilding/mhal_1ar2_bg.png", xalign=0.5, yalign=0.5)
image mhal_1ar3 = Image("background/mainbuilding/mhal_1ar3.png", xalign=0.5, yalign=0.5)
image mhal_1ar3_bg = Image("background/mainbuilding/mhal_1ar3_bg.png", xalign=0.5, yalign=0.5)
image mhal_1c = Image("background/mainbuilding/mhal_1c.png", xalign=0.5, yalign=0.5)
image mhal_1c2 = Image("background/mainbuilding/mhal_1c2.png", xalign=0.5, yalign=0.5)
image mhal_1c3 = Image("background/mainbuilding/mhal_1c3.png", xalign=0.5, yalign=0.5)
image mhal_1cn = Image("background/mainbuilding/mhal_1cn.png", xalign=0.5, yalign=0.5)
image mhal_1cn = Image("background/mainbuilding/mhal_1cn.png", xalign=0.5, yalign=0.5)
image mhal_1cn = Image("background/mainbuilding/mhal_1cn.png", xalign=0.5, yalign=0.5)
image mhal_1cr = Image("background/mainbuilding/mhal_1cr.png", xalign=0.5, yalign=0.5)
image mhal_1cr = Image("background/mainbuilding/mhal_1cr.png", xalign=0.5, yalign=0.5)
image mhal_1cr = Image("background/mainbuilding/mhal_1cr.png", xalign=0.5, yalign=0.5)
image mhal_2a = Image("background/mainbuilding/mhal_2a.png", xalign=0.5, yalign=0.5)
image mhal_2a_bg = Image("background/mainbuilding/mhal_2a_bg.png", xalign=0.5, yalign=0.5)
image mhal_2am = Image("background/mainbuilding/mhal_2am.png", xalign=0.5, yalign=0.5)
image mhal_2an = Image("background/mainbuilding/mhal_2an.png", xalign=0.5, yalign=0.5)
image mhal_2ar = Image("background/mainbuilding/mhal_2ar.png", xalign=0.5, yalign=0.5)
image mhal_2ar_bg = Image("background/mainbuilding/mhal_2ar_bg.png", xalign=0.5, yalign=0.5)
image mhal_2b = Image("background/mainbuilding/mhal_2b.png", xalign=0.5, yalign=0.5)
image mhal_2b_bg = Image("background/mainbuilding/mhal_2b_bg.png", xalign=0.5, yalign=0.5)
image mhal_2bm = Image("background/mainbuilding/mhal_2bm.png", xalign=0.5, yalign=0.5)
image mhal_2bn = Image("background/mainbuilding/mhal_2bn.png", xalign=0.5, yalign=0.5)
image mhal_2br = Image("background/mainbuilding/mhal_2br.png", xalign=0.5, yalign=0.5)
image mhal_2br_bg = Image("background/mainbuilding/mhal_2br_bg.png", xalign=0.5, yalign=0.5)
image mhal_2c = Image("background/mainbuilding/mhal_2c.png", xalign=0.5, yalign=0.5)
image mhal_2c2 = Image("background/mainbuilding/mhal_2c2.png", xalign=0.5, yalign=0.5)
image mhal_2c3 = Image("background/mainbuilding/mhal_2c3.png", xalign=0.5, yalign=0.5)
image mhal_2cn = Image("background/mainbuilding/mhal_2cn.png", xalign=0.5, yalign=0.5)
image mhal_2cn2 = Image("background/mainbuilding/mhal_2cn2.png", xalign=0.5, yalign=0.5)
image mhal_2cn3 = Image("background/mainbuilding/mhal_2cn3.png", xalign=0.5, yalign=0.5)
image mhal_2cr = Image("background/mainbuilding/mhal_2c.png", xalign=0.5, yalign=0.5)
image mhal_2cr2 = Image("background/mainbuilding/mhal_2cr2.png", xalign=0.5, yalign=0.5)
image mhal_2cr3 = Image("background/mainbuilding/mhal_2cr3.png", xalign=0.5, yalign=0.5)
image mhal_2d = Image("background/mainbuilding/mhal_2d.png", xalign=0.5, yalign=0.5)
image mhal_2dn = Image("background/mainbuilding/mhal_2dn.png", xalign=0.5, yalign=0.5)
image mhal_2dr = Image("background/mainbuilding/mhal_2dr.png", xalign=0.5, yalign=0.5)
image mhal_ta1a = Image("background/mainbuilding/mhal_ta1a.png", xalign=0.5, yalign=0.5)
image mjes_1a = Image("background/mainbuilding/mjes_1a.png", xalign=0.5, yalign=0.5)
image mjes_1a_bg = Image("background/mainbuilding/mjes_1a_bg.png", xalign=0.5, yalign=0.5)
image mjes_1af = Image("background/mainbuilding/mjes_1af.png", xalign=0.5, yalign=0.5)
image mjes_1an = Image("background/mainbuilding/mjes_1an.png", xalign=0.5, yalign=0.5)
image mjes_1an_bg = Image("background/mainbuilding/mjes_1an_bg.png", xalign=0.5, yalign=0.5)
image mjes_1ar = Image("background/mainbuilding/mjes_1ar.png", xalign=0.5, yalign=0.5)
image mjes_1ar_bg = Image("background/mainbuilding/mjes_1ar_bg.png", xalign=0.5, yalign=0.5)
image mjes_1c = Image("background/mainbuilding/mjes_1c.png", xalign=0.5, yalign=0.5)
image mjes_1c_bg = Image("background/mainbuilding/mjes_1c_bg.png", xalign=0.5, yalign=0.5)
image mjes_1cn = Image("background/mainbuilding/mjes_1cn.png", xalign=0.5, yalign=0.5)
image mjes_1cn_bg = Image("background/mainbuilding/mjes_1cn_bg.png", xalign=0.5, yalign=0.5)
image mjes_1cr = Image("background/mainbuilding/mjes_1cr.png", xalign=0.5, yalign=0.5)
image mjes_1cr_bg = Image("background/mainbuilding/mjes_1cr_bg.png", xalign=0.5, yalign=0.5)
image mjes_1e = Image("background/mainbuilding/mjes_1e.png", xalign=0.5, yalign=0.5)
image mjes_1en = Image("background/mainbuilding/mjes_1en.png", xalign=0.5, yalign=0.5)
image mjes_1er = Image("background/mainbuilding/mjes_1er.png", xalign=0.5, yalign=0.5)
image mkit_1a = Image("background/mainbuilding/mkit_1a.png", xalign=0.5, yalign=0.5)
image mkit_1a_bg = Image("background/mainbuilding/mkit_1a_bg.png", xalign=0.5, yalign=0.5)
image mkit_1an = Image("background/mainbuilding/mkit_1an.png", xalign=0.5, yalign=0.5)
image mkit_1an_bg = Image("background/mainbuilding/mkit_1an_bg.png", xalign=0.5, yalign=0.5)
image mkit_1ar = Image("background/mainbuilding/mkit_1ar.png", xalign=0.5, yalign=0.5)
image mkit_1ar_bg = Image("background/mainbuilding/mkit_1ar_bg.png", xalign=0.5, yalign=0.5)
image mkit_1c = Image("background/mainbuilding/mkit_1c.png", xalign=0.5, yalign=0.5)
image mkit_1cn = Image("background/mainbuilding/mkit_1cn.png", xalign=0.5, yalign=0.5)
image mkit_1cr = Image("background/mainbuilding/mkit_1cr.png", xalign=0.5, yalign=0.5)
image mlib_1a = Image("background/mainbuilding/mlib_1a.png", xalign=0.5, yalign=0.5)
image mlib_1a_bg = Image("background/mainbuilding/mlib_1a_bg.png", xalign=0.5, yalign=0.5)
image mlib_1a2 = Image("background/mainbuilding/mlib_1a2.png", xalign=0.5, yalign=0.5)
image mlib_1a2_bg = Image("background/mainbuilding/mlib_1a2.png", xalign=0.5, yalign=0.5)
image mlib_1a3 = Image("background/mainbuilding/mlib_1a3.png", xalign=0.5, yalign=0.5)
image mlib_1a3_bg = Image("background/mainbuilding/mlib_1a3_bg.png", xalign=0.5, yalign=0.5)
image mlib_1an = Image("background/mainbuilding/mlib_1an.png", xalign=0.5, yalign=0.5)
image mlib_1an_bg = Image("background/mainbuilding/mlib_1an_bg.png", xalign=0.5, yalign=0.5)
image mlib_1an2 = Image("background/mainbuilding/mlib_1an2.png", xalign=0.5, yalign=0.5)
image mlib_1an2_bg = Image("background/mainbuilding/mlib_1an2_bg.png", xalign=0.5, yalign=0.5)
image mlib_1an3 = Image("background/mainbuilding/mlib_1an3.png", xalign=0.5, yalign=0.5)
image mlib_1an3_bg = Image("background/mainbuilding/mlib_1an3_bg.png", xalign=0.5, yalign=0.5)
image mlib_1ar = Image("background/mainbuilding/mlib_1ar.png", xalign=0.5, yalign=0.5)
image mlib_1ar_bg = Image("background/mainbuilding/mlib_1ar_bg.png", xalign=0.5, yalign=0.5)
image mlib_1ar2 = Image("background/mainbuilding/mlib_1a2.png", xalign=0.5, yalign=0.5)
image mlib_1ar2_bg = Image("background/mainbuilding/mlib_1a2_bg.png", xalign=0.5, yalign=0.5)
image mlib_1ar3 = Image("background/mainbuilding/mlib_1a3.png", xalign=0.5, yalign=0.5)
image mlib_1ar3_bg = Image("background/mainbuilding/mlib_1a3_bg.png", xalign=0.5, yalign=0.5)
image mlib_1b = Image("background/mainbuilding/mlib_1b.png", xalign=0.5, yalign=0.5)
image mlib_1b_bg = Image("background/mainbuilding/mlib_1b_bg.png", xalign=0.5, yalign=0.5)
image mlib_1bn = Image("background/mainbuilding/mlib_1bn.png", xalign=0.5, yalign=0.5)
image mlib_1bn_bg = Image("background/mainbuilding/mlib_1bn_bg.png", xalign=0.5, yalign=0.5)
image mlib_1br = Image("background/mainbuilding/mlib_1br.png", xalign=0.5, yalign=0.5)
image mlib_1br_bg = Image("background/mainbuilding/mlib_1br_bg.png", xalign=0.5, yalign=0.5)
image mlib_1c = Image("background/mainbuilding/mlib_1c.png", xalign=0.5, yalign=0.5)
image mlib_1c_bg = Image("background/mainbuilding/mlib_1c_bg.png", xalign=0.5, yalign=0.5)
image mlib_1c2 = Image("background/mainbuilding/mlib_1c2.png", xalign=0.5, yalign=0.5)
image mlib_1c2_bg = Image("background/mainbuilding/mlib_1c2_bg.png", xalign=0.5, yalign=0.5)
image mlib_1c3 = Image("background/mainbuilding/mlib_1c3.png", xalign=0.5, yalign=0.5)
image mlib_1c3_bg = Image("background/mainbuilding/mlib_1c3_bg.png", xalign=0.5, yalign=0.5)
image mlib_1cn = Image("background/mainbuilding/mlib_1cn.png", xalign=0.5, yalign=0.5)
image mlib_1cn_bg = Image("background/mainbuilding/mlib_1cn_bg.png", xalign=0.5, yalign=0.5)
image mlib_1cn2 = Image("background/mainbuilding/mlib_1cn2.png", xalign=0.5, yalign=0.5)
image mlib_1cn2_bg = Image("background/mainbuilding/mlib_1cn2.png", xalign=0.5, yalign=0.5)
image mlib_1cn3 = Image("background/mainbuilding/mlib_1cn3.png", xalign=0.5, yalign=0.5)
image mlib_1cn3_bg = Image("background/mainbuilding/mlib_1cn3.png", xalign=0.5, yalign=0.5)
image mlib_1cr = Image("background/mainbuilding/mlib_1cr.png", xalign=0.5, yalign=0.5)
image mlib_1cr_bg = Image("background/mainbuilding/mlib_1cr_bg.png", xalign=0.5, yalign=0.5)
image mlib_1cr2 = Image("background/mainbuilding/mlib_1cn2.png", xalign=0.5, yalign=0.5)
image mlib_1cr2_bg = Image("background/mainbuilding/mlib_1cn2_bg.png", xalign=0.5, yalign=0.5)
image mlib_1cr3 = Image("background/mainbuilding/mlib_1cn3.png", xalign=0.5, yalign=0.5)
image mlib_1cr3_bg = Image("background/mainbuilding/mlib_1cn3_bg.png", xalign=0.5, yalign=0.5)
image mlib_1e = Image("background/mainbuilding/mlib_1e.png", xalign=0.5, yalign=0.5)
image mlib_1en = Image("background/mainbuilding/mlib_1en.png", xalign=0.5, yalign=0.5)
image mlib_1er = Image("background/mainbuilding/mlib_1er.png", xalign=0.5, yalign=0.5)
image mnaka_1a = Image("background/mainbuilding/mnaka_1a.png", xalign=0.5, yalign=0.5)
image mnaka_1an = Image("background/mainbuilding/mnaka_1an.png", xalign=0.5, yalign=0.5)
image mnaka_1ar = Image("background/mainbuilding/mnaka_1ar.png", xalign=0.5, yalign=0.5)
image mnat_1a = Image("background/mainbuilding/mnat_1a.png", xalign=0.5, yalign=0.5)
image mnat_1a_bg = Image("background/mainbuilding/mnat_1a_bg.png", xalign=0.5, yalign=0.5)
image mnat_1am = Image("background/mainbuilding/mnat_1am.png", xalign=0.5, yalign=0.5)
image mnat_1an = Image("background/mainbuilding/mnat_1an.png", xalign=0.5, yalign=0.5)
image mnat_1ar = Image("background/mainbuilding/mnat_1ar.png", xalign=0.5, yalign=0.5)
image mnat_1ar_bg = Image("background/mainbuilding/mnat_1ar_bg.png", xalign=0.5, yalign=0.5)
image mnat_2b = Image("background/mainbuilding/mnat_2b.png", xalign=0.5, yalign=0.5)
image mnat_2bn = Image("background/mainbuilding/mnat_2bn.png", xalign=0.5, yalign=0.5)
image mnat_2br = Image("background/mainbuilding/mnat_2br.png", xalign=0.5, yalign=0.5)
image msta_1b = Image("background/mainbuilding/msta_1b.png", xalign=0.5, yalign=0.5)
image msta_1b_bg = Image("background/mainbuilding/msta_1b_bg.png", xalign=0.5, yalign=0.5)
image msta_1c = Image("background/mainbuilding/msta_1c.png", xalign=0.5, yalign=0.5)
image mvip_1a = Image("background/mainbuilding/mvip_1a.png", xalign=0.5, yalign=0.5)
image mvip_1a_bg = Image("background/mainbuilding/mvip_1a_bg.png", xalign=0.5, yalign=0.5)
image mvip_1an = Image("background/mainbuilding/mvip_1an.png", xalign=0.5, yalign=0.5)
image mvip_1ar = Image("background/mainbuilding/mvip_1ar.png", xalign=0.5, yalign=0.5)
image mvip_1c = Image("background/mainbuilding/mvip_1c.png", xalign=0.5, yalign=0.5)
image mvip_1c_bg = Image("background/mainbuilding/mvip_1c_bg.png", xalign=0.5, yalign=0.5)
image mvip_1cn = Image("background/mainbuilding/mvip_1cn.png", xalign=0.5, yalign=0.5)
image mvip_1cr = Image("background/mainbuilding/mvip_1cr.png", xalign=0.5, yalign=0.5)
image portrait1 = "background/mainbuilding/portrait1.png"
image portrait2 = Image("background/mainbuilding/portrait2.png", xalign=0.5, yalign=0.5)
image portrait3 = Image("background/mainbuilding/portrait3.png", xalign=0.5, yalign=0.5)
image portrait4 = Image("background/mainbuilding/portrait4.png", xalign=0.5, yalign=0.5)
image portrait4b = Image("background/mainbuilding/portrait4b.png", xalign=0.5, yalign=0.5)

image nan_r1a = Image("background/nanclinic/nan_r1a.png", xalign=0.5, yalign=0.5)
image nan_r1c = Image("background/nanclinic/nan_r1c.png", xalign=0.5, yalign=0.5)

image res_i1a = Image("background/restaurant/res_i1a.png", xalign=0.5, yalign=0.5)
image res_i1af = Image("background/restaurant/res_i1af.png", xalign=0.5, yalign=0.5)
image res_i1c = Image("background/restaurant/res_i1c.png", xalign=0.5, yalign=0.5)
image res_i1cf = Image("background/restaurant/res_i1cf.png", xalign=0.5, yalign=0.5)
image res_i2c = Image("background/restaurant/res_i2c.png", xalign=0.5, yalign=0.5)
image res_i2cf = Image("background/restaurant/res_i2cf.png", xalign=0.5, yalign=0.5)
image res_i3a = Image("background/restaurant/res_i3a.png", xalign=0.5, yalign=0.5)
image res_i3ar = Image("background/restaurant/res_i3ar.png", xalign=0.5, yalign=0.5)
image res_i3d = Image("background/restaurant/res_i3d.png", xalign=0.5, yalign=0.5)
image res_i3dr = Image("background/restaurant/res_i3dr.png", xalign=0.5, yalign=0.5)
image res_i4a = Image("background/restaurant/res_i4a.png", xalign=0.5, yalign=0.5)

image ros_m1a = Image("background/rosehouse/ros_m1a.png", xalign=0.5, yalign=0.5)
image ros_m1an = Image("background/rosehouse/ros_m1an.png", xalign=0.5, yalign=0.5)
image ros_m1ar = Image("background/rosehouse/ros_m1ar.png", xalign=0.5, yalign=0.5)
image ros_o1an = Image("background/rosehouse/ros_o1an.png", xalign=0.5, yalign=0.5)
image ros_p1a = Image("background/rosehouse/ros_p1a.png", xalign=0.5, yalign=0.5)
image ros_p1an = Image("background/rosehouse/ros_p1an.png", xalign=0.5, yalign=0.5)
image ros_p1ar = Image("background/rosehouse/ros_p1ar.png", xalign=0.5, yalign=0.5)
image ros_r1a = Image("background/rosehouse/ros_r1a.png", xalign=0.5, yalign=0.5)
image ros_r1an = Image("background/rosehouse/ros_r1an.png", xalign=0.5, yalign=0.5)
image ros_r1ar = Image("background/rosehouse/ros_r1ar.png", xalign=0.5, yalign=0.5)
image ros_ro1a = Image("background/rosehouse/ros_ro1a.png", xalign=0.5, yalign=0.5)
image ros_ro1an = Image("background/rosehouse/ros_ro1an.png", xalign=0.5, yalign=0.5)
image ros_ro1ar = Image("background/rosehouse/ros_ro1ar.png", xalign=0.5, yalign=0.5)

image schd_p1a = Image("background/school/schd_p1a.png", xalign=0.5, yalign=0.5)
image schd_p1ar = Image("background/school/schd_p1ar.png", xalign=0.5, yalign=0.5)
image schf_c2a = Image("background/school/schf_c2a.png", xalign=0.5, yalign=0.5)
image schf_c2ar = Image("background/school/schf_c2ar.png", xalign=0.5, yalign=0.5)
image schf_c2b = Image("background/school/schf_c2b.png", xalign=0.5, yalign=0.5)
image schf_c2br = Image("background/school/schf_c2br.png", xalign=0.5, yalign=0.5)
image schf_p1a = Image("background/school/schf_p1a.png", xalign=0.5, yalign=0.5)
image schf_r1a = Image("background/school/schf_r1a.png", xalign=0.5, yalign=0.5)
image schf_s1a = Image("background/school/schf_s1a.png", xalign=0.5, yalign=0.5)
image schr_o1a = Image("background/school/schr_o1a.png", xalign=0.5, yalign=0.5)
image schr_o2a = Image("background/school/schr_o2a.png", xalign=0.5, yalign=0.5)
image schr_p1b = Image("background/school/schr_p1b.png", xalign=0.5, yalign=0.5)
image schr_r1a = Image("background/school/schr_r1a.png", xalign=0.5, yalign=0.5)
image schr_r1an = Image("background/school/schr_r1an.png", xalign=0.5, yalign=0.5)
image schr_r1ar = Image("background/school/schr_r1ar.png", xalign=0.5, yalign=0.5)
image schr_r1d = Image("background/school/schr_r1d.png", xalign=0.5, yalign=0.5)
image toi_1a = Image("background/school/toi_1a.png", xalign=0.5, yalign=0.5)

image fence_1a = Image("background/secrethouse/fence_1a.png", xalign=0.5, yalign=0.5)
image se_o1a = Image("background/secrethouse/se_o1a.png", xalign=0.5, yalign=0.5)
image se1f_s1a = Image("background/secrethouse/se1f_s1a.png", xalign=0.5, yalign=0.5)
image se1f_s1an = Image("background/secrethouse/se1f_s1an.png", xalign=0.5, yalign=0.5)
image sehal_1a = Image("background/secrethouse/sehal_1a.png", xalign=0.5, yalign=0.5)

image sea_1a = Image("background/ship/sea_1a.png", xalign=0.5, yalign=0.5)
image sea_1af = Image("background/ship/sea_1af.png", xalign=0.5, yalign=0.5)
image sea_1b = Image("background/ship/sea_1b.png", xalign=0.5, yalign=0.5)
image sea_1bf = Image("background/ship/sea_1bf.png", xalign=0.5, yalign=0.5)
image sea_1bn = Image("background/ship/sea_1bn.png", xalign=0.5, yalign=0.5)
image sea_1c = Image("background/ship/sea_1c.png", xalign=0.5, yalign=0.5)
image sea_1cf = Image("background/ship/sea_1cf.png", xalign=0.5, yalign=0.5)
image sea_3a = Image("background/ship/sea_3a.png", xalign=0.5, yalign=0.5)
image sea_3af = Image("background/ship/sea_3af.png", xalign=0.5, yalign=0.5)
image sea_3ar = Image("background/ship/sea_3ar.png", xalign=0.5, yalign=0.5)
image sea_3b = Image("background/ship/sea_3b.png", xalign=0.5, yalign=0.5)
image sea_3bc = Image("background/ship/sea_3bc.png", xalign=0.5, yalign=0.5)
image sea_3bf = Image("background/ship/sea_3bf.png", xalign=0.5, yalign=0.5)
image sea_3bi = Image("background/ship/sea_3bi.png", xalign=0.5, yalign=0.5)
image sea_3bm = Image("background/ship/sea_3bm.png", xalign=0.5, yalign=0.5)
image sea_3bp = Image("background/ship/sea_3bp.png", xalign=0.5, yalign=0.5)
image sea_3br = Image("background/ship/sea_3br.png", xalign=0.5, yalign=0.5)
image sea2a = Image("background/ship/sea2a.png", xalign=0.5, yalign=0.5)
image sea2an = Image("background/ship/sea2an.png", xalign=0.5, yalign=0.5)
image sea2b = Image("background/ship/sea2b.png", xalign=0.5, yalign=0.5)
image sea2bn = Image("background/ship/sea2bn.png", xalign=0.5, yalign=0.5)
image ship_p1a = Image("background/ship/ship_p1a.png", xalign=0.5, yalign=0.5)
image ship_p1ac = Image("background/ship/ship_p1ac.png", xalign=0.5, yalign=0.5)
image ship_p1c = Image("background/ship/ship_p1c.png", xalign=0.5, yalign=0.5)
image ship_p1cc = Image("background/ship/ship_p1cc.png", xalign=0.5, yalign=0.5)
image ship_s1a = Image("background/ship/ship_s1a.png", xalign=0.5, yalign=0.5)
image ship_s1af = Image("background/ship/ship_s1af.png", xalign=0.5, yalign=0.5)
image ship_s1b = Image("background/ship/ship_s1b.png", xalign=0.5, yalign=0.5)
image ship_s1bf = Image("background/ship/ship_s1bf.png", xalign=0.5, yalign=0.5)
image ship_s2a = Image("background/ship/ship_s2a.png", xalign=0.5, yalign=0.5)
image ship_s2af = Image("background/ship/ship_s2af.png", xalign=0.5, yalign=0.5)
image ship_s2b = Image("background/ship/ship_s2b.png", xalign=0.5, yalign=0.5)
image ship_s2bf = Image("background/ship/ship_s2bf.png", xalign=0.5, yalign=0.5)
image ship_s3a = Image("background/ship/ship_s3a.png", xalign=0.5, yalign=0.5)
image shr_1a = Image("background/ship/shr_1a.png", xalign=0.5, yalign=0.5)
image shr_1an = Image("background/ship/shr_1an.png", xalign=0.5, yalign=0.5)

image pri_i1a = Image("background/subway/pri_i1a.png", xalign=0.5, yalign=0.5)
image pri_i1a_2_sak = Image("background/subway/pri_i1a_2_sak.png", xalign=0.5, yalign=0.5)
image pri_i1a_sak = Image("background/subway/pri_i1a_sak.png", xalign=0.5, yalign=0.5)
image pri_i1ac = Image("background/subway/pri_i1ac.png", xalign=0.5, yalign=0.5)
image pri_i1ac_sak = Image("background/subway/pri_i1ac_sak.png", xalign=0.5, yalign=0.5)
image pri_i1acb = Image("background/subway/pri_i1acb.png", xalign=0.5, yalign=0.5)
image pri_i1acb_zoom = "background/subway/pri_i1acb2.png"
image pri_i1b = Image("background/subway/pri_i1b.png", xalign=0.5, yalign=0.5)
image pri_i1c = Image("background/subway/pri_i1c.png", xalign=0.5, yalign=0.5)
image pri_i1c_2_sak = Image("background/subway/pri_i1c_2_sak.png", xalign=0.5, yalign=0.5)
image pri_i1c_sak = Image("background/subway/pri_i1c_sak.png", xalign=0.5, yalign=0.5)
image pri_i1d = Image("background/subway/pri_i1d.png", xalign=0.5, yalign=0.5)
image pri_i1d_sak = Image("background/subway/pri_i1d_sak.png", xalign=0.5, yalign=0.5)
image sub_d1a = Image("background/subway/sub_d1a.png", xalign=0.5, yalign=0.5)
image sub_p1a = Image("background/subway/sub_p1a.png", xalign=0.5, yalign=0.5)
image sub_p1a_blur = Image("background/subway/sub_p1a_blur.png", xalign=0.5, yalign=0.5)
image sub_p1b = Image("background/subway/sub_p1b.png", xalign=0.5, yalign=0.5)
image sub_r1a = Image("background/subway/sub_r1a.png", xalign=0.5, yalign=0.5)
image sub_r1ap = Image("background/subway/sub_r1ap.png", xalign=0.5, yalign=0.5)
image sub_r1b = Image("background/subway/sub_r1b.png", xalign=0.5, yalign=0.5)
image sub_r1bp = Image("background/subway/sub_r1bp.png", xalign=0.5, yalign=0.5)
image sub_sta1a = Image("background/subway/sub_sta1a.png", xalign=0.5, yalign=0.5)

# Image variants go here.
image rainback orange:
    contains:
        SnowBlossom(im.MatrixColor("efe/RAIN_small.png", im.matrix.colorize("#ffcc88", "#ffcc88")), count=100, border=190, xspeed=(0, 1), yspeed=(10000, 12000), start=0, horizontal=False)
    contains:
        SnowBlossom(im.MatrixColor("efe/rain_bg1.png", im.matrix.colorize("#ffcc88", "#ffcc88")), count=100, border=190, xspeed=(0, 1), yspeed=(10000, 12000), start=0, horizontal=False)
    contains:
        SnowBlossom(im.MatrixColor("efe/rain_bg2.png", im.matrix.colorize("#ffcc88", "#ffcc88")), count=100, border=250, xspeed=(0, 1), yspeed=(10000, 12000), start=0, horizontal=False)
image rainfront orange:
    contains:
        SnowBlossom(im.MatrixColor("efe/rain_fg.png", im.matrix.colorize("#ffcc88", "#ffcc88")), count=100, border=300, xspeed=(0, 1), yspeed=(10000, 12000), start=0, horizontal=False)
    contains:
        SnowBlossom(im.MatrixColor("efe/RAIN_medium.png", im.matrix.colorize("#ffcc88", "#ffcc88")), count=100, border=300, xspeed=(0, 1), yspeed=(10000, 12000), start=0, horizontal=False)
    contains:
        SnowBlossom(im.MatrixColor("efe/RAIN_large.png", im.matrix.colorize("#ffcc88", "#ffcc88")), count=100, border=300, xspeed=(0, 1), yspeed=(10000, 12000), start=0, horizontal=False)

image rainback e0406:
    rotate 6 xanchor 0.5 xpos (1425.0/1920.0) yalign 0.5
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_small.png", count=100, border=128, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                        "rain_static == 1", Image("efe/rain_bg_static.png"))
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg1.png", count=100, border=161, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg2.png", count=100, border=214, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_small.png", count=100, border=128, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg1.png", count=100, border=161, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                        "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_bg2.png", count=100, border=214, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                        "rain_static == 1", Null())
image rainfront e0406:
    rotate 6 xanchor 0.5 xpos (1425.0/1920.0) yalign 0.5
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/rain_fg.png", count=100, border=268, xspeed=0, yspeed=(10000, 12000), start=10, horizontal=False),
                                "rain_static == 1", Image("efe/rain_fg_static.png"))
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_medium.png", count=100, border=256, xspeed=0, yspeed=(10000, 12000), start=5, horizontal=False),
                                "rain_static == 1", Null())
    contains:
        ConditionSwitch("rain_static == 0", SnowBlossom("efe/RAIN_large.png", count=100, border=384, xspeed=0, yspeed=(10000, 12000), start=0, horizontal=False),
                                "rain_static == 1", Null())


image no33_00069 gray = im.MatrixColor("anime/no33_00069.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image no54_00059 gray = im.MatrixColor("anime/no54_00059.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image air_out2b gray = im.MatrixColor("background/airport/air_out2b.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image aqu_i1a sepia = im.Sepia("background/aquarium/aqu_i1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image aqu_i2a sepia = im.Sepia("background/aquarium/aqu_i2a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image aqu_i2b sepia = im.Sepia("background/aquarium/aqu_i2b.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)

image amu_i1a sepia = im.Sepia("background/city/amu_i1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image cit_1a gray = im.MatrixColor("background/city/cit_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image cit_2a gray = im.MatrixColor("background/city/cit_2a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image cit_3a gray = im.MatrixColor("background/city/cit_3a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image hos_r1cm gray = im.MatrixColor("background/city/hos_r1cm.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image hot_r1a gray = im.MatrixColor("background/city/hot_r1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image par_1a gray = im.MatrixColor("background/city/par_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image par_1c gray = im.MatrixColor("background/city/par_1c.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image blade4p gray = im.MatrixColor("background/efe/blade4p.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image blood_1a gray = im.MatrixColor("background/efe/blood_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image blood_1a sepia = im.Sepia("background/efe/blood_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image blood_1ar sepia = im.Sepia("background/efe/blood_1ar.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image blood_2e gray = im.MatrixColor("background/efe/blood_2e.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image bullet1a gray = im.MatrixColor("background/efe/bullet1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image bullet1b gray = im.MatrixColor("background/efe/bullet1b.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image butterfly_3a nega = im.MatrixColor("background/efe/butterfly_3a.png", im.matrix.invert())
image butterfly_3a sepia = im.Sepia("background/efe/butterfly_3a.png", tint=(.722, .6, .435))
image butterfly_4sp2 gray = im.MatrixColor("background/efe/butterfly_4sp2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8))
image chess1 gray = im.MatrixColor("background/efe/chess1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image different_spiral_1a gray = im.MatrixColor("background/efe/different_spiral_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image gold1 gray = im.MatrixColor("background/efe/gold1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image gold2 gray = im.MatrixColor("background/efe/gold2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image homing1 gray = im.MatrixColor("background/efe/homing1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image homing6 gray = im.MatrixColor("background/efe/homing6.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image letter1 gray = im.MatrixColor("background/efe/letter1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image map10 gray = im.MatrixColor("background/efe/map10.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image map10 gray_888 = im.MatrixColor("background/efe/map10.png", im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xalign=0.5, yalign=0.5)
image red_b gray = im.MatrixColor("background/efe/red_b.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sakutaro1ab gray = im.MatrixColor("background/efe/sakutaro1ab.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sakutaro2ab gray = im.MatrixColor("background/efe/sakutaro2ab.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sakutaro2bb gray = im.MatrixColor("background/efe/sakutaro2bb.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sweet1 gray = im.MatrixColor("background/efe/sweet1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image tel1a gray = im.MatrixColor("background/efe/tel1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image tower2 gray = im.MatrixColor("background/efe/tower2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image white sepia = im.Sepia("background/efe/white.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)

image cha_i1a gray = im.MatrixColor("background/chapel/cha_i1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image cha_i1a_bg gray = im.MatrixColor("background/chapel/cha_i1a_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image cha_o2a gray = im.MatrixColor("background/chapel/cha_o2a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image beach_2a gray = im.MatrixColor("background/forest/beach_2a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image forest_p1a sepia = im.Sepia("background/forest/forest_p1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image moon_1b gray = im.MatrixColor("background/forest/moon_1b.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image o_beach_1a sepia = im.Sepia("background/forest/o_beach_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image o_sky_1a sepia = im.Sepia("background/forest/o_sky_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image sky_1a gray = im.MatrixColor("background/forest/sky_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sky_1a sepia = im.Sepia("background/forest/sky_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image sky_2b sepia = im.Sepia("background/forest/sky_2b.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)

image garden_1af gray = im.Grayscale("background/garden/garden_1af.png", xalign=0.5, yalign=0.5)
image garden_r1an gray = im.MatrixColor("background/garden/garden_r1an.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image garden_r1an_bg gray = im.MatrixColor("background/garden/garden_r1an_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image garden_se1b gray = im.Grayscale("background/garden/garden_se1b.png", xalign=0.5, yalign=0.5)
image garden_seaia gray = im.Grayscale("background/garden/garden_seaia.png", xalign=0.5, yalign=0.5)
image rose_1a gray = im.Grayscale("background/garden/rose_1a.png", xalign=0.5, yalign=0.5)
image rose_1an gray = im.Grayscale("background/garden/rose_1an.png", xalign=0.5, yalign=0.5)
image rose_1ar gray = im.MatrixColor("background/garden/rose_1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image rose_1ep nega = im.MatrixColor("background/garden/rose_1ep.png", im.matrix.invert(), xalign=0.5, yalign=0.5)
image rose_3apr gray = im.MatrixColor("background/garden/rose_3apr.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image rose_g1af gray = im.Grayscale("background/garden/rose_g1af.png", xalign=0.5, yalign=0.5)
image rose_g1c sepia = im.Sepia("background/garden/rose_g1c.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image warehous_i1a gray = im.Grayscale("background/garden/warehous_i1a.png", xalign=0.5, yalign=0.5)
image warehous_i1a_bg gray = im.Grayscale("background/garden/warehous_i1a_bg.png", xalign=0.5, yalign=0.5)
image warehous_o1a gray = im.Grayscale("background/garden/warehous_o1a.png", xalign=0.5, yalign=0.5)

image g_o1cf red = im.MatrixColor(
    "background/guesthouse/g_o1cf.png",
    im.matrix.desaturate() * im.matrix.tint(1, 0, 0), xalign=0.5, yalign=0.5)
image g1f_p1ar gray = im.MatrixColor("background/guesthouse/g1f_p1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g1f_p1ar_bg gray = im.MatrixColor("background/guesthouse/g1f_p1ar_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g1f_p1c gray = im.MatrixColor("background/guesthouse/g1f_p1c.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g1f_r2ar gray = im.MatrixColor("background/guesthouse/g1f_r2ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g1f_r2ar_bg gray = im.MatrixColor("background/guesthouse/g1f_r2ar_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g1f_s1ap gray = im.MatrixColor("background/guesthouse/g1f_s1ap.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g1f_s1bp gray = im.MatrixColor("background/guesthouse/g1f_s1bp.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g2f_p1ar gray = im.MatrixColor("background/guesthouse/g2f_p1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g2f_p1ar_bg gray = im.MatrixColor("background/guesthouse/g2f_p1ar_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g2f_r1ar gray = im.MatrixColor("background/guesthouse/g2f_r1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image g2f_r1ar_bg gray = im.MatrixColor("background/guesthouse/g2f_r1ar_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image gdin_1ad2 gray = im.MatrixColor("background/guesthouse/gdin_1ad2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image gdin_1ad2 sepia = im.Sepia("background/guesthouse/gdin_1ad2.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image glob_1d gray_888 = im.MatrixColor("background/guesthouse/glob_1d.png", im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xalign=0.5, yalign=0.5)
image glob_1d_bg gray_888 = im.MatrixColor("background/guesthouse/glob_1d_bg.png", im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xalign=0.5, yalign=0.5)


image m_door1 gray = im.MatrixColor("background/mainbuilding/m_door1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m_door1k gray = im.MatrixColor("background/mainbuilding/m_door1k.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m_door2 gray = im.MatrixColor("background/mainbuilding/m_door2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m_o1a gray = im.MatrixColor("background/mainbuilding/m_o1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m_o1a sepia = im.Sepia("background/mainbuilding/m_o1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m_o1af sepia = im.Sepia("background/mainbuilding/m_o1af.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m_o1af gray = im.MatrixColor("background/mainbuilding/m_o1af.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m_o1ar gray = im.MatrixColor("background/mainbuilding/m_o1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m2f_p1af gray = im.Grayscale("background/mainbuilding/m2f_p1af.png", xalign=0.5, yalign=0.5)
image m1f_p1b gray = im.Grayscale("background/mainbuilding/m1f_p1b.png", xalign=0.5, yalign=0.5)
image m1f_p1b_bg gray = im.Grayscale("background/mainbuilding/m1f_p1b_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1b sepia = im.Sepia("background/mainbuilding/m1f_p1b.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_p1b_bg sepia = im.Sepia("background/mainbuilding/m1f_p1b_bg.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_p2b gray = im.Grayscale("background/mainbuilding/m1f_p2b.png", xalign=0.5, yalign=0.5)
image m1f_p2b_bg gray = im.Grayscale("background/mainbuilding/m1f_p2b_bg.png", xalign=0.5, yalign=0.5)
image m1f_p2br gray = im.Grayscale("background/mainbuilding/m1f_p2br.png", xalign=0.5, yalign=0.5)
image m1f_p2br_bg gray = im.Grayscale("background/mainbuilding/m1f_p2br_bg.png", xalign=0.5, yalign=0.5)
image m1f_p1d sepia = im.Sepia("background/mainbuilding/m1f_p1d.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_p1d_bg sepia = im.Sepia("background/mainbuilding/m1f_p1d_bg.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_s1a gray = im.MatrixColor("background/mainbuilding/m1f_s1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m1f_s1a_bg gray = im.MatrixColor("background/mainbuilding/m1f_s1a_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m1f_s1a sepia = im.Sepia("background/mainbuilding/m1f_s1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_s1a_bg sepia = im.Sepia("background/mainbuilding/m1f_s1a_bg.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_s1ar_bg gray = im.MatrixColor("background/mainbuilding/m1f_s1ar_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m1f_s1ar gray = im.MatrixColor("background/mainbuilding/m1f_s1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m1f_s1c gray = im.MatrixColor("background/mainbuilding/m1f_s1c.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m1f_s1c sepia = im.Sepia("background/mainbuilding/m1f_s1c.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m1f_s1cr gray = im.MatrixColor("background/mainbuilding/m1f_s1cr.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image m1f_s1d sepia = im.Sepia("background/mainbuilding/m1f_s1d.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image m2f_p1b gray = im.Grayscale("background/mainbuilding/m2f_p1b.png", xalign=0.5, yalign=0.5)
image m2f_p1b_bg gray = im.Grayscale("background/mainbuilding/m2f_p1b_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1c gray = im.Grayscale("background/mainbuilding/m2f_p1c.png", xalign=0.5, yalign=0.5)
image m2f_p1c_bg gray = im.Grayscale("background/mainbuilding/m2f_p1c_bg.png", xalign=0.5, yalign=0.5)
image m2f_p1cr gray = im.Grayscale("background/mainbuilding/m2f_p1cr.png", xalign=0.5, yalign=0.5)
image m2f_p1cr_bg gray = im.Grayscale("background/mainbuilding/m2f_p1cr_bg.png", xalign=0.5, yalign=0.5)
image mdin_1a gray = im.MatrixColor("background/mainbuilding/mdin_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mdin_1ar gray = im.MatrixColor("background/mainbuilding/mdin_1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mdin_1a sepia = im.Sepia("background/mainbuilding/mdin_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image mdin_1c gray = im.Grayscale("background/mainbuilding/mdin_1c.png", xalign=0.5, yalign=0.5)
image mdin_1c_bg gray = im.Grayscale("background/mainbuilding/mdin_1c_bg.png", xalign=0.5, yalign=0.5)
image mdin_1c sepia = im.Sepia("background/mainbuilding/mdin_1c.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image mdin_1c_bg sepia = im.Sepia("background/mainbuilding/mdin_1c_bg.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image mdin_1cr gray = im.Grayscale("background/mainbuilding/mdin_1cr.png", xalign=0.5, yalign=0.5)
image mdin_1cr_bg gray = im.Grayscale("background/mainbuilding/mdin_1cr_bg.png", xalign=0.5, yalign=0.5)
image mdin_1e gray = im.MatrixColor("background/mainbuilding/mdin_1e.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mdin_1e sepia = im.Sepia("background/mainbuilding/mdin_1e.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image mdin_1f gray = im.Grayscale("background/mainbuilding/mdin_1f.png", xalign=0.5, yalign=0.5)
image mdin_1fr gray = im.Grayscale("background/mainbuilding/mdin_1fr.png", xalign=0.5, yalign=0.5)
image mdin_1gr gray = im.Grayscale("background/mainbuilding/mdin_1gr.png", xalign=0.5, yalign=0.5)
image mdin_1gr_bg gray = im.Grayscale("background/mainbuilding/mdin_1gr_bg.png", xalign=0.5, yalign=0.5)
image mhal_1a gray = im.MatrixColor("background/mainbuilding/mhal_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mhal_1a_bg gray = im.MatrixColor("background/mainbuilding/mhal_1a_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mhal_2a gray = im.MatrixColor("background/mainbuilding/mhal_2a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mhal_2a_bg gray = im.MatrixColor("background/mainbuilding/mhal_2a_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mhal_2c gray = im.MatrixColor("background/mainbuilding/mhal_2c.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mjes_1af gray = im.Grayscale("background/mainbuilding/mjes_1af.png", xalign=0.5, yalign=0.5)
image mjes_1cr gray = im.MatrixColor("background/mainbuilding/mjes_1cr.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mjes_1cr_bg gray = im.MatrixColor("background/mainbuilding/mjes_1cr_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mjes_1e gray = im.Grayscale("background/mainbuilding/mjes_1e.png", xalign=0.5, yalign=0.5)
image mkit_1a gray = im.Grayscale("background/mainbuilding/mkit_1a.png", xalign=0.5, yalign=0.5)
image mkit_1a_bg gray = im.Grayscale("background/mainbuilding/mkit_1a_bg.png", xalign=0.5, yalign=0.5)
image mlib_1a sepia = im.Sepia("background/mainbuilding/mlib_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image mlib_1a_bg sepia = im.Sepia("background/mainbuilding/mlib_1a_bg.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image mlib_1a gray = im.MatrixColor("background/mainbuilding/mlib_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mlib_1a_bg gray = im.MatrixColor("background/mainbuilding/mlib_1a_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mlib_1b gray = im.MatrixColor("background/mainbuilding/mlib_1b.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mlib_1b_bg gray = im.MatrixColor("background/mainbuilding/mlib_1b_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mlib_1c gray = im.MatrixColor("background/mainbuilding/mlib_1c.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image mlib_1c_bg gray = im.MatrixColor("background/mainbuilding/mlib_1c_bg.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image portrait2 gray = im.MatrixColor("background/mainbuilding/portrait2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image portrait2 sepia = im.Sepia("background/mainbuilding/portrait2.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image portrait3 gray = im.MatrixColor("background/mainbuilding/portrait3.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image ros_m1a gray = im.MatrixColor("background/rosehouse/ros_m1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image ros_r1a gray = im.MatrixColor("background/rosehouse/ros_r1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image ros_r1ar gray = im.MatrixColor("background/rosehouse/ros_r1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image schr_r1an gray = im.MatrixColor("background/school/schr_r1an.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image schr_r1ar gray = im.MatrixColor("background/school/schr_r1ar.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image sehal_1a sepia = im.Sepia("background/secrethouse/sehal_1a.png", tint=(.722, .6, .435), xalign=0.5, yalign=0.5)
image sehal_1a gray = im.MatrixColor("background/secrethouse/sehal_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image sea_1b gray = im.MatrixColor("background/ship/sea_1b.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sea_1c gray = im.MatrixColor("background/ship/sea_1c.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image sea_1cf gray = im.MatrixColor("background/ship/sea_1cf.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image shr_1a gray = im.MatrixColor("background/ship/shr_1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)
image shr_1an gray = im.MatrixColor("background/ship/shr_1an.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image sub_p1a gray = im.MatrixColor("background/subway/sub_p1a.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xalign=0.5, yalign=0.5)

image g0402 gray = im.MatrixColor("cg/g0402.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8))

image gen a11_komaru1 gray = im.MatrixColor("tati/gen/gen_a11_komaru1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=368, yanchor=1022, ypos=1.0)
image gen a11_def1 boi = im.MatrixColor("tati/gen/gen_a11_def1.png", im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=368, yanchor=1022, ypos=1.0)
image gen a11_komaru1 boi = im.MatrixColor("tati/gen/gen_a11_komaru1.png", im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=368, yanchor=1022, ypos=1.0)
image gen a11_majime1 boi = im.MatrixColor("tati/gen/gen_a11_majime1.png", im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=368, yanchor=1022, ypos=1.0)

image geo a11_def1 gray = im.MatrixColor(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=372, yanchor=1031, ypos=1.0)
image geo a11_hohoemi1 gray = im.MatrixColor(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11_hohoemi1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=372, yanchor=1031, ypos=1.0)
image geo a11_ikari2 gray = im.MatrixColor(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11_ikari2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=372, yanchor=1031, ypos=1.0)
image geo a11_warai1 gray = im.MatrixColor(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=372, yanchor=1031, ypos=1.0)
image geo a11k_majime2k gray = im.MatrixColor(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11k_majime2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=372, yanchor=1031, ypos=1.0)
image geo a11k_majime3k gray_888 = im.MatrixColor(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11k_majime3.png"), im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xanchor=372, yanchor=1031, ypos=1.0)
image geo c11_hohoemi1 sepia = im.Sepia(im.Composite((722, 1174), (0, 0), "tati/geo/geo_c11.png", (0, 0), "tati/geo/geo_c11_hohoemi1.png"), tint=(.722, .6, .435), xanchor=370, yanchor=1031, ypos=1.0)
image geo c11k_def1k sepia = im.Sepia(im.Composite((722, 1174), (0, 0), "tati/geo/geo_c11.png", (0, 0), "tati/geo/geo_c11k_def1.png"), tint=(.722, .6, .435), xanchor=370, yanchor=1031, ypos=1.0)
image geo c11k_warai1k sepia = im.Sepia(im.Composite((722, 1174), (0, 0), "tati/geo/geo_c11.png", (0, 0), "tati/geo/geo_c11k_warai1.png"), tint=(.722, .6, .435), xanchor=370, yanchor=1031, ypos=1.0)
image geo c11k_warai1k sunset = im.MatrixColor(im.Composite((722, 1174), (0, 0), "tati/geo/geo_c11.png", (0, 0), "tati/geo/geo_c11k_warai1.png"), im.matrix.tint(1.0, (234.0/255.0), (196.0/255.0)), xanchor=370, yanchor=1031, ypos=1.0)
image geo c12_hohoemi1 sunset = im.MatrixColor(im.Composite((1032, 1174), (0, 0), "tati/geo/geo_c12.png", (0, 0), "tati/geo/geo_c11k_warai1.png"), im.matrix.tint(1.0, (234.0/255.0), (196.0/255.0)), xanchor=370, yanchor=1031, ypos=1.0)

image but b11_warai1 sepia = im.Sepia(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_warai1.png"), tint=(.722, .6, .435), xanchor=399, yanchor=1076, ypos=1.0)
image but b11_def2 gray = im.MatrixColor(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_def2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=399, yanchor=1076, ypos=1.0)
image but b11_def2 sepia = im.Sepia(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_def2.png"), tint=(.722, .6, .435), xanchor=399, yanchor=1076, ypos=1.0)
image but b11_kuyasigaru1 gray = im.Grayscale(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_kuyasigaru1.png"), xanchor=399, yanchor=1076, ypos=1.0)
image but b11_nayamu1 gray = im.Grayscale(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_nayamu1.png"), xanchor=399, yanchor=1076, ypos=1.0)
image but b22_kuyasigaru1 gray = im.MatrixColor(im.Composite((816, 1208), (0, 0), "tati/but/but_b22.png", (0, 0), "tati/but/but_b22_kuyasigaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=399, yanchor=1065, ypos=1.0)
image but b22_odoroki1 gray = im.MatrixColor(im.Composite((816, 1208), (0, 0), "tati/but/but_b22.png", (0, 0), "tati/but/but_b22_odoroki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=399, yanchor=1065, ypos=1.0)
image but b22_odoroki2 sepia = im.Sepia(im.Composite((816, 1208), (0, 0), "tati/but/but_b22.png", (0, 0), "tati/but/but_b22_odoroki2.png"), tint=(.722, .6, .435), xanchor=399, yanchor=1065, ypos=1.0)
image but b25_odoroki1 gray = im.MatrixColor(im.Composite((919, 1208), (0, 0), "tati/but/but_b25.png", (0, 0), "tati/but/but_b22_odoroki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=502, yanchor=1065, ypos=1.0)
image but b11_nayamu1 boi = im.MatrixColor(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_nayamu1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=399, yanchor=1076, ypos=1.0)
image but b11_nayamu2 boi = im.MatrixColor(im.Composite((756, 1219), (0, 0), "tati/but/but_b11.png", (0, 0), "tati/but/but_b11_nayamu2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=399, yanchor=1076, ypos=1.0)
image but b22_komaru2 boi = im.MatrixColor(im.Composite((816, 1208), (0, 0), "tati/but/but_b22.png", (0, 0), "tati/but/but_b22_komaru2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=399, yanchor=1065, ypos=1.0)
image but b22_odoroki1 boi = im.MatrixColor(im.Composite((816, 1208), (0, 0), "tati/but/but_b22.png", (0, 0), "tati/but/but_b22_odoroki1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=399, yanchor=1065, ypos=1.0)

image eva a11_akire1 gray = im.MatrixColor(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_akire1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_akire1 sepia = im.Sepia(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_akire1.png"), tint=(.722, .6, .435), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_akuwarai1 sepia = im.Sepia(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_akuwarai1.png"), tint=(.722, .6, .435), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_def1 gray = im.MatrixColor(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_futeki1 sepia = im.Sepia(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_futeki1.png"), tint=(.722, .6, .435), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_ikari2 gray = im.MatrixColor(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_ikari2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_ikari2 sepia = im.Sepia(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_ikari2.png"), tint=(.722, .6, .435), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_majime1 gray = im.MatrixColor(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_majime1 sepia = im.Sepia(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_majime1.png"), tint=(.722, .6, .435), xanchor=238, yanchor=998, ypos=1.0)
image eva a11_warai1 gray = im.MatrixColor(im.Composite((468, 1141), (0, 0), "tati/eva/eva_a11.png", (0, 0), "tati/eva/eva_a11_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=238, yanchor=998, ypos=1.0)
image eva b21_akire2b gray = im.MatrixColor(im.Composite((788, 1155), (0, 0), "tati/eva/eva_b21.png", (0, 0), "tati/eva/eva_b21_akire2b.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=471, yanchor=1012, ypos=1.0)
image eva b23_komaru4 gray = im.MatrixColor(im.Composite((792, 1155), (0, 0), "tati/eva/eva_b23.png", (-170, 0), "tati/eva/eva_b21_komaru4.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=301, yanchor=1012, ypos=1.0)
image eva b24_majime1 gray = im.MatrixColor(im.Composite((490, 1155), (0, 0), "tati/eva/eva_b24.png", (-182, 0), "tati/eva/eva_b21_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=289, yanchor=1012, ypos=1.0)
image eva b32 gray = im.MatrixColor("tati/eva/eva_b32.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=294, yanchor=975, ypos=1.0)

image kir a11_def1 gray = im.MatrixColor(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=374, yanchor=958, ypos=1.0)
image kir a11_futeki1 gray = im.MatrixColor(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_futeki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=374, yanchor=958, ypos=1.0)
image kir a11_komaru1 gray = im.MatrixColor(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_komaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=374, yanchor=958, ypos=1.0)
image kir a11_komaru1 sepia = im.Sepia(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_komaru1.png"), tint=(.722, .6, .435), xanchor=374, yanchor=958, ypos=1.0)
image kir a11_majime1 gray = im.MatrixColor(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=374, yanchor=958, ypos=1.0)
image kir a11_warai1 sepia = im.Sepia(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_warai1.png"), tint=(.722, .6, .435), xanchor=374, yanchor=958, ypos=1.0)
image kir a11_warai2 sepia = im.Sepia(im.Composite((658, 1101), (0, 0), "tati/kir/kir_a11.png", (0, 0), "tati/kir/kir_a11_warai2.png"), tint=(.722, .6, .435), xanchor=374, yanchor=958, ypos=1.0)
image kir a13_komaru1 gray = im.MatrixColor(im.Composite((549, 1101), (0, 0), "tati/kir/kir_a13.png", (-91, 0), "tati/kir/kir_a11_komaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=283, yanchor=958, ypos=1.0)
image kir a14_komaru1 gray = im.MatrixColor(im.Composite((568, 1101), (0, 0), "tati/kir/kir_a14.png", (-66, 0), "tati/kir/kir_a11_komaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=308, yanchor=958, ypos=1.0)
image kir a26_majime1 gray = im.MatrixColor(im.Composite((778, 1098), (0, 0), "tati/kir/kir_a26.png", (91, 0), "tati/kir/kir_a23_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=374, yanchor=955, ypos=1.0)
image kir a27_majime1 gray = im.MatrixColor(im.Composite((543, 1098), (0, 0), "tati/kir/kir_a27.png", (0, 0), "tati/kir/kir_a23_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=283, yanchor=955, ypos=1.0)
image kir a38_majime1 gray = im.MatrixColor("tati/kir/kir_a38_majime1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=283, yanchor=949, ypos=1.0)
image kir a38_nayamu1 gray = im.MatrixColor("tati/kir/kir_a38_nayamu1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=283, yanchor=949, ypos=1.0)

image mar a11_akuwarai1 sepia = im.Sepia(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_akuwarai1.png"), tint=(.722, .6, .435), xanchor=269, yanchor=875, ypos=1.0)
image mar a11_def1 gray = im.MatrixColor(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=269, yanchor=875, ypos=1.0)
image mar a11_fukigen2 sepia = im.Sepia(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_fukigen2.png"), tint=(.722, .6, .435), xanchor=269, yanchor=875, ypos=1.0)
image mar a22_def1 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_majime1 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_niyari1 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_niyari1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_naku1 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_naku1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_odoroki1 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_odoroki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_warai1 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_warai2 gray = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_warai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=410, yanchor=861, ypos=1.0)
image mar a24_naku1 gray = im.MatrixColor(im.Composite((624, 1004), (0, 0), "tati/mar/mar_a24.png", (0, 0), "tati/mar/mar_a24_naku1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=276, yanchor=861, ypos=1.0)
image mar b22_warai2 gray = im.MatrixColor(im.Composite((1158, 1222), (0, 0), "tati/mar/mar_b22.png", (0, 0), "tati/mar/mar_b22_warai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=438, yanchor=1079, ypos=1.0)
image mar c11_warai1 gray = im.MatrixColor(im.Composite((872, 934), (0, 0), "tati/mar/mar_c11.png", (158, -84), "tati/mar/mar_a11_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=427, yanchor=791, ypos=1.0)
image mar a11_akuwarai2 boi = im.MatrixColor(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_akuwarai2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=269, yanchor=875, ypos=1.0)
image mar a11_fukigen2 boi = im.MatrixColor(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_fukigen2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=269, yanchor=875, ypos=1.0)
image mar a11_majime1 boi = im.MatrixColor(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_majime1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=269, yanchor=875, ypos=1.0)
image mar a11_uu1 boi = im.MatrixColor(im.Composite((617, 1018), (0, 0), "tati/mar/mar_a11.png", (0, 0), "tati/mar/mar_a11_uu1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=269, yanchor=875, ypos=1.0)
image mar a22_akuwarai1 boi = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_akuwarai1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_akuwarai2 boi = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_akuwarai2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=410, yanchor=861, ypos=1.0)
image mar a22_def1k boi = im.MatrixColor(im.Composite((758, 1004), (0, 0), "tati/mar/mar_a22.png", (0, 0), "tati/mar/mar_a22_def1k.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=410, yanchor=861, ypos=1.0)

image nat a12_majime1 gray = im.Grayscale(im.Composite((633, 1150), (0, 0), "tati/nat/nat_a12.png", (0, 0), "tati/nat/nat_a11_majime1.png"), xanchor=329, yanchor=1007, ypos=1.0)
image nat a12_majime1 boi = im.MatrixColor(im.Composite((633, 1150), (0, 0), "tati/nat/nat_a12.png", (0, 0), "tati/nat/nat_a11_majime1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=329, yanchor=1007, ypos=1.0)
image nat a12_tukare1 boi = im.MatrixColor(im.Composite((633, 1150), (0, 0), "tati/nat/nat_a12.png", (0, 0), "tati/nat/nat_a11_tukare1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=329, yanchor=1007, ypos=1.0)
image nat a12_zutuu1 boi = im.MatrixColor(im.Composite((633, 1150), (0, 0), "tati/nat/nat_a12.png", (0, 0), "tati/nat/nat_a11_zutuu1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=329, yanchor=1007, ypos=1.0)
image nat a16_majime1 boi = im.MatrixColor(im.Composite((633, 1150), (0, 0), "tati/nat/nat_a16.png", (0, 0), "tati/nat/nat_a11_majime1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=329, yanchor=1007, ypos=1.0)
image nat a26_majime1 boi = im.MatrixColor(im.Composite((633, 1151), (0, 0), "tati/nat/nat_a26.png", (0, 0), "tati/nat/nat_a21_majime1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=329, yanchor=1008, ypos=1.0)
image nat a26_odoroki2 boi = im.MatrixColor(im.Composite((633, 1151), (0, 0), "tati/nat/nat_a26.png", (0, 0), "tati/nat/nat_a21_odoroki2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=329, yanchor=1008, ypos=1.0)

image cla a11_akuwarai2 gray = im.Grayscale(im.Composite((938, 1158), (0, 0), "tati/cla/cla_a11.png", (0, 0), "tati/cla/cla_a11_akuwarai2.png"), xanchor=358, yanchor=1015, ypos=1.0)
image cla a11_komaru1 gray = im.Grayscale(im.Composite((938, 1158), (0, 0), "tati/cla/cla_a11.png", (0, 0), "tati/cla/cla_a11_komaru1.png"), xanchor=358, yanchor=1015, ypos=1.0)
image cla a11_nayamu1 gray = im.Grayscale(im.Composite((938, 1158), (0, 0), "tati/cla/cla_a11.png", (0, 0), "tati/cla/cla_a11_nayamu1.png"), xanchor=358, yanchor=1015, ypos=1.0)

image jes a11_ikari2 gray = im.MatrixColor(im.Composite((607, 1118), (0, 0), "tati/jes/jes_a11.png", (0, 0), "tati/jes/jes_a11_ikari2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=340, yanchor=975, ypos=1.0)
image jes a11_majime1 gray = im.MatrixColor(im.Composite((607, 1118), (0, 0), "tati/jes/jes_a11.png", (0, 0), "tati/jes/jes_a11_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=340, yanchor=975, ypos=1.0)
image jes a11_naki1 gray = im.MatrixColor(im.Composite((607, 1118), (0, 0), "tati/jes/jes_a11.png", (0, 0), "tati/jes/jes_a11_naki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=340, yanchor=975, ypos=1.0)
image jes a11_naki1 gray_888 = im.MatrixColor(im.Composite((607, 1118), (0, 0), "tati/jes/jes_a11.png", (0, 0), "tati/jes/jes_a11_naki1.png"), im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xanchor=340, yanchor=975, ypos=1.0)
image jes a11_odoroki1 gray = im.MatrixColor(im.Composite((607, 1118), (0, 0), "tati/jes/jes_a11.png", (0, 0), "tati/jes/jes_a11_odoroki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=340, yanchor=975, ypos=1.0)
image jes a11_warai1 sepia = im.Sepia(im.Composite((607, 1118), (0, 0), "tati/jes/jes_a11.png", (0, 0), "tati/jes/jes_a11_warai1.png"), tint=(.722, .6, .435), xanchor=340, yanchor=975, ypos=1.0)
image jes a12_ikari1 gray = im.MatrixColor(im.Composite((560, 1118), (0, 0), "tati/jes/jes_a12.png", (-86, 0), "tati/jes/jes_a11_ikari1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=254, yanchor=975, ypos=1.0)
image jes a23_tereru2 gray = im.MatrixColor(im.Composite((487, 1104), (0, 0), "tati/jes/jes_a23.png", (0, 0), "tati/jes/jes_a23_tereru2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=220, yanchor=961, ypos=1.0)
image jes b22_def1 gray = im.MatrixColor(im.Composite((447, 1104), (0, 0), "tati/jes/jes_b22.png", (19, 0), "tati/jes/jes_a23_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=239, yanchor=961, ypos=1.0)

image sha a11_def1 gray = im.MatrixColor(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_hajirai3 gray = im.MatrixColor(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_hajirai3.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_komaru1 gray = im.MatrixColor(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_komaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_odoroki1 sepia = im.Sepia(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_odoroki1.png"), tint=(.722, .6, .435), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_odoroki2 sepia = im.Sepia(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_odoroki2.png"), tint=(.722, .6, .435), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_tokui1 gray = im.MatrixColor(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_tokui1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_tokui1 sepia = im.Sepia(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_tokui1.png"), tint=(.722, .6, .435), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_warai1 gray = im.MatrixColor(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=991, ypos=1.0)
image sha a11_warai2 gray = im.MatrixColor(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_warai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=991, ypos=1.0)
image sha c11_def1 sepia = im.Sepia(im.Composite((606, 1126), (0, 0), "tati/sha/sha_c11.png", (0, 0), "tati/sha/sha_c11_def1.png"), tint=(.722, .6, .435), xanchor=232, yanchor=1003, ypos=1.0)
image sha c11_hajirai2 sepia = im.Sepia(im.Composite((606, 1126), (0, 0), "tati/sha/sha_c11.png", (0, 0), "tati/sha/sha_c11_hajirai2.png"), tint=(.722, .6, .435), xanchor=232, yanchor=1003, ypos=1.0)
image sha c11_warai2 sepia = im.Sepia(im.Composite((606, 1126), (0, 0), "tati/sha/sha_c11.png", (0, 0), "tati/sha/sha_c11_warai2.png"), tint=(.722, .6, .435), xanchor=232, yanchor=1003, ypos=1.0)
image sha c11_hajirai1 sunset = im.MatrixColor(im.Composite((606, 1126), (0, 0), "tati/sha/sha_c11.png", (0, 0), "tati/sha/sha_c11_hajirai1.png"), im.matrix.tint(1.0, (234.0/255.0), (196.0/255.0)), xanchor=232, yanchor=1003, ypos=1.0)
image sha c11_hajirai2 sunset = im.MatrixColor(im.Composite((606, 1126), (0, 0), "tati/sha/sha_c11.png", (0, 0), "tati/sha/sha_c11_hajirai2.png"), im.matrix.tint(1.0, (234.0/255.0), (196.0/255.0)), xanchor=232, yanchor=1003, ypos=1.0)

image bea a11_akuwarai1 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_akuwarai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_akuwarai2 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_akuwarai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_akuwarai4 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_akuwarai4.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_aseru1 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_aseru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_def1 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_futeki1 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_futeki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_futeki2 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_futeki2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
#image bea a11_futeki2 dark gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_futeki2.png"), im.matrix.desaturate() * im.matrix.tint(0.61176,0.61176,0.62745), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_majime1 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_warai2 gray = im.MatrixColor(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_warai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1018, ypos=1.0)
image bea a11_warai2 sepia = im.Sepia(im.Composite((1070, 1161), (0, 0), "tati/bea/bea_a11.png", (0, 0), "tati/bea/bea_a11_warai2.png"), tint=(.722, .6, .435), xanchor=603, yanchor=1018, ypos=1.0)
image bea a21_akuwarai2 gray = im.MatrixColor(im.Composite((1070, 1162), (0, 0), "tati/bea/bea_a21.png", (0, 0), "tati/bea/bea_a21_akuwarai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=603, yanchor=1019, ypos=1.0)
image bea a31_warai1 sepia = im.Sepia(im.Composite((1070, 1136), (0, 0), "tati/bea/bea_a31.png", (0, 0), "tati/bea/bea_a31_warai1.png"), tint=(.722, .6, .435), xanchor=603, yanchor=993, ypos=1.0)

image kan a11_def1 gray = im.MatrixColor(im.Composite((575, 1140), (0, 0), "tati/kan/kan_a11.png", (0, 0), "tati/kan/kan_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=279, yanchor=997, ypos=1.0)
image kan a11_majime1 gray = im.MatrixColor(im.Composite((575, 1140), (0, 0), "tati/kan/kan_a11.png", (0, 0), "tati/kan/kan_a11_majime1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=279, yanchor=997, ypos=1.0)
image kan a11_nayamu1 gray = im.MatrixColor(im.Composite((575, 1140), (0, 0), "tati/kan/kan_a11.png", (0, 0), "tati/kan/kan_a11_nayamu1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=279, yanchor=997, ypos=1.0)
image kan a12b_ikari2 gray = im.MatrixColor(im.Composite((1126, 1140), (0, 0), "tati/kan/kan_a12b.png", (79, 0), "tati/kan/kan_a11_ikari2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=358, yanchor=997, ypos=1.0)
image kan a11_def2 boi = im.MatrixColor(im.Composite((575, 1140), (0, 0), "tati/kan/kan_a11.png", (0, 0), "tati/kan/kan_a11_def2.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=279, yanchor=997, ypos=1.0)
image kan a11_komaru1 boi = im.MatrixColor(im.Composite((575, 1140), (0, 0), "tati/kan/kan_a11.png", (0, 0), "tati/kan/kan_a11_komaru1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=279, yanchor=997, ypos=1.0)
image kan a12_ikari1 boi = im.MatrixColor(im.Composite((653, 1140), (0, 0), "tati/kan/kan_a12.png", (35, 0), "tati/kan/kan_a11_ikari1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=357, yanchor=997, ypos=1.0)
image kan b21_fuman1 boi = im.MatrixColor(im.Composite((400, 1143), (0, 0), "tati/kan/kan_b21.png", (0, 0), "tati/kan/kan_b21_fuman1.png"), im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=206, yanchor=1000, ypos=1.0)
image kan b32_def1 boi = im.MatrixColor("tati/kan/kan_b32_def1.png", im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=175, yanchor=996, ypos=1.0)
image kan b32_nayamu1 boi = im.MatrixColor("tati/kan/kan_b32_nayamu1.png", im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=175, yanchor=996, ypos=1.0)

image kum a11_majime1 gray = im.MatrixColor("tati/kum/kum_a11_majime1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=292, yanchor=872, ypos=1.0)
image kum a11_warai1 gray = im.MatrixColor("tati/kum/kum_a11_warai1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=292, yanchor=872, ypos=1.0)
image kum a11_odoroki1 boi = im.MatrixColor("tati/kum/kum_a11_odoroki1.png", im.matrix.brightness(-0.25) * im.matrix.contrast(0.7) * im.matrix.tint(1.15,1.0,1.0), xanchor=374, yanchor=953, ypos=1.0)

image nan a1_def1 gray = im.MatrixColor("tati/nan/nan_a1_def1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=374, yanchor=953, ypos=1.0)
image nan a1_komaru3 gray_888 = im.MatrixColor("tati/nan/nan_a1_komaru3.png", im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xanchor=374, yanchor=953, ypos=1.0)

image ros a11_ikari3 gray = im.MatrixColor(im.Composite((518, 1080), (0, 0), "tati/ros/ros_a11.png", (0, 0), "tati/ros/ros_a11_ikari3.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=275, yanchor=937, ypos=1.0)
image ros a11_warai1 gray = im.MatrixColor(im.Composite((518, 1080), (0, 0), "tati/ros/ros_a11.png", (0, 0), "tati/ros/ros_a11_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=275, yanchor=937, ypos=1.0)
image ros a32_ikari3 gray = im.MatrixColor(im.Composite((642, 1077), (0, 0), "tati/ros/ros_a32.png", (0, 0), "tati/ros/ros_a32_ikari3.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=302, yanchor=934, ypos=1.0)
image ros a34_ikari4 gray = im.MatrixColor(im.Composite((574, 1077), (0, 0), "tati/ros/ros_a34.png", (21, 0), "tati/ros/ros_a32_ikari4.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=323, yanchor=934, ypos=1.0)
image ros c11_ikari3 gray = im.MatrixColor(im.Composite((752, 1080), (26, 0), "tati/ros/ros_a11_ikari3.png", (0, 0), "tati/ros/ros_c11.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=301, yanchor=937, ypos=1.0)
image ros c32_ikari4 gray = im.MatrixColor(im.Composite((638, 1077), (0, 0), "tati/ros/ros_c32.png", (35, 0), "tati/ros/ros_c31_ikari4.png"), im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xanchor=336, yanchor=934, ypos=1.0)

image rud a11_def1 gray = im.MatrixColor(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=269, yanchor=1050, ypos=1.0)
image rud a11_majime2 gray_888 = im.MatrixColor(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_majime2.png"), im.matrix.desaturate() * im.matrix.tint(0.5333, 0.5333, 0.5333), xanchor=269, yanchor=1050, ypos=1.0)
image rud a11_warai1 sepia = im.Sepia(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_warai1.png"), tint=(.722, .6, .435), xanchor=269, yanchor=1050, ypos=1.0)
image rud a11_warai2 gray = im.Grayscale(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_warai2.png"), xanchor=269, yanchor=1050, ypos=1.0)
image rud a14_def1 gray = im.MatrixColor(im.Composite((932, 1193), (0, 0), "tati/rud/rud_a14.png", (157, 0), "tati/rud/rud_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=426, yanchor=1050, ypos=1.0)
image rud a14_odoroki1 gray = im.MatrixColor(im.Composite((932, 1193), (0, 0), "tati/rud/rud_a14.png", (157, 0), "tati/rud/rud_a11_odoroki1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=426, yanchor=1050, ypos=1.0)

image wal a11_akuwarai2 gray = im.MatrixColor(im.Composite((752, 1211), (0, 0), "tati/wal/wal_a11.png", (0, 0), "tati/wal/wal_a11_akuwarai2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=389, yanchor=1068, ypos=1.0)
image wal a11_def1 gray = im.MatrixColor(im.Composite((752, 1211), (0, 0), "tati/wal/wal_a11.png", (0, 0), "tati/wal/wal_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=389, yanchor=1068, ypos=1.0)
image wal a11_def1 sepia = im.Sepia(im.Composite((752, 1211), (0, 0), "tati/wal/wal_a11.png", (0, 0), "tati/wal/wal_a11_def1.png"), tint=(.722, .6, .435), xanchor=389, yanchor=1068, ypos=1.0)
image wal a11_ikari2 gray = im.MatrixColor(im.Composite((752, 1211), (0, 0), "tati/wal/wal_a11.png", (0, 0), "tati/wal/wal_a11_ikari2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=389, yanchor=1068, ypos=1.0)
image wal a11_komaru1 gray = im.MatrixColor(im.Composite((752, 1211), (0, 0), "tati/wal/wal_a11.png", (0, 0), "tati/wal/wal_a11_komaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=389, yanchor=1068, ypos=1.0)
image wal a11_warai1 sepia = im.Sepia(im.Composite((752, 1211), (0, 0), "tati/wal/wal_a11.png", (0, 0), "tati/wal/wal_a11_warai1.png"), tint=(.722, .6, .435), xanchor=389, yanchor=1068, ypos=1.0)
image wal a13_ikari1 sunset = im.MatrixColor(im.Composite((1220, 1211), (0, 0), "tati/wal/wal_a13.png", (88, 0), "tati/wal/wal_a11_ikari1.png"), im.matrix.tint(1.0, (234.0/255.0), (196.0/255.0)), xanchor=477, yanchor=1068, ypos=1.0)
image wal a13_ikari2 sunset = im.MatrixColor(im.Composite((1220, 1211), (0, 0), "tati/wal/wal_a13.png", (88, 0), "tati/wal/wal_a11_ikari2.png"), im.matrix.tint(1.0, (234.0/255.0), (196.0/255.0)), xanchor=477, yanchor=1068, ypos=1.0)

image enj a11_def1 gray = im.MatrixColor(im.Composite((734, 1120), (0, 0), "tati/enj/enj_a11.png", (0, 0), "tati/enj/enj_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=354, yanchor=977, ypos=1.0)

image kin a11_def1 gray = im.MatrixColor("tati/kin/kin_a11_def1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=556, yanchor=1041, ypos=1.0)
image kin a12_akuwarai1 gray = im.MatrixColor("tati/kin/kin_a12_akuwarai1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=610, yanchor=1041, ypos=1.0)

image ber a11_def1 gray = im.MatrixColor("tati/ber/ber_a11_def1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=385, yanchor=816, ypos=1.0)
image ber a11_def2 gray = im.MatrixColor("tati/ber/ber_a11_def2.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=385, yanchor=816, ypos=1.0)

image sak a11_warai1 gray = im.MatrixColor(im.Composite((888, 886), (0, 0), "tati/sak/sak_a11.png", (0, 0), "tati/sak/sak_a11_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=401, yanchor=743, ypos=1.0)
image sak a11_warai3 gray = im.MatrixColor(im.Composite((888, 886), (0, 0), "tati/sak/sak_a11.png", (0, 0), "tati/sak/sak_a11_warai3.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=401, yanchor=743, ypos=1.0)
image sak a12_warai1 gray = im.MatrixColor(im.Composite((933, 886), (0, 0), "tati/sak/sak_a12.png", (0, 0), "tati/sak/sak_a12_warai1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=401, yanchor=743, ypos=1.0)
image sak a12_warai3 gray = im.MatrixColor(im.Composite((933, 886), (0, 0), "tati/sak/sak_a12.png", (0, 0), "tati/sak/sak_a12_warai3.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=401, yanchor=743, ypos=1.0)

image s00 a11_def1 gray = im.MatrixColor(im.Composite((770, 1269), (0, 0), "tati/s00/s00_a11.png", (0, 0), "tati/s00/s00_a11_def1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=381, yanchor=1126, ypos=1.0)

image gap a11_def2 gray = im.MatrixColor(im.Composite((787, 1186), (0, 0), "tati/gap/gap_a11.png", (0, 0), "tati/gap/gap_a11_def2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=455, yanchor=1043, ypos=1.0)

image ron a11_majime2 gray = im.MatrixColor(im.Composite((995, 1224), (0, 0), "tati/ron/ron_a11.png", (0, 0), "tati/ron/ron_a11_majime2.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=592, yanchor=1081, ypos=1.0)

image kas a11_akuwarai1 gray = im.MatrixColor("tati/kas/kas_a11_akuwarai1.png", im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=267, yanchor=990, ypos=1.0)

image ev2 a11_akuwarai8 gray = im.MatrixColor(im.Composite((1187, 1064), (0, 0), "tati/ev2/ev2_a11.png", (0, 0), "tati/ev2/ev2_a11_akuwarai8.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=407, yanchor=921, ypos=1.0)
image ev2 a11_akuwarai8 sepia = im.Sepia(im.Composite((1187, 1064), (0, 0), "tati/ev2/ev2_a11.png", (0, 0), "tati/ev2/ev2_a11_akuwarai8.png"), tint=(.722, .6, .435), xanchor=407, yanchor=921, ypos=1.0)
image ev2 b11_fukigen3 sepia = im.Sepia(im.Composite((644, 1052), (0, 0), "tati/ev2/ev2_b11.png", (0, 0), "tati/ev2/ev2_b11_fukigen3.png"), tint=(.722, .6, .435), xanchor=379, yanchor=909, ypos=1.0)
image ev2 b11_komaru1 gray = im.MatrixColor(im.Composite((644, 1052), (0, 0), "tati/ev2/ev2_b11.png", (0, 0), "tati/ev2/ev2_b11_komaru1.png"), im.matrix.desaturate() * im.matrix.tint(0.8, 0.8, 0.8), xanchor=379, yanchor=909, ypos=1.0)

image mlib_1er_blur = Image("background/mainbuilding/mlib_1er_blur.png", xalign=0.5, yalign=0.5)
image sub_p1a_blur = Image("background/subway/sub_p1a_blur.png", xalign=0.5, yalign=0.5)
#image rg1 b12_13_zoomed = Image("tati/rg1/rg1_b12_13_zoomed.png", xanchor=602)

image m_nat_1 = Image("background/sspecial/m_nat/1.png")
image m_nat_2 = Image("background/sspecial/m_nat/2.png")
image m_nat_3 = Image("background/sspecial/m_nat/3.png")
image m_nat_4 = Image("background/sspecial/m_nat/4.png")
image m_nat_5 = Image("background/sspecial/m_nat/5.png")
image m_nat_6 = Image("background/sspecial/m_nat/6.png")
image m_nat_7 = Image("background/sspecial/m_nat/7.png")
image m_nat_8 = Image("background/sspecial/m_nat/8.png")
image m_nat_9 = Image("background/sspecial/m_nat/9.png")
image m_nat_10 = Image("background/sspecial/m_nat/10.png")
image m_nat_11 = Image("background/sspecial/m_nat/11.png")
image m_nat_12 = Image("background/sspecial/m_nat/12.png")
image m_nat_13 = Image("background/sspecial/m_nat/13.png")
image m_nat_14_1 = Image("background/sspecial/m_nat/14_1.png")
image m_nat_14_2 = Image("background/sspecial/m_nat/14_2.png")

image ss_m1f_p1b = Image("background/sspecial/m1f_p1b.png")
image ss_m1f_p2b = Image("background/sspecial/m1f_p2b.png")
image ss_mkit_1ar = Image("background/sspecial/mkit_1ar.png")
image ss_mlib_1br = Image("background/sspecial/mlib_1br.png")
image ss_mlib_1cr = Image("background/sspecial/mlib_1cr.png")

image rg2 a32_ikari1_zoom = im.FactorScale(im.Composite((1094, 1021), (0, 0), "tati/rg2/rg2_a32.png", (0, 0), "tati/rg2/rg2_a31_ikari1.png"),1.7)
image rg4 a32_def1_zoom = im.FactorScale(im.Composite((1094, 1035), (0, 0), "tati/rg4/rg4_a32.png", (0, 0), "tati/rg4/rg4_a32_def1.png"),2.0)
image rg4 a32_hohoemi1_zoom = im.FactorScale(im.Composite((1094, 1035), (0, 0), "tati/rg4/rg4_a32.png", (0, 0), "tati/rg4/rg4_a32_hohoemi1.png"),2.0)
image rg4 a12_fuman1_zoom = im.FactorScale(im.Composite((1094, 1061), (0, 0), "tati/rg4/rg4_a12.png", (0, 0), "tati/rg4/rg4_a11_fuman1.png"),2.0)
image rg4 a12_odoroki1_zoom = im.FactorScale(im.Composite((1094, 1061), (0, 0), "tati/rg4/rg4_a12.png", (0, 0), "tati/rg4/rg4_a11_odoroki1.png"),2.0)
image rud a11_warai1_zoom = im.FactorScale(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_warai1.png"),2.0)
image rud a11_akuwarai1_zoom = im.FactorScale(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_akuwarai1.png"),2.0)
image rud a11_majime2_zoom = im.FactorScale(im.Composite((700, 1193), (0, 0), "tati/rud/rud_a11.png", (0, 0), "tati/rud/rud_a11_majime2.png"),2.0)
image rud a14_nayamu1_zoom = im.FactorScale(im.Composite((932, 1193), (0, 0), "tati/rud/rud_a14.png", (157, 0), "tati/rud/rud_a11_nayamu1.png"),2.0)

#image pri_i1acb_zoom = im.FactorScale("background/subway/pri_i1acb2.png",2.25)
image sha a11_odoroki1_zoom = im.FactorScale(im.Composite((745, 1134), (0, 0), "tati/sha/sha_a11.png", (0, 0), "tati/sha/sha_a11_odoroki1.png"), 2.5)

image geo a11k_ikari2k_zoom = im.FactorScale(im.Composite((724, 1174), (0, 0), "tati/geo/geo_a11.png", (0, 0), "tati/geo/geo_a11k_ikari2.png"), 2.0)


###### complicated images that probably can't be done with ATL ######
image ep1_cla a11_def1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (333,65), "cla a11_def1"), "efe/screen_split1.png")
image ep1_cla a11_komaru1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (333,65), "cla a11_komaru1"), "efe/screen_split1.png")
image ep1_cla a11_majime1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (333,65), "cla a11_majime1"), "efe/screen_split1.png")
image ep1_nat a12_ikari1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (1001,73), "nat a12_ikari1"), "efe/screen_split2.png")
image ep1_nat a12_tukare1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (1001,73), "nat a12_tukare1"), "efe/screen_split2.png")
image ep1_nat a33_odoroki2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (969,72), "nat a33_odoroki2"), "efe/screen_split2.png")

image ep2_c0203_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "butterfly_3a", (0,0), "butterfly_4sp1", (68,-143), "goa a11b"), "efe/screen_split1.png")
image ep2_c0203_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c0203_lwall.png", (440,0), "cg/c0203_lc.png"), "efe/screen_split2.png")
image ep2_c0203_3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mjes_1a_bg", (0,0), "rainback", (-254,-143), "mjes_1a", (0,0), "butterfly_4sp1r", (170,105), "jes a11_komaru1"), "efe/screen_split3.png")
image ep2_meta_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (0,0), "butterfly_4sp1r", (-191,62), "bea a11_fukigen1"), "efe/screen_split3.png")
image ep2_meta_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (0,0), "butterfly_4sp1r", (-191,62), "bea a11_aseru1"), "efe/screen_split3.png")

image ep2_bea a11_futeki2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mnat_1ar", (727,62), "bea a11_futeki2"), "efe/screen_split2.png")
image ep2_bea a11_akuwarai3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mnat_1ar", (727,62), "bea a11_akuwarai3"), "efe/screen_split2.png")
image ep2_geo a11k_komaru1k = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mnat_1ar_bg", (0,0), "rainback", (-254,-143), "mnat_1ar", (0,0), "barrier", (312,49), "geo a11k_komaru1k"), "efe/screen_split1.png")
image ep2_bea a11_akuwarai3_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mnat_1ar", (697,62), "bea a11_akuwarai3"), "efe/screen_split2.png")
image ep2_bea a11_futeki2_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mnat_1ar", (697,62), "bea a11_futeki2"), "efe/screen_split2.png")
image ep2_bea a11_odoroki1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mnat_1ar", (697,62), "bea a11_odoroki1"), "efe/screen_split2.png")
image ep2_bea white = AlphaMask("white", "efe/screen_split2.png")
image ep2_bea a21_akuwarai2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "white", (0,0), "butterfly_4sp1r", (697,61), "bea a21_akuwarai2"), "efe/screen_split2.png")

image ep3_c0203_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1cr_bg", (0,0), "rainback", (-254,-143), "mlib_1cr", (625, 160), "rg1 a12_hohoemi1"), "efe/screen_split4.png")
image ep3_c0203_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1br_bg", (0,0), "rainback", (-254,-143), "mlib_1br", (232, 83), "kan a12b_fuman1", (561, 160), "rg1 b11b_odoroki1"), "efe/screen_split4.png")
image ep3_c0204_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1ar_bg", (0,0), "rainback", (-254,-143), "mlib_1ar", (78, -1), "ron a11_def2"), "efe/screen_split1.png")
image ep3_c0204 2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1ar_bg", (0,0), "rainback", (-254,-143), "mlib_1ar", (647,62), "bea a11_akuwarai2"), "efe/screen_split2.png")
image ep3_c0204 3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1ar_bg", (0,0), "rainback", (-254,-143), "mlib_1ar", (647,61), "bea a21_akuwarai5"), "efe/screen_split2.png")
image ep3_c0204 4 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1ar_bg", (0,0), "rainback", (-254,-143), "mlib_1ar", (647,62), "bea a11_fukigen1"), "efe/screen_split2.png")
image ep3_c0204 5 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mlib_1ar_bg", (0,0), "rainback", (-254,-143), "mlib_1ar", (647,62), "bea a11_futeki2"), "efe/screen_split2.png")
image ep3_e0103_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "g1f_s1bp", (-13, 62), "bea a11_aseru1"), "efe/screen_split1.png")         ## s1ap ???
image ep3_e0103_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "g1f_s1bp", (-13, 62), "bea a11_iiwake1"), "efe/screen_split1.png")        ## s1ap ???

image ep3_e0305_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "m2f_p1br", (923, 159), "ev2 a11_akuwarai2"), "efe/screen_split2.png")

#image ep3_c0901 1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "m1f_p1c", (-640,90), "rg2 a32_ikari1_zoom"), "efe/screen_split_ep3_c0901.png")
image ep3_c0901 1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "m1f_p1c", (-640,87), "rg2 a32_ikari1_zoom"), "efe/screen_split_ep3_c0901.png")
image ep3_c0901_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "m1f_p2b_bg", (0,0), "rainback", (-254,-143), "m1f_p2b", (-36,202), "rg2 a32_odoroki1"), "efe/screen_split3.png")
image ep3_c0901 3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "white"), "efe/screen_split_ep3_c0901_3.png")
image ep3_c0901 4 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_c0901_a.png"), "efe/screen_split_ep3_c0901_3.png")
image ep3_c0901 5 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (320,0), "cg/c_c0901_a.png"), "efe/screen_split4.png")
image ep3_c0902 1 = AlphaMask("white", "efe/screen_split2.png")
image ep3_c0902 2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (400,0), "cg/c_c0902_a.png"), "efe/screen_split2.png")
image ep3_c0902 3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "white"), "efe/screen_split1.png")
image ep3_c0902 4 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-400,0), "cg/c_c0902_a.png"), "efe/screen_split1.png")
image ep3_c0902 5 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mhal_2c", (923, 159), "ev2 a11_akuwarai1"), "efe/screen_split4.png")
image ep3_c0902 6 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mhal_2c", (923, 159), "ev2 a11_akuwarai4"), "efe/screen_split4.png")
image ep3_c0902_7 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-500,0), "cg/c_c0902_a.png"), "efe/screen_split3.png")
image ep3_c0902 7 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "mhal_2c", (923, 159), "ev2 a11_akuwarai4", (804, 162), "rg4 a12b_odoroki1"), "efe/screen_split4.png")
image ep3_c0902 8 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-480,0), "cg/c_c0902_a.png"), "efe/screen_split3.png")

#image ep3_c0901 1 = im.AlphaMask(im.Composite((config.screen_width,config.screen_height), (-254,-143), "background/mainbuilding/m1f_p1c.png", (-622,132), "tati/rg2/rg2_a32_06_zoom.png"), "efe/screen_split_ep3_c0901.png")
#image ep3_c0901_2 = im.AlphaMask(im.Composite((config.screen_width,config.screen_height), (-254,-143), "background/mainbuilding/m1f_p2b_bg.png", (-254,-143), "background/mainbuilding/m1f_p2b.png", (-314,202), "tati/rg2/rg2_a32.png", (-314,202), "tati/rg2/rg2_a31_13.png"), "efe/screen_split_ep3_c0901_2.png")
#image ep3_c0901 3 = im.AlphaMask(im.Crop("background/efe/white.png", 0,0,config.screen_width,config.screen_height), "efe/screen_split_ep3_c0901_3.png")
#image ep3_c0901 4 = im.AlphaMask("cg/c_c0901_a.png", "efe/screen_split_ep3_c0901_3.png")
#image ep3_c0902 1 = im.AlphaMask(im.Crop("background/efe/white.png", 0,0,config.screen_width,config.screen_height), "efe/screen_split_ep3_c0902.png")
#image ep3_c0902 2 = im.AlphaMask("cg/c_c0902_a.png", "efe/screen_split_ep3_c0902.png")
#image ep3_c0902 3 = im.AlphaMask(im.Crop("background/efe/white.png", 0,0,config.screen_width,config.screen_height), "efe/screen_split1.png")
#image ep3_c0902 4 = im.AlphaMask("cg/c_c0902_a.png", "efe/screen_split1.png")
#image ep3_c0902 5 = im.AlphaMask(im.Composite((config.screen_width,config.screen_height), (-254,-143), "background/mainbuilding/mhal_2c.png", (922, 159), "tati/ev2/ev2_a11.png", (922, 159), "tati/ev2/ev2_a11_11.png"), "efe/screen_split_ep3_c0902_2.png")
#image ep3_c0902 6 = im.AlphaMask(im.Composite((config.screen_width,config.screen_height), (-254,-143), "background/mainbuilding/mhal_2c.png", (922, 159), "tati/ev2/ev2_a11.png", (922, 159), "tati/ev2/ev2_a11_14.png"), "efe/screen_split_ep3_c0902_2.png")
#image ep3_c0902_7 = im.AlphaMask("cg/c_c0902_a.png", "efe/screen_split_ep3_c0902_3.png")

image ep3_rg4 a32_def1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (-52,96), "rg4 a32_def1_zoom"), "efe/screen_split2.png")
image ep3_rg4 a32_hohoemi1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (-52,96), "rg4 a32_hohoemi1_zoom"), "efe/screen_split2.png")
image ep3_rg4 a12_fuman1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (-52,44), "rg4 a12_fuman1_zoom"), "efe/screen_split2.png")
image ep3_rg4 a12_odoroki1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (-52,44), "rg4 a12_odoroki1_zoom"), "efe/screen_split2.png")
image ep3_rud a11_warai1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (22,-120), "rud a11_warai1_zoom"), "efe/screen_split1.png")
image ep3_rud a11_akuwarai1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (22,-120), "rud a11_akuwarai1_zoom"), "efe/screen_split1.png")
image ep3_rud a11_majime2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (22,-120), "rud a11_majime2_zoom"), "efe/screen_split1.png")
image ep3_rud a14_nayamu1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (-292,-120), "rud a14_nayamu1_zoom"), "efe/screen_split1.png")

image ep3_chain 1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "different_spiral_1a", (0,0),  "chain7r_sp", (0,0),  "chain5r_sp", (141,4),  "but b11_kuyasigaru1", (0,0),  "chain2r_sp", (0,0),  "chain6r_sp", (0,0),  "chain4r_sp", (0,0),  "chain3r_sp"), "efe/screen_split3.png")
image ep3_chain 2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "different_spiral_1a", (0,0),  "chain7r_sp", (0,0),  "chain5r_sp", (141,15),  "but b22_odoroki2", (0,0),  "chain2r_sp", (0,0),  "chain6r_sp", (0,0),  "chain4r_sp", (0,0),  "chain3r_sp"), "efe/screen_split3.png")

image ep4_car_ama a11_def2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (911,2),  "ama a11_def2"), "efe/screen_split2.png")
image ep4_car_ama a11_def1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (911,2),  "ama a11_def1"), "efe/screen_split2.png")
image ep4_car_ama a11_akuwarai1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (911,2),  "ama a11_akuwarai1"), "efe/screen_split2.png")
image ep4_car_ama a11_majime1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (911,2),  "ama a11_majime1"), "efe/screen_split2.png")
image ep4_car_enj a11_fuman2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (236,103),  "enj a11_fuman2"), "efe/screen_split3.png")
image ep4_car_enj a11_nayamu1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (236,103),  "enj a11_nayamu1"), "efe/screen_split3.png")
image ep4_car_enj a11_def1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (236,103),  "enj a11_def1"), "efe/screen_split3.png")
image ep4_car_enj a11_majime1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (236,103),  "enj a11_majime1"), "efe/screen_split3.png")
image ep4_car_enj a11_komaru1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "car_i3b2", (236,103),  "enj a11_komaru1"), "efe/screen_split3.png")

image pri_i1acb2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "pri_i1acb_zoom"), "efe/screen_split1.png")
image pri_i1acb2_1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "pri_i1acb_zoom", (-970,-1695), "sha a11_odoroki1_zoom"), "efe/screen_split1.png")
image pri_i1acb2_2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-143), "pri_i1a", (-254,-143), "pri_i1a_sak", (232,65), "cla a11_komaru1 dark", (956,122), "kir a11_majime1 dark"), "efe/screen_split2.png")

image ep4_black2 = AlphaMask("black", "efe/screen_split2.png")
image ep4_white2 = AlphaMask("white", "efe/screen_split2.png")
image ep4_c0401_wall = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-20,0), "cg/c_c0401_wall.png"), "efe/screen_split2.png")
image ep4_c0401 1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-20,0), "cg/c_c0401_wall.png", (-20,0), "cg/c_c0401_a.png"), "efe/screen_split1.png")
image ep4_c0401 2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_c0401_lwall.png", (0,0), "cg/c_c0401_la.png"), "efe/screen_split1.png")
image ep4_c0401 3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_c0401_wall.png", (0,0), "cg/c_c0401_lb.png"), "efe/screen_split1.png")

image ep4_c0402 1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-254,-128), "black", (-370,-80), "geo a11k_ikari2k_zoom"), "efe/screen_split1.png")
image ep4_c0402 2 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_c0402_lwall.png", (0,0), "cg/c_c0402_ld.png"), "efe/screen_split2.png")
image ep4_c0402 3 = AlphaMask("background/efe/bite.png", "efe/screen_split1.png")
image ep4_c0402_4 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_c0402_lwall.png", (0,0), "cg/c_c0402_la.png"), "efe/screen_split2.png")
image ep4_c0402 5 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_c0402_lwall.png", (0,0), "cg/c_c0402_lc.png"), "efe/screen_split2.png")
image ep4_c0402 6 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-940,0), "cg/c_c0402_wall.png", (-940,0), "cg/c_c0402_d.png"), "efe/screen_split2.png")

image ep4_c0403 1 = AlphaMask("cg/c_c0403_la.png", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0)
image ep4_c0403 2 = AlphaMask("cg/c_c0403_lb.png", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0)
image ep4_c0403 3 = AlphaMask("cg/c_c0403_lc.png", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0)
image ep4_c0403 4 = AlphaMask("cg/c_c0403_le.png", "efe/screen_split1.png", xanchor=0.0, yanchor=0.0)
image ep4_c0403 5 = AlphaMask("cg/c_c0403_ld.png", "efe/screen_split1.png", xanchor=0.0, yanchor=0.0)
image ep4_c0403 6 = AlphaMask("cg/c_c0403_lb.png", "efe/screen_split1.png", xanchor=0.0, yanchor=0.0)
image ep4_c0403 7 = AlphaMask("cg/c_c0403_la.png", "efe/screen_split1.png", xanchor=0.0, yanchor=0.0)

image ep4_c0404 1 = AlphaMask("cg/c_c0404_lb.png", "efe/screen_split2.png", xanchor=0.0, yanchor=0.0)
image ep4_c0404 1a = AlphaMask("cg/c_c0404_la.png", "efe/screen_split2.png", xanchor=0.0, yanchor=0.0)
image ep4_c0404 1c = AlphaMask("cg/c_c0404_lc.png", "efe/screen_split2.png", xanchor=0.0, yanchor=0.0)
image ep4_c0404 2 = AlphaMask("cg/c_c0404_le.png", "efe/screen_split2.png", xanchor=0.0, yanchor=0.0)
image ep4_c0404 3 = AlphaMask("cg/c_c0404_lf.png", "efe/screen_split2.png", xanchor=0.0, yanchor=0.0)

image ep4_white1 = AlphaMask("white", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_white3 = AlphaMask("white", "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406 a = AlphaMask("cg/c_e0406_a.png", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406 b = AlphaMask("cg/c_e0406_b.png", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406 c = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_e0406_c.png", (0,-640), "rainback e0406", (0,-640), "rainfront e0406"), "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406 d = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_e0406_d.png", (0,-640), "rainback e0406", (0,-640), "rainfront e0406"), "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406 e = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_e0406_e.png", (0,-640), "rainback e0406", (0,-640), "rainfront e0406"), "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406 f = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (0,0), "cg/c_e0406_f.png", (0,-640), "rainback e0406", (0,-640), "rainfront e0406"), "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_rain = AlphaMask(im.Composite((config.screen_width,config.screen_height), (0,0),"cg/c_e0406_c.png", (0,0), "efe/rain_bg_static.png", (0,0), "efe/rain_fg_static.png"), "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_rain2 = AlphaMask(im.Composite((config.screen_width,config.screen_height), (0,0),"cg/c_e0406_d.png", (0,0), "efe/rain_bg_static.png", (0,0), "efe/rain_fg_static.png"), "efe/screen_split_ep4_c0403_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_e0406_1 = AlphaMask("cg/e0406.png", "efe/screen_split_ep4_c0403_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)

image ep4_meta_bea b11_nayamu1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-104,-143), "m_o1anc", (0,0), "rainback 2", (10,62), im.MatrixColor("tati/bea/bea_b11.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (10,62), im.MatrixColor("tati/bea/bea_b11_nayamu1.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (-104,-143), "m_o1anc_sak"), "efe/ep4_meta_mask_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_meta_bea b11_majime1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-104,-143), "m_o1anc", (0,0), "rainback 2", (10,62), im.MatrixColor("tati/bea/bea_b11.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (10,62), im.MatrixColor("tati/bea/bea_b11_majime1.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (-104,-143), "m_o1anc_sak"), "efe/ep4_meta_mask_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_meta_bea b11_fuman1 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-104,-143), "m_o1anc", (0,0), "rainback 2", (10,62), im.MatrixColor("tati/bea/bea_b11.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (10,62), im.MatrixColor("tati/bea/bea_b11_fuman1.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (-104,-143), "m_o1anc_sak"), "efe/ep4_meta_mask_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_meta_bea b11_fuman3 = AlphaMask(LiveComposite((config.screen_width,config.screen_height), (-104,-143), "m_o1anc", (0,0), "rainback 2", (10,62), im.MatrixColor("tati/bea/bea_b11.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (10,62), im.MatrixColor("tati/bea/bea_b11_fuman3.png", im.matrix.brightness(-0.15) * im.matrix.contrast(0.8)), (-104,-143), "m_o1anc_sak"), "efe/ep4_meta_mask_1.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
image ep4_meta_bg = AlphaMask(im.Crop("background/mainbuilding/m_o1an.png", 254,143,config.screen_width,config.screen_height), "efe/ep4_meta_mask_2.png", xanchor=0.0, yanchor=0.0, xpos=0.0, ypos=0.0)
