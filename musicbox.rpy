#init:
#    $ default_vol = 0.7

define default_vol = 0.7

init python:
    
    #extra sound channels
    renpy.music.register_channel("dummy", "sfx", True)
    renpy.music.register_channel("me0", "sfx", True)
    renpy.music.register_channel("me1", "sfx", True)
    renpy.music.register_channel("me2", "sfx", True)
    renpy.music.register_channel("me3", "sfx", True)
    renpy.music.register_channel("me4", "sfx", True)
    renpy.music.register_channel("me5", "sfx", True)
    renpy.music.register_channel("moviefx", "sfx", False)
    renpy.music.register_channel("maria", "voice", True)
    renpy.music.register_channel("vo2", "voice", False)
    renpy.music.register_channel("vo3", "voice", False)
    renpy.music.register_channel("vo4", "voice", False)
    renpy.music.register_channel("vo5", "voice", False)
    renpy.music.register_channel("vo6", "voice", False)
    renpy.music.register_channel("vo7", "voice", False)
    renpy.music.register_channel("se1", "sfx", False)
    renpy.music.register_channel("se2", "sfx", False)
    renpy.music.register_channel("se3", "sfx", False)
    renpy.music.register_channel("se9", "sfx", False)
    renpy.music.register_channel("se10", "sfx", False) #button use
    renpy.music.register_channel("se20", "sfx", False) #button use
    
    
    # Step 1. Create a MusicRoom instance.
    mb = MusicRoom(channel='music', fadeout=0.4)
#    mb = MusicRoom(channel='music', fadeout=0.5, loop=True, single_track=True)

    # Step 2. Add music files.
    mb.add("bgm/umineko_senkyou.ogg", always_unlocked=True)
    mb.add("bgm/umineko_op.ogg", always_unlocked=True)
    mb.add("bgmmode/mbox.ogg", always_unlocked=True)
    bgm_list =["bgm/umib_001.ogg",
        "bgm/umib_002.ogg",
        "bgm/umib_003.ogg",
        "bgm/umib_004.ogg",
        "bgm/umib_005.ogg",
        "bgm/umib_006.ogg",
        "bgm/umib_007.ogg",
        "bgm/umib_008.ogg",
        "bgm/umib_009.ogg",
        "bgm/umib_010.ogg",
        "bgm/umib_011.ogg",
        "bgm/umib_012.ogg",
        "bgm/umib_013.ogg",
        "bgm/umib_014.ogg",
        "bgm/umib_015.ogg",
        "bgm/umib_016.ogg",
        "bgm/umib_017.ogg",
        "bgm/umib_018.ogg",
        "bgm/umib_019.ogg",
        "bgm/umib_020.ogg",
        "bgm/umib_021.ogg",
        "bgm/umib_022.ogg",
        "bgm/umib_023.ogg",
        "bgm/umib_024.ogg",
        "bgm/umib_025.ogg",
        "bgm/umib_026.ogg",
        "bgm/umib_027.ogg",
        "bgm/umib_028.ogg",
        "bgm/umib_029.ogg",
        "bgm/umib_030.ogg",
        "bgm/umib_031.ogg",
        "bgm/umib_032.ogg",
        "bgm/umib_033.ogg",
        "bgm/umib_034.ogg",
        "bgm/umib_035.ogg",
        "bgm/umib_036.ogg",
        "bgm/system0.ogg",
        "bgm/umib_038.ogg",
        "bgm/umib_039.ogg",
#        "bgm/UmiNeko C FINALMIX_01.ogg",
        "bgm/bgm_final.ogg",
        "bgm/umib_040.ogg",
        "bgm/umib_041.ogg",
        "bgm/umib_042.ogg",
        
        "bgm2/umib_043.ogg",
        "bgm2/umib_044.ogg",
        "bgm2/umib_045.ogg",
        "bgm2/umib_046.ogg",
        "bgm2/umib_047.ogg",
        "bgm2/umib_048.ogg",
        "bgm2/umib_049.ogg",
        "bgm2/umib_050.ogg",
        "bgm2/umib_051.ogg",
        "bgm2/umib_052.ogg",
        "bgm2/umib_053.ogg",
        "bgm2/umib_054.ogg",
        "bgm2/umib_055.ogg",
        "bgm2/umib_056.ogg",
        "bgm2/umib_057.ogg",
        "bgm2/umib_058.ogg",
        "bgm2/umib_059.ogg",
        "bgm2/umib_1000.ogg",
        "bgm2/tsurupeta-128.ogg",
        
        "bgm3/umib_060.ogg",
        "bgm3/umib_061.ogg",
        "bgm3/umib_062.ogg",
        "bgm3/umib_063.ogg",
        "bgm3/umib_064.ogg",
        "bgm3/umib_065.ogg",
        "bgm3/umib_066.ogg",
        "bgm3/umib_067.ogg",
        "bgm3/umib_068.ogg",
        "bgm3/umib_069.ogg",
        "bgm3/umib_070.ogg",
        "bgm3/umib_071.ogg",
        "bgm3/umib_072.ogg",
        "bgm3/umib_073.ogg",
        "bgm3/umib_074.ogg",
        "bgm3/umib_075.ogg",
        "bgm3/umib_076.ogg",
        "bgm3/umib_077.ogg",
        "bgm3/umib_078.ogg",
        "bgm3/umib_079.ogg",
        "bgm3/umib_080.ogg",
        "bgm3/umib_081.ogg",
        "bgm3/umib_082.ogg",
        "bgm3/umib_083.ogg",
        "bgm3/umib_084.ogg",
        
        "bgm4/umib_085.ogg",
        "bgm4/umib_086.ogg",
        "bgm4/umib_087.ogg",
        "bgm4/umib_088.ogg",
        "bgm4/umib_089.ogg",
        "bgm4/umib_090.ogg",
        "bgm4/umib_091.ogg",
        "bgm4/umib_092.ogg",
        "bgm4/umib_093.ogg",
        "bgm4/umib_095.ogg",
        "bgm4/umib_096.ogg",
        "bgm4/umib_097.ogg",
        "bgm4/umib_098.ogg",
        "bgm4/umib_099.ogg",
        "bgm4/umib_100.ogg",
        "bgm4/umib_101.ogg",
        "bgm4/umib_102.ogg",
        "bgm4/umib_103.ogg",
        "bgm4/umib_104.ogg",
        "bgm4/umib_105.ogg",
        "bgm4/umib_106.ogg",
        "bgm4/umib_107.ogg",
        "bgm4/umib_108.ogg",
        "bgm4/umib_109.ogg",
        "bgm4/umib_110.ogg"]
    
    bgm_list2 = ["bgma/umib_201.ogg",
        "bgma/umib_202.ogg",
#        "bgma/umib_203.ogg",
        "bgma/umib_204.ogg",
        "bgma/umib_205.ogg",
        "bgma/umib_206.ogg",
        "bgma/umib_207.ogg",
        "bgma/umib_208.ogg",
        "bgma/umib_209.ogg",
        "bgma/umib_210.ogg",
        "bgma/umib_211.ogg",
        "bgma/umib_212.ogg",
        "bgma/umib_213.ogg",
        "bgma/umib_214.ogg",
        "bgma/umib_215.ogg",
        "bgma/umib_216.ogg",
        "bgma/umib_217.ogg",
        "bgma/umib_218.ogg",
        "bgma/umib_219.ogg",
        "bgma/umib_220.ogg",
        "bgma/umib_221.ogg",
        "bgma/umib_222.ogg",
        "bgma/umib_223.ogg",
        "bgma/umib_224.ogg",
        "bgma/umib_225.ogg",
        "bgma/umib_226.ogg",
#        "bgma/umib_227.ogg",
        "bgma/umib_228.ogg",
        "bgma/umib_229.ogg",
        "bgma/umib_230.ogg",
        "bgma/umib_231.ogg",
        "bgma/umib_232.ogg",
        "bgma/umib_233.ogg",
        "bgma/umib_234.ogg",
        "bgma/umib_235.ogg",
        "bgma/umib_1002.ogg"]
    
    for x in bgm_list:
        mb.add(x)
    for x in bgm_list2:
        mb.add(x)
    
#    if persistent.bgm_text is None:
#        persistent.bgm_text = True
    
    def bgm_counter():
        global bgm_count
        global bgm_count2
        global bgm_per
        global bgm_per2
        global bgm_list
        global bgm_list2
        bgm_count = 0.0
        bgm_count2 = 0.0
        for bgm_name in bgm_list:
            if mb.is_unlocked(bgm_name):
                bgm_count += 1.0
        for bgm_name in bgm_list2:
            if mb.is_unlocked(bgm_name):
                bgm_count2 += 1.0
        
        ## DON'T FORGET THIS FOR COMBINATION ##
        
        if renpy.seen_label('umi1_op2') or renpy.seen_label('umi2_op2') or renpy.seen_label('umi3_op2'):
            bgm_count += 1.0
        if renpy.seen_label('umi4_op2'):
            bgm_count += 1.0
        
        bgm_per = round((bgm_count/(len(bgm_list) + 2))*100,2)
        bgm_per2 = round((bgm_count2/len(bgm_list2))*100,2)
        if bgm_per >= 100.00 and not achievement.has(27):
            get_achievement(27)
        if bgm_per2 >= 100.00 and not achievement.has(28):
            get_achievement(28)
    bgm_counter1 = renpy.curry(bgm_counter)
    
    def bgm_pg(exeres):
        global bgm_page
        bgm_page2 = 3        ## number of pages
        if exeres == "+":
            if bgm_page >= bgm_page2:
                bgm_page = 1
            else:
                bgm_page += 1
        elif exeres == "-":
            if bgm_page <= 1:
                bgm_page = bgm_page2
            else:
                bgm_page -= 1
        renpy.restart_interaction()
    bgm_pg1 = renpy.curry(bgm_pg)
    
#    but_rnd1 = ['but a11_aseru1', 'but a11_futeki1', 'but a11_komaru1', 'but a11_warai2', 'but b11_aseru1', 'but b11_def1', 'but b11_def2', 'but b11_futeki1', 'but b11_komaru1', 'but b11_komaru2', 'but b11_komaru3', 'but b11_majime1', 'but b11_nayamu1', 'but b11_nayamu2', 'but b11_niramu4', 'but b11_odoroki1', 'but b11_odoroki2', 'but b11_odoroki3', 'but b11_oya1', 'but b11_warai1', 'but b11_warai2', 'but b22_futeki1', 'but b11_komaru1', 'but b22_komaru2', 'but b23_majime1', 'but b22_nayamu1', 'but b22_nayamu2', 'but b22_niramu4', 'but b22_odoroki1', 'but b22_odoroki2', 'but b22_oya1', 'but b22_warai1']
#    jes_rnd1 = ['jes a11_aisowarai1', 'jes a11_akuwarai1', 'jes a11_atya1', 'jes a11_def1', 'jes a11_futeki2', 'jes a11_ikari1', 'jes a11_komaru1', 'jes a11_majime1', 'jes a11_nakiwarai1', 'jes a11_nayamu1', 'jes a11_odoroki1', 'jes a11_tereru2', 'jes a11_tohoho1', 'jes a11_warai1', 'jes a12_akuwarai1', 'jes a12_ikari1', 'jes a23_nakiwarai1']
#    geo_rnd1 = ['geo a11_def1', 'geo a11_hohoemi1', 'geo a11_komaru1', 'geo a11_komaru2', 'geo a11_komaru3', 'geo a11_majime2', 'geo a11_majime3', 'geo a11_majime5', 'geo a11_warai1', 'geo a11k_def1k', 'geo a11k_hohoemi1k', 'geo a11k_komaru1k', 'geo a11k_komaru2k', 'geo a11k_komaru3k', 'geo a11k_majime2k', 'geo a11k_majime3k', 'geo a11k_majime5k', 'geo a11k_warai1k', 'geo a21_akuwarai1', 'geo a21_def1', 'geo a21_komaru5', 'geo a21_majime2', 'geo a21_majime4', 'geo a23_majime5', 'geo a21k_akuwarai1k', 'geo a21k_def1k', 'geo a21k_komaru5k', 'geo a21k_majime2k', 'geo a21k_majime4k', 'geo a23k_majime5k']
#    mar_rnd1 = ['mar a11_def1', 'mar a11_fukigen2', 'mar a11_niyari1', 'mar a11_odoroki1', 'mar a11_warai1', 'mar a11_uu1', 'mar a22_def1', 'mar a22_niyari1', 'mar a22_odoroki1', 'mar a22_warai1', 'mar a22_warai2']
#    nat_rnd1 = ['nat a11_def1', 'nat a11_hisu1', 'nat a11_ikari1', 'nat a11_majime1', 'nat a11_odoroki1', 'nat a11_tukare1', 'nat a11_tukare2', 'nat a11_warai1', 'nat a11_zutuu1', 'nat a12_def1', 'nat a12_hisu1', 'nat a12_ikari1', 'nat a12_majime1', 'nat a12_odoroki1', 'nat a12_tukare1', 'nat a12_tukare2', 'nat a12_warai1', 'nat a12_zutuu1', 'nat a21_def1', 'nat a21_hisu1', 'nat a21_majime1', 'nat a21_odoroki1', 'nat a21_odoroki2', 'nat a21_tukare1', 'nat a21_tukare2', 'nat a21_warai1', 'nat a21_zutuu1', 'nat a41_zutuu1', 'nat a43_zutuu1']
#    sha_rnd1 = ['sha a11_def1', 'sha a11_fuman1', 'sha a11_hajirai1', 'sha a11_hajirai2', 'sha a11_hajirai3', 'sha a11_komaru1', 'sha a11_majime1', 'sha a11_odoroki1', 'sha a11_odoroki2', 'sha a11_warai1', 'sha a11_warai2', 'sha a21_def1', 'sha a21_fuman1', 'sha a21_hajirai1', 'sha a21_hajirai2', 'sha a21_komaru1', 'sha a21_majime1', 'sha a21_odoroki1', 'sha a21_odoroki2', 'sha a21_tokui1', 'sha a21_warai1', 'sha a21_warai2']
#    gen_rnd1 = ['gen a11_def1', 'gen a11_komaru1', 'gen a11_majime1', 'gen a11_odoroki1', 'gen a21_def1', 'gen a21_kashikomari1', 'gen a21_shian1']
#    kan_rnd1 = ['kan a11_def1', 'kan a11_def2', 'kan a11_komaru1', 'kan a11_majime1', 'kan a11_nayamu1', 'kan a11_odoroki1', 'kan a12_def1', 'kan a12_def2', 'kan a12_komaru1', 'kan a12_majime1', 'kan a12_nayamu1', 'kan a12_odoroki1', 'kan b21_def1', 'kan b21_nayamu1', 'kan b21_odoroki1', 'kan b32_def1', 'kan b32_nayamu1']
#    goh_rnd1 = ['goh a11_def1', 'goh a11_hohoemi1', 'goh a11_iiwake1', 'goh a11_iiwake2', 'goh a11_komaru1', 'goh a12_komaru2', 'goh a11_majime1', 'goh a12_odoroki1', 'goh a11_omakase1', 'goh a11_omakase2', 'goh a11_warai1']
#    kum_rnd1 = ['kum a11_def1', 'kum a11_def2', 'kum a11_komaru1', 'kum a11_majime1', 'kum a11_odoroki1', 'kum a11_warai1', 'kum a12_majime1', 'kum a12_warai1']
#    cla_rnd1 = ['cla a13_akuwarai1', 'cla a13_akuwarai2', 'cla a13_akuwarai3', 'cla a11_def1', 'cla a11_ikari1', 'cla a12_komaru1', 'cla a13_komaru2', 'cla a11_komaru3', 'cla a12_komaru4', 'cla a11_majime1', 'cla a11_nayamu1', 'cla a24_komaru1', 'cla a24_komaru2', 'cla a24_komaru4']
#    eva_rnd1 = ['eva a11_def1', 'eva b21_akire1go', 'eva b21_akire2b', 'eva b21_def1', 'eva b22_futeki1', 'eva b21_hohoemi1', 'eva a11_ikari2', 'eva b11_majime1', 'eva b21_komaru1', 'eva b23_majime1', 'eva b23_ikari2', 'eva a11_warai1', 'eva b21_warai1', 'eva a11_komaru1', 'eva b11_hohoemi1', 'eva b21_futeki1', 'eva b22_komaru1']
#    rud_rnd1 = ['rud a11_akire1', 'rud a11_akuwarai1', 'rud a11_akuwarai2', 'rud a11_def1', 'rud a11_def2', 'rud a11_komaru1', 'rud a11_majime2', 'rud a11_nayamu1', 'rud a11_odoroki1', 'rud a11_warai1', 'rud a11_warai2','rud a12_akuwarai1', 'rud a12_akuwarai2', 'rud a12_komaru1', 'rud a12_majime2', 'rud a12_nayamu1', 'rud a13_def2', 'rud a13_nayamu1', 'rud a13_odoroki1']
#    ros_rnd1 = ['ros a11_akuwarai1', 'ros a11_aseru1', 'ros a11_def1', 'ros a11_ikari2', 'ros a11_ikari3', 'ros a11_komaru1', 'ros a11_komaru3', 'ros a11_komaru4', 'ros a11_majime1', 'ros a11_nayamu1', 'ros a11_odoroki1']
#    hid_rnd1 = ['hid a11_aseri1', 'hid a11_def1', 'hid a11_fumu1', 'hid a11_komaru2', 'hid a11_majime1', 'hid a11_odayaka1', 'hid a21_warai1', 'hid a21_warai2']
#    kir_rnd1 = ['kir a11_def1', 'kir a11_futeki1', 'kir a11_komaru1', 'kir a11_komaru2', 'kir a11_majime1', 'kir a11_nayamu1', 'kir a11_warai1', 'kir a11_warai2', 'kir a12_def1', 'kir a12_futeki1', 'kir a12_komaru1', 'kir a12_komaru2', 'kir a12_majime1', 'kir a12_nayamu1', 'kir a12_warai1', 'kir a12_warai2', 'kir a13_def1', 'kir a13_futeki1', 'kir a13_komaru1', 'kir a13_komaru2', 'kir a13_majime1', 'kir a13_nayamu1', 'kir a13_warai1', 'kir a13_warai2', 'kir a23_futeki1', 'kir a23_komaru1', 'kir a23_majime1', 'kir a23_nayamu1', 'kir a25_futeki1', 'kir a25_komaru1', 'kir a25_majime1', 'kir a25_nayamu1', 'kir a26_futeki1', 'kir a26_komaru1', 'kir a26_majime1', 'kir a26_nayamu1', 'kir a27_futeki1', 'kir a27_komaru1', 'kir a27_majime1', 'kir a27_nayamu1']
#    nan_rnd1 = ['nan a1_def1', 'nan a1_fumu1', 'nan a1_hohoemi1', 'nan a1_komaru2', 'nan a1_komaru3', 'nan a1_majime1', 'nan a1_odoroki1', 'nan a2_def1', 'nan a2_fumu1', 'nan a2_hohoemi1', 'nan a2_komaru2', 'nan a2_komaru3', 'nan a2_majime1', 'nan a2_odoroki1' ]
#    but_rnd2 = ['but a11_aseru1', 'but a11_futeki1', 'but a11_komaru1', 'but a11_warai2', 'but b11_aseru1', 'but b11_def1', 'but b11_def2', 'but b11_futeki1', 'but b11_futeki2', 'but b11_futeki3', 'but b11_komaru1', 'but b11_komaru2', 'but b11_komaru3', 'but b11_majime1', 'but b11_majime2', 'but b11_majime3', 'but b11_majime4', 'but b11_majime5', 'but b11_nayamu1', 'but b11_nayamu2', 'but b11_niramu3', 'but b11_niramu4', 'but b11_odoroki1', 'but b11_odoroki2', 'but b11_odoroki3', 'but b11_oya1', 'but b11_warai1', 'but b11_warai2', 'but b22_futeki1', 'but b22_futeki3', 'but b11_komaru1', 'but b22_komaru2', 'but b22_kuyasigaru1', 'but b22_majime1', 'but b22_majime2', 'but b22_majime4', 'but b22_majime5', 'but b22_naku1', 'but b22_naku2', 'but b22_naku3', 'but b22_nayamu1', 'but b22_nayamu2', 'but b22_nayamu3', 'but b22_niramu4', 'but b22_odoroki1', 'but b22_odoroki2', 'but b22_oya1', 'but b22_warai1', 'but b26_naku1', 'but b26_naku2', 'but b26_naku3']
#    bea_rnd1 = ['bea a11_akuwarai1', 'bea a11_akuwarai2', 'bea a11_akuwarai3', 'bea a11_akuwarai4', 'bea a11_akuwarai5', 'bea a11_aseru1', 'bea a11_def1', 'bea a11_def2', 'bea a11_fukigen1', 'bea a11_fukigen2', 'bea a11_fukigen3', 'bea a11_futeki1', 'bea a11_futeki2', 'bea a11_gaman1', 'bea a11_gaman2', 'bea a11_gaman3', 'bea a11_gaman4', 'bea a11_gaman5', 'bea a11_gaman6', 'bea a11_gaman7', 'bea a11_hanbeso1', 'bea a11_hanbeso2', 'bea a11_hanbeso5', 'bea a11_hanbeso6', 'bea a11_iiwake1', 'bea a11_iiwake2', 'bea a11_iiwake3', 'bea a11_komaru1', 'bea a11_komaru2', 'bea a11_komaru3', 'bea a11_komaru4', 'bea a11_majime1', 'bea a11_majime2', 'bea a11_majime4', 'bea a11_nayamu1', 'bea a11_nayamu2', 'bea a11_odoroki1', 'bea a11_odoroki2', 'bea a11_warai2', 'bea a11_warai3', 'bea a11_warai4', 'bea a12_akuwarai1', 'bea a12_akuwarai2', 'bea a12_akuwarai3', 'bea a12_akuwarai4', 'bea a12_akuwarai5', 'bea a12_aseru1', 'bea a12_def1', 'bea a12_def2', 'bea a12_fukigen1', 'bea a12_fukigen2', 'bea a12_fukigen3', 'bea a12_futeki1', 'bea a12_futeki2', 'bea a12_gaman1', 'bea a12_gaman2', 'bea a12_gaman3', 'bea a12_gaman4', 'bea a12_gaman5', 'bea a12_gaman6', 'bea a12_gaman7', 'bea a12_hanbeso1', 'bea a12_hanbeso2', 'bea a12_hanbeso5', 'bea a12_hanbeso6', 'bea a12_iiwake1', 'bea a12_iiwake2', 'bea a12_iiwake3', 'bea a12_komaru1', 'bea a12_komaru2', 'bea a12_komaru3', 'bea a12_komaru4', 'bea a12_majime1', 'bea a12_majime2', 'bea a12_majime4', 'bea a12_nayamu1', 'bea a12_nayamu2', 'bea a12_odoroki1', 'bea a12_odoroki2', 'bea a12_warai2', 'bea a12_warai3', 'bea a12_warai4', 'bea a13_akuwarai1', 'bea a13_akuwarai2', 'bea a13_akuwarai3', 'bea a13_akuwarai4', 'bea a13_akuwarai5', 'bea a13_aseru1', 'bea a13_def1', 'bea a13_def2', 'bea a13_fukigen1', 'bea a13_fukigen2', 'bea a13_fukigen3', 'bea a13_futeki1', 'bea a13_futeki2', 'bea a13_gaman1', 'bea a13_gaman2', 'bea a13_gaman3', 'bea a13_gaman4', 'bea a13_gaman5', 'bea a13_gaman6', 'bea a13_gaman7', 'bea a13_hanbeso1', 'bea a13_hanbeso2', 'bea a13_hanbeso5', 'bea a13_hanbeso6', 'bea a13_iiwake1', 'bea a13_iiwake2', 'bea a13_iiwake3', 'bea a13_komaru1', 'bea a13_komaru2', 'bea a13_komaru3', 'bea a13_komaru4', 'bea a13_majime1', 'bea a13_majime2', 'bea a13_majime4', 'bea a13_nayamu1', 'bea a13_nayamu2', 'bea a13_odoroki1', 'bea a13_odoroki2', 'bea a13_warai2', 'bea a13_warai3', 'bea a13_warai4', 'bea a14_akuwarai1', 'bea a14_akuwarai2', 'bea a14_akuwarai3', 'bea a14_akuwarai4', 'bea a14_akuwarai5', 'bea a14_aseru1', 'bea a14_def1', 'bea a14_def2', 'bea a14_fukigen1', 'bea a14_fukigen2', 'bea a14_fukigen3', 'bea a14_futeki1', 'bea a14_futeki2', 'bea a14_gaman1', 'bea a14_gaman2', 'bea a14_gaman3', 'bea a14_gaman4', 'bea a14_gaman5', 'bea a14_gaman6', 'bea a14_gaman7', 'bea a14_hanbeso1', 'bea a14_hanbeso2', 'bea a14_hanbeso5', 'bea a14_hanbeso6', 'bea a14_iiwake1', 'bea a14_iiwake2', 'bea a14_iiwake3', 'bea a14_komaru1', 'bea a14_komaru2', 'bea a14_komaru3', 'bea a14_komaru4', 'bea a14_majime1', 'bea a14_majime2', 'bea a14_majime4', 'bea a14_nayamu1', 'bea a14_nayamu2', 'bea a14_odoroki1', 'bea a14_odoroki2', 'bea a14_warai2', 'bea a14_warai3', 'bea a14_warai4', 'bea a21_akuwarai2', 'bea a21_akuwarai4', 'bea a21_akuwarai5', 'bea a21_def1', 'bea a21_def2', 'bea a21_gaman1', 'bea a21_gaman3', 'bea a21_gaman4', 'bea a21_odoroki1', 'bea a22_akuwarai2', 'bea a22_akuwarai4', 'bea a22_akuwarai5', 'bea a22_def1', 'bea a22_def2', 'bea a22_gaman1', 'bea a22_gaman3', 'bea a22_gaman4', 'bea a22_odoroki1', 'bea a23_akuwarai2', 'bea a23_akuwarai4', 'bea a23_akuwarai5', 'bea a23_def1', 'bea a23_def2', 'bea a23_gaman1', 'bea a23_gaman3', 'bea a23_gaman4', 'bea a23_odoroki1', 'bea a24_akuwarai2', 'bea a24_akuwarai4', 'bea a24_akuwarai5', 'bea a24_def1', 'bea a24_def2', 'bea a24_gaman1', 'bea a24_gaman3', 'bea a24_gaman4', 'bea a24_odoroki1', 'bea a31_akuwarai1', 'bea a31_akuwarai2', 'bea a31_akuwarai5', 'bea a31_def1', 'bea a31_fukigen3', 'bea a31_futeki1', 'bea a31_gaman4', 'bea a31_warai1', 'bea a32_akuwarai1', 'bea a32_akuwarai2', 'bea a32_akuwarai5', 'bea a32_def1', 'bea a32_fukigen3', 'bea a32_futeki1', 'bea a32_gaman4', 'bea a32_warai1', 'bea a33_akuwarai1', 'bea a33_akuwarai2', 'bea a33_akuwarai5', 'bea a33_def1', 'bea a33_fukigen3', 'bea a33_futeki1', 'bea a33_gaman4', 'bea a33_warai1', 'bea a34_akuwarai1', 'bea a34_akuwarai2', 'bea a34_akuwarai5', 'bea a34_def1', 'bea a34_fukigen3', 'bea a34_futeki1', 'bea a34_gaman4', 'bea a34_warai1']
#    ron_rnd1 = ['ron a11_akuwrai1', 'ron a11_def1', 'ron a11_def2', 'ron a11_majime1', 'ron a11_majime2', 'ron a11_odoroki1', 'ron a11_odoroki2', 'ron a13_warai1', 'ron a13_warai2', 'ron a21_akuwarai1', 'ron a21_def2', 'ron a23_warai1', 'ron a23_warai2']
    ber_rnd1 = ['ber a11_def1', 'ber a11_def2', 'ber a12_def1', 'ber a12_def2']
#    lam_rnd1 = ['lam a11_akuwarai1', 'lam a11_akuwarai2', 'lam a11_akuwarai3', 'lam a11_akuwarai4', 'lam a12_akuwarai1', 'lam a12_akuwarai2', 'lam a12_akuwarai3', 'lam a12_akuwarai4', 'lam a11_odoroki1']
#    s45_rnd1 = ['s45 a11_def1', 's45 a11_def2', 's45 a11_komaru1', 's45 a11_komaru2', 's45 a11_majime1', 's45 a11_odoroki1', 's45 a12_def1', 's45 a12_def2', 's45 a12_komaru1', 's45 a12_komaru2', 's45 a12_majime1', 's45 a12_odoroki1']
#    s41_rnd1 = ['s41 a11_akuwarai1', 's41 a11_akuwarai2', 's41 a11_def1', 's41 a11_def2', 's41 a11_majime1', 's41 a11_odoroki1', 's41 a13_akuwarai1', 's41 a13_akuwarai2', 's41 a13_def1', 's43 a11_def2', 's43 a11_majime1', 's41 a13_odoroki1']
#    s00_rnd1 = ['s00 a11_def1', 's00 a11_komaru1', 's00 a11_majime1', 's00 a11_majime2', 's00 a11_odoroki1', 's00 a11_odoroki2', 's00 a13_def1', 's00 a13_komaru1', 's00 a13_majime1', 's00 a13_majime2', 's00 a13_odoroki1', 's00 a13_odoroki2']
    
    but_rnd1 = [['a11_','a21_','a33_','b11_','b22_','b23_','b24_','b34_'], ['aseru1', 'def1', 'def2', 'futeki1', 'hohoemi1', 'komaru1', 'komaru2', 'komaru3', 'majime1', 'nayamu1', 'nayamu2', 'niramu4', 'odoroki1', 'odoroki2', 'odoroki3', 'oya1', 'warai1', 'warai2']]
    jes_rnd1 = [['a11_','a12_','a23_','b12_','b22_'], ['aisowarai1', 'akuwarai1', 'atya1', 'atya2', 'atya3', 'def1', 'def2', 'futeki1', 'futeki2', 'ikari1', 'komaru1', 'komaru2', 'komaru3', 'majime1', 'nakiwarai1', 'nayamu1', 'odoroki1', 'tereru1', 'tereru2', 'tohoho1', 'tohoho2', 'tohoho3', 'tohoho4', 'warai2', 'warai1']]
    geo_rnd1 = [['a11_','a11k_','a12_','a12k_','a21_','a21k_','a22_','a22k_','a23_','a23k_','b11_','b11k_','b12_','b12k_','b13_','b13k_','b14_','b14k_','b21_','b21k_','b23_','b23k_','b24_','b24k_'],['def1', 'hohoemi1', 'komaru1', 'komaru2', 'komaru3', 'majime2', 'majime3', 'majime5', 'warai1', 'def1k', 'hohoemi1k', 'komaru1k', 'komaru2k', 'komaru3k', 'majime2k', 'majime3k', 'majime5k', 'warai1k', 'akuwarai1', 'komaru5', 'majime4', 'akuwarai1k', 'komaru5k', 'majime4k', 'warai2', 'warai2k']]
    mar_rnd1 = [['a11_','a22_','a23_'], ['def1', 'def2', 'fukigen2', 'niyari1', 'odoroki1', 'warai1', 'uu1', 'warai2']]
    nat_rnd1 = [['a11_','a12_','a21_','a32_','a33_','a41_','a43_'], ['def1', 'hisu1', 'ikari1', 'majime1', 'odoroki1', 'odoroki2', 'tukare1', 'tukare2', 'warai1', 'warai2', 'zutuu1']]
    sha_rnd1 = [['a11_','a12_','a21_','b21_','b31_'], ['def1', 'fuman1', 'hajirai1', 'hajirai2', 'hajirai3', 'komaru1', 'majime1', 'odoroki1', 'odoroki2', 'tokui1', 'warai1', 'warai2']]
    gen_rnd1 = [['a11_','a21_'], ['def1', 'komaru1', 'majime1', 'odoroki1', 'kashikomari1']]
    kan_rnd1 = [['a11_','a12_','a13_','b21_','b32_'], ['def1', 'def2', 'komaru1', 'majime1', 'nayamu1', 'odoroki1', 'odoroki2']]
    goh_rnd1 = [['a11_','a12_'], ['def1', 'hohoemi1', 'iiwake1', 'iiwake2', 'komaru1', 'komaru2', 'majime1', 'odoroki1', 'omakase1', 'omakase2', 'warai1']]
    kum_rnd1 = [['a11_','a12_'], ['def1', 'def2', 'komaru1', 'majime1', 'odoroki1', 'warai1']]
    cla_rnd1 = [['a11_','a13_','a14_','a24_'], ['akuwarai1', 'akuwarai2', 'akuwarai3', 'def1', 'ikari1', 'komaru1', 'komaru2', 'komaru3', 'komaru4', 'majime1', 'nayamu1']]
    eva_rnd1 = [['a11_','b11_','b21_','b22_','b23_','b25_'], ['akire1', 'def1', 'futeki1', 'hohoemi1', 'ikari2', 'komaru1', 'majime1', 'warai1', 'akire1go', 'akire2', 'akire2b', 'akire2go', 'ikari1', 'komaru2']]
    rud_rnd1 = [['a11_','a12_','a13_','a21_','a22_'], ['akuwarai1', 'akuwarai2', 'def1', 'def2', 'komaru1', 'majime2', 'nayamu1', 'odoroki1', 'warai1', 'warai2']]
    ros_rnd1 = [['a11_','a12_','a13_','a25_','a32_','a33_'], ['akuwarai1', 'aseru1', 'def1', 'ikari1', 'ikari2', 'ikari3', 'ikari4', 'komaru1', 'komaru3', 'komaru4', 'majime1', 'nayamu1', 'odoroki1']]
    hid_rnd1 = [['a11_','a21_'], ['def1', 'fumu1', 'komaru2', 'majime1', 'odayaka1', 'warai1', 'warai2']]
    kir_rnd1 = [['a11_','a12_','a13_','a23_','a25_','a26_','a27_','a33_','a38_'], ['def1', 'futeki1', 'komaru1', 'komaru2', 'majime1', 'nayamu1', 'warai1', 'warai2', 'majime2']]
    nan_rnd1 = [['a1_','a2_'], ['def1', 'fumu1', 'hohoemi1', 'komaru2', 'komaru3', 'majime1']]
    but_rnd2 = [['a11_','a21_','a33_','b11_','b22_','b23_','b24_','b26_','b34_'], ['aseru1', 'def1', 'def2', 'futeki1', 'futeki2', 'futeki3', 'hohoemi1', 'komaru1', 'komaru2', 'komaru3', 'kuyasigaru1', 'majime1', 'majime2', 'majime3', 'majime4', 'majime5', 'naku1', 'naku2', 'naku3', 'nayamu1', 'nayamu2', 'nayamu3', 'niramu1', 'niramu2', 'niramu3', 'niramu4', 'odoroki1', 'odoroki2', 'odoroki3', 'oya1', 'warai1', 'warai2']]
    bea_rnd1 = [['a11_','a12_','a13_','a14_','a21_','a22_','a23_','a24_','a31_','a32_','a33_','a34_'], ['akuwarai1', 'akuwarai2', 'akuwarai3', 'akuwarai4', 'akuwarai5', 'aseru1', 'def1', 'def2', 'fukigen1', 'fukigen2', 'fukigen3', 'futeki1', 'futeki2', 'gaman1', 'gaman2', 'gaman3', 'gaman4', 'gaman5', 'gaman6', 'gaman7', 'hanbeso1', 'hanbeso2', 'hanbeso5', 'hanbeso6', 'iiwake1', 'iiwake2', 'iiwake3', 'komaru1', 'komaru2', 'komaru3', 'komaru4', 'majime1', 'majime2', 'majime4', 'nayamu1', 'nayamu2', 'odoroki1', 'odoroki2', 'warai2', 'warai3', 'warai4', '1_hanbeso3star', '1_hanbeso4star', '1_majime3star', '1_warai1']]
    ron_rnd1 = [['a11_','a12_','a13_','a21_','a22_','a23_'], ['akuwrai1', 'def1', 'def2', 'majime1', 'majime2', 'odoroki1', 'odoroki2', 'warai1', 'warai2']]
    lam_rnd1 = [['a11_','a12_','b21_'], ['akuwarai1', 'akuwarai2', 'akuwarai3', 'akuwarai4', 'odoroki1']]
    s45_rnd1 = [['a11_','a12_'], ['def1', 'def2', 'komaru1', 'komaru2', 'majime1', 'odoroki1']]
    s41_rnd1 = [['a11_','a13_'], ['akuwarai1', 'akuwarai2', 'def1', 'def2', 'majime1', 'odoroki1']]
    s00_rnd1 = [['a11_','a13_'], ['def1', 'komaru1', 'majime1', 'majime2', 'odoroki1', 'odoroki2']]
    
    bgm_res = [[0,0],
        ["bgm/umib_001.ogg", "透百合", "Sukashiyuri"],
        ["bgm/umib_002.ogg", "夏の扉", "Doorway of Summer"],
        ["bgm/umib_003.ogg", "ＨＡＮＥ", "Feathers"],
        ["bgm/umib_004.ogg", "Ｒｉｄｅ　ｏｎ", "Ride on"],
        ["bgm/umib_005.ogg", "ｓｅａ", "sea"],
        ["bgm/umib_006.ogg", "暗闇の刻", "Hour of Darkness"],
        ["bgm/umib_007.ogg", "Ｎｏｖｅｌｅｔｔｅ", "Novelette"],
        ["bgm/umib_008.ogg", "ｈｏｐｅ", "hope"],
        ["bgm/umib_009.ogg", "白い影", "White Shadow"],
        ["bgm/umib_010.ogg", "てくてく", "Steady Pace"],
        ["bgm/umib_011.ogg", "Towering cloud in summer", "Towering Cloud in Summer"],
        ["bgm/umib_012.ogg", "月夜", "Moonlight Night"],
        ["bgm/umib_013.ogg", "薔薇", "Rose"],
        ["bgm/umib_014.ogg", "隣死", "At Death's Door"],
        ["bgm/umib_015.ogg", "煉沙回廊", "Corridor of Purgatory's Sands"],
        ["bgm/umib_016.ogg", "Ｆｏｒｔｉｔｕｄｅ", "Fortitude"],
        ["bgm/umib_017.ogg", "witch_in_gold(cembalo)", "Witch in Gold (Cembalo)"],
        ["bgm/umib_018.ogg", "誘い", "Lure"],
        ["bgm/umib_019.ogg", "胡散の香り", "Fishy Aroma"],
        ["bgm/umib_027.ogg", "ｓｔｕｐｅｆａｃｔｉｏｎ", "stupefaction"],
        ["bgm/umib_021.ogg", "Ｐｒａｉｓｅ", "Praise"],
        ["bgm/umib_022.ogg", "Ｐａｓｓ", "Pass"],
        ["bgm/umib_023.ogg", "ａｇｅｈａ", "Swallowtail Butterfly"],
        ["bgm/umib_024.ogg", "ｇｏｌｄｅｎｓｌａｕｇｈｔｅｒｅｒ", "Golden Slaughterer"],
        ["bgm/umib_025.ogg", "ｗｏｒｌｄｅｎｄ(bp)", "World End (baby piano)"],
        ["bgm/umib_026.ogg", "絵画の魔女", "Witch of the Painting"],
        ["bgm/umib_020.ogg", "ｓｕｓｐｉｃｉｏｎ", "suspicion"],
        ["bgm/umib_028.ogg", "痕音", "Scar Sound"],
        ["bgm/umib_029.ogg", "Ｃｏｒｅ", "Core"],
        ["bgm/umib_030.ogg", "Ｍｉｎｕｔｅ　ｄａｒｋｎｅｓｓ", "Minute Darkness"],
        ["bgm/umib_031.ogg", "ｎｉｇｈｔｅｙｅｓ", "Nighteyes"],
        ["bgm/umib_032.ogg", "Ｃｌｏｓｅｄ　Ｍｙ　Ｈｅａｒｔ", "Closed My Heart"],
        ["bgm/umib_033.ogg", "Ｒｅｑｕｉｅｍ", "Requiem"],
        ["bgm/umib_034.ogg", "ｍｉｎｄ", "Mind"],
        ["bgm/umib_035.ogg", "Ｗｏｒｌｄｅｎｄ", "World End"],
        ["bgm/umib_036.ogg", "ｐｌａｙ", "Play"],
#        ["bgm/umib_037.ogg", "システム零", "System 0"],
        ["bgm/system0.ogg", "システム零", "System 0"],
        ["bgm/umib_038.ogg", "Ｖｏｉｃｅｌｅｓｓ", "Voiceless"],
        ["bgm/umib_039.ogg", "ｄｅａｄ　ａｎｇｌｅ", "dead angle"],
        ["bgm/umib_040.ogg", "オルガン小曲　第６億番　ハ短調", "Organ Short #600 Million in C Minor"],
        ["bgm/umib_041.ogg", "牢獄ＳＴＲＩＰ", "Prison Strip"],
        ["bgm/umib_042.ogg", "弦楽四重奏曲第１番ト長調-I.Allegro", "String Quartet #1 in G Major - I. Allegro"],
        ["bgm2/umib_043.ogg", "ｃａｇｅ", "Cage"],
        ["bgm2/umib_044.ogg", "金色の嘲笑", "Golden Sneer"],
        ["bgm2/umib_045.ogg", "サソリのハラワタ", "Scorpion Entrails"],
        ["bgm2/umib_046.ogg", "終焉_VerC", "Life's End"],
        ["bgm2/umib_047.ogg", "Answer", "Answer"],
        ["bgm2/umib_048.ogg", "Answer_short", "Answer_short"],
        ["bgm2/umib_049.ogg", "旋律（シラベ）inst.ver", "Melody inst.ver"],
        ["bgm2/umib_050.ogg", "Red_Dread", "Red_Dread"],
        ["bgm2/umib_051.ogg", "moon", "moon"],
        ["bgm2/umib_052.ogg", "where", "where"],
        ["bgm2/umib_053.ogg", "Dread of the grave", "Dread of the grave"],
        ["bgm2/umib_054.ogg", "Worldend dominator", "Worldend dominator"],
        ["bgm2/umib_055.ogg", "黒のリリアナ", "Black Lilliana"],
        ["bgm2/umib_056.ogg", "休息", "Rest"],
        ["bgm2/umib_057.ogg", "白日夢の果て", "Daydream's End"],
        ["bgm2/umib_058.ogg", "旋律（シラベ）", "Melody"],
        ["bgm2/umib_059.ogg", "Over the sky", "Over the sky"],
        ["bgm3/umib_060.ogg", "ひだまり", "In the Sun"],
        ["bgm3/umib_061.ogg", "ロウソクたちが踊る", "The Candles Dance"],
        ["bgm3/umib_062.ogg", "Ｈａｒｕｋａ", "Distant"],
        ["bgm3/umib_063.ogg", "ｐｓｙ－ｃｈｏｒｕｓ", "psy-chrous"],
        ["bgm3/umib_064.ogg", "ｆａｒ", "far"],
        ["bgm3/umib_065.ogg", "あかいくつ偽", "Fake Red Shoes"],
        ["bgm3/umib_066.ogg", "ｍｏｔｈｅｒ", "mother"],
        ["bgm3/umib_067.ogg", "ｈａｚｅ", "haze"],
        ["bgm3/umib_068.ogg", "踊る煙管", "Dancing Pipe"],
        ["bgm3/umib_069.ogg", "Dread of the grave -More fear-", "Dread of the grave -More fear-"],
        ["bgm3/umib_070.ogg", "オルガン小曲　第２億番　ハ短調", "Organ Short #200 Million in C Minor"],
        ["bgm3/umib_071.ogg", "rhythm-changer", "rhythm-changer"],
        ["bgm3/umib_072.ogg", "happiness of marionette omake", "happiness of marionette (short)"],
        ["bgm3/umib_073.ogg", "happiness of marionette", "happiness of marionette"],
        ["bgm3/umib_074.ogg", "月うさぎの舞踏", "Dance of the Moon Rabbits"],
        ["bgm3/umib_075.ogg", "Melting away", "Melting away"],
        ["bgm3/umib_076.ogg", "soul of soul", "soul of soul"],
        ["bgm3/umib_077.ogg", "miragecoordinator", "miragecoordinator"],
        ["bgm3/umib_078.ogg", "ｐｒｉｓｏｎ", "prison"],
        ["bgm3/umib_079.ogg", "生まれてきてくれてありがとう", "Thanks for Being Born"],
        ["bgm3/umib_080.ogg", "翼", "Wings"],
        ["bgm3/umib_081.ogg", "失楽園", "Lost Paradise"],
        ["bgm3/umib_082.ogg", "ｗｉｎｇｌｅｓｓ", "wingless"],
        ["bgm3/umib_083.ogg", "ａｃｔｉｖｅｐａｉｎ", "Active Pain"],
        ["bgm3/umib_084.ogg", "Dread of the grave -rhythm ver-", "Dread of the grave -rhythm ver-"],
        ["bgm4/umib_085.ogg", "久遠", "Eternity"],
        ["bgm4/umib_086.ogg", "over", "over"],
        ["bgm4/umib_087.ogg", "Like the gale", "Like the gale"],
        ["bgm4/umib_088.ogg", "F Style", "F Style"],
        ["bgm4/umib_089.ogg", "Monochrome Clock", "Monochrome Clock"],
        ["bgm4/umib_090.ogg", "apathy", "apathy"],
        ["bgm4/umib_091.ogg", "神秘の森", "Mystic Forest"],
        ["bgm4/umib_092.ogg", "さくたろうの頑張り物語", "Sakutarou's Adventure"],
        ["bgm4/umib_093.ogg", "Parallel", "Parallel"],
        ["bgm4/umib_088.ogg", "F Style", "F Style"],
        ["bgm4/umib_095.ogg", "599 million ruins", "599 million ruins"],
        ["bgm4/umib_096.ogg", "Happy_Maria!(Instrumental)", "Happy_Maria!(Instrumental)"],
        ["bgm4/umib_097.ogg", "Surrounding", "Surrounding"],
        ["bgm4/umib_098.ogg", "HIBUTA", "Launch"],
        ["bgm4/umib_099.ogg", "death(from_stupefaction)", "death(from_stupefaction)"],
        ["bgm4/umib_100.ogg", "mortal stampede", "mortal stampede"],
        ["bgm4/umib_101.ogg", "Victima propiciatoria", "Victima propiciatoria"],
        ["bgm4/umib_102.ogg", "Revolt", "Revolt"],
        ["bgm4/umib_103.ogg", "煉獄凶狂葬曲", "The Dark and Crazed Requiem of Purgatory"],
        ["bgm4/umib_104.ogg", "Ｈａｐｐｙ　Ｍａｒｉａ！", "Happy_Maria!"],
        ["bgm4/umib_105.ogg", "dive to emergency", "dive to emergency"],
        ["bgm4/umib_106.ogg", "dir", "dir"],
        ["bgm4/umib_107.ogg", "エンドレスナイン", "Endless Nine"],
        ["bgm4/umib_108.ogg", "dreamenddischarger", "dreamenddischarger"],
        ["bgm4/umib_109.ogg", "ｄｉｓｃｏｄｅ", "discode"],
        ["bgm4/umib_110.ogg", "くるり", "About Face"],
        ["bgm5/umib_111.ogg", "Future", "Future"],
        ["bgm5/umib_112.ogg", "蒼色の冷笑", "Deep Blue Jeer"],
        ["bgm5/umib_113.ogg", "名探偵は知っている", "The Great Detective Knows"],
        ["bgm5/umib_114.ogg", "笑み亡きソワレ", "Smile-less Soiree"],
        ["bgm5/umib_115.ogg", "one", "one"],
        ["bgm5/umib_116.ogg", "螺旋", "Spiral"],
        ["bgm5/umib_117.ogg", "弦楽三重奏曲　第６億番　嬰ヘ短調", "String Trio #600 Million in F# Minor"],
        ["bgm5/umib_118.ogg", "トーテンブルーメ", "Toten Blume"],
        ["bgm5/umib_119.ogg", "JUSTICE", "JUSTICE"],
        ["bgm5/umib_120.ogg", "ACI-L", "ACI-L"],
        ["bgm5/umib_121.ogg", "喰那", "Kuina"],
        ["bgm5/umib_122.ogg", "Proud-dust", "Proud-dust"],
        ["bgm5/umib_123.ogg", "hello your dream", "hello your dream"],
        ["bgm5/umib_124.ogg", "孤独な深海魚", "Solitary Deep Sea Fish"],
        ["bgm5/umib_125.ogg", "少女たちの魔女狩り", "The Girls' Witch Hunt"],
        ["bgm5/umib_126.ogg", "継接キメラ", "Patchwork Chimera"],
        ["bgm5/umib_127.ogg", "discolor", "discolor"],
        ["bgm5/umib_128.ogg", "resurrectedreplayer", "resurrectedreplayer"],
        ["bgm5/umib_129.ogg", "Final Answer", "Final Answer"],
        ["bgm5/umib_130.ogg", "hikari", "Light"],
        ["bgm5/umib_131.ogg", "命のパン", "Bread of Life"],
        ["bgm5/umib_132.ogg", "約束", "Promise"],
        ["bgm5/umib_133.ogg", "Tomorrow", "Tomorrow"],
        ["bgm5/umib_134.ogg", "TSUBASA(Ver hope)", "Wings (Ver hope)"],
        ["bgm6/umib_135.ogg", "鈍色の空笑", "Gray Empty Smile"],
        ["bgm6/umib_136.ogg", "永遠の鎖", "Eternal Chains"],
        ["bgm6/umib_137.ogg", "Love Examination", "Love Examination"],
        ["bgm6/umib_138.ogg", "刹那", "A Single Moment"],
        ["bgm6/umib_139.ogg", "Look Back", "Look Back"],
        ["bgm6/umib_140.ogg", "青い蝶", "Blue Butterfly"],
        ["bgm6/umib_141.ogg", "my dear", "my dear"],              ## uses orignal sound file instead of PS3 version
        ["bgm6/umib_142.ogg", "キ・ナの香り", "Kina no Kaori"],
        ["bgm6/umib_143.ogg", "rog-limitation", "rog-limitation"],
        ["bgm6/umib_144.ogg", "ワルツOp.34", "Waltz Op.34"],
        ["bgm6/umib_145.ogg", "ALIVE", "ALIVE"],
        ["bgm6/umib_146.ogg", "birth of new witch(inst)", "birth of new witch(inst)"],
        ["bgm6/umib_147.ogg", "ruriair", "ruriair"],
        ["bgm6/umib_148.ogg", "Engage of marionette", "Engage of marionette"],
        ["bgm6/umib_149.ogg", "Life", "Life"],
        ["bgm6/umib_150.ogg", "Loreley", "Loreley"],
        ["bgm6/umib_151.ogg", "罪", "The Sin"],
        ["bgm6/umib_152.ogg", "The first and The last", "The first and The last"],
        ["bgm6/umib_153.ogg", "反魔セクエンツィア", "Anti-Demon Sequentia"],
        ["bgm6/umib_154.ogg", "battle field", "battle field"],
        ["bgm6/umib_155.ogg", "Rebirth", "Rebirth"],
        ["bgm6/umib_156.ogg", "道", "Pathway"],
        ["bgm6/umib_157.ogg", "liberatedliberator", "liberatedliberator"],
        ["bgm6/umib_158.ogg", "Thanks for all people", "Thanks for all people"],
        ["bgm6/umib_159.ogg", "嬰児クインビー", "Infant Queen Bee"],
        ["bgm6/umib_160.ogg", "birth_of_new_witch(Short Ver)", "birth_of_new_witch(Short Ver)"],
        ["bgm6/umib_161.ogg", "ウサンノカオリ", "Fishy Aroma"],
        ["bgm7/umib_162.ogg", "le4-octobre", "le4-octobre"],
        ["bgm7/umib_163.ogg", "l&d-circulation", "l&d-circulation"],
        ["bgm7/umib_164.ogg", "reflection-call", "reflection-call"],
        ["bgm7/umib_165.ogg", "rain", "rain"],
        ["bgm7/umib_166.ogg", "7-weights", "7-weights"],
        ["bgm7/umib_167.ogg", "fall", "fall"],
        ["bgm7/umib_168.ogg", "bore-ral", "bore-ral"],
        ["bgm7/umib_169.ogg", "ballde-continuer", "ballde-continuer"],
        ["bgm7/umib_170.ogg", "なまえのないうた ver.2007 inst", "Song Without a Name(ver.2007 inst)"],
        ["bgm7/umib_171.ogg", "lie-alaia", "lie-alaia"],
        ["bgm7/umib_172.ogg", "Golden Nocturne(inst)", "Golden Nocturne(inst)"],
        ["bgm7/umib_173.ogg", "far(flat)", "far(flat)"],
        ["bgm7/umib_174.ogg", "おもちゃ箱", "Toy Box"],
        ["bgm7/umib_175.ogg", "terminal entrance", "terminal entrance"],
        ["bgm7/umib_176.ogg", "人形劇", "Puppet Show"],
        ["bgm7/umib_177.ogg", "s/he-end", "s/he-end"],
        ["bgm7/bgm_final.ogg", "Bring The Fate", "Bring The Fate"],
        ["bgm7/umib_179.ogg", "なまえのないうた full-inst", "Song Without a Name(full-inst)"],
        ["bgm7/umib_180.ogg", "The End Of The World", "The End Of The World"],
        ["bgm7/umib_181.ogg", "goddess-gardena", "goddess-gardena"],
        ["bgm2/umib_044.ogg", "金色の嘲笑", "Golden Sneer"],
        ["bgm7/umib_183.ogg", "ridicule", "ridicule"],
        ["bgm7/umib_184.ogg", "黄泉津比良坂Corruption", "Yomitsu Hirasaka Corruption"],
        ["bgm7/umib_185.ogg", "the executioner", "the executioner"],
        ["bgm7/umib_186.ogg", "なまえのないうた ver.sakura EDサイズ", "Song Without a Name(ver.sakura ED size)"],
        ["bgm8/umib_187.ogg", "ぬいぐるみ", "Stuffed Animal"],
        ["bgm8/umib_188.ogg", "怪奇ディヴェルティメント", "Bizarre Divertimento"],
        ["bgm3/umib_069_PS3.ogg", "Dread of the grave -More fear-(remake)", "Dread of the grave -More fear-(remake)"],
        ["bgm8/umib_190.ogg", "en-counse", "en-counse"],
        ["bgm8/umib_191.ogg", "lixAxil", "lixAxil"],
        ["bgm8/umib_192.ogg", "Revelations(inst)", "Revelations(inst)"],
        ["bgm8/umib_193.ogg", "飛翔", "Soar"],
        ["bgm8/umib_194.ogg", "lastendconductor", "lastendconductor"],
        ["bgm8/umib_195.ogg", "Revelations", "Revelations"],
        [0,0],[0,0],[0,0],[0,0],[0,0],
        ["bgma/umib_201.ogg", "魔女が棲む島", "The Witch's Island"],
        ["bgma/umib_202.ogg", "穏やかな午後", "Mild Afternoon"],
        ["bgma/umib_203.ogg", "踊る少女人形", "Puppet Girl's Dance"],
        ["bgma/umib_204.ogg", "追い求めた先", "Old Pursuit"],
        ["bgma/umib_205.ogg", "這いよる不安", "Creeping Anxiety"],            ## English???
        ["bgma/umib_206.ogg", "開かれた禁忌", "Imminent Contraindications"],
        ["bgma/umib_207.ogg", "サソリのハラワタ (Anime ver)", "Scorpion Entrails (Anime ver)"],
        ["bgma/umib_208.ogg", "Requiem (Anime ver)", "Requiem (Anime ver)"],
        ["bgma/umib_209.ogg", "零れ落ちる涙", "Overflowing Autumn Cracks"],
        ["bgma/umib_210.ogg", "憂鬱な午後", "Gloomy Afternoon"],
        ["bgma/umib_211.ogg", "静かな葛藤", "Quiet Conflict"],
        ["bgma/umib_212.ogg", "moon (Anime ver)", "moon (Anime ver)"],
        ["bgma/umib_213.ogg", "心奥の焔", "Inner Heart's Flame"],
        ["bgma/umib_214.ogg", "金色の悲哀", "Golden Sorrow"],
        ["bgma/umib_215.ogg", "暗緑に沈む館", "Gloomy Mansion Scenery"],
        ["bgma/umib_216.ogg", "笑うモノクル", "Laughing Monocle"],
        ["bgma/umib_217.ogg", "宿願の不可思議", "Mysterious Desire"],
        ["bgma/umib_218.ogg", "時を旅する者", "Those Who Traverse Time"],
        ["bgma/umib_219.ogg", "可憐な冷笑者", "Cynically Sweet"],
        ["bgma/umib_220.ogg", "闇で微笑む者達", "Dark Smile"],
        ["bgma/umib_221.ogg", "小さな世界", "Small World"],
        ["bgma/umib_222.ogg", "閉じた部屋", "Closed Room"],
        ["bgma/umib_223.ogg", "あかいくつ偽 (Anime ver)", "Fake Red Shoes (Anime ver)"],
        ["bgma/umib_224.ogg", "下される審判", "Judgement"],
        ["bgma/umib_225.ogg", "mortal stampede (Anime ver)", "mortal stampede (Anime ver)"],
        ["bgma/umib_226.ogg", "王者の戦い", "Battle of the Champions"],
        ["bgma/umib_227.ogg", "終端の旋律", "Melodious Terminal"],
        ["bgma/umib_228.ogg", "miragecoordinator (Anime ver)", "miragecoordinator (Anime ver)"],
        ["bgma/umib_229.ogg", "dreamenddischarger (Anime ver)", "dreamenddischarger (Anime ver)"],
        ["bgma/umib_230.ogg", "happiness of marionette (Anime ver)", "happiness of marionette (Anime ver)"],
        ["bgma/umib_231.ogg", "Answer (Anime ver)", "Answer (Anime ver)"],
        ["bgma/umib_232.ogg", "Answer_short (Anime ver)", "Answer_short (Anime ver)"],
        ["bgma/umib_233.ogg", "オルガン小曲　第６億番　ハ短調 (Anime ver)", "Organ Short #600 Million in C Minor (Anime ver)"],
        ["bgma/umib_234.ogg", "ロウソクたちが踊る (Anime ver)", "The Candles Dance (Anime ver)"],
        ["bgma/umib_235.ogg", "黒のリリアナ (Anime ver)", "Black Lilliana (Anime ver)"],
        [0,0],[0,0],[0,0],[0,0],
        ["bgm8/umib_240.ogg", "白夢の繭 -Ricordando il passato-", "White Dream Cocoon -Ricordando il passato-"],
        ["bgm8/umib_241.ogg", "うみねこのなく頃に", "When the Seagulls Cry"]
        ]
    
    bgmmode_btn = [[0,0],
        ["bgm/umib_001.ogg", "bgm_mode_sample_u3", ["透百合", "Sukashiyuri"], [["【Title 】　透百合", "【Artist】　スミイ酸", "【Time　】　４：４９"], ["Title: Sukashiyuri", "Artist: Sumiisan", "Time: 4:49"]]],
        ["bgm/umib_002.ogg", "bgm_mode_natunotobira", ["夏の扉", "Doorway of Summer"], [["【Title 】　夏の扉 ", "【Artist】　ｄａｉ", "【Time　】　１：５７"], ["Title: Doorway of Summer", "Artist: ｄａｉ", "Time: 1:57"]]]]

label bgm_jump:
    show black as blk zorder 10:
        alpha (120.0/255.0)
    $ renpy.show_screen('bgm')
    with t22
    $ ui.interact()
    jump _noisy_return
screen _bgm_jump:
    if bgm_text == "op_one":
        key "dismiss" action Jump("bgm_mode_op_sk")
    elif bgm_text == "op_two":
        key "dismiss" action Jump("bgm_mode_op2_sk")
    elif bgm_text == "001":
        key "dismiss" action Jump("bgm_sample_u3_1000")
    elif bgm_text == "002":
        key "dismiss" action Jump("bgm_mode_natunotobira_1000")

#    bgm_mode = [[0 for x in range(0,5)] for x in range(0,215)]

style bgm_btn:
        size 40
        drop_shadow (2, 2)
        font "msgothic.ttc"
        color "#b7b7b7"
        insensitive_color (183, 183, 183, 255)

style bgm_per_text:
        size 70
        outlines [(1, "#000000", 0, 0)]
        #drop_shadow (2, 2)
        font "times.ttf"
        color "#ffffff"
        hover_color "#ffffff"
        insensitive_color (255, 255, 255, 255)

# Step 3. Create the music room screen.
screen bgm_controls:
    
    fixed:
        xysize (1440,1080)
        xalign 0.5 yalign 0.5
        
        add "bgmmode/window.png" xpos (4.0/1440.0) ypos (731.0/1080.0) alpha (230.0/255.0)
        
        imagebutton idle back_i hover back_h xpos (37.0/1440.0) ypos (678.0/1080.0) focus_mask None action bgm_pg1("-")
        imagebutton idle next_i hover next_h xpos (1192.0/1440.0) ypos (678.0/1080.0) focus_mask None action bgm_pg1("+")
        
        imagebutton idle play_i hover play_h selected_idle play_s_i xpos (92.0/1440.0) ypos (992.0/1080.0) focus_mask None action mb.Play()
        imagebutton idle shuffle_i hover shuffle_h selected_idle shuffle_s_i xpos (202.0/1440.0) ypos (992.0/1080.0) focus_mask None action mb.ToggleShuffle()
        imagebutton idle all_s_i hover all_h selected_idle all_i xpos (349.0/1440.0) ypos (992.0/1080.0) focus_mask None action mb.ToggleSingleTrack()
        imagebutton idle stop_i hover stop_h selected_idle stop_s_i xpos (546.0/1440.0) ypos (992.0/1080.0) focus_mask None action [ SetVariable("bgm_text", 0), mb.Stop(), _E_MA() ]
        if mb.single_track == True:
            imagebutton idle repeat_1_i hover repeat_1_h selected_idle repeat_1_s_i xpos (664.0/1440.0) ypos (992.0/1080.0) focus_mask None action mb.ToggleLoop()
        else:
            imagebutton idle repeat_a_i hover repeat_a_h selected_idle repeat_a_s_i xpos (664.0/1440.0) ypos (992.0/1080.0) focus_mask None action mb.ToggleLoop()
        imagebutton idle bgm_exit_i hover bgm_exit_h selected_idle bgm_exit_s_i xpos (1282.0/1440.0) ypos (992.0/1080.0) focus_mask None action [ Play ("se20", "sys_se/ZS1.ogg"), MainMenu(confirm=False) ]

screen bgm_tmp:

    tag menu
    
#    text "[bgm_per]% Unlocked" style style.bgm_per_text xpos (1200.0/1920.0) ypos (32.0/1080.0)
    text "[bgm_per]% Unlocked" style style.bgm_per_text xpos (1800.0/1920.0) xanchor 1.0 ypos (32.0/1080.0)
    
    if persistent.UMINEKOEND >= 50:
        text "Anime: [bgm_per2]%" style style.bgm_per_text xpos (700.0/1920.0) ypos (32.0/1080.0)
    
#    add "bgmmode/caption.png" at caption
    add "bgmmode/caption.png" xpos (32.0/1920.0) ypos (0.0/1080.0)
    
#    use bgm_back
    
    add "bgmmode/window.png" at bgm_win
    
    use bgm_txt
    use bgm_controls
    
    if bgm_page == 1:
        
#        if mb.is_unlocked("bgm/umib_%s.ogg") % (bgm_mode[1][1]):
#            textbutton bgm_mode[1][0] xpos x ypos y focus_mask None action [ SetVariable("bgm_text", bgm_mode[1][1]), mb.Play ("bgm/umib_%s.ogg"), With(t22) ] % (bgm_mode[1][1])
        
        imagebutton idle next_i hover next_h xpos (1432.0/1920.0) ypos (678.0/1080.0) focus_mask None action SetVariable("bgm_page", 2)
        $ x=(75.0/1920.0)
        $ y=(138.0/1080.0)
        textbutton "誓響～" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "op_one"), Hide('bgm'), mb.Stop(), Jump('bgm_mode_op'), With(t22) ]#, mb.Play ("bgm/umineko_senkyou.ogg") ]
        $ y+=(48.0/1080.0)
        for tmp in range(1,55):
            if mb.is_unlocked(bgmmode_btn[tmp][0]):
                textbutton bgmmode_btn[tmp][2][0] xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "001"), mb.Play (bgmmode_btn[tmp][0]), Hide('bgm'), Jump(bgmmode_btn[tmp][1]), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn

screen bgm:

    tag menu
    
#    text "[bgm_per]% Unlocked" style style.bgm_per_text xpos (1200.0/1920.0) ypos (32.0/1080.0)
    text "[bgm_per]% Unlocked" style style.bgm_per_text xpos (1800.0/1920.0) xanchor 1.0 ypos (32.0/1080.0)
    
    if persistent.UMINEKOEND >= 50:
        text "Anime: [bgm_per2]%" style style.bgm_per_text xpos (700.0/1920.0) ypos (32.0/1080.0)
    
#    add "bgmmode/caption.png" at caption
    add "bgmmode/caption.png" xpos (32.0/1920.0) ypos (0.0/1080.0)
    
#    use bgm_back
    
    use bgm_controls
    use bgm_txt
    
    if bgm_page == 1:
        
#        if mb.is_unlocked("bgm/umib_%s.ogg") % (bgm_mode[1][1]):
#            textbutton bgm_mode[1][0] xpos x ypos y focus_mask None action [ SetVariable("bgm_text", bgm_mode[1][1]), mb.Play ("bgm/umib_%s.ogg"), With(t22) ] % (bgm_mode[1][1])
        
#        imagebutton idle next_i hover next_h xpos (1432.0/1920.0) ypos (678.0/1080.0) focus_mask None action SetVariable("bgm_page", 2)
        $ x=(75.0/1920.0)
        $ y=(138.0/1080.0)
        textbutton "誓響～" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "op_one"), Hide('bgm'), mb.Stop(), Jump('bgm_mode_op'), With(t22) ]#, mb.Play ("bgm/umineko_senkyou.ogg") ]
        $ y+=(48.0/1080.0)
        if renpy.seen_label('umi1_op2') or renpy.seen_label('umi2_op2') or renpy.seen_label('umi3_op2'):
            textbutton "Umineko/ver.A" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "op_two"), Hide('bgm'), mb.Stop(), Jump('bgm_mode_op2'), With(t22) ]#, mb.Play ("bgm/umineko_op.ogg") ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if renpy.seen_label('umi4_op2'):
            textbutton "Umineko/ver.B" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "op_two"), Hide('bgm'), mb.Stop(), Jump('bgm_mode_op3'), With(t22) ]#, mb.Play ("bgm/umineko_op.ogg") ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_001.ogg"):
            textbutton "透百合" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "001"), mb.Play ("bgm/umib_001.ogg"), Hide('bgm'), Jump('bgm_mode_sample_u3'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_002.ogg"):
            textbutton "夏の扉" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "002"), mb.Play ("bgm/umib_002.ogg"), Hide('bgm'), Jump('bgm_mode_natunotobira'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_003.ogg"):
            textbutton "ＨＡＮＥ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "003"), mb.Play ("bgm/umib_003.ogg"), Hide('bgm'), Jump('bgm_mode_hane'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_004.ogg"):
            textbutton "Ｒｉｄｅ　ｏｎ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "004"), mb.Play ("bgm/umib_004.ogg"), Hide('bgm'), Jump('bgm_mode_ride_on'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_005.ogg"):
            textbutton "Ｓｅａ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "005"), mb.Play ("bgm/umib_005.ogg"), Hide('bgm'), Jump('bgm_mode_natunotobira'), With(t22) ]#, Jump('bgm_mode_sea'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_006.ogg"):
            textbutton "暗闇の刻" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "006"), mb.Play ("bgm/umib_006.ogg"), Hide('bgm'), Jump('bgm_mode_kurayaminotoki'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_007.ogg"):
            textbutton "Novelette" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "007"), mb.Play ("bgm/umib_007.ogg"), Hide('bgm'), Jump('bgm_mode_q_Sample17'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_008.ogg"):
            textbutton "ｈｏｐｅ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "008"), mb.Play ("bgm/umib_008.ogg"), Hide('bgm'), Jump('bgm_mode_hope'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        $ x=(435.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm/umib_009.ogg"):
            textbutton "白い影" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "009"), mb.Play ("bgm/umib_009.ogg"), Hide('bgm'), Jump('bgm_mode_siroikage'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_010.ogg"):
            textbutton "てくてく" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "010"), mb.Play ("bgm/umib_010.ogg"), Hide('bgm'), Jump('bgm_mode_u_Sample21'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_011.ogg"):
            textbutton "T_c_in_summer" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "011"), mb.Play ("bgm/umib_011.ogg"), Hide('bgm'), Jump('bgm_mode_towering'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_012.ogg"):
            textbutton "月夜" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "012"), mb.Play ("bgm/umib_012.ogg"), Hide('bgm'), Jump('bgm_mode_t_Sample20'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_013.ogg"):
            textbutton "薔薇" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "013"), mb.Play ("bgm/umib_013.ogg"), Hide('bgm'), Jump('bgm_mode_sample_u4'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_014.ogg"):
            textbutton "隣死" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "014"), mb.Play ("bgm/umib_014.ogg"), Hide('bgm'), Jump('bgm_mode_rinnsi'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_015.ogg"):
            textbutton "煉沙回廊" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "015"), mb.Play ("bgm/umib_015.ogg"), Hide('bgm'), Jump('bgm_mode_rennsakairou'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_016.ogg"):
            textbutton "Fortitude" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "016"), mb.Play ("bgm/umib_016.ogg"), Hide('bgm'), Jump('bgm_mode_fortitude'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_017.ogg"):
            textbutton "w_in_gold(cembalo)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "017"), mb.Play ("bgm/umib_017.ogg"), Hide('bgm'), Jump('bgm_mode_witch_cenba'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_018.ogg"):
            textbutton "誘い" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "018"), mb.Play ("bgm/umib_018.ogg"), Hide('bgm'), Jump('bgm_mode_sasoi'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_019.ogg"):
            textbutton "胡散の香り" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "019"), mb.Play ("bgm/umib_019.ogg"), Hide('bgm'), Jump('bgm_mode_yomiage'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        $ x=(815.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm/umib_027.ogg"):
            textbutton "stupefaction" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "027"), mb.Play ("bgm/umib_027.ogg"), Hide('bgm'), Jump('bgm_mode_stupefaction'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_021.ogg"):
            textbutton "Ｐｒａｉｓｅ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "021"), mb.Play ("bgm/umib_021.ogg"), Hide('bgm'), Jump('bgm_mode_h_sample8'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_022.ogg"):
            textbutton "Ｐａｓｓ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "022"), mb.Play ("bgm/umib_022.ogg"), Hide('bgm'), Jump('bgm_mode_c_sample3'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_023.ogg"):
            textbutton "ａｇｅｈａ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "023"), mb.Play ("bgm/umib_023.ogg"), Hide('bgm'), Jump('bgm_mode_sample_u5'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_024.ogg"):
            textbutton "goldenslaughterer" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "024"), mb.Play ("bgm/umib_024.ogg"), Hide('bgm'), Jump('bgm_mode_goldenslaughterer'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_025.ogg"):
            textbutton "worldend(bp)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "025"), mb.Play ("bgm/umib_025.ogg"), Hide('bgm'), Jump('bgm_mode_worldend_solo'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_026.ogg"):
            textbutton "絵画の魔女" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "026"), mb.Play ("bgm/umib_026.ogg"), Hide('bgm'), Jump('bgm_mode_eganomajo'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_020.ogg"):
            textbutton "suspicion" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "020"), mb.Play ("bgm/umib_020.ogg"), Hide('bgm'), Jump('bgm_mode_suspicion'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_028.ogg"):
            textbutton "痕音" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "028"), mb.Play ("bgm/umib_028.ogg"), Hide('bgm'), Jump('bgm_mode_kizuoto'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_029.ogg"):
            textbutton "Ｃｏｒｅ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "029"), mb.Play ("bgm/umib_029.ogg"), Hide('bgm'), Jump('bgm_mode_toitume'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_030.ogg"):
            textbutton "minute_darkness" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "030"), mb.Play ("bgm/umib_030.ogg"), Hide('bgm'), Jump('bgm_mode_m_darkness'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        $ x=(1175.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm/umib_031.ogg"):
            textbutton "nighteyes" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "031"), mb.Play ("bgm/umib_031.ogg"), Hide('bgm'), Jump('bgm_mode_m_u2_tipica1'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_032.ogg"):
            textbutton "Closed_My_Heart" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "032"), mb.Play ("bgm/umib_032.ogg"), Hide('bgm'), Jump('bgm_mode_closed_My_Heart'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_033.ogg"):
            textbutton "Requiem" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "033"), mb.Play ("bgm/umib_033.ogg"), Hide('bgm'), Jump('bgm_mode_requiem'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_034.ogg"):
            textbutton "ｍｉｎｄ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "034"), mb.Play ("bgm/umib_034.ogg"), Hide('bgm'), Jump('bgm_mode_mind_2'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_035.ogg"):
            textbutton "worldend" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "035"), mb.Play ("bgm/umib_035.ogg"), Hide('bgm'), Jump('bgm_mode_worldend'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_036.ogg"):
            textbutton "ｐｌａｙ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "036"), mb.Play ("bgm/umib_036.ogg"), Hide('bgm'), Jump('bgm_mode_play'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/system0.ogg"):
            textbutton "システム零" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "037"), mb.Play ("bgm/system0.ogg"), Hide('bgm'), Jump('bgm_mode_system0'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_038.ogg"):
            textbutton "voiceless" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "038"), mb.Play ("bgm/umib_038.ogg"), Hide('bgm'), Jump('bgm_mode_voiceless'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_039.ogg"):
            textbutton "dead_angle" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "039"), mb.Play ("bgm/umib_039.ogg"), Hide('bgm'), Jump('bgm_mode_deadangle'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
#        if mb.is_unlocked("bgm/UmiNeko C FINALMIX_01.ogg"):
        if mb.is_unlocked("bgm/bgm_final.ogg"):
#            textbutton "Bring_The_Fate" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "final"), mb.Play ("bgm/UmiNeko C FINALMIX_01.ogg"), Hide('bgm'), Jump('bgm_mode_ed'), With(t22) ]
            textbutton "Bring_The_Fate" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "final"), mb.Play ("bgm/bgm_final.ogg"), Hide('bgm'), Jump('bgm_mode_ed'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_040.ogg"):
            textbutton "オルガン～６億番" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "040"), mb.Play ("bgm/umib_040.ogg"), Hide('bgm'), Jump('bgm_mode_orugann'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        $ x=(1535.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm/umib_041.ogg"):
            textbutton "牢獄ＳＴＲＩＰ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "041"), mb.Play ("bgm/umib_041.ogg"), Hide('bgm'), Jump('bgm_mode_rougoku'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm/umib_042.ogg"):
            textbutton "弦楽～　第１番～" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "042"), mb.Play ("bgm/umib_042.ogg"), Hide('bgm'), Jump('bgm_mode_gc_01'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        ## EPISODE 2 ##
        
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_043.ogg"):
            textbutton "ｃａｇｅ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "043"), mb.Play ("bgm2/umib_043.ogg"), Hide('bgm'), Jump('bgm_mode_cage'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/tsurupeta-128.ogg"):
            textbutton "つるぺったん" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "1001"), mb.Play ("bgm2/tsurupeta-128.ogg"), Hide('bgm'), Jump('bgm_mode_turu_pettan'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_1000.ogg"):
            textbutton "すいすい☆スイーツ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "1000"), mb.Play ("bgm2/umib_1000.ogg"), Hide('bgm'), Jump('bgm_mode_turu_pettan2'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_049.ogg"):
            textbutton "旋律(inst.ver)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "049"), mb.Play ("bgm2/umib_049.ogg"), Hide('bgm'), Jump('bgm_mode_sirabe_oche'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_047.ogg"):
            textbutton "Answer" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "047"), mb.Play ("bgm2/umib_047.ogg"), Hide('bgm'), Jump('bgm_mode_Answer'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_044.ogg"):
            textbutton "金色の嘲笑" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "044"), mb.Play ("bgm2/umib_044.ogg"), Hide('bgm'), Jump('bgm_mode_ougon_no_kage'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_045.ogg"):
            textbutton "サソリのハラワタ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "045"), mb.Play ("bgm2/umib_045.ogg"), Hide('bgm'), Jump('bgm_mode_sasorinoharawata'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_046.ogg"):
            textbutton "終焉_VerC" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "046"), mb.Play ("bgm2/umib_046.ogg"), Hide('bgm'), Jump('bgm_mode_sy'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_052.ogg"):
            textbutton "where" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "052"), mb.Play ("bgm2/umib_052.ogg"), Hide('bgm'), Jump('bgm_mode_where'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        
    if bgm_page == 2:
        
#        imagebutton idle back_i hover back_h xpos (277.0/1920.0) ypos (678.0/1080.0) focus_mask None action SetVariable("bgm_page", 1)
#        imagebutton idle next_i hover next_h xpos (1432.0/1920.0) ypos (678.0/1080.0) focus_mask None action SetVariable("bgm_page", 3)
        $ x=(75.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm2/umib_051.ogg"):
            textbutton "moon" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "051"), mb.Play ("bgm2/umib_051.ogg"), Hide('bgm'), Jump('bgm_mode_moon'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_048.ogg"):
            textbutton "Answer_short" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "048"), mb.Play ("bgm2/umib_048.ogg"), Hide('bgm'), Jump('bgm_mode_Answer_short'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_053.ogg"):
            textbutton "D_of_the_grave" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "053"), mb.Play ("bgm2/umib_053.ogg"), Hide('bgm'), Jump('bgm_mode_Dread_grave'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_050.ogg"):
            textbutton "Red_Dread" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "050"), mb.Play ("bgm2/umib_050.ogg"), Hide('bgm'), Jump('bgm_mode_Read_Dread'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_054.ogg"):
            textbutton "Worldenddominator" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "054"), mb.Play ("bgm2/umib_054.ogg"), Hide('bgm'), Jump('bgm_mode_Worldenddominator'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_055.ogg"):
            textbutton "黒のリリアナ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "055"), mb.Play ("bgm2/umib_055.ogg"), Hide('bgm'), Jump('bgm_mode_ririana'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_056.ogg"):
            textbutton "休息" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "056"), mb.Play ("bgm2/umib_056.ogg"), Hide('bgm'), Jump('bgm_mode_kiyuusoku'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_057.ogg"):
            textbutton "白日夢の果て" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "057"), mb.Play ("bgm2/umib_057.ogg"), Hide('bgm'), Jump('bgm_mode_hakujitunohate'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_058.ogg"):
            textbutton "旋律（シラベ）" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "058"), mb.Play ("bgm2/umib_058.ogg"), Hide('bgm'), Jump('bgm_mode_sirabe_vocal'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm2/umib_059.ogg"):
            textbutton "Over_the_sky" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "059"), mb.Play ("bgm2/umib_059.ogg"), Hide('bgm'), Jump('bgm_mode_Over_the_sky'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        ## EPISODE 3 ##
        
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_060.ogg"):
            textbutton "ひだまり" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "060"), mb.Play ("bgm3/umib_060.ogg"), Hide('bgm'), Jump('bgm_mode_hidamari'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        
        $ x=(435.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm3/umib_061.ogg"):
            textbutton "ロウソクたちが踊る" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "061"), mb.Play ("bgm3/umib_061.ogg"), Hide('bgm'), Jump('bgm_mode_org_remake'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_062.ogg"):
            textbutton "Haruka" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "062"), mb.Play ("bgm3/umib_062.ogg"), Hide('bgm'), Jump('bgm_mode_Haruka'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_063.ogg"):
            textbutton "psy-chorus" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "063"), mb.Play ("bgm3/umib_063.ogg"), Hide('bgm'), Jump('bgm_mode_psy_chorus_mx'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_064.ogg"):
            textbutton "far " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "064"), mb.Play ("bgm3/umib_064.ogg"), Hide('bgm'), Jump('bgm_mode_far'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_065.ogg"):
            textbutton "あかいくつ偽" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "065"), mb.Play ("bgm3/umib_065.ogg"), Hide('bgm'), Jump('bgm_mode_akaikutu2'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_066.ogg"):
            textbutton "mother" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "066"), mb.Play ("bgm3/umib_066.ogg"), Hide('bgm'), Jump('bgm_mode_mother'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_067.ogg"):
            textbutton "haze" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "067"), mb.Play ("bgm3/umib_067.ogg"), Hide('bgm'), Jump('bgm_mode_haze'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_068.ogg"):
            textbutton "踊る煙管" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "068"), mb.Play ("bgm3/umib_068.ogg"), Hide('bgm'), Jump('bgm_mode_ennkan'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_069.ogg"):
            textbutton "D_g_-More_fear- " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "069"), mb.Play ("bgm3/umib_069.ogg"), Hide('bgm'), Jump('bgm_mode_dread_grave2'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_070.ogg"):
            textbutton "オルガン小曲～" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "070"), mb.Play ("bgm3/umib_070.ogg"), Hide('bgm'), Jump('bgm_mode_orugan_2okuban'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_071.ogg"):
            textbutton "rhythm-changer" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "071"), mb.Play ("bgm3/umib_071.ogg"), Hide('bgm'), Jump('bgm_mode_rhythm_changer_mx'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        
        $ x=(815.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm3/umib_072.ogg"):
            textbutton "h_of_m_omake" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "072"), mb.Play ("bgm3/umib_072.ogg"), Hide('bgm'), Jump('bgm_mode_happiness_omake'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_073.ogg"):
            textbutton "h_of_m" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "073"), mb.Play ("bgm3/umib_073.ogg"), Hide('bgm'), Jump('bgm_mode_happiness'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_074.ogg"):
            textbutton "月うさぎの舞踏" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "074"), mb.Play ("bgm3/umib_074.ogg"), Hide('bgm'), Jump('bgm_mode_tuki_usagi'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_075.ogg"):
            textbutton "Melting away" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "075"), mb.Play ("bgm3/umib_075.ogg"), Hide('bgm'), Jump('bgm_mode_melting_away'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_076.ogg"):
            textbutton "soul of soul" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "076"), mb.Play ("bgm3/umib_076.ogg"), Hide('bgm'), Jump('bgm_mode_soul_of_soul'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_078.ogg"):
            textbutton "prison" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "078"), mb.Play ("bgm3/umib_078.ogg"), Hide('bgm'), Jump('bgm_mode_prison'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_079.ogg"):
            textbutton "生まれてきて～" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "079"), mb.Play ("bgm3/umib_079.ogg"), Hide('bgm'), Jump('bgm_mode_umare'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_080.ogg"):
            textbutton "翼" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "080"), mb.Play ("bgm3/umib_080.ogg"), Hide('bgm'), Jump('bgm_mode_tubasa'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_081.ogg"):
            textbutton "失楽園" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "081"), mb.Play ("bgm3/umib_081.ogg"), Hide('bgm'), Jump('bgm_mode_siturakuenn'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_082.ogg"):
            textbutton "wingless" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "082"), mb.Play ("bgm3/umib_082.ogg"), Hide('bgm'), Jump('bgm_mode_wingless'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_084.ogg"):
            textbutton "D_g-rhythm- " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "084"), mb.Play ("bgm3/umib_084.ogg"), Hide('bgm'), Jump('bgm_mode_Dread_grave_rhythm'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        
        $ x=(1175.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm3/umib_077.ogg"):
            textbutton "miragecoordinator " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "077"), mb.Play ("bgm3/umib_077.ogg"), Hide('bgm'), Jump('bgm_mode_miragecoordinator'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm3/umib_083.ogg"):
            textbutton "activepain" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "083"), mb.Play ("bgm3/umib_083.ogg"), Hide('bgm'), Jump('bgm_mode_activepain'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        
        ## EPISODE 4 ##
        
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_093.ogg"):
            textbutton "Parallel" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "093"), mb.Play ("bgm4/umib_093.ogg"), Hide('bgm'), Jump('bgm_mode_fs2'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_088.ogg"):
            textbutton "F Style " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "088"), mb.Play ("bgm4/umib_088.ogg"), Hide('bgm'), Jump('bgm_mode_f1_02'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_096.ogg"):
            textbutton "Happy Maria!(Inst)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "096"), mb.Play ("bgm4/umib_096.ogg"), Hide('bgm'), Jump('bgm_mode_happy_maria'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_095.ogg"):
            textbutton "599 million ruins " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "095"), mb.Play ("bgm4/umib_095.ogg"), Hide('bgm'), Jump('bgm_mode_org_kui'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_091.ogg"):
            textbutton "神秘の森" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "091"), mb.Play ("bgm4/umib_091.ogg"), Hide('bgm'), Jump('bgm_mode_forest'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_089.ogg"):
            textbutton "M_Clock " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "089"), mb.Play ("bgm4/umib_089.ogg"), Hide('bgm'), Jump('bgm_mode_mclock'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_090.ogg"):
            textbutton "apathy" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "090"), mb.Play ("bgm4/umib_090.ogg"), Hide('bgm'), Jump('bgm_mode_apathy'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_087.ogg"):
            textbutton "Like the gale " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "087"), mb.Play ("bgm4/umib_087.ogg"), Hide('bgm'), Jump('bgm_mode_gc19'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_086.ogg"):
            textbutton "over" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "086"), mb.Play ("bgm4/umib_086.ogg"), Hide('bgm'), Jump('bgm_mode_over'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        
        $ x=(1535.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm4/umib_085.ogg"):
            textbutton "久遠" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "085"), mb.Play ("bgm4/umib_085.ogg"), Hide('bgm'), Jump('bgm_mode_kuonn'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_092.ogg"):
            textbutton "さくたろうの～" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "092"), mb.Play ("bgm4/umib_092.ogg"), Hide('bgm'), Jump('bgm_mode_mdoramu'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_097.ogg"):
            textbutton "Surrounding " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "097"), mb.Play ("bgm4/umib_097.ogg"), Hide('bgm'), Jump('bgm_mode_Surrounding'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_099.ogg"):
            textbutton "death " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "099"), mb.Play ("bgm4/umib_099.ogg"), Hide('bgm'), Jump('bgm_mode_death'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_098.ogg"):
            textbutton "hibuta " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "098"), mb.Play ("bgm4/umib_098.ogg"), Hide('bgm'), Jump('bgm_mode_hibuta'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_100.ogg"):
            textbutton "m_stampede" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "100"), mb.Play ("bgm4/umib_100.ogg"), Hide('bgm'), Jump('bgm_mode_mortal'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_101.ogg"):
            textbutton "Victima_P " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "101"), mb.Play ("bgm4/umib_101.ogg"), Hide('bgm'), Jump('bgm_mode_Victima'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_102.ogg"):
            textbutton "Revolt" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "102"), mb.Play ("bgm4/umib_102.ogg"), Hide('bgm'), Jump('bgm_mode_Revolt'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_103.ogg"):
            textbutton "煉獄凶狂葬曲" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "103"), mb.Play ("bgm4/umib_103.ogg"), Hide('bgm'), Jump('bgm_mode_renngoku_kyousou'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_104.ogg"):
            textbutton "Happy Maria!" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "104"), mb.Play ("bgm4/umib_104.ogg"), Hide('bgm'), Jump('bgm_mode_h_maria_uta'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_105.ogg"):
            textbutton "dive to emergency " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "105"), mb.Play ("bgm4/umib_105.ogg"), Hide('bgm'), Jump('bgm_mode_dive_to_emergency'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        
        
    if bgm_page == 3:
        
#        imagebutton idle back_i hover back_h xpos (277.0/1920.0) ypos (678.0/1080.0) focus_mask None action SetVariable("bgm_page", 2)
        $ x=(75.0/1920.0)
        $ y=(138.0/1080.0)
        if mb.is_unlocked("bgm4/umib_106.ogg"):
            textbutton "dir " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "106"), mb.Play ("bgm4/umib_106.ogg"), Hide('bgm'), Jump('bgm_mode_dir'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn 
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_108.ogg"):
            textbutton "dreamenddischarger" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "108"), mb.Play ("bgm4/umib_108.ogg"), Hide('bgm'), Jump('bgm_mode_dreamenddischarger'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_107.ogg"):
            textbutton "エンドレスナイン" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "107"), mb.Play ("bgm4/umib_107.ogg"), Hide('bgm'), Jump('bgm_mode_e_nain'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_109.ogg"):
            textbutton "discode " xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "109"), mb.Play ("bgm4/umib_109.ogg"), Hide('bgm'), Jump('bgm_mode_discode'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        if mb.is_unlocked("bgm4/umib_110.ogg"):
            textbutton "くるり" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "110"), mb.Play ("bgm4/umib_110.ogg"), Hide('bgm'), Jump('bgm_mode_kururi'), With(t22) ]
        else:
            text "???" xpos x ypos y style style.bgm_btn
        $ y+=(48.0/1080.0)
        textbutton "オトナノノミモノ" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "mbox"), mb.Play ("bgmmode/mbox.ogg"), Hide('bgm'), Jump('bgm_mode_mbox'), With(t22) ]
        $ y+=(48.0/1080.0)
        
        if persistent.UMINEKOEND >= 50:
            if mb.is_unlocked("bgma/umib_204.ogg"):
                textbutton "追い求めた先" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "204"), mb.Play ("bgma/umib_204.ogg"), Hide('bgm'), Jump('bgm_mode_oimotometa'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_201.ogg"):
                textbutton "魔女が棲む島" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "201"), mb.Play ("bgma/umib_201.ogg"), Hide('bgm'), Jump('bgm_mode_majoshima'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_207.ogg"):
                textbutton "サソリ(Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "207"), mb.Play ("bgma/umib_207.ogg"), Hide('bgm'), Jump('bgm_mode_sasorinoharawata'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_210.ogg"):
                textbutton "憂鬱な午後" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "210"), mb.Play ("bgma/umib_210.ogg"), Hide('bgm'), Jump('bgm_mode_yuutsunagogo'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_209.ogg"):
                textbutton "零れ落ちる涙" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "209"), mb.Play ("bgma/umib_209.ogg"), Hide('bgm'), Jump('bgm_mode_koboreochiru'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            
            $ x=(435.0/1920.0)
            $ y=(138.0/1080.0)
            if mb.is_unlocked("bgma/umib_205.ogg"):
                textbutton "這いよる不安" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "205"), mb.Play ("bgma/umib_205.ogg"), Hide('bgm'), Jump('bgm_mode_haiyoru_fuan'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_208.ogg"):
                textbutton "Requiem(Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "208"), mb.Play ("bgma/umib_208.ogg"), Hide('bgm'), Jump('bgm_mode_requiem'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_233.ogg"):
                textbutton "～６億番 (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "233"), mb.Play ("bgma/umib_233.ogg"), Hide('bgm'), Jump('bgm_mode_orugann'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_202.ogg"):
                textbutton "穏やかな午後" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "202"), mb.Play ("bgma/umib_202.ogg"), Hide('bgm'), Jump('bgm_mode_odayaka'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_1002.ogg"):
                textbutton "どっきゅん☆ハート" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "1002"), mb.Play ("bgma/umib_1002.ogg"), Hide('bgm'), Jump('bgm_mode_dokkyun'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_231.ogg"):
                textbutton "Answer (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "231"), mb.Play ("bgma/umib_231.ogg"), Hide('bgm'), Jump('bgm_mode_Answer'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_232.ogg"):
                textbutton "Answer_short (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "232"), mb.Play ("bgma/umib_232.ogg"), Hide('bgm'), Jump('bgm_mode_Answer_short'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_212.ogg"):
                textbutton "moon (Anime ver)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "212"), mb.Play ("bgma/umib_212.ogg"), Hide('bgm'), Jump('bgm_mode_moon'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_206.ogg"):
                textbutton "開かれた禁忌" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "206"), mb.Play ("bgma/umib_206.ogg"), Hide('bgm'), Jump('bgm_mode_akareta'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_235.ogg"):
                textbutton "リリアナ (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "235"), mb.Play ("bgma/umib_235.ogg"), Hide('bgm'), Jump('bgm_mode_ririana'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_234.ogg"):
                textbutton "ロウソクた (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "234"), mb.Play ("bgma/umib_234.ogg"), Hide('bgm'), Jump('bgm_mode_org_remake'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            
            $ x=(815.0/1920.0)
            $ y=(138.0/1080.0)
            if mb.is_unlocked("bgma/umib_215.ogg"):
                textbutton "暗緑に沈む館" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "215"), mb.Play ("bgma/umib_215.ogg"), Hide('bgm'), Jump('bgm_mode_anryoku'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_216.ogg"):
                textbutton "笑うモノクル" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "216"), mb.Play ("bgma/umib_216.ogg"), Hide('bgm'), Jump('bgm_mode_monocle'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_222.ogg"):
                textbutton "閉じた部屋" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "222"), mb.Play ("bgma/umib_222.ogg"), Hide('bgm'), Jump('bgm_mode_tojitaheya'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_223.ogg"):
                textbutton "あかいくつ偽(Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "223"), mb.Play ("bgma/umib_223.ogg"), Hide('bgm'), Jump('bgm_mode_akaikutu2'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_230.ogg"):
                textbutton "h_of_m (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "230"), mb.Play ("bgma/umib_230.ogg"), Hide('bgm'), Jump('bgm_mode_happiness'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_219.ogg"):
                textbutton "可憐な冷笑者" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "219"), mb.Play ("bgma/umib_219.ogg"), Hide('bgm'), Jump('bgm_mode_clown'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_217.ogg"):
                textbutton "宿願の不可思議" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "217"), mb.Play ("bgma/umib_217.ogg"), Hide('bgm'), Jump('bgm_mode_fukashigi'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_211.ogg"):
                textbutton "静かな葛藤" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "211"), mb.Play ("bgma/umib_211.ogg"), Hide('bgm'), Jump('bgm_mode_shizukana'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_213.ogg"):
                textbutton "心奥の焔" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "213"), mb.Play ("bgma/umib_213.ogg"), Hide('bgm'), Jump('bgm_mode_shinounohomura'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_228.ogg"):
                textbutton "mirage~ (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "228"), mb.Play ("bgma/umib_228.ogg"), Hide('bgm'), Jump('bgm_mode_miragecoordinator'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_214.ogg"):
                textbutton "金色の悲哀" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "214"), mb.Play ("bgma/umib_214.ogg"), Hide('bgm'), Jump('bgm_mode_ougon_no_hiai'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            
            $ x=(1175.0/1920.0)
            $ y=(138.0/1080.0)
            if mb.is_unlocked("bgma/umib_218.ogg"):
                textbutton "時を旅する者" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "218"), mb.Play ("bgma/umib_218.ogg"), Hide('bgm'), Jump('bgm_mode_time_travel'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_220.ogg"):
                textbutton "闇で微笑む者達" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "220"), mb.Play ("bgma/umib_220.ogg"), Hide('bgm'), Jump('bgm_mode_yami_no_hohoemu'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_221.ogg"):
                textbutton "小さな世界" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "221"), mb.Play ("bgma/umib_221.ogg"), Hide('bgm'), Jump('bgm_mode_chiisanasekai'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_226.ogg"):
                textbutton "王者の戦い" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "226"), mb.Play ("bgma/umib_226.ogg"), Hide('bgm'), Jump('bgm_mode_tatakai'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_225.ogg"):
                textbutton "m_stampede (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "225"), mb.Play ("bgma/umib_225.ogg"), Hide('bgm'), Jump('bgm_mode_mortal'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_224.ogg"):
                textbutton "下される審判" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "224"), mb.Play ("bgma/umib_224.ogg"), Hide('bgm'), Jump('bgm_mode_kudasarerushinpan'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            $ y+=(48.0/1080.0)
            if mb.is_unlocked("bgma/umib_229.ogg"):
                textbutton "dreamend~ (Anime)" xpos x ypos y focus_mask None action [ SetVariable("bgm_text", "229"), mb.Play ("bgma/umib_229.ogg"), Hide('bgm'), Jump('bgm_mode_dreamenddischarger'), With(t22) ]
            else:
                text "???" xpos x ypos y style style.bgm_btn
            
    
    
    
style bgm_text:
        size 50
        drop_shadow (2, 2)
        font "msgothic.ttc"
        color "#808080"
        hover_color "#ffffff"
        insensitive_color (255, 255, 255, 255)
    
screen bgm_txt:
    
    if bgm_text == 0:
        add "saveload/load_null.png" at bgm_win
    elif bgm_text == "op_one":
#        add "bgmmode/text/op_1.png" at bgm_win
        text "Title: 誓響のイグレージャ [[Senkyou no Igreja]" style style.bgm_text at bgm_title
        text "Artist: 志倉 千代丸 [[Shikura Chiyomaru]" style style.bgm_text at bgm_artist
        text "Vocal: KOKOMI" style style.bgm_text at bgm_time
    elif bgm_text == "op_two":
        text "Title: うみねこのなく頃に [[When the Seagulls Cry]" style style.bgm_text at bgm_title
        text "Artist: 志方あきこ [[Shikata Akiko]" style style.bgm_text at bgm_artist
        text "Time: 1:28" style style.bgm_text at bgm_time
    elif bgm_text == "001":
        text "Title: 透百合 [[Sukashiyuri]" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 4:49" style style.bgm_text at bgm_time
    elif bgm_text == "002":
        text "Title: 夏の扉 [[Doorway of Summer]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:57" style style.bgm_text at bgm_time
    elif bgm_text == "003":
        text "Title: ＨＡＮＥ [[Feathers]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:34" style style.bgm_text at bgm_time
    elif bgm_text == "004":
        text "Title: Ｒｉｄｅ　ｏｎ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 3:07" style style.bgm_text at bgm_time
    elif bgm_text == "005":
        text "Title: ｓｅａ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 0:45" style style.bgm_text at bgm_time
    elif bgm_text == "006":
        text "Title: 暗闇の刻 [[Hour of Darkness]" style style.bgm_text at bgm_title
        text "Artist: ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 1:16" style style.bgm_text at bgm_time
    elif bgm_text == "007":
        text "Title: Ｎｏｖｅｌｅｔｔｅ" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 5:32" style style.bgm_text at bgm_time
    elif bgm_text == "008":
        text "Title: ｈｏｐｅ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:59" style style.bgm_text at bgm_time
    elif bgm_text == "009":
        text "Title: 白い影 [[White Shadow]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:23" style style.bgm_text at bgm_time
    elif bgm_text == "010":
        text "Title: てくてく [[Steady Pace]" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 4:20" style style.bgm_text at bgm_time
    elif bgm_text == "011":
        text "Title: Towering_cloud_in_summer" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:48" style style.bgm_text at bgm_time
    elif bgm_text == "012":
        text "Title: 月夜 [[Moonlit Night]" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 3:26" style style.bgm_text at bgm_time
    elif bgm_text == "013":
        text "Title: 薔薇 [[Rose]" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 8:41" style style.bgm_text at bgm_time
    elif bgm_text == "014":
        text "Title: 隣死 [[At Death's Door]" style style.bgm_text at bgm_title
        text "Artist: プレコ [[Pureco]" style style.bgm_text at bgm_artist
        text "Time: 3:13" style style.bgm_text at bgm_time
    elif bgm_text == "015":
        text "Title: 煉沙回廊 [[Corridor of Purgatory's Sands]" style style.bgm_text at bgm_title
        text "Artist: プレコ [[Pureco]" style style.bgm_text at bgm_artist
        text "Time: 3:00" style style.bgm_text at bgm_time
    elif bgm_text == "016":
        text "Title: Ｆｏｒｔｉｔｕｄｅ" style style.bgm_text at bgm_title
        text "Artist: 荒井英理也 [[Arai Eriya]" style style.bgm_text at bgm_artist
        text "Time: 5:05" style style.bgm_text at bgm_time
    elif bgm_text == "017":
        text "Title: witch_in_gold(cembalo)" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 1:18" style style.bgm_text at bgm_time
    elif bgm_text == "018":
        text "Title: 誘い [[Lure]" style style.bgm_text at bgm_title
        text "Artist: ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 1:39" style style.bgm_text at bgm_time
    elif bgm_text == "019":
        text "Title: 胡散の香り [[Fishy Aroma]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 3:13" style style.bgm_text at bgm_time
    elif bgm_text == "027":
        text "Title: ｓｔｕｐｅｆａｃｔｉｏｎ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 2:30" style style.bgm_text at bgm_time
    elif bgm_text == "021":
        text "Title: Ｐｒａｉｓｅ" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 2:26" style style.bgm_text at bgm_time
    elif bgm_text == "022":
        text "Title: Ｐａｓｓ" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 4:42" style style.bgm_text at bgm_time
    elif bgm_text == "023":
        text "Title: ａｇｅｈａ [[Swallowtail Butterfly]" style style.bgm_text at bgm_title
        text "Artist: スミイ酸 [[Sumiisan]" style style.bgm_text at bgm_artist
        text "Time: 1:32" style style.bgm_text at bgm_time
    elif bgm_text == "024":
        text "Title: ｇｏｌｄｅｎｓｌａｕｇｈｔｅｒｅｒ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 6:47" style style.bgm_text at bgm_time
    elif bgm_text == "025":
        text "Title: ｗｏｒｌｄｅｎｄ(baby piano)" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 2:51" style style.bgm_text at bgm_time
    elif bgm_text == "026":
        text "Title: 絵画の魔女 [[Witch of the Painting]" style style.bgm_text at bgm_title
        text "Artist: ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 1:06" style style.bgm_text at bgm_time
    elif bgm_text == "020":
        text "Title: ｓｕｓｐｉｃｉｏｎ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 2:09" style style.bgm_text at bgm_time
    elif bgm_text == "028":
        text "Title: 痕音 [[Scar Sound]" style style.bgm_text at bgm_title
        text "Artist: ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 2:48" style style.bgm_text at bgm_time
    elif bgm_text == "029":
        text "Title: Ｃｏｒｅ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:48" style style.bgm_text at bgm_time
    elif bgm_text == "030":
        text "Title: Ｍｉｎｕｔｅ　ｄａｒｋｎｅｓｓ" style style.bgm_text at bgm_title
        text "Artist: プレコ [[Pureco]" style style.bgm_text at bgm_artist
        text "Time: 2:10" style style.bgm_text at bgm_time
    elif bgm_text == "031":
        text "Title: ｎｉｇｈｔｅｙｅｓ" style style.bgm_text at bgm_title
        text "Artist: あきやまうに [[U2 Akiyama]" style style.bgm_text at bgm_artist
        text "Time: 3:02" style style.bgm_text at bgm_time
    elif bgm_text == "032":
        text "Title: Ｃｌｏｓｅｄ　Ｍｙ　Ｈｅａｒｔ" style style.bgm_text at bgm_title
        text "Artist: ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 2:56" style style.bgm_text at bgm_time
    elif bgm_text == "033":
        text "Title: Ｒｅｑｕｉｅｍ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:51" style style.bgm_text at bgm_time
    elif bgm_text == "034":
        text "Title: ｍｉｎｄ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 0:57" style style.bgm_text at bgm_time
    elif bgm_text == "035":
        text "Title: Ｗｏｒｌｄｅｎｄ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 2:56" style style.bgm_text at bgm_time
    elif bgm_text == "036":
        text "Title: ｐｌａｙ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 3:43" style style.bgm_text at bgm_time
    elif bgm_text == "037":
        text "Title: システム零 [[System 0]" style style.bgm_text at bgm_title
        text "Artist: －４５" style style.bgm_text at bgm_artist
        text "Time: 3:26" style style.bgm_text at bgm_time
    elif bgm_text == "038":
        text "Title: Ｖｏｉｃｅｌｅｓｓ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 2:03" style style.bgm_text at bgm_time
    elif bgm_text == "039":
        text "Title: ｄｅａｄ　ａｎｇｌｅ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 6:34" style style.bgm_text at bgm_time
    elif bgm_text == "final":
        text "Title: Ｂｒｉｎｇ　Ｔｈｅ　Ｆａｔｅ" style style.bgm_text at bgm_title
        text "Artist: 土井宏紀 [[Doi Hironori]" style style.bgm_text at bgm_artist
        text "Time: 4:39" style style.bgm_text at bgm_time
    elif bgm_text == "040":
        text "Title: オルガン小曲　第６億番　ハ短調" style style.bgm_text at bgm_title
        text "       [[Organ Short #600 Million in C Minor]" style style.bgm_text at bgm_artist
        text "Artist: ラック眼力 [[Luck Ganriki]   Time: 1:33" style style.bgm_text at bgm_time
    elif bgm_text == "041":
        text "Title: 牢獄ＳＴＲＩＰ [[Prison Strip]" style style.bgm_text at bgm_title
        text "Artist: －４５" style style.bgm_text at bgm_artist
        text "Time: 4:17" style style.bgm_text at bgm_time
    elif bgm_text == "042":
        text "Title: 弦楽四重奏曲第１番ト長調-I.Allegro" style style.bgm_text at bgm_title
        text "        [[String Quartet #1 in G Major - I. Allegro]" style style.bgm_text at bgm_artist
        text "Artist: 北大路瑞希（グラサンねこ） [[Kitaouji Mizuki]" style style.bgm_text at bgm_time
    elif bgm_text == "043":
        text "Title: ｃａｇｅ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 3:58" style style.bgm_text at bgm_time
    elif bgm_text == "1001":
        text "Title: つるぺったん（short.ver) [[Tsuru Pettan]" style style.bgm_text at bgm_title
        text "Artist: Silver_Forest" style style.bgm_text at bgm_artist
        text "Time: 1:54" style style.bgm_text at bgm_time
    elif bgm_text == "1000":
        text "Title: すいすい☆スイーツ（＾－＾） [[Sui-Sui Sweet]" style style.bgm_text at bgm_title
        text "Artist: dai, ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Vocal: 井上麻里奈 [[Inoue Marina]" style style.bgm_text at bgm_time
    elif bgm_text == "1002":
        text "Title: どっきゅん☆ハート [[Dokkyun Heart]" style style.bgm_text at bgm_title
        text "Vocal: 井上麻里奈 [[Inoue Marina]" style style.bgm_text at bgm_artist
        text "Time: 2:19" style style.bgm_text at bgm_time
    elif bgm_text == "049":
        text "Title: 旋律（シラベ）inst.ver [[Melody]" style style.bgm_text at bgm_title
        text "Artist: ｓｕｎｎｙ、ｃａｐ、ｘａｋｉ" style style.bgm_text at bgm_artist
        text "Time: 8:04" style style.bgm_text at bgm_time
    elif bgm_text == "047":
        text "Title: Answer" style style.bgm_text at bgm_title
        text "Artist: dai" style style.bgm_text at bgm_artist
        text "Time: 2:30" style style.bgm_text at bgm_time
    elif bgm_text == "044":
        text "Title: 金色の嘲笑 [[Golden Sneer]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 5:49" style style.bgm_text at bgm_time
    elif bgm_text == "045":
        text "Title: サソリのハラワタ [[Scorpion Entrails]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 3:22" style style.bgm_text at bgm_time
    elif bgm_text == "046":
        text "Title: 終焉_VerC [[Life's End]" style style.bgm_text at bgm_title
        text "Artist: pre-holder" style style.bgm_text at bgm_artist
        text "Time: 2:39" style style.bgm_text at bgm_time
    elif bgm_text == "052":
        text "Title: where" style style.bgm_text at bgm_title
        text "Artist: pre-holder" style style.bgm_text at bgm_artist
        text "Time: 3:55" style style.bgm_text at bgm_time
    elif bgm_text == "051":
        text "Title: moon" style style.bgm_text at bgm_title
        text "Artist: dai" style style.bgm_text at bgm_artist
        text "Time: 2:52" style style.bgm_text at bgm_time
    elif bgm_text == "048":
        text "Title: Answer_short" style style.bgm_text at bgm_title
        text "Artist: dai" style style.bgm_text at bgm_artist
        text "Time: 1:02" style style.bgm_text at bgm_time
    elif bgm_text == "053":
        text "Title: Dread_of_the_grave" style style.bgm_text at bgm_title
        text "Artist: ＳＢ　ＹＵＮＥ" style style.bgm_text at bgm_artist
        text "Time: 5:43" style style.bgm_text at bgm_time
    elif bgm_text == "050":
        text "Title: Red_Dread" style style.bgm_text at bgm_title
        text "Artist: Ryu-Ga" style style.bgm_text at bgm_artist
        text "Time: 2:43" style style.bgm_text at bgm_time
    elif bgm_text == "054":
        text "Title: Worldend dominator" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 7:37" style style.bgm_text at bgm_time
    elif bgm_text == "055":
        text "Title: 黒のリリアナ [[Black Lilliana]" style style.bgm_text at bgm_title
        text "Artist: あきやまうに [[U2 Akiyama]" style style.bgm_text at bgm_artist
        text "Time: 5:19" style style.bgm_text at bgm_time
    elif bgm_text == "056":
        text "Title: 休息 [[Rest]" style style.bgm_text at bgm_title
        text "Artist: Ryu-Ga" style style.bgm_text at bgm_artist
        text "Time: 1:30" style style.bgm_text at bgm_time
    elif bgm_text == "057":
        text "Title: 白日夢の果て [[Daydream's End]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Chorus: 木野寧 [[Kino Nei]" style style.bgm_text at bgm_time
    elif bgm_text == "058":
        text "Title: 旋律（シラベ） [[Melody]" style style.bgm_text at bgm_title
        text "Artist: ｓｕｎｎｙ、ｃａｐ、ｘａｋｉ" style style.bgm_text at bgm_artist
        text "Vocal: 木村 圭見 [[Kimura Kazumi]" style style.bgm_text at bgm_time
    elif bgm_text == "059":
        text "Title: Over_the_sky" style style.bgm_text at bgm_title
        text "Artist: pre-holder" style style.bgm_text at bgm_artist
        text "Time: 3:31" style style.bgm_text at bgm_time
    elif bgm_text == "060":
        text "Title: ひだまり [[In the Sun]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 3:12" style style.bgm_text at bgm_time
    elif bgm_text == "061":
        text "Title: ロウソクたちが踊る [[The Candles Dance]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 2:21" style style.bgm_text at bgm_time
    elif bgm_text == "062":
        text "Title: Ｈａｒｕｋａ [[Distant]" style style.bgm_text at bgm_title
        text "Artist: ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 3:14" style style.bgm_text at bgm_time
    elif bgm_text == "063":
        text "Title: ｐｓｙ－ｃｈｏｒｕｓ" style style.bgm_text at bgm_title
        text "Artist: ｘａｋｉ" style style.bgm_text at bgm_artist
        text "Time: 7:46" style style.bgm_text at bgm_time
    elif bgm_text == "064":
        text "Title: ｆａｒ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 3:09" style style.bgm_text at bgm_time
    elif bgm_text == "065":
        text "Title: あかいくつ偽 [[Fake Red Shoes]" style style.bgm_text at bgm_title
        text "Artist: －４５" style style.bgm_text at bgm_artist
        text "Time: 4:03" style style.bgm_text at bgm_time
    elif bgm_text == "066":
        text "Title: ｍｏｔｈｅｒ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:16" style style.bgm_text at bgm_time
    elif bgm_text == "067":
        text "Title: ｈａｚｅ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 5:29" style style.bgm_text at bgm_time
    elif bgm_text == "068":
        text "Title: 踊る煙管 [[Dancing Pipe]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 4:05" style style.bgm_text at bgm_time
    elif bgm_text == "069":
        text "Title: Dread of the grave -More fear-" style style.bgm_text at bgm_title
        text "Artist: ＳＢ　ＹＵＮＥ" style style.bgm_text at bgm_artist
        text "Time: 6:07" style style.bgm_text at bgm_time
    elif bgm_text == "069b":
        text "Title: Dread of the grave -More fear-" style style.bgm_text at bgm_title
        text "Artist: ＳＢ　ＹＵＮＥ" style style.bgm_text at bgm_artist
        text "Time: 6:22" style style.bgm_text at bgm_time
    elif bgm_text == "070":
        text "Title: オルガン小曲　第２億番　ハ短調" style style.bgm_text at bgm_title
        text "         [[Organ Short #200 Million in C Minor]" style style.bgm_text at bgm_artist
        text "Artist: ラック眼力 [[Luck Ganriki]   Time: 1:33" style style.bgm_text at bgm_time
    elif bgm_text == "071":
        text "Title: rhythm-changer" style style.bgm_text at bgm_title
        text "Artist: ｘａｋｉ" style style.bgm_text at bgm_artist
        text "Time: 3:53" style style.bgm_text at bgm_time
    elif bgm_text == "072":
        text "Title: happiness of marionette omake" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:59" style style.bgm_text at bgm_time
    elif bgm_text == "073":
        text "Title: happiness of marionette" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:18" style style.bgm_text at bgm_time
    elif bgm_text == "074":
        text "Title: 月うさぎの舞踏 [[Dance of the Moon Rabbits]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:36" style style.bgm_text at bgm_time
    elif bgm_text == "075":
        text "Title: Melting away" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 3:00" style style.bgm_text at bgm_time
    elif bgm_text == "076":
        text "Title: soul of soul" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:09" style style.bgm_text at bgm_time
    elif bgm_text == "077":
        text "Title: miragecoordinator" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 7:12" style style.bgm_text at bgm_time
    elif bgm_text == "078":
        text "Title: ｐｒｉｓｏｎ" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:55" style style.bgm_text at bgm_time
    elif bgm_text == "079":
        text "Title: 生まれてきてくれてありがとう" style style.bgm_text at bgm_title
        text "        [[Thanks for Being Born]" style style.bgm_text at bgm_artist
        text "Artist: ｄａｉ    Time: 3:08" style style.bgm_text at bgm_time
    elif bgm_text == "080":
        text "Title: 翼 [[Wings]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:44" style style.bgm_text at bgm_time
    elif bgm_text == "081":
        text "Title: 失楽園 [[Lost Paradise]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 4:00" style style.bgm_text at bgm_time
    elif bgm_text == "082":
        text "Title: ｗｉｎｇｌｅｓｓ" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 3:43" style style.bgm_text at bgm_time
    elif bgm_text == "083":
        text "Title: ａｃｔｉｖｅｐａｉｎ" style style.bgm_text at bgm_title
        text "Artist: ｓｕｎｎｙ、ｘａｋｉ    Time: 2:13" style style.bgm_text at bgm_artist
        text "Vocal: 本木咲黒 [[Motoki Zakuro]" style style.bgm_text at bgm_time
    elif bgm_text == "084":
        text "Title: Dread of the grave -rhythm ver-" style style.bgm_text at bgm_title
        text "Artist: ＳＢ　ＹＵＮＥ" style style.bgm_text at bgm_artist
        text "Time: 4:37" style style.bgm_text at bgm_time
    elif bgm_text == "085":
        text "Title: 久遠 [[Eternity]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:24" style style.bgm_text at bgm_time
    elif bgm_text == "086":
        text "Title: over" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 2:22" style style.bgm_text at bgm_time
    elif bgm_text == "087":
        text "Title: Like_the_gale" style style.bgm_text at bgm_title
        text "Artist: 北大路瑞希（グラサンねこ） [[Kitaouji Mizuki]" style style.bgm_text at bgm_artist
        text "Time: 3:54" style style.bgm_text at bgm_time
    elif bgm_text == "088":
        text "Title: F Style" style style.bgm_text at bgm_title
        text "Artist: Ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 2:49" style style.bgm_text at bgm_time
    elif bgm_text == "089":
        text "Title: Monochrome Clock" style style.bgm_text at bgm_title
        text "Artist: Ｍ．Ｚａｋｋｙ" style style.bgm_text at bgm_artist
        text "Time: 2:00" style style.bgm_text at bgm_time
    elif bgm_text == "090":
        text "Title: apathy" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 4:16" style style.bgm_text at bgm_time
    elif bgm_text == "091":
        text "Title: 神秘の森 [[Mystic Forest]" style style.bgm_text at bgm_title
        text "Artist: Ｒｙｕ－Ｇａ" style style.bgm_text at bgm_artist
        text "Time: 2:45" style style.bgm_text at bgm_time
    elif bgm_text == "092":
        text "Title: さくたろうの頑張り物語 [[Sakutarou's Adventure]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:56" style style.bgm_text at bgm_time
    elif bgm_text == "093":
        text "Title: Parallel" style style.bgm_text at bgm_title
        text "Artist: Ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 4:11" style style.bgm_text at bgm_time
    elif bgm_text == "094":
        text "Title: " style style.bgm_text at bgm_title
        text "Artist: " style style.bgm_text at bgm_artist
        text "Time: " style style.bgm_text at bgm_time
    elif bgm_text == "095":
        text "Title: 599_million_ruins" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 1:32" style style.bgm_text at bgm_time
    elif bgm_text == "096":
        text "Title: Happy_Maria!(Instrumental)" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 2:49" style style.bgm_text at bgm_time
    elif bgm_text == "097":
        text "Title: Surrounding" style style.bgm_text at bgm_title
        text "Artist: Ｐｒｅ－ｈｏｌｄｅｒ" style style.bgm_text at bgm_artist
        text "Time: 2:37" style style.bgm_text at bgm_time
    elif bgm_text == "098":
        text "Title: HIBUTA [[Launch]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 2:29" style style.bgm_text at bgm_time
    elif bgm_text == "099":
        text "Title: death(from_stupefaction)" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 7:59" style style.bgm_text at bgm_time
    elif bgm_text == "100":
        text "Title: mortal_stampede" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 3:59" style style.bgm_text at bgm_time
    elif bgm_text == "101":
        text "Title: Victima_propiciatoria" style style.bgm_text at bgm_title
        text "Artist: ＳＢ　ＹＵＮＥ" style style.bgm_text at bgm_artist
        text "Time: 5:33" style style.bgm_text at bgm_time
    elif bgm_text == "102":
        text "Title: Revolt" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 3:12" style style.bgm_text at bgm_time
    elif bgm_text == "103":
        text "Title: 煉獄凶狂葬曲" style style.bgm_text at bgm_title
        text "        [[The Dark and Crazed Requiem of Purgatory]" style style.bgm_text at bgm_artist
        text "Artist: 北大路瑞希（グラサンねこ） [[Kitaouji Mizuki]" style style.bgm_text at bgm_time
    elif bgm_text == "104":
        text "Title: Ｈａｐｐｙ　Ｍａｒｉａ！" style style.bgm_text at bgm_title
        text "Artist: ラック眼力、E.Kida、ナカオボウシ、ますだ麻美" style style.bgm_text at bgm_artist
        text "Vocal: 木野寧 [[Kino Nei]" style style.bgm_text at bgm_time
    elif bgm_text == "105":
        text "Title: dive_to_emergency" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 5:52" style style.bgm_text at bgm_time
    elif bgm_text == "106":
        text "Title: dir" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:56" style style.bgm_text at bgm_time
    elif bgm_text == "107":
        text "Title: エンドレスナイン [[Endless Nine]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 5:36" style style.bgm_text at bgm_time
    elif bgm_text == "108":
        text "Title: dreamenddischarger" style style.bgm_text at bgm_title
        text "Artist: ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 9:28" style style.bgm_text at bgm_time
    elif bgm_text == "109":
        text "Title: ｄｉｓｃｏｄｅ" style style.bgm_text at bgm_title
        text "Artist: sunny,xaki,cap,pyon,佐倉かなえ [[Sakura Kanae]" style style.bgm_text at bgm_artist
        text "Vocal: 佐倉かなえ [[Sakura Kanae]" style style.bgm_text at bgm_time
    elif bgm_text == "110":
        text "Title: くるり [[About Face]" style style.bgm_text at bgm_title
        text "Artist: ｄａｉ" style style.bgm_text at bgm_artist
        text "Time: 1:46" style style.bgm_text at bgm_time
    elif bgm_text == "mbox":
        text "Title: オトナノノミモノ [[Grown-Up Drinks]" style style.bgm_text at bgm_title
        text "Artist: ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 3:08" style style.bgm_text at bgm_time
    elif bgm_text == "201":
        text "Title: 魔女が棲む島 [[The Witch's Island]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Vocal: Rehori, tohko              Time: 2:39" style style.bgm_text at bgm_time
    elif bgm_text == "202":
        text "Title: 穏やかな午後 [[Mild Afternoon]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:15" style style.bgm_text at bgm_time
    elif bgm_text == "203":
        text "Title: 踊る少女人形 [[Puppet Girl's Dance]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:04" style style.bgm_text at bgm_time
    elif bgm_text == "204":
        text "Title: 追い求めた先 [[Old Pursuit]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 1:58" style style.bgm_text at bgm_time
    elif bgm_text == "205":
        text "Title: 這いよる不安 [[Creeping Anxiety]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 1:59" style style.bgm_text at bgm_time
    elif bgm_text == "206":
        text "Title: 開かれた禁忌 [[Imminent Contraindications]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:15" style style.bgm_text at bgm_time
    elif bgm_text == "207":
        text "Title: サソリのハラワタ [[Scorpion Entrails] (Anime)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 3:23" style style.bgm_text at bgm_time
    elif bgm_text == "208":
        text "Title: Requiem (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, dai" style style.bgm_text at bgm_artist
        text "Time: 2:54" style style.bgm_text at bgm_time
    elif bgm_text == "209":
        text "Title: 零れ落ちる涙 [[Overflowing Autumn Cracks]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:05" style style.bgm_text at bgm_time
    elif bgm_text == "210":
        text "Title: 憂鬱な午後 [[Gloomy Afternoon]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 3:03" style style.bgm_text at bgm_time
    elif bgm_text == "211":
        text "Title: 静かな葛藤 [[Quiet Conflict]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 3:34" style style.bgm_text at bgm_time
    elif bgm_text == "212":
        text "Title: moon (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, dai" style style.bgm_text at bgm_artist
        text "Time: 2:33" style style.bgm_text at bgm_time
    elif bgm_text == "213":
        text "Title: 心奥の焔 [[Inner Heart's Flame]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:05" style style.bgm_text at bgm_time
    elif bgm_text == "214":
        text "Title: 金色の悲哀 [[Golden Sorrow]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:13" style style.bgm_text at bgm_time
    elif bgm_text == "215":
        text "Title: 暗緑に沈む館 [[Gloomy Mansion Scenery]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:35" style style.bgm_text at bgm_time
    elif bgm_text == "216":
        text "Title: 笑うモノクル [[Laughing Monocle]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 1:52" style style.bgm_text at bgm_time
    elif bgm_text == "217":
        text "Title: 宿願の不可思議 [[Mysterious Desire]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 1:54" style style.bgm_text at bgm_time
    elif bgm_text == "218":
        text "Title: 時を旅する者 [[Those Who Traverse Time]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 1:57" style style.bgm_text at bgm_time
    elif bgm_text == "219":
        text "Title: 可憐な冷笑者 [[Cynically Sweet]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:05" style style.bgm_text at bgm_time
    elif bgm_text == "220":
        text "Title: 闇で微笑む者達 [[Dark Smile]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 3:55" style style.bgm_text at bgm_time
    elif bgm_text == "221":
        text "Title: 小さな世界 [[Small World]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 3:07" style style.bgm_text at bgm_time
    elif bgm_text == "222":
        text "Title: 閉じた部屋 [[Closed Room]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 2:37" style style.bgm_text at bgm_time
    elif bgm_text == "223":
        text "Title: あかいくつ偽 [[Fake Red Shoes] (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, －４５" style style.bgm_text at bgm_artist
        text "Time: 3:13" style style.bgm_text at bgm_time
    elif bgm_text == "224":
        text "Title: 下される審判 [[Judgement]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 4:13" style style.bgm_text at bgm_time
    elif bgm_text == "225":
        text "Title: mortal stampede (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, dai" style style.bgm_text at bgm_artist
        text "Time: 4:08" style style.bgm_text at bgm_time
    elif bgm_text == "226":
        text "Title: 王者の戦い [[Battle of the Champions]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 3:28" style style.bgm_text at bgm_time
    elif bgm_text == "227":
        text "Title: 終端の旋律 [[Melodious Terminal]" style style.bgm_text at bgm_title
        text "Artist: GranMusik" style style.bgm_text at bgm_artist
        text "Time: 3:11" style style.bgm_text at bgm_time
    elif bgm_text == "228":
        text "Title: miragecoordinator (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 4:28" style style.bgm_text at bgm_time
    elif bgm_text == "229":
        text "Title: dreamenddischarger (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, ｚｔｓ" style style.bgm_text at bgm_artist
        text "Time: 5:34" style style.bgm_text at bgm_time
    elif bgm_text == "230":
        text "Title: happiness of marionette (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, dai" style style.bgm_text at bgm_artist
        text "Time: 2:20" style style.bgm_text at bgm_time
    elif bgm_text == "231":
        text "Title: Answer (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, dai" style style.bgm_text at bgm_artist
        text "Time: 2:19" style style.bgm_text at bgm_time
    elif bgm_text == "232":
        text "Title: Answer_short (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, dai" style style.bgm_text at bgm_artist
        text "Time: 1:38" style style.bgm_text at bgm_time
    elif bgm_text == "233":
        text "Title: オルガン小曲　第６億番　ハ短調 (Anime ver)" style style.bgm_text at bgm_title
        text "       [[Organ Short #600 Million in C Minor]" style style.bgm_text at bgm_artist
        text "Artist: GranMusik, ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_time
    elif bgm_text == "234":
        text "Title: ロウソクたちが踊る [[The Candles Dance] (Anime)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, ラック眼力 [[Luck Ganriki]" style style.bgm_text at bgm_artist
        text "Time: 2:22" style style.bgm_text at bgm_time
    elif bgm_text == "235":
        text "Title: 黒のリリアナ [[Black Lilliana] (Anime ver)" style style.bgm_text at bgm_title
        text "Artist: GranMusik, あきやまうに [[U2 Akiyama]" style style.bgm_text at bgm_artist
        text "Time: 5:15" style style.bgm_text at bgm_time
    
    
    
init python:
    
    def bgm1(BGM_s_Ch=999):
#        renpy.music.stop(channel='music')
        renpy.music.set_volume(default_vol, 0, channel="music")
        try:
            bgm_res[BGM_s_Ch]
#        if BGM_s_Ch:
            if persistent.anime_bgm2:
                BGM_s_Ch = animebgm(BGM_s_Ch)
            renpy.music.play(bgm_res[BGM_s_Ch][0],channel='music')
            if persistent.bgm_text:
                if persistent.bgm_lang == 0:
                    renpy.notify("♪" + bgm_res[BGM_s_Ch][1])
                else:
                    renpy.notify("♪" + bgm_res[BGM_s_Ch][2])
        except IndexError:
#        else:
            renpy.music.stop(channel='music')
            renpy.notify("No track selected")
        
        bgm_counter()
        renpy.with_statement(None, always=True)
    
    def bgm1v(BGM_s_Ch=999,Set_vol=default_vol):
#        renpy.music.stop(channel='music')
        renpy.music.set_volume(Set_vol, 0, channel="music")
        try:
            bgm_res[BGM_s_Ch]
#        if BGM_s_Ch:
            if persistent.anime_bgm2:
                BGM_s_Ch = animebgm(BGM_s_Ch)
            renpy.music.play(bgm_res[BGM_s_Ch][0],channel='music')
            if persistent.bgm_text:
                if persistent.bgm_lang == 0:
                    renpy.notify("♪" + bgm_res[BGM_s_Ch][1])
                else:
                    renpy.notify("♪" + bgm_res[BGM_s_Ch][2])
        except IndexError:
#        else:
            renpy.music.stop(channel='music')
            renpy.notify("No track selected")
        
        bgm_counter()
        renpy.with_statement(None, always=True)
    
    def animebgm(BGM_s_Ch):
        tmp1 = [45, 33, 51, 65, 100,77, 108,73, 47, 48, 40, 61, 55]
        tmp2 = [207,208,212,223,225,228,229,230,231,232,233,234,235]
        try:
            x = tmp1.index(BGM_s_Ch)
        except ValueError:
            return BGM_s_Ch
        y = tmp2[x]
        return y
    
    def moviefx(Movie_Number="no01"):
        renpy.music.stop(channel='moviefx')
        renpy.music.set_volume(default_vol, 0, channel="moviefx")
        renpy.music.play("me/" + Movie_Number + ".ogg",channel='moviefx')
    
    def me1(Me_Number=1):
        renpy.music.stop(channel='me1')
        renpy.music.set_volume(default_vol, 0, channel="me1")
        renpy.music.play(Me_Number,channel='me1')
    
    def me1v(Me_Number=1,Set_vol=0.7):
        renpy.music.stop(channel='me1')
        renpy.music.set_volume(Set_vol, 0, channel="me1")
        renpy.music.play(Me_Number,channel='me1')
    
    def me2(Me_Number=1):
        renpy.music.stop(channel='me2')
        renpy.music.set_volume(default_vol, 0, channel="me2")
        renpy.music.play(Me_Number,channel='me2')
    
    def me2v(Me_Number=1,Set_vol=0.7):
        renpy.music.stop(channel='me2')
        renpy.music.set_volume(Set_vol, 0, channel="me2")
        renpy.music.play(Me_Number,channel='me2')
    
    def me3(Me_Number=1):
        renpy.music.stop(channel='me3')
        renpy.music.set_volume(default_vol, 0, channel="me3")
        renpy.music.play(Me_Number,channel='me3')
    
    def me3v(Me_Number=1,Set_vol=0.7):
        renpy.music.stop(channel='me3')
        renpy.music.set_volume(Set_vol, 0, channel="me3")
        renpy.music.play(Me_Number,channel='me3')
    
    def me4(Me_Number=1):
        renpy.music.stop(channel='me4')
        renpy.music.set_volume(default_vol, 0, channel="me4")
        renpy.music.play(Me_Number,channel='me4')
    
    def me4v(Me_Number=1,Set_vol=0.7):
        renpy.music.stop(channel='me4')
        renpy.music.set_volume(Set_vol, 0, channel="me4")
        renpy.music.play(Me_Number,channel='me4')
    
    def me5(Me_Number=1):
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(default_vol, 0, channel="me5")
        renpy.music.play(Me_Number,channel='me5')
    
    def me5v(Me_Number=1,Set_vol=0.7):
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(Set_vol, 0, channel="me5")
        renpy.music.play(Me_Number,channel='me5')
    
    def se1(Se_Number=1):
        renpy.music.set_volume(default_vol, 0, channel="sound")
        renpy.music.play(Se_Number,channel='sound')
    
    def se1v(Se_Number=1,Set_vol=0.7):
        renpy.music.set_volume(Set_vol, 0, channel="sound")
        renpy.music.play(Se_Number,channel='sound')
    
    def se2(Se_Number=1):
        renpy.music.set_volume(default_vol, 0, channel="se2")
        renpy.music.play(Se_Number,channel='se2')
    
    def se2v(Se_Number=1,Set_vol=0.7):
        renpy.music.set_volume(Set_vol, 0, channel="se2")
        renpy.music.play(Se_Number,channel='se2')
    
    def se3(Se_Number=1):
        renpy.music.set_volume(default_vol, 0, channel="se3")
        renpy.music.play(Se_Number,channel='se3')
    
    def se3v(Se_Number=1,Set_vol=0.7):
        renpy.music.set_volume(Set_vol, 0, channel="se3")
        renpy.music.play(Se_Number,channel='se3')
    
    def seplay(Se_Play_Channel,Se_Number=1):
        if Se_Play_Channel == 1:
            renpy.music.set_volume(default_vol, 0, channel="se1")
            renpy.music.play(Se_Number,channel='se1')
        elif Se_Play_Channel == 2:
            renpy.music.set_volume(default_vol, 0, channel="se2")
            renpy.music.play(Se_Number,channel='se2')
        elif Se_Play_Channel == 3:
            renpy.music.set_volume(default_vol, 0, channel="se3")
            renpy.music.play(Se_Number,channel='se3')
        elif Se_Play_Channel == 9:
            renpy.music.set_volume(default_vol, 0, channel="se9")
            renpy.music.play(Se_Number,channel='se9')
        elif Se_Play_Channel == 10:
            renpy.music.set_volume(default_vol, 0, channel="se10")
            renpy.music.play(Se_Number,channel='se10')
        elif Se_Play_Channel == 20:
            renpy.music.set_volume(default_vol, 0, channel="se20")
            renpy.music.play(Se_Number,channel='se20')
    
    def seplay2(Se_Play_Channel=9,Se_Number=1,Set_vol=0.7):
        if Se_Play_Channel == 1:
            renpy.music.set_volume(Set_vol, 0, channel="se1")
            renpy.music.play(Se_Number,channel='se1')
        elif Se_Play_Channel == 2:
            renpy.music.set_volume(Set_vol, 0, channel="se2")
            renpy.music.play(Se_Number,channel='se2')
        elif Se_Play_Channel == 3:
            renpy.music.set_volume(Set_vol, 0, channel="se3")
            renpy.music.play(Se_Number,channel='se3')
        elif Se_Play_Channel == 9:
            renpy.music.set_volume(Set_vol, 0, channel="se9")
            renpy.music.play(Se_Number,channel='se9')
        elif Se_Play_Channel == 10:
            renpy.music.set_volume(Set_vol, 0, channel="se10")
            renpy.music.play(Se_Number,channel='se10')
        elif Se_Play_Channel == 20:
            renpy.music.set_volume(Set_vol, 0, channel="se20")
            renpy.music.play(Se_Number,channel='se20')
    
    def fede(free1,free9):
        if free1 == 0:
            fede_0(free9)
        elif free1 == 1:
            fede_10(free9)
        elif free1 == 10:
            fede_1(free9)
        elif free1 == 11:
            fede_11(free1,free9)
        elif free1 == 12:
            fede_11(free1,free9)
        elif free1 == 13:
            fede_11(free1,free9)
        elif free1 == 14:
            fede_11(free1,free9)
        elif free1 == 15:
            fede_11(free1,free9)
        
    def fede_0(free9):
        renpy.music.set_volume(0.0, free9, channel="music")
        renpy.music.set_volume(0.0, free9, channel="me0")
        renpy.music.set_volume(0.0, free9, channel="me1")
        renpy.music.set_volume(0.0, free9, channel="me2")
        renpy.music.set_volume(0.0, free9, channel="me3")
        renpy.music.set_volume(0.0, free9, channel="me4")
        renpy.music.set_volume(0.0, free9, channel="me5")
        renpy.pause(free9, hard=True)
        renpy.pause(0.5)
        E_A()
        
    def fede_1(free9):
        renpy.music.set_volume(0.0, free9, channel="me0")
        renpy.music.set_volume(0.0, free9, channel="me1")
        renpy.music.set_volume(0.0, free9, channel="me2")
        renpy.music.set_volume(0.0, free9, channel="me3")
        renpy.music.set_volume(0.0, free9, channel="me4")
        renpy.music.set_volume(0.0, free9, channel="me5")
        renpy.pause(free9, hard=True)
        renpy.pause(0.5)
        E_MA()
        
    def fede_10(free9):
        renpy.music.set_volume(0.0, free9, channel="music")
        renpy.pause(free9, hard=True)
        renpy.pause(0.5)
        E_B()
        
    def fede_11(free1,free9):
        if free1 == 11:
            renpy.music.stop(channel='me1',fadeout=free9)
            renpy.pause(free9, hard=True)
            renpy.pause(0.5)
            renpy.music.set_volume(default_vol, 0, channel="me1")
        elif free1 == 12:
            renpy.music.stop(channel='me2',fadeout=free9)
            renpy.pause(free9, hard=True)
            renpy.pause(0.5)
            renpy.music.set_volume(default_vol, 0, channel="me2")
        elif free1 == 13:
            renpy.music.stop(channel='me3',fadeout=free9)
            renpy.pause(free9, hard=True)
            renpy.pause(0.5)
            renpy.music.set_volume(default_vol, 0, channel="me3")
        elif free1 == 14:
            renpy.music.stop(channel='me4',fadeout=free9)
            renpy.pause(free9, hard=True)
            renpy.pause(0.5)
            renpy.music.set_volume(default_vol, 0, channel="me4")
        elif free1 == 15:
            renpy.music.stop(channel='me5',fadeout=free9)
            renpy.pause(free9, hard=True)
            renpy.pause(0.5)
            renpy.music.set_volume(default_vol, 0, channel="me5")
            
        
    #    $ free1 = 10
    #    $ free3 = 2
    #    call e_
#        return
        
#    def erase():
#        e_()
#        return
#    def silent():
#        e_()
#        return

    def e_(free3=0,free1=0):
        if free3 == 1:
            E_B()
            return
        elif free3 == 2:
            if free1 == 0:
                renpy.music.stop(channel='me0')
                renpy.music.set_volume(default_vol, 0, channel="me0")
            if free1 == 1:
                renpy.music.stop(channel='me1')
                renpy.music.set_volume(default_vol, 0, channel="me1")
            if free1 == 2:
                renpy.music.stop(channel='me2')
                renpy.music.set_volume(default_vol, 0, channel="me2")
            if free1 == 3:
                renpy.music.stop(channel='me3')
                renpy.music.set_volume(default_vol, 0, channel="me3")
            if free1 == 4:
                renpy.music.stop(channel='me4')
                renpy.music.set_volume(default_vol, 0, channel="me4")
            if free1 == 5:
                renpy.music.stop(channel='me5')
                renpy.music.set_volume(default_vol, 0, channel="me5")
            return
        elif free3 == 3:
            if free1 > 3:
                renpy.music.stop(channel='sound')
                renpy.music.set_volume(default_vol, 0, channel="sound")
            if free1 == 1:
                renpy.music.stop(channel='sound')
            if free1 == 2:
                renpy.music.stop(channel='se2')
            if free1 == 3:
                renpy.music.stop(channel='se3')
            return
        E_A()
        return
        
    def E_C():
        renpy.music.stop()
        renpy.music.set_volume(default_vol, 0, channel="music")
        return
        
    def E_B():
        renpy.music.stop()
        renpy.music.set_volume(default_vol, 0, channel="music")
        
    def E_B1():
        renpy.music.stop()
        renpy.music.set_volume(default_vol, 0, channel="music")
        return
        
    def E_B2():
        renpy.music.stop(channel='me0')
        renpy.music.set_volume(default_vol, 0, channel="me0")
        return
        
    def E_M0():
        renpy.music.stop(channel='me0')
        renpy.music.set_volume(default_vol, 0, channel="me0")
        return

    def E_B3():
        renpy.music.stop(channel='me1')
        renpy.music.set_volume(default_vol, 0, channel="me1")
        return
        
    def E_M1():
        renpy.music.stop(channel='me1')
        renpy.music.set_volume(default_vol, 0, channel="me1")
        return

    def E_B4():
        renpy.music.stop(channel='me2')
        renpy.music.set_volume(default_vol, 0, channel="me2")
        return
        
    def E_M2():
        renpy.music.stop(channel='me2')
        renpy.music.set_volume(default_vol, 0, channel="me2")
        return

    def E_B5():
        renpy.music.stop(channel='me3')
        renpy.music.set_volume(default_vol, 0, channel="me3")
        return
        
    def E_M3():
        renpy.music.stop(channel='me3')
        renpy.music.set_volume(default_vol, 0, channel="me3")
        return

    def E_B6():
        renpy.music.stop(channel='me4')
        renpy.music.set_volume(default_vol, 0, channel="me4")
        return
        
    def E_M4():
        renpy.music.stop(channel='me4')
        renpy.music.set_volume(default_vol, 0, channel="me4")
        return

    def E_M5():
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(default_vol, 0, channel="me5")
        return

    def E_S1():
        renpy.music.stop(channel='sound')
        renpy.music.set_volume(default_vol, 0, channel="sound")
        return

    def E_S2():
        renpy.music.stop(channel='se2')
        renpy.music.set_volume(default_vol, 0, channel="se2")
        return
        
    def E_S3():
        renpy.music.stop(channel='se3')
        renpy.music.set_volume(default_vol, 0, channel="se3")
        return

    def E_A():
        renpy.music.stop()
        renpy.music.stop(channel='me0')
        renpy.music.stop(channel='me1')
        renpy.music.stop(channel='me2')
        renpy.music.stop(channel='me3')
        renpy.music.stop(channel='me4')
        renpy.music.stop(channel='me5')
        renpy.music.stop(channel='sound')
        renpy.music.stop(channel='se1')
        renpy.music.stop(channel='se2')
        renpy.music.stop(channel='se3')
        
        renpy.music.set_volume(default_vol, 0, channel="music")
        renpy.music.set_volume(default_vol, 0, channel="me0")
        renpy.music.set_volume(default_vol, 0, channel="me1")
        renpy.music.set_volume(default_vol, 0, channel="me2")
        renpy.music.set_volume(default_vol, 0, channel="me3")
        renpy.music.set_volume(default_vol, 0, channel="me4")
        renpy.music.set_volume(default_vol, 0, channel="me5")
        renpy.music.set_volume(default_vol, 0, channel="sound")
        renpy.music.set_volume(default_vol, 0, channel="se1")
        renpy.music.set_volume(default_vol, 0, channel="se2")
        renpy.music.set_volume(default_vol, 0, channel="se3")
        renpy.music.set_volume(default_vol, 0, channel="se9")
        renpy.music.set_volume(default_vol, 0, channel="se10")
        renpy.music.set_volume(default_vol, 0, channel="se20")
        
        
    def E_A2():
        renpy.music.stop()
        renpy.music.stop(channel='me0')
        renpy.music.stop(channel='me1')
        renpy.music.stop(channel='me2')
        renpy.music.stop(channel='me3')
        renpy.music.stop(channel='me4')
        renpy.music.stop(channel='me5')
        renpy.music.stop(channel='sound')
        renpy.music.stop(channel='se2')
        renpy.music.stop(channel='se3')
        
        
    def E_Me_all():
        renpy.music.stop(channel='me0')
        renpy.music.stop(channel='me1')
        renpy.music.stop(channel='me2')
        renpy.music.stop(channel='me3')
        renpy.music.stop(channel='me4')
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(default_vol, 0, channel="me0")
        renpy.music.set_volume(default_vol, 0, channel="me1")
        renpy.music.set_volume(default_vol, 0, channel="me2")
        renpy.music.set_volume(default_vol, 0, channel="me3")
        renpy.music.set_volume(default_vol, 0, channel="me4")
        renpy.music.set_volume(default_vol, 0, channel="me5")
        
        
    def E_Me_a():
        renpy.music.stop(channel='me0')
        renpy.music.stop(channel='me1')
        renpy.music.stop(channel='me2')
        renpy.music.stop(channel='me3')
        renpy.music.stop(channel='me4')
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(default_vol, 0, channel="me0")
        renpy.music.set_volume(default_vol, 0, channel="me1")
        renpy.music.set_volume(default_vol, 0, channel="me2")
        renpy.music.set_volume(default_vol, 0, channel="me3")
        renpy.music.set_volume(default_vol, 0, channel="me4")
        renpy.music.set_volume(default_vol, 0, channel="me5")
        
    def E_MA():
        renpy.music.stop(channel='me0')
        renpy.music.stop(channel='me1')
        renpy.music.stop(channel='me2')
        renpy.music.stop(channel='me3')
        renpy.music.stop(channel='me4')
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(default_vol, 0, channel="me0")
        renpy.music.set_volume(default_vol, 0, channel="me1")
        renpy.music.set_volume(default_vol, 0, channel="me2")
        renpy.music.set_volume(default_vol, 0, channel="me3")
        renpy.music.set_volume(default_vol, 0, channel="me4")
        renpy.music.set_volume(default_vol, 0, channel="me5")
        
    def E_L():
        renpy.music.stop(channel='me0')
        renpy.music.stop(channel='me1')
        renpy.music.stop(channel='me2')
        renpy.music.stop(channel='me3')
        renpy.music.stop(channel='me4')
        renpy.music.stop(channel='me5')
        renpy.music.set_volume(default_vol, 0, channel="me0")
        renpy.music.set_volume(default_vol, 0, channel="me1")
        renpy.music.set_volume(default_vol, 0, channel="me2")
        renpy.music.set_volume(default_vol, 0, channel="me3")
        renpy.music.set_volume(default_vol, 0, channel="me4")
        renpy.music.set_volume(default_vol, 0, channel="me5")
        
    def E_SE():
        renpy.music.stop(channel='sound')
        renpy.music.stop(channel='se2')
        renpy.music.stop(channel='se3')
        renpy.music.set_volume(default_vol, 0, channel="sound")
        renpy.music.set_volume(default_vol, 0, channel="se2")
        renpy.music.set_volume(default_vol, 0, channel="se3")
        
    def cross1(free9,free1,free2,free3,free4,free5):
        renpy.music.set_volume(free1, free9, channel="me1")
        renpy.music.set_volume(free2, free9, channel="me2")
        renpy.music.set_volume(free3, free9, channel="me3")
        renpy.music.set_volume(free4, free9, channel="me4")
        renpy.music.set_volume(free5, free9, channel="me5")
        renpy.music.set_volume(0.0, free9, channel="music")
        renpy.pause(free9, hard=True)
        E_B()
        
        if not renpy.music.is_playing('me1'):
            renpy.music.set_volume(default_vol, 0, channel="me1")
        if not renpy.music.is_playing('me2'):
            renpy.music.set_volume(default_vol, 0, channel="me2")
        if not renpy.music.is_playing('me3'):
            renpy.music.set_volume(default_vol, 0, channel="me3")
        if not renpy.music.is_playing('me4'):
            renpy.music.set_volume(default_vol, 0, channel="me4")
        if not renpy.music.is_playing('me5'):
            renpy.music.set_volume(default_vol, 0, channel="me5")
        if free1 < 0.1:
            e_(2,1)
        if free2 < 0.1:
            e_(2,2)
        if free3 < 0.1:
            e_(2,3)
        if free4 < 0.1:
            e_(2,4)
        if free5 < 0.1:
            e_(2,5)
    
    def cross2(free9,free1):
        renpy.music.set_volume(0.0, free9, channel="me1")
        renpy.music.set_volume(0.0, free9, channel="me2")
        renpy.music.set_volume(0.0, free9, channel="me3")
        renpy.music.set_volume(0.0, free9, channel="me4")
        renpy.music.set_volume(0.0, free9, channel="me5")
        renpy.music.set_volume(free1, free9, channel="music")
        renpy.pause(free9, hard=True)
        E_MA()
        
        if free1 == 0.0:
            E_B()
    
    def fedexx(freebgm,free1,free2,free3,free4,free5,free9):
        if free1 == -1:
            pass
        else:
            renpy.music.set_volume(free1, free9, channel="me1")
        if free2 == -1:
            pass
        else:
            renpy.music.set_volume(free2, free9, channel="me2")
        if free3 == -1:
            pass
        else:
            renpy.music.set_volume(free3, free9, channel="me3")
        if free4 == -1:
            pass
        else:
            renpy.music.set_volume(free4, free9, channel="me4")
        if free5 == -1:
            pass
        else:
            renpy.music.set_volume(free5, free9, channel="me5")
        if freebgm == -1:
            pass
        else:
            renpy.music.set_volume(freebgm, free9, channel="music")
        renpy.pause(free9, hard=True)
        
        """
        ## V does fedexx keep these? V
        
        if not renpy.music.is_playing('me1'):
            renpy.music.set_volume(default_vol, 0, channel="me1")
        if not renpy.music.is_playing('me2'):
            renpy.music.set_volume(default_vol, 0, channel="me2")
        if not renpy.music.is_playing('me3'):
            renpy.music.set_volume(default_vol, 0, channel="me3")
        if not renpy.music.is_playing('me4'):
            renpy.music.set_volume(default_vol, 0, channel="me4")
        if not renpy.music.is_playing('me5'):
            renpy.music.set_volume(default_vol, 0, channel="me5")
        if not renpy.music.is_playing('music'):
            renpy.music.set_volume(default_vol, 0, channel="music")
        if free1 < 0.1:
            E_M1()
        if free2 < 0.1:
            E_M2()
        if free3 < 0.1:
            E_M3()
        if free4 < 0.1:
            E_M4()
        if free5 < 0.1:
            E_M5()
        if freebgm < 0.1:
            E_B()
        
        """
        
    def bgmvol(Set_vol,t=0):
        renpy.music.set_volume(Set_vol, t, channel="music")
        
    def mevol(Me_Play_Channel,Set_vol,t=0):
        if Me_Play_Channel == 1:
            renpy.music.set_volume(Set_vol, t, channel="me1")
        elif Me_Play_Channel == 2:
            renpy.music.set_volume(Set_vol, t, channel="me2")
        elif Me_Play_Channel == 3:
            renpy.music.set_volume(Set_vol, t, channel="me3")
        elif Me_Play_Channel == 4:
            renpy.music.set_volume(Set_vol, t, channel="me4")
        elif Me_Play_Channel == 5:
            renpy.music.set_volume(Set_vol, t, channel="me5")
        elif Me_Play_Channel == 6:
            renpy.music.set_volume(Set_vol, t, channel="maria")
        
    _E_MA = renpy.curry(E_MA)
    _E_A = renpy.curry(E_A)
    _E_B = renpy.curry(E_B)
    _E_B2 = renpy.curry(bgmvol)
    
screen music_box:
    tag menu
    add "background/efe/white.png"
    timer 1.7 action Start('music_box')
label music_box:
    scene white with None
    
    $ _game_menu_screen = None
        
    $ bgm_counter()
    $ E_A()
#    play se9 "se/A5_07201.ogg"
#    show white with t18
#    with Pause(0.5)
    
    if persistent.UMINEKOEND_BGM_flg == 1:
        $ persistent.UMINEKOEND_BGM_flg = 0
    
    $ renpy.music.set_volume(0.7, 0, channel="music")
#    $ renpy.music.play("bgmmode/umib_007.ogg")
    $ renpy.music.play("bgmmode/mbox.ogg")
    
    scene mhal_1c
    show black:
        alpha (120.0/255.0)
    with t22
    
    $ bgm_text = 0
    
    $ mb.single_track = True
    
    $ renpy.show_screen('bgm')
    with t2
    $ ui.interact()
    jump _noisy_return


label turu_pettann:
    
    $ E_A()
    
    scene black with t22
    scene white with t22
    scene c0202_a with t28
    
    $ renpy.music.play("bgm2/tsurupeta-128.ogg", loop=False)
    
    show pettan20:
        xpos 1.0 ypos 0
        linear 2.4 xpos 0.0 xanchor 1.0
    with Pause(2.4)
    
    hide pettan20
    show pettan:
        xcenter (310.0/640.0)
        ypos 0.0
    show pettan32:
        xpos (370.0/640.0)
        ypos (368.0/480.0)
    show pettan33:
        xpos (370.0/640.0)
        ypos (430.0/480.0)
    with None
    with Pause(2.2)
    
    hide pettan
    hide pettan32
    hide pettan33
    with Pause(0.8)
    
    show pettan10:
        xpos 1.0 ypos 0
        linear 2.0 xpos 0.0 xanchor 1.0
    with Pause(1.0)
    
    show pettan80:
        xpos 1.0 ypos 0
        linear 3.5 xpos 0.0 xanchor 1.0
    show pettan83:
        xpos 1.0 ypos (120.0/480.0)
        linear 3.5 xpos 0.0 xanchor 1.0
    show pettan110:
        xpos 1.0 ypos (210.0/480.0)
        linear 3.5 xpos 0.0 xanchor 1.0
    with Pause(1.5)
    
    hide pettan10
    show pettan40:
        xpos 1.0 ypos 0
        linear 3.0 xpos 0.0 xanchor 1.0
    with Pause(1.5)
    
    show pettan70:
        xpos 1.0 ypos 0
        linear 3.5 xpos 0.0 xanchor 1.0
    show pettan72:
        xpos 1.0 ypos (55.0/480.0)
        linear 3.5 xpos 0.0 xanchor 1.0
    show pettan73:
        xpos 1.0 ypos (320.0/480.0)
        linear 3.5 xpos 0.0 xanchor 1.0
    show pettan74:
        xpos 1.0 ypos (370.0/480.0)
        linear 3.5 xpos 0.0 xanchor 1.0
    show pettan75:
        xpos 1.0 ypos (410.0/480.0)
        linear 3.5 xpos 0.0 xanchor 1.0
    with Pause(1.5)
    
    hide pettan80
    hide pettan83
    hide pettan110
    hide pettan40
    
    show pettan50:
        xpos 1.0 ypos 0
        linear 2.5 xpos 0.0 xanchor 1.0
    show pettan52:
        xpos 1.0 ypos (120.0/480.0)
        linear 2.5 xpos 0.0 xanchor 1.0
    show pettan56:
        xpos 1.0 ypos (360.0/480.0)
        linear 2.5 xpos 0.0 xanchor 1.0
    with Pause(1.0)
    
    show pettan90:
        xpos 1.0 ypos 0
        linear 4.0 xpos 0.0 xanchor 1.0
    show pettan91:
        xpos 1.0 ypos (370.0/480.0)
        linear 4.0 xpos 0.0 xanchor 1.0
#    show pettan92:
#        xpos 1920 ypos (120.0/480.0)
#        linear 4.0 xpos -1017
    show pettan93:
        xpos 1.0 ypos (170.0/480.0)
        linear 4.0 xpos 0.0 xanchor 1.0
    with Pause(1.5)
    
    hide pettan50
    hide pettan52
    hide pettan56
    
    show pettan60:
        xpos 1.0 ypos 0
        linear 2.5 xpos 0.0 xanchor 1.0
    show pettan62:
        xpos 1.0 ypos (120.0/480.0)
        linear 2.5 xpos 0.0 xanchor 1.0
    show pettan66:
        xpos 1.0 ypos (360.0/480.0)
        linear 2.5 xpos 0.0 xanchor 1.0
    with Pause(1.5)
    
    show pettan100:
        xpos 1.0 ypos 0
        linear 3.0 xpos 0.0 xanchor 1.0
    with Pause(3.0)
    
    
    return

label sweet_sweet:
    
    $ E_A()
    
    scene black with t22
#    scene white with t22
    
    if persistent.bgm_text:
        if persistent.bgm_lang == 0:
            $ renpy.notify("♪すいすい☆スイーツ（＾－＾）")
        else:
            $ renpy.notify("♪Sui-Sui Sweet")
    
    $ renpy.music.play("bgm2/umib_1000.ogg")
    scene no66_00000 with t29
    
    with Pause(2.223-0.5)
    $ renpy.movie_cutscene("movie/no66.mkv", stop_music=False)
    scene no66_00239
    stop movie
    with None
    
    return


label dokkyun_heart:
    
    $ E_A()
    
    scene black with t22
#    scene white with t22
    
    if persistent.bgm_text:
        if persistent.bgm_lang == 0:
            $ renpy.notify("♪どっきゅん☆ハート")
        else:
            $ renpy.notify("♪Dokkyun Heart")
    
    $ renpy.music.play("bgma/umib_1002.ogg")
    scene no66_00000 with t29
    
    with Pause(6.31-0.5)
    $ renpy.movie_cutscene("movie/no66.mkv", stop_music=False)
    scene no66_00239
    stop movie
    with None
    
    return


init -2:
    transform bgm_win:
        xalign 0.5 ypos (731.0/1080.0) alpha (230.0/255.0)
    transform bgm_title:
        xpos (310.0/1920.0) ypos (769.0/1080.0)
    transform bgm_artist:
        xpos (310.0/1920.0) ypos (825.0/1080.0)
    transform bgm_time:
        xpos (310.0/1920.0) ypos (882.0/1080.0)
    
#image pettan = im.AlphaMask(im.Crop("pettan/pettan.bmp", (0, 0, 225, 1080)), im.Crop("pettan/pettan.bmp", (225, 0, 225, 1080)))
#image pettan_aa1 = im.AlphaMask(im.Crop("pettan/pettan_aa1.bmp", (0, 0, 564, 160)), im.Crop("pettan/pettan_aa1.bmp", (564, 0, 564, 160)))
#image pettan_aa2 = im.AlphaMask(im.Crop("pettan/pettan_aa2.bmp", (0, 0, 588, 227)), im.Crop("pettan/pettan_aa2.bmp", (588, 0, 588, 227)))
#image pettan_aa3 = im.AlphaMask(im.Crop("pettan/pettan_aa3.bmp", (0, 0, 578, 180)), im.Crop("pettan/pettan_aa3.bmp", (578, 0, 578, 180)))
#image pettan_aa4 = im.AlphaMask(im.Crop("pettan/pettan_aa4.bmp", (0, 0, 250, 109)), im.Crop("pettan/pettan_aa4.bmp", (250, 0, 250, 109)))

image pettan = Image("pettan/pettan.png", xanchor=0.0, yanchor=0.0)
image pettan10 = Image("pettan/pettan10.png", xanchor=0.0, yanchor=0.0)
image pettan20 = Image("pettan/pettan20.png", xanchor=0.0, yanchor=0.0)
image pettan31:
    Text("{color=#ff0000}（じゃない！！！）{/color}", font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan32:
#    Text("{color=#80ff00}Title ：つるぺったん{/color}", font="default.ttf", size=56, drop_shadow=(2, 2))
    Text("{color=#80ff00}Title： つるぺったん\n        (Tsurupettan){/color}", font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan33:
    Text("{color=#00ffff}Artist：Silver Forest {/color}", font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan40 = Image("pettan/pettan40.png", xanchor=0.0, yanchor=0.0)
image pettan50 = Image("pettan/pettan50.png", xanchor=0.0, yanchor=0.0)
image pettan52:
    Text(["{color=#ff8040}　ぺったん　　　ぺったん　　　餅ぺったん☆{/color}",
          "{color=#80ff00}\n　　　　　ぺったん　　　ぺったん　　　餅ぺったん☆{/color}",
          "{color=#0000ff}\n　　　　ぺったん　　　ぺったん　　　餅ぺったん☆{/color}",
          "{color=#ff0000}\n　　ぺったん　　　ぺったん　　　餅ぺったん☆{/color}"], font="default.ttf", size=67, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan56 = Image("pettan/pettan56.png", xanchor=0.0, yanchor=0.0)
image pettan60 = Image("pettan/pettan60.png", xanchor=0.0, yanchor=0.0)
image pettan62:
    Text(["{color=#ff8040}　　　ぺったん　　　ぺったん　　　胸ぺったん☆{/color}",
          "{color=#80ff00}\nぺったん　　　ぺったん　　　胸ぺったん☆{/color}",
          "{color=#0000ff}\n　　　　　　ぺったん　　　ぺったん　　　胸ぺったん☆{/color}",
          "{color=#ff0000}\n　　ぺったん　　　ぺったん　　　胸ぺったん☆{/color}"], font="default.ttf", size=67, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan66 = Image("pettan/pettan66.png", xanchor=0.0, yanchor=0.0)
image pettan70:
    Text(["{color=#ff8040}　　　　　　　　許可取ってんのかよ氏ね{/color}",
          "{color=#80ff00}\n　　　　　　　　　　　　　　　　↑ちゃんと取りました！{/color}"], font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan72 = Image("pettan/pettan_aa2.png", xanchor=0.0, yanchor=0.0)
image pettan73:
    Text("{color=#ff8040}　　　　全俺が萌えた！！！{/color}", font="default.ttf", size=113, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan74:
    Text("{color=#00ffff}☆　　（　＾∇＾）σ）≧∇≦）　　☆{/color}", font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan75:
    Text(["{color=#ff0000}［←樹海］{/color}",
          "{color=#ff0000}\n　　||　　　　オワタ ┗(^o^）┓三{/color}",
          "{color=#ff0000}\n　　||　　　　　　　　┏┗　 三{/color}"], font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan80:
    Text(["{color=#ffff00}ヽξ(`・３・)ﾉ うぜぇぜ！{/color}",
          "{color=#ffff00}\n　　（　へ）{/color}",
          "{color=#ffff00}\n　　 く {/color}"], font="default.ttf", size=67, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan83:
    Text(["{color=#ff0000}この早さなら言える！　朱志香は俺の嫁！！！{/color}",
          "{color=#ff0000}\n　　　　　　　　　　　　　　いや、俺の嫁だ！！！{/color}",
          "{color=#ff0000}\n　　　　　　　　　　　　　　　　　　　朱志香なら、俺の隣で寝ているぜ{/color}"], font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan90 = Image("pettan/pettan_aa1.png", xanchor=0.0, yanchor=0.0)
image pettan91 = Image("pettan/pettan_aa3.png", xanchor=0.0, yanchor=0.0)
image pettan92:
    Text("{color=#ff0000}全俺が萌えた！！！{/color}", font="default.ttf", size=113, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan93:
    Text(["{color=#ffffff}／hidden／hidden／hidden／hidden／hidden／hidden {/color}",
          "{color=#ffffff}\n　　　／hidden／hidden／hidden／hidden／hidden／hidden{/color}",
          "{color=#ffffff}\n／hidden／hidden／hidden／hidden／hidden／hidden{/color}",
          "{color=#ffffff}\n　　　　　　　／hidden／hidden／hidden／hidden／hidden／hidden{/color}",
          "{color=#ffffff}\n　　　／hidden／hidden／hidden／hidden／hidden／hidden{/color}",
          "{color=#ffffff}\n／hidden／hidden／hidden／hidden／hidden／hidden{/color}"], font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
image pettan99 = Image("pettan/pettan_aa4.png", xanchor=0.0, yanchor=0.0)
image pettan100 = Image("pettan/pettan100.png", xanchor=0.0, yanchor=0.0)
image pettan110:
    Text(["{color=#ffffff}＼　　　∩─－、　　　＝＝ {/color}",
          "{color=#ffffff}\n　＼／　●　､_ ｀ヽ 　　＝＝＝{/color}",
          "{color=#ffffff}\n　／＼（　●　●　| つ{/color}",
          "{color=#ffffff}\n　| 　Ｘ＿入＿ノ　　ミ　　　そんな貧乳で俺様が釣られクマ――{/color}",
          "{color=#ffffff}\n　、　（＿／　　　ノ　／⌒l {/color}",
          "{color=#ffffff}\n　／＼＿＿＿ノ＿／　／　　＝＝＝＝{/color}",
          "{color=#ffffff}\nく　　　　　　　　　　ノ　　＝＝＝＝{/color}",
          "{color=#ffffff}\n　＼　＼＿　　　　　＼{/color}",
          "{color=#ffffff}\n　　＼＿＿）　　　　　＼　　　＝＝＝＝　（⌒{/color}",
          "{color=#ffffff}\n　　　　＼　　＿＿＿＿　＼＿＿　　（⌒（⌒{/color}",
          "{color=#ffffff}\n　　　　　＼＿＿＿）＿＿＿）（⌒　（⌒　　ズザザザ{/color}"], font="default.ttf", size=56, drop_shadow=(2, 2))
    xanchor 0.0
    yanchor 0.0
    
image bgm_hane = Image("bgmmode/bgm_hane.png", xanchor=0.0, yanchor=0.0)
image m_o1bn = Image("background/efe/t/m_cy1an.png", xalign=0.5, yalign=0.5)
image mnat_2g = Image("background/efe/t/mnat_2g.png", xalign=0.5, yalign=0.5)

label bgm_mode_op:
    $ E_MA()
    scene black with None
    with Pause(1.0)
    $ renpy.movie_cutscene("movie/umineko_op.mkv")
    scene black
    call bgm_jump
label bgm_mode_op2:
    $ E_MA()
    scene black with None
    with Pause(1.0)
    $ renpy.movie_cutscene("movie/umineko_op1.mkv")
    scene black
    call bgm_jump
label bgm_mode_op3:
    $ E_MA()
    scene black with None
    with Pause(1.0)
    $ renpy.movie_cutscene("movie/umineko_op3.mkv")
    scene black
    call bgm_jump

label bgm_mode_sample_u3:
    $ E_MA()
    scene black with None
    #call E_A
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,2)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 40:
        $ rnd = renpy.random.randint(1,4)
    elif persistent.UMINEKOEND == 40:
        $ rnd = renpy.random.randint(1,5)
    else:
        $ rnd = renpy.random.randint(1,10)
    show screen _bgm_jump
    with Pause(0.4)
    scene black with t22
    if rnd == 1:
        scene mlib_1cr_bg
        show mlib_1cr
        show nan a1_fumu1 at left
        show kin a11_warai2 at right
    elif rnd == 2:
        scene sea_1a
    elif rnd == 3:
        scene g1f_s1ap
        show bea a11_aseru1 at left
        show ron a11_majime1 at right
    elif rnd == 4:
        scene mdin_1ar
        show cla a11_nayamu1 at far_left
        show ros a32_komaru4 at center
        show rud a22_majime2 at far_right
    elif rnd == 5:
        scene hos_r1am
    elif rnd == 6:
        scene bui_r1a
        show enj a11_fuman2 at left
        show oko a11_def1 at right
    elif rnd == 7:
        scene res_i4a
        show pro a11_majime1 at center
    elif rnd == 8:
        scene ship_s2af
        show layer master at ship_slow
        show ama a12_def1 at left
        show enj a11_nayamu1 at right
    elif rnd == 9:
        scene nan_r1a
        show na2 a21_def2 at left
        show enj a11_def1 at right
    elif rnd == 10:
        show bea b11_nayamu1:
            xanchor 0 yanchor 0 xpos (500.0/1920.0) ypos -(150.0/1080.0) zoom 2.0
        show but b22_nayamu4:
            xanchor 0 yanchor 0 xpos -(330.0/1920.0) ypos -(150.0/1080.0) zoom 2.0
    with t6
    with Pause(3.0)
label bgm_sample_u3_1000:
    hide screen _bgm_jump
    $ renpy.pause(0.001, hard=True)
#    if rnd == 1:
#        scene mlib_1cr_bg
#        show mlib_1cr
#        show nan a1_fumu1 at left
#        show kin a11_warai2 at right
    call bgm_jump
    return
    
label bgm_mode_natunotobira:
    $ E_MA()
    scene black with None
    $ bgm_mode_rnd_tati1()
    $ bgm_mode_rnd_bg1()
    show screen _bgm_jump
    with Pause(0.4)
    scene white with t28
    $ renpy.scene()
    $ renpy.show(tmp,at_list=[center])
    $ renpy.show(tmp_bg,at_list=[center])
    $ renpy.show(tmp1,at_list=[far_left])
    $ renpy.show(tmp2,at_list=[center])
    $ renpy.show(tmp3,at_list=[far_right],zorder=5)
    with t6
    with Pause(3.0)
label bgm_mode_natunotobira_1000:
    hide screen _bgm_jump
    $ renpy.pause(0.001, hard=True)
    $ renpy.scene()
    $ renpy.show(tmp)
    $ renpy.show(tmp_bg,at_list=[center])
    $ renpy.show(tmp1,at_list=[far_left])
    $ renpy.show(tmp2,at_list=[center])
    $ renpy.show(tmp3,at_list=[far_right],zorder=5)
    call bgm_jump
    return

label bgm_mode_hane:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,4)
    elif persistent.UMINEKOEND >= 41 and persistent.UMINEKOEND < 51:
        $ rnd = renpy.random.randint(1,5)
    scene white with t22
    
    if rnd == 1:
        scene beach_2af with t26
        with Pause(2.0)
    elif rnd == 2 or rnd == 3:
        scene sea_1af with t22
        
        $ me2v(me03,1.0)
        $ tmp = 1
        
        while tmp <= 8:
            with quakey_3_500
            $ tmp+=1
        
        show but b22_odoroki2 at center with t26
        show bgm_hane:
            xpos 1.0 xanchor 0.0 ypos (114.0/1080.0)
            linear 7.0 xpos 0.0 xanchor 1.0
        with Pause(7.0)
        hide bgm_hane
    elif rnd == 4:
        scene beach_2a
        show sha a21_majime1 at left
        show geo a11_warai1 at right
        with t26
    elif rnd == 5:
        jump bgm_mode_yami_no_hohoemu
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return

label bgm_mode_ride_on:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    $ free1 = 8.0
    scene black with t24
    
    if rnd == 1:
        scene op0101 with t2
        with Pause(free1)
        with Pause(2.0)
        scene white with t24
        scene op0102 with t2
        with Pause(free1)
        scene white with t24
        scene op0103 with t2
        with Pause(free1)
        scene white with t24
        scene op0104 with t2
        with Pause(free1)
        scene white with t24
        scene op0105 with t2
        with Pause(free1)
        scene white with t24
        scene op0106 with t2
        with Pause(free1)
        scene white with t24
        scene op0107 with t2
        with Pause(free1)
        scene white with t24
        scene op0108 with t2
    elif rnd == 2:
        scene op0201 with t2
        with Pause(free1)
        with Pause(2.0)
        scene white with t24
        scene op0202 with t2
        with Pause(free1)
        scene white with t24
        scene op0203 with t2
        with Pause(free1)
        scene white with t24
        scene op0204 with t2
        with Pause(free1)
        scene white with t24
        scene op0205 with t2
        with Pause(free1)
        scene white with t24
        scene op0206 with t2
        with Pause(free1)
        scene white with t24
        scene op0207 with t2
        with Pause(free1)
        scene white with t24
        scene op0208 with t2
    elif rnd == 3:
        scene airp_out2b with t2
        with Pause(free1)
        with Pause(2.0)
        scene white with t24
        scene airp_w1bc
        show airp_w1bc_bg
        with t2
        with Pause(free1)
        scene white with t24
        scene airp_w1cc
        show airp_w1cc_bg
        with t2
        with Pause(free1)
        scene white with t24
        scene airp_w1d with t2
        with Pause(free1)
        scene white with t24
        scene airp_w1j with t2
    with Pause(free1)
    with Pause(3.0)
    scene white with t2
    $ renpy.pause(0.001, hard=True)
    if rnd == 1:
        scene op0108
    elif rnd == 2:
        scene op0208
    elif rnd == 3:
        scene end_1b
    call bgm_jump
    return

label bgm_mode_sea:
    $ E_MA()
    scene black with None
    $ bgm_mode_rnd_tati1()
    $ bgm_mode_rnd_bg1()
    
    call bgm_jump
    return
    
label bgm_mode_kurayaminotoki:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,13)
    scene black with t22
    if rnd == 1:
        scene g_o1ar
    elif rnd == 2:
        scene g_o1cr
    elif rnd == 3:
        scene m_o1ar
    elif rnd == 4:
        scene m_o1bn
    elif rnd == 5:
        scene mdin_1fr
    elif rnd == 6:
        scene m2f_p1br_bg
        show m2f_p1br
    elif rnd == 7:
        scene m1f_p1br_bg
        show m1f_p1br
    elif rnd == 8:
        scene mhal_2cr
    elif rnd == 9:
        scene garden_1cr
    elif rnd == 10:
        scene garden_1ar
    elif rnd == 11:
        scene rose_g1br
    elif rnd == 12:
        scene m_door2
    elif rnd == 13:
        scene m1f_p1c_bg
        show rainback
        show m1f_p1c
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_q_Sample17:
    $ E_MA()
    scene black with None
    $ bgm_mode_rnd_bg_mhal()
    $ renpy.scene()
    $ renpy.show(tmp,at_list=[center])
    $ renpy.show(tmp_bg,at_list=[center])
    with t6
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_hope:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,5)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,8)
    else:
        $ rnd = renpy.random.randint(1,9)
    scene white with t22
    if rnd == 1:
        scene rose_1af
    elif rnd == 2:
#        scene rose_1cf
        scene garden_1cf
    elif rnd == 3:
        scene rose_g1c
    elif rnd == 4:
        scene beach_2a
    elif rnd == 5:
        scene sky_1a
    elif rnd == 6:
        scene garden_se2b
    elif rnd == 7:
        scene garden_seaia
    elif rnd == 8:
        scene garden_se1b
    elif rnd == 9:
        scene sea_3a
    with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return

label bgm_mode_siroikage:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,2)
    elif persistent.UMINEKOEND >= 21 and  persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,4)
    else:
        $ rnd = renpy.random.randint(1,7)
    if rnd == 1:
        scene white with t22
        scene rose_g1bf
        show kan a12_def1 at left
        with t6
    elif rnd == 2:
        scene mlib_1c_bg
        show rainback
        show mlib_1c
        show nat a11_tukare2 at right
        with t6
    elif rnd == 3:
        scene beach_2a
        show kan a13_komaru1 at center
        with t6
    elif rnd == 4:
        scene schf_c2a
        show kan c11_7 at right
        with t6
    elif rnd == 5:
        scene white with t2
        scene se_o1a with t49
    elif rnd == 6:
        scene white with t22
        scene sky_1b with t5
    elif rnd == 7:
        scene white with t2
        scene garden_se2b
        show bea a11_nayamu1 at left
        show kin a11_def1 at right
        with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_u_Sample21:
    $ E_MA()
    scene black with None
    $ bgm_mode_rnd_bg_mhal()
    python:
        while True:
            tmp1 = ("nat " + renpy.random.choice(nat_rnd1[0]) + renpy.random.choice(nat_rnd1[1]))
            if renpy.has_image(tmp1):
                break
    scene black with t22
    $ renpy.scene()
    $ renpy.show(tmp,at_list=[center])
    $ renpy.show(tmp_bg,at_list=[center])
    $ renpy.show(tmp1,at_list=[center])
    with t6
    with Pause(7.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_towering:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,5)
    else:
        $ rnd = renpy.random.randint(1,6)
    scene white with t22
    if rnd == 1:
        scene sky_2b
    elif rnd == 2:
        scene ship_p1a
        show jes b22_odoroki1 at left
        show but b11_warai1 at right
    elif rnd == 3:
        scene ship_s2a
        show layer master at ship_slow
        show hid a21_warai2 at far_left
        show jes a11_warai1 at center
        show but b23_komaru1 at far_right
    elif rnd == 4:
        scene mjes_1af
        show sha a11_tokui1 at left
        show jes a11_aisowarai1 at right
    elif rnd == 5:
        scene mkit_1a_bg
        show mkit_1a
        show goh a11_omakase1 at center
    elif rnd == 6:
        scene beach_2a
        show but b11_warai2 at left
        show jes a23_tereru2 at right
    with t28
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_t_Sample20:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,6)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,10)
    else:
        $ rnd = renpy.random.randint(1,13)
    with Pause(0.4)
    if rnd <= 10:
        scene black with t22
    else:
        scene white with t22
    if rnd <= 3:
        $ bgm_mode_rnd_bg_mhal()
        python:
            while True:
                tmp1 = ("sha " + renpy.random.choice(sha_rnd1[0]) + renpy.random.choice(sha_rnd1[1]))
                if renpy.has_image(tmp1):
                    break
        $ renpy.scene()
        $ renpy.show(tmp,at_list=[center])
        $ renpy.show(tmp_bg,at_list=[center])
        $ renpy.show(tmp1,at_list=[center])
    elif rnd == 4:
        scene mdin_1e
        show but b23_warai1 at left
        show nat a11_warai1 at right
    elif rnd == 5:
        scene m1f_s1a_bg
        show m1f_s1a
        show eva a11_hohoemi1 at far_left
        show jes a11_warai1 at center
        show mar a22_warai2 at far_right
    elif rnd == 6:
        scene m1f_s1ar_bg
        show rainback
        show m1f_s1ar
        show kir a11_warai1 at left
        show rud a13_def1 at right
    elif rnd == 7:
        scene m1f_s1af
        show geo a11_warai1 at left
        show cla a11_akuwarai2 at right
    elif rnd == 8:
        scene cof_1a
        show geo c11_warai1 at left
        show sha c11_hajirai1 at right
    elif rnd == 9:
        scene rose_g1ac
        show geo a11_hohoemi1 at far_left
        show but b11_def2 at center
        show jes a23_def1 at far_right
    elif rnd == 10:
        scene g2f_r1ar_bg
        show rainback
        show g2f_r1ar
        show sha a11_warai2 at far_left
        show jes a11_warai1 at center
        show geo a11_warai1 at far_right
    elif rnd == 11:
        scene car_i3c
        show ep4_car_enj a11_fuman2:
            xpos -(400.0/1920.0)
        show ep4_car_ama a11_def1:
            xpos (400.0/1920.0)
    elif rnd == 12:
        scene m1f_s1cr
        show ros a13_warai1 at left
        show mar a22_warai1 at right
    elif rnd == 13:
        scene schd_p1ar
    with t2
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_sample_u4:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [1,2,3,4]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ xtmp = [1,2,3,4,5,6,7]
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ xtmp = [1,2,3,4,5,6,7,9,10]
    else:
        $ xtmp = [1,2,3,4,5,6,7,9,10,11,12,13]
    if renpy.seen_image('e0301_b'):
        $ xtmp.append(8)
    $ rnd = renpy.random.choice(xtmp)
    if rnd == 1:
        scene white with t22
        $ bgm_mode_rnd_tati_siyounin()
        $ bgm_mode_rnd_bg_mhal()
        $ renpy.scene()
        $ renpy.show(tmp,at_list=[center])
        $ renpy.show(tmp_bg,at_list=[center])
        $ renpy.show(tmp1,at_list=[far_left])
        $ renpy.show(tmp2,at_list=[center])
        $ renpy.show(tmp3,at_list=[far_right],zorder=5)
        with t6
        with Pause(3.0)
    elif rnd >= 2 and rnd <= 4:
        scene black with t22
        scene mlib_1c_bg
        show mlib_1c
        show kin a11_fumu1 at center
        with t6
        with Pause(4.0)
    elif rnd == 5:
        scene black with t25
        scene sta_1a
        show ros a25_ikari2 at center
        show mar a22_naku1 at right
        with t42
        with Pause(4.0)
    elif rnd == 6:
        scene black with t22
        scene sweet1 gray with t22
        with Pause(1.0)
        scene black with t22
        scene rose_1ac
        show mar a22_komaru1 at left
        show kan a11_majime1 at right
        with t26
        with Pause(3.0)
    elif rnd == 7:
        scene black with t22
        scene m1f_p1dr_bg
        show rainback
        show m1f_p1dr
        show kan a11_majime1 at left
        show sha a11_odoroki1 at right
        with t26
        with Pause(3.0)
    elif rnd == 8:
        scene black with t22
        scene e0301_b with t6
        with Pause(4.0)
    elif rnd == 9:
        scene black with t22
        scene mhal_2a_bg
        show rainback
        show mhal_2a
        show hid a12_komaru2 at left
        show ev2 a11_fukigen1 at right
        with t5
        with Pause(3.0)
    elif rnd == 10:
        scene black with t22
        scene mlib_1br_bg
        show rainback
        show mlib_1br
        show kin a11_fukigen1 at right
        with t2
        with Pause(3.0)
    elif rnd == 11:
        scene black with t22
        scene mdin_1e
        show nan a1_komaru3 at far_left
        show rud a12_majime2 at center
        show eva a11_akire1 at far_right
        with t24
        with Pause(4.0)
    elif rnd == 12:
        scene black with t22
        scene garden_r1an_bg
        show rainback
        show garden_r1an
        show geo a11k_majime2k at left
        show gap a11_warai2a at right
        with t6
        with Pause(3.0)
    elif rnd == 13:
        scene black with t22
        scene hill_1b
        show kas a11_komaru1 at left
        show enj a11_fuman2 at right
        with t6
        with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_rinnsi:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,4)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,6)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,10)
    else:
        $ rnd = renpy.random.randint(1,11)
    scene black with t22
    if rnd == 1:
        show portrait1:
            xalign 0.5 ypos -(2108.0/1080.0)
            linear 12.36 ypos -(143.0/1080.0)
        with Pause(12.36)
        with Pause(3.0)
    elif rnd == 2:
        $ bgm_mode_rnd_tati_4kyoudai()
        scene m1f_s1a_bg
        show rainback
        show m1f_s1a
        $ renpy.show(tmp1,at_list=[far_left])
        $ renpy.show(tmp2,at_list=[center])
        $ renpy.show(tmp3,at_list=[far_right],zorder=5)
        with t2
    elif rnd == 3:
        scene m1f_s1a_bg
        show rainback
        show m1f_s1a
        show but b11_nayamu1 at far_left
        show jes a11_nayamu1 at center
        show geo a11k_majime3k at far_right
        with t6
    elif rnd == 4:
        scene m1f_p1dr_bg
        show rainback
        show m1f_p1dr
        show gen a11_majime1 at far_left
#        show gen a11_komaru1 at far_left
        show geo a11k_majime2k at center
        show jes a11_odoroki1 at far_right
        with t2
    elif rnd == 5:
        show bea b14_akuwarai3 at center with t2
    elif rnd == 6:
        scene mcou_1an
        show rainback
        show gen a11_komaru1 dark at left
        show ros a14_komaru1 dark at right
        show rainfront
        with t6
    elif rnd == 7:
        scene mhal_2a_bg
        show rainback
        show mhal_2a
        show rud a14_warai1 at left
        show hid a12_aseri1 at right
        with t23
    elif rnd == 8:
        scene g1f_p1c
        show cla a15_komaru1 at left
        show eva b24_komaru4 at right
        with t24
    elif rnd == 9:
        scene number with t2
    elif rnd == 10:
        $ me1(me13)
        scene g_o1cr
        show rainback
        show rainfront
        with t26
    elif rnd == 11:
        scene warehous_i1ar2_bg
        show rainback
        show warehous_i1ar2
        show goh a11_komaru2 at far_left
        show kum a11_odoroki1 at center
        show geo a11_komaru1 at far_right
        with t26
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    if rnd == 1:
        scene portrait1:
            xalign 0.5 ypos -(143.0/1080.0)
    call bgm_jump
    return
    
label bgm_mode_rennsakairou:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,10)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,15)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,17)
    else:
        $ rnd = renpy.random.randint(1,19)
    scene black with t22
    if rnd == 1 or rnd == 9:
        scene m1f_p1dr_bg
        show rainback
        show m1f_p1dr
        if rnd == 9:
            show gen a11_komaru1 behind kan at left
            show kan a13_majime1 at right
    elif rnd == 2:
        scene m2f_p1ar_bg
        show rainback
        show m2f_p1ar
    elif rnd == 3:
        scene m1f_p1cr_bg
        show rainback
        show m1f_p1cr
    elif rnd == 4:
        scene m2f_p1br_bg
        show rainback
        show m2f_p1br
    elif rnd == 5:
        scene ment_1br_bg
        show rainback
        show ment_1br
    elif rnd == 6:
        scene mhal_2cr
    elif rnd == 7:
        scene portrait2
    elif rnd == 8:
        scene m1f_s1a_bg
        show m1f_s1a
        show eva a11_majime1 at far_left
        show hid a11_majime1 at center
        show cla a11_akuwarai2 at far_right
    elif rnd == 10:
        scene magicsquare_moon1
    elif rnd == 11:
        scene portrait3
    elif rnd == 12 or rnd == 13:
        scene m2f_r4ar_bg
        show rainback
        show m2f_r4ar
        if rnd == 13:
            show rud a11_komaru1 at left
            show kir a11_nayamu1 at right
    elif rnd == 14:
        scene magicsquare_sun7
    elif rnd == 15:
        scene cha_o2a
        show rainback
        show goh a11_komaru1 at far_left
        show sha a11_komaru1 at center
        show ros a11_majime1 at far_right
        show rainfront
    elif rnd == 16:
        scene rose_1a
        show rainback
        show eva a11_akire1 at left
        show ros a34_ikari4 at right
        show rainfront
    elif rnd == 17:
        scene portrait4
    elif rnd == 18:
        scene pri_i1c
        show pri_i1c_sak
    elif rnd == 19:
        scene g2f_r1ar_bg
        show rainback
        show g2f_r1ar
        show jes a11_nayamu1 at far_left
        show geo a11k_komaru1k at center
        show but b11_majime4 at far_right
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_fortitude:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,6)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,10)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 40:
        $ rnd = renpy.random.randint(1,13)
    elif persistent.UMINEKOEND == 40:
        $ rnd = renpy.random.randint(1,14)
    else:
        $ rnd = renpy.random.randint(1,19)
    if rnd <= 10:
        scene black with t28
    else:
        scene black with t22
    if rnd <= 4:
        $ bgm_mode_rnd_bg_mhal2()
        if rnd == 1:
            $ tmp = 'rose_1a'
            $ tmp_bg = 'tmp_null'
        $ renpy.scene()
        $ renpy.show(tmp,at_list=[center])
        $ renpy.show(tmp_bg,at_list=[center])
    elif rnd == 5:
        scene ment_1br_bg
        show rainback
        show ment_1br
#        show kum a11_komaru1 at far_right
    elif rnd == 6:
        scene m1f_p1cr_bg
        show rainback
        show m1f_p1cr
    elif rnd == 7 or rnd == 8:
        scene garden_1cn
        if rnd == 8:
            show jes a11_nayamu1 dark at far_left
            show kan a11_ikari1 dark at center
    elif rnd == 9:
        $ rnd2 = renpy.random.randint(1,2)
        scene rose_1ac
        if rnd2 == 1:
            show ros a25_ikari3 at center
        elif rnd2 == 2:
            show ros a25_ikari2 at center
            show mar a22_sakebu1 at right
    elif rnd == 10:
        $ rnd2 = renpy.random.randint(1,3)
        scene m1f_s1ar_bg
        show rainback
        show m1f_s1ar
        if rnd2 == 1:
            show but b22_naku1 at center
        elif rnd2 == 2:
            show but b22_naku2 at center
        elif rnd2 == 3:
            show but b22_naku3 at center
    elif rnd == 11:
        scene ship_s3a
        show hid a11_fumu1 at left
        show eva a11_komaru1 at right
    elif rnd == 12:
        scene g1f_p1c
        show mar a22_sakebu1 at left
        show ros a11_komaru4 at right
    elif rnd == 13:
        scene glob_1ar_bg
        show rainback
        show glob_1ar
        show cla a15_komaru1 at left
        show nat a11_tukare1 at right
        with t3
    elif rnd == 14:
        scene hos_r1am
        show enj a21_fuman1 at center
        with t4
    elif rnd == 15:
        scene moon_2a with t2
    elif rnd == 16:
        scene schr_o2a
        show enj c11_komaru2
    elif rnd == 17:
        scene ros_o1an
        show mar c23_naku1 dark at center
        show sak a11_odoroki1 dark behind mar at far_left
        with t3
    elif rnd == 18:
        scene ros_p1ar
        show mar c21_sakebu1 at far_left
        show sak a21_naku1 at center
        show ros c11_ikari3 at far_left
        with t3
    elif rnd == 19:
        scene different_spiral_1a gray
        show eva b32 gray at center
        show ev2 a11_akuwarai8 gray at right:
            alpha (135.0/255.0)
        with t8
    if rnd <= 12 or rnd == 16:
        with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_witch_cenba:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,9)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,11)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,14)
    else:
        $ rnd = renpy.random.randint(1,16)
    scene black with t22
    if rnd == 1:
        scene g_o1an
    elif rnd == 2:
        scene g_o1cn
    elif rnd == 3:
        scene m_o1ar
    elif rnd == 4:
        scene m_o1bn
    elif rnd == 5:
        scene mlib_1ar_bg
        show rainback
        show mlib_1ar
    elif rnd == 6:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
    elif rnd == 7:
        scene mlib_1br_bg
        show rainback
        show mlib_1br
    elif rnd == 8:
        scene gold1
    elif rnd == 9:
        scene mboi_1a
        show mar a22_akuwarai2 boi at left
        show but b11_nayamu1 boi at right
    elif rnd == 10:
        scene mlib_1c_bg
        show mlib_1c
        show kin a11_fukigen1 at right
    elif rnd == 11:
        scene mhal_1ar_bg
        show rainback
        show mhal_1ar
        show ros a11_majime1 at center
        show mar a11_majime1 at far_right
    elif rnd == 12:
        scene rose_1ar
        show rainback
        show mar a22_odoroki1 dark at center
        show bea a12_def2 dark at far_right
        show rainfront
    elif rnd == 13:
        scene mdin_1cr_bg
        show rainback
        show mdin_1cr
        show ros a11_nayamu1 at center
        show rud a13_odoroki1 at far_right
    elif rnd == 14:
        scene garden_se2b
        show bea a11_nayamu1 at center
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_komaru1 at right
        show ron a11_majime1 at left
    elif rnd == 15:
        scene mlib_1ar_bg
        show rainback
        show mlib_1ar
        show wal a11_komaru1 at right
        show gap a11_ikari1a at far_left:
            alpha (125.0/255.0)
    elif rnd == 16:
        scene mlib_1er
    if rnd <= 4:
        $ me1v(me12,0.7)
        show rainback
        show rainfront
    with t22
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_sasoi:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 12:
        $ rnd = renpy.random.randint(1,11)
    elif persistent.UMINEKOEND >= 12 and persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,12)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,15)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,19)
    else:
        $ rnd = renpy.random.randint(1,21)
    scene black with t22
    if rnd == 1:
        scene g_o1an
    elif rnd == 2:
        scene g_o1cn
    elif rnd == 3:
        scene m_o1ar
    elif rnd == 4:
        scene m_o1bn
    elif rnd == 5:
        scene mdin_1fr
    elif rnd == 6:
        scene m2f_p1br_bg
        show rainback
        show m2f_p1br
    elif rnd == 7:
        scene m1f_p1br_bg
        show rainback
        show m1f_p1br
    elif rnd == 8:
        scene mhal_2cr
    elif rnd == 9:
        scene m1f_p1dr_bg
        show rainback
        show m1f_p1dr
    elif rnd == 10:
        scene m1f_s1c
        show mat a22_def1 at left
        show jes b21_ikari2 at right
    elif rnd == 11:
        scene mlib_1er
    elif rnd == 12:
        scene g1f_s1a
        show kan a13_def1 at left
        show but b23_odoroki2 at right
    elif rnd == 13:
        scene cha_i1d_bg
        show rainback
        show cha_i1d
        show kan a11_def2 dark at right
    elif rnd == 14:
        scene pumpkin2
    elif rnd == 15:
        if renpy.seen_image('g0201'):
            $ rnd2 = renpy.random.randint(1,2)
        else:
            $ rnd2 = 2
        if rnd2 == 1:
            scene g0201
        else:
            scene m1f_s1a_bg
            show rainback
            show m1f_s1a
            show ros a11_ikari3 at left
    elif rnd == 16:
        scene mdin_1ar
        show rud a11_nayamu1 at left
        show kir a13_majime1 at right
    elif rnd == 17:
        scene mdin_1ar
        show eva b21_akire2b at center
    elif rnd == 18:
        scene text012_r
    elif rnd == 19:
        scene glob_1a_bg
        show rainback
        show glob_1a
        show rud a11_warai1 at left
        show nat a11_majime1 at right
    elif rnd == 20:
        scene letter1
    elif rnd == 21:
        scene nan_r1c
    if rnd <= 4:
        $ me1v(me12,0.7)
        $ me2v(me05,0.7)
        show rainback
        show rainfront
    with t22
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_yomiage:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [1,3]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 30:
        $ xtmp = [1,3,4,5,6,7]
    elif persistent.UMINEKOEND == 30:
        $ xtmp = [1,3,4,5,6,7,8]
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ xtmp = [1,3,4,5,6,7,8,9,10]
    else:
        $ xtmp = [1,3,4,5,6,7,8,9,10,11,12,13,14,15]
    if renpy.seen_image('c0101_c'):
        $ xtmp.append(2)
    $ rnd = renpy.random.choice(xtmp)
    if rnd == 1:
        $ bgm_mode_rnd_yomiage()
        $ rnd2 = renpy.random.randint(1,3)
        if rnd2 == 1:
            $ tmp = 'mdin_1ar'
        elif rnd2 == 2:
            $ tmp = 'mdin_1er'
        elif rnd2 == 3:
            $ tmp = 'mdin_1fr'
    elif rnd == 10:
        $ bgm_mode_rnd_yomiage2()
        $ rnd2 = renpy.random.randint(1,3)
        if rnd2 == 1:
            $ tmp = 'different_spiral_1a'
        elif rnd2 == 2:
            $ tmp = 'g1f_s1ap'
        elif rnd2 == 3:
            $ tmp = 'g1f_s1bp'
    if rnd == 2 or rnd == 3 or rnd == 6 or rnd == 7 or rnd == 8:
        scene black with t22
    else:
        scene white with t22
    if rnd == 1 or rnd == 10:
        $ renpy.scene()
        $ renpy.show(tmp,at_list=[center])
        $ renpy.show(tmp1,at_list=[far_left])
        $ renpy.show(tmp2,at_list=[center])
        $ renpy.show(tmp3,at_list=[far_right],zorder=5)
    elif rnd == 2:
        scene c0101_c
    elif rnd == 3:
        scene m1f_s1a_bg
        show rainback
        show m1f_s1a
        show mar a22_akuwarai2 at right
    elif rnd == 4:
        scene mhal_2cr
        show bea a11_def1 at center
    elif rnd == 5:
        scene mhal_2a_bg
        show mhal_2a
        show kir a11_majime1 at left
        show bea b11_def2 at right
    elif rnd == 6:
        scene g1f_s1bp
        show bea a31_warai1 at center
    elif rnd == 7:
        scene mjes_1a_bg
        show rainback
        show mjes_1a
        show goh a12_iiwake2 at far_left
        show geo a11_ikari2 at center
        show ros a14_ikari3 at far_right
    elif rnd == 8:
        scene different_space_1a
    elif rnd == 9:
        scene black
        show hana1:
            alpha (180.0/255.0)
        show bea a11_warai2 at far_right
        show ron a11_def1 at center
        show but b11_kuyasigaru1 at far_left
    elif rnd == 11:
        scene mdin_1g_bg
        show mdin_1g
    elif rnd == 12:
        scene mlib_1e
    elif rnd == 13:
        scene different_space_p1a
        show rg5 b11_akuwarai1 at center:
            additive 1.0
        show enj a11_def1 at far_right
        show lam a11_akuwarai3 at far_left
    elif rnd == 14:
        scene mjes_1cr_bg
        show rainback
        show mjes_1cr
        show jes a11_odoroki1 at right
        show ron a11_akuwarai1 behind jes at left
    elif rnd == 15:
        scene ep4_meta_1
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_kuyasigaru1 at right
        show bea a11_majime4 at left
    with t26
    if rnd == 8:
        with Pause(0.3)
        scene white with None
        with Pause(0.03)
        scene different_space_1a
        show lam a11_akuwarai4 at left
        with t2
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_stupefaction:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,7)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,10)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,12)
    else:
        $ rnd = renpy.random.randint(1,15)
    scene black with t22
    if rnd == 1:
        scene m1f_p1dr_bg
        show rainback
        show m1f_p1dr
    elif rnd == 2:
        $ rnd2 = renpy.random.randint(1,2)
        if rnd2 == 1:
            scene m2f_p1ar_bg
            show rainback
            show m2f_p1ar
        elif rnd2 == 2:
            scene m2f_p1br_bg
            show rainback
            show m2f_p1br
    elif rnd == 3:
        $ me1v(me13,0.4)
        scene m1f_p1br_bg
        show rainback
        show m1f_p1br
    elif rnd == 4:
        scene m1f_s1cr
        show kir a27_majime1 at left
        show but b22_komaru2 at right
    elif rnd == 5:
        $ rnd2 = renpy.random.randint(1,2)
        scene warehous_i1c_bg
        show rainback
        show warehous_i1c
        show hid a11_majime1 at left
        if rnd2 == 1:
            show nat a12_zutuu1 at right
        elif rnd2 == 2:
            show eva a11_majime1 at right
    elif rnd == 6:
        show mar a22_def1k dark at center
    elif rnd == 7:
        scene mkit_1c
        show mar a11_akuwarai2 at left
        show but b22_majime1 at right
    elif rnd == 8:
        scene mhal_2cr
        show mar a22_warai1 at left
        show ros a11_komaru4 at right
    elif rnd == 9 or rnd == 10:
        scene portrait3
        if rnd == 10:
            show black:
                alpha (150.0/255.0)
            show hana1:
                alpha (180.0/255.0)
            show bea a11_futeki1 at right
            show but b23_nayamu1 at left
    elif rnd == 11:
        scene mdin_1cr_bg
        show rainback
        show mdin_1cr
        show kir a11_warai1 at left
        show mar a22_warai2 at right
    elif rnd == 12:
        scene rose_g1ar
        show rainback
        show rainfront
        show barrier
        show s45 a11_majime1 at right
    elif rnd == 13:
        scene pri_i1a
        show pri_i1a_sak
        show kir a11_komaru2 dark at center
    elif rnd == 14:
        scene number
    elif rnd == 15:
        scene blood_2e
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_h_sample8:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    if rnd == 1:
        $ tmp_bg = 'garden_r1an_bg'
        $ tmp = 'garden_r1an'
        $ rand = renpy.random.randint(1,6)
        $ ran2 = renpy.random.randint(1,7)
        if rand == 1:
            $ tmp1 = 'sha a11_warai1'
        elif rand == 2:
            $ tmp1 = 'sha a11_warai2'
        elif rand == 3:
            $ tmp1 = 'sha a21_warai2'
        elif rand == 4:
            $ tmp1 = 'sha a11_hajirai1'
        elif rand == 5:
            $ tmp1 = 'sha a11_hajirai2'
        elif rand == 6:
            $ tmp1 = 'sha a11_hajirai3'
        if ran2 == 1:
            $ tmp2 = 'geo a21_def1'
        elif ran2 == 2:
            $ tmp2 = 'geo a21k_def1k'
        elif ran2 == 3:
            $ tmp2 = 'geo a11_hohoemi1'
        elif ran2 == 4:
            $ tmp2 = 'geo a11k_hohoemi1k'
        elif ran2 == 5:
            $ tmp2 = 'geo a11_warai1'
        elif ran2 == 6:
            $ tmp2 = 'geo a11k_warai1k'
        elif ran2 == 7:
            $ tmp2 = 'geo b11_warai2'
    elif rnd == 2:
        $ ran2 = renpy.random.randint(1,4)
        if ran2 == 1:
            $ tmp = 'aqu_i1a'
            $ tmp_bg = 'tmp_null'
        elif ran2 == 2:
            $ tmp = 'aqu_i2a'
            $ tmp_bg = 'tmp_null'
        elif ran2 == 3:
            $ tmp = 'aqu_i2b'
            $ tmp_bg = 'tmp_null'
        elif ran2 == 4:
            $ tmp = 'o_beach_1ac'
            $ tmp_bg = 'tmp_null'
        $ rand = renpy.random.randint(1,5)
        $ ran2 = renpy.random.randint(1,11)
        if rand == 1:
            $ tmp2 = 'sha c11_warai1'
        elif rand == 2:
            $ tmp2 = 'sha c11_warai2'
        elif rand == 3:
            $ tmp2 = 'sha c11_hajirai1'
        elif rand == 4:
            $ tmp2 = 'sha c11_hajirai1'
        elif rand == 5:
            $ tmp2 = 'sha c11_hajirai2'
        if ran2 == 1:
            $ tmp1 = 'geo c21_def1'
        elif ran2 == 2:
            $ tmp1 = 'geo c21k_def1k'
        elif ran2 == 3:
            $ tmp1 = 'geo c11_hohoemi1'
        elif ran2 == 4:
            $ tmp1 = 'geo c11k_hohoemi1k'
        elif ran2 == 5:
            $ tmp1 = 'geo c11_warai1'
        elif ran2 == 6:
            $ tmp1 = 'geo c11k_warai1k'
        elif ran2 == 7:
            $ tmp1 = 'geo c23_def1'
        elif ran2 == 8:
            $ tmp1 = 'geo c11_komaru3'
        elif ran2 == 9:
            $ tmp1 = 'geo c11k_komaru3k'
        elif ran2 == 10:
            $ tmp1 = 'geo c21_komaru5'
        elif ran2 == 11:
            $ tmp1 = 'geo c21k_komaru5k'
    if rnd == 1 or rnd == 2:
        scene white with t22
        $ renpy.scene()
        $ renpy.show(tmp_bg,at_list=[center])
        if rnd == 1:
            show rainback
        $ renpy.show(tmp,at_list=[center])
        $ renpy.show(tmp1,at_list=[left])
        $ renpy.show(tmp2,at_list=[right],zorder=4)
        with t8
    elif rnd == 3:
        scene black with t22
        scene garden_1cn
        show rainback
        show sha a11_hajirai2 dark at left
        show geo a11k_warai1k dark at right
        show rainfront
        with t22
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_c_sample3:
    $ E_MA()
    scene black with None
    $ xtmp = [3,4,5,6,7,8]
    if renpy.seen_image('e0104_a'):
        $ xtmp.append(1)
    if renpy.seen_image('e0104_b'):
        $ xtmp.append(2)
    if renpy.seen_image('e0104_c'):
        $ xtmp.append(3)
    if renpy.seen_image('e0104_d'):
        $ xtmp.append(4)
    $ rnd = renpy.random.choice(xtmp)
    scene white with t22
    if rnd == 1:
        scene e0104_a with t8
    elif rnd == 2:
        scene e0104_b with t8
    elif rnd == 3:
        scene e0104_c with t8
    elif rnd == 4:
        scene e0104_d with t8
    elif rnd >= 5:
        scene garden_r1an_bg
        show rainback
        show garden_r1an
        show sha a11_hajirai1 at left
        show geo a11_majime2 at right
        with t8
        show sha a12_hajirai3
        show geo a11_hohoemi1
        with t22
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    if rnd >= 5:
        show sha a12_hajirai3 at left
        show geo a11_hohoemi1 at right
    call bgm_jump
    return
    
label bgm_mode_sample_u5:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    scene mhal_2cr
    with t6
    with Pause(70.0)
    if rnd == 1 or rnd == 3:
        scene portrait2
        if rnd == 3:
            show bea a11_akuwarai1 at right
        with t8
    else:
        scene portrait3 with t2
    with Pause(18.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_goldenslaughterer:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [1]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ xtmp = [1,4]
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ xtmp = [1,4,5,6]
    else:
        $ xtmp = [1,4,5,6,7,8,9,10]
    if not renpy.seen_image('g0102'):
        $ xtmp.append(2)
    if not renpy.seen_image('g0103'):
        $ xtmp.append(3)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene warehous_o2a
        show nat a32_odoroki2 at left
        show jes a11_ikari1 at right
        with t28
        with Pause(3.0)
    elif rnd == 2:
        scene g0102 with t46
        with Pause(2.0)
    elif rnd == 3:
        scene g0103:
            xpos 0.0
            pause 0.4
            linear 27.0 xalign 1.0
        with t22
#        with t46
        with Pause(27.0)
        with Pause(4.0)
    elif rnd == 4:
        scene pumpkin2 with t22
        with Pause(3.0)
    elif rnd == 5:
        $ rnd2 = renpy.random.randint(1,2)
        scene blood_2e
        if rnd2 == 1:
            show black:
                alpha (150.0/255.0)
            show hana1:
                alpha (180.0/255.0)
            show bea a11_akuwarai3 at center
        with t28
        with Pause(3.0)
    elif rnd == 6:
        scene g1f_s1ap
        show but b22_kuyasigaru1 at left
        with t2
    elif rnd == 7:
        scene schr_r1ar
        show different_spiral_1a:
            alpha (128.0/255.0)
        show enj c11_ikari2 at center
        with t5
    elif rnd == 8:
        scene blood_1ar with t22
    elif rnd == 9:
        show homing6r with t26
    elif rnd == 10:
        show enj b21_naku2 at center with t2
        with Pause(1.0)
        scene red_b with ImageDissolve("efe/blood_2a_efe.png", 4.0, 256, reverse=True)
        scene black with None
        with Pause(0.03)
        scene blood_2e with None
    with Pause(1.0)
    $ renpy.pause(0.001, hard=True)
    if rnd == 3:
        scene g0103:
            xalign 1.0
    call bgm_jump
    return
    
label bgm_mode_worldend_solo:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,5)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,7)
    elif persistent.UMINEKOEND == 41:
        $ rnd = renpy.random.randint(1,9)
    else:
        $ rnd = renpy.random.randint(1,10)
    scene black with t22
    if rnd == 1 or rnd == 2:
#        $ rand = renpy.random.randint(1,2)
        scene warehous_i1c_bg
        show rainback
        show warehous_i1c
        if rnd == 1:
            show geo a21k_naki2k at right
        else:
            show kan b32_nayamu1 at center
        with t6
    elif rnd == 3:
        scene rose_g1c sepia
        show jes a11_warai1 sepia at left
        show sha a11_odoroki2 sepia at right    ## odoroki1? as well as in episode 1?
        with t6
    elif rnd == 4:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show nan a1_fumu1 at left
        show kin a11_warai2 at right
        with t4
    elif rnd == 5:
        scene ment_1br_bg
        show rainback
        show ment_1br
        show sha a11_tokui1 at left
        show kan a11_majime1 at right
        with t3
    elif rnd == 6:
        scene g1f_r2a_bg
        show rainback
        show g1f_r2a
        show hid a11_odayaka1 at right
        with t24
    elif rnd == 7:
        scene mhal_2c
        show ev2 a11_odoroki2 at center
        show hid a11_komaru2 at right
        with t23
    elif rnd == 8:
        scene kaw_r3bn
        show enj a11_nayamu1 at left
        show kaw a12_nayamu1 at right
        with t23
    elif rnd == 9:
        scene gdin_1ad2 sepia
        show kir a11_warai2 sepia at right
        with t22
    elif rnd == 10:
        if renpy.seen_image('no45_00150'):
            $ rand = renpy.random.randint(1,2)
        else:
            $ rand = 2
        if rand == 1:
            scene no45_00150
        else:
            scene bullet_1e
        with t2
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    if rnd == 3:
        show sha a11_tokui1 sepia
    call bgm_jump
    return
    
label bgm_mode_eganomajo:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [1,2,3]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ xtmp = [1,2,3,4,5]
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ xtmp = [1,2,3,4,5,6]
    else:
        $ xtmp = [1,2,3,4,5,6,7,8]
    if renpy.seen_image('g0401'):
        $ xtmp.append(9)
    if renpy.seen_image('g0402'):
        $ xtmp.append(10)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene m1f_s1c
        show hid a11_majime1 at left
        show eva b21_ikari2 at right
    elif rnd == 2:
        scene mkit_1c
        show gen a11_def1:
            xpos (240.0/1920.0)
        show mar a22_akuwarai2:
            xpos (720.0/1920.0)
        show kan a11_def1:
            xpos (1200.0/1920.0)
        show kum a11_majime1:
            xpos (1680.0/1920.0)
    elif rnd == 3:
        scene m1f_s1ar_bg
        show rainback
        show m1f_s1ar
        show but b22_nayamu1 at far_left
        show jes a11_nayamu1 at center
        show geo a11_majime3 at far_right
    elif rnd == 4:
        scene g2f_r1ar_bg
        show rainback
        show g2f_r1ar
        show but b22_komaru2 at left
        show mar a22_akuwarai2 at right
    elif rnd == 5:
        scene forest_p1b
        show rainback
        show goh a11_komaru2 at left
        show sha a11_komaru1 at right
        show rainfront
    elif rnd == 6:
        scene mdin_1cr_bg
        show rainback
        show mdin_1cr
        show nat a21_odoroki2 at far_right
        show ros a11_komaru4 at center
        show rud a11_akuwarai2 at far_right
    elif rnd == 7:
        scene pri_i1a
        show pri_i1a_sak
        show kir a13_majime1 dark at left
        show cla a11_komaru1 dark at right
        with t22
    elif rnd == 8:
        scene mjes_1e gray with t9
    elif rnd == 9:
        scene g0401 with t5
    elif rnd == 10:
        scene g0402 with t5
    if rnd <= 6:
        with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_suspicion:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,2)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,4)
    else:
        $ rnd = renpy.random.randint(1,8)
    scene black with t22
    if rnd == 1:
        scene m1f_s1d
    elif rnd == 2:
        scene m1f_s1c
        show but b11_majime1 at right
    elif rnd == 3:
        scene cha_i1a_bg gray
        show rainback static
        show cha_i1a gray
    elif rnd == 4:
        scene cha_o2a
        show rainback
        show but b11_nayamu1 at far_left
        show mar a11_uu1 at center
        show ros a11_majime1 at far_right
        show rainfront
    elif rnd == 5:
        scene mdin_1er
        show cla a11_nayamu1 at far_left
        show rud a12_majime2 at center
        show eva a11_majime1 at far_right
    elif rnd == 6:
        scene chess1
    elif rnd == 7:
        scene g1f_s1bp
        show but b22_odoroki1 at center
    elif rnd == 8:
        scene g1f_p1c
        show hid a11_komaru2 at far_left
        show ros a11_komaru3 at center
        show kir a11_komaru1 at far_right
    with t22
    with Pause(1.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_kizuoto:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,4)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,5)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,7)
    else:
        $ rnd = renpy.random.randint(1,9)
    scene black with t22
    if rnd == 1:
        scene m1f_s1c
        show eva a11_akire1 at left
        show but b22_komaru2 at right
    elif rnd == 2:
        $ rnd2 = renpy.random.randint(1,2)
        if rnd2 == 1:
            scene m1f_s1ar_bg
            show rainback
            show m1f_s1ar
            show nat a26_majime1 at center
        else:
            scene m1f_s1a_bg
            show rainback
            show m1f_s1a
            show nat a16_majime1 at center
    elif rnd == 3:
        scene m1f_s1c
        show eva a11_akire1 at left
        show nat a26_odoroki2 at right
    elif rnd == 4:
        scene warehous_i1er
    elif rnd == 5:
        scene map05
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_majime1 at right
        show bea a11_akuwarai1 at left
    elif rnd == 6:
        scene letter1 with t26
    elif rnd == 7:
        scene mkit_1a_bg
        show rainback
        show mkit_1a
        show kir a13_majime1 at left
        show rud a14_komaru1 at right
        with t6
    elif rnd == 8:
        scene mdin_1f
        show kir a11_majime1 at left
        show rud a22_majime2 at right
        with t22
    elif rnd == 9:
        if renpy.seen_image('e0406'):
            $ rnd2 = renpy.random.randint(1,2)
        else:
            $ rnd2 = 1
        if rnd2 == 1:
            scene m_o1an
            show rainback
            show rainfront
        elif rnd2 == 2:
            scene e0406
        with t2
    if rnd <= 5:
        with t28
    with Pause(1.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_toitume:
    $ E_MA()
    scene black with None
    $ xtmp = [1,2,3,4]
    if persistent.UMINEKOEND >= 31:
        $ xtmp.append(6)
    if renpy.seen_image('e0103 a') or renpy.seen_image('c_e0103_la'):
        $ xtmp.append(5)
        if persistent.UMINEKOEND >= 31:
            $ xtmp.append(7)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        show but b22_nayamu2 at right with t3
    elif rnd == 2:
        show kir a27_futeki1 at left with t4
    elif rnd == 3:
        scene mkit_1a_bg
        show rainback
        show mkit_1a
        show but b24_futeki3 at right with t6
    elif rnd == 4 or rnd == 5:
        scene m1f_s1a_bg
        show rainback
        show m1f_s1a
        show eva a11_ikari2 at left
        show but b22_odoroki1 at right
        if rnd == 5:
            show e0103_wall
            show e0103 a
        with t5
    elif rnd == 6 or rnd == 7:
        scene g1f_s1ap
        if rnd == 6:
            show but b25_odoroki1 at center
        elif rnd == 7:
            show e0103_wall
            show e0103 a
        with t23
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_m_darkness:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,4)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 42:
        $ rnd = renpy.random.randint(1,6)
    else:
        if renpy.seen_image('g0404'):
            $ rnd = renpy.random.randint(1,8)
        else:
            $ rnd = renpy.random.randint(1,7)
    scene black with t22
    if rnd == 1:
        scene m1f_s1ar_bg
        show rainback
        show m1f_s1ar
        show but b22_nayamu1 at far_left
        show jes a11_nayamu1 at center
        show geo a11_majime3 at far_right
    elif rnd == 2:
        scene mkit_1a_bg
        show rainback
        show mkit_1a
        show gen a11_majime1 at left
        show kan a13_majime1 at right
    elif rnd == 3:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show gen a11_komaru1 at far_left
        show kum a12_majime1 at center
        show nan a1_komaru3 at far_right
    elif rnd == 4:
        scene garden_r1an_bg
        show rainback
        show garden_r1an
        show geo a11k_majime2k at left
        show sha a11_majime1 at right
    elif rnd == 5:
        scene glob_1a_bg
        show rainback
        show glob_1a
        show ros a11_komaru4 at left
        show rud a11_nayamu1 at right
    elif rnd == 6:
        scene glob_1d_bg
        show rainback
        show glob_1d
        show nat a11_majime1 at far_left
        show kir a11_def1 at center
        show eva a11_majime1 at far_right
    elif rnd == 7:
        scene well_1ar
        show rainback
        show rainfront
    elif rnd == 8:
        scene g0404
    with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_m_u2_tipica1:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [2]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ xtmp = [2,3]
    else:
        $ xtmp = [2,3,4,5]
    if renpy.seen_image('e0101 c') and renpy.seen_image('e0102 a'):
        $ xtmp.append(1)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene m1f_s1a_bg
        show m1f_s1a
        with t26
        show e0101_wall:
            xpos 1.0 ypos 1.0
            linear 0.5 xpos 0.0 ypos 0.0
        show e0102_wall:
            xpos -1.0 ypos -1.0
            linear 0.5 xpos 0.0 ypos 0.0
        show e0101 c:
            xpos 1.0 ypos 1.0
            linear 0.5 xpos 0.0 ypos 0.0
        show e0102 a:
            xpos -1.0 ypos -1.0
            linear 0.5 xpos 0.0 ypos 0.0
        with Pause(0.5)
    elif rnd == 2:
        scene m1f_s1a_bg
        show rainback
        show m1f_s1a
        show eva a11_futeki1 at left
        show nat a12_ikari1 at right
        with t26
    elif rnd == 3:
        scene m1f_s1ar_bg
        show rainback
        show m1f_s1ar
        show ros ros a14_ikari3 at left
        show but b22_odoroki2 at right
        with t26
    elif rnd == 4:
        scene mlib_1br_bg
        show rainback
        show mlib_1br
        show rg7 a12_hohoemi1:
            xpos (212.0/1920.0)
        show rg6 a12_akuwarai1:
            xpos (552.0/1920.0)
        show rg5 a12_akuwarai2:
            xpos (812.0/1920.0)
        show rg4 a12_akuwarai1:
            xpos (1108.0/1920.0)
        show rg3 a12_fuman1:
            xpos (1368.0/1920.0)
        show rg2 a12_hohoemi1:
            xpos (1708.0/1920.0)
        with t26
    elif rnd == 5:
        scene white with None
        with Pause(0.03)
        scene system1 with t80
        scene white with None
        with Pause(0.03)
        scene system2 with t80
        scene white with None
        with Pause(0.03)
        scene system3 with t80
        scene white with None
        with Pause(0.03)
        scene system4 with t80
        scene white with None
        with Pause(0.03)
        scene system5
        if renpy.seen_image('c_e0305_a'):
            with t80
            scene white with None
            with Pause(0.03)
            scene c_e0305_a:
                ypos -(400.0/1080.0)
        with t22
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_closed_My_Heart:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,5)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,7)
    else:
        $ rnd = renpy.random.randint(1,9)
    scene black with t22
    if rnd == 1:
        scene mhal_2ar_bg
        show rainback
        show mhal_2ar
    elif rnd == 2:
        scene m1f_p1br_bg
        show rainback
        show m1f_p1br
        show kan a11_odoroki1 at left
        show kum a11_komaru1 at right
    elif rnd == 3:
        scene m_door1k
        show nat a16_majime1 at far_left
        show but b22_odoroki1 at center
        show geo a11k_majime2k at far_right
    elif rnd == 4:
        scene m1f_r1a_bg
        show rainback
        show m1f_r1a
        show ka2 a13_3 at center
    elif rnd == 5:
        scene magicsquare_mars3
    elif rnd == 6:
        scene g1f_s1bp
        show but b22_niramu1 at left
        show bea a11_fukigen1 at right
        with t24
    elif rnd == 7:
        scene g2f_p1ar_bg
        show rainback
        show g2f_p1ar
        show but b11_komaru2 at left
        show nan a1_majime1 at right
        with t26
    elif rnd == 8:
        scene mdin_1a
        show nat a33_odoroki2 at far_left
        show cla a14_akuwarai1 at center
        show kir a25_majime1 at far_right
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_futeki3 at right
        show enj a11_nayamu1 at left
        with t23
    elif rnd == 9:
        scene g1f_s1bp
        show but b11_komaru2 at left
        show enj a11_nayamu1 at right
        with t23
    if rnd <= 5:
        with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_requiem:     ## add scenes from episodes?
    $ E_MA()
    scene black with None
    scene black with t2
    with Pause(5.0)
    scene butterfly_3a with ImageDissolve("title/kannon_r.png", 5.0, 256, reverse=True)
    with Pause(10.0)
    scene black with ImageDissolve("title/kannon_r.png", 5.0, 256, reverse=True)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_mind_2:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,6)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,9)
    else:
        $ rnd = renpy.random.randint(1,11)
    scene black with t22
    if rnd == 1:
#        scene m1f_s1ar_bg gray
#        show rainback static
#        show m1f_s1ar gray
#        show kir a11_majime1 gray at center
        scene gdin_1ad2 gray
        show kir a27_majime1 gray at center
    elif rnd == 2:
        scene chess1 gray
    elif rnd == 3:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show but b22_odoroki1 at left
        show nat a26_majime1 at right
    elif rnd == 4:
        scene m2f_r4ar_bg
        show rainback
        show m2f_r4ar
        show kir a38_majime1 at center
    elif rnd == 5:
        scene cha_o2a
        show rainback
        show ros a11_majime1 at far_left
        show geo a11k_komaru1k at center
        show but b22_niramu1 at far_right
        show rainfront
    elif rnd == 6:
        scene m1f_s1a_bg
        show rainback
        show m1f_s1a
        show but b11_nayamu2 behind kum at left
        show kum a11_majime1 at right
    elif rnd == 7:
        scene rose_g1ar
        show rainback
        show rainfront
        with t22
    elif rnd == 8:
        scene rose_g1c
        show rainback
        show rud a11_akuwarai1 at left
        show eva a11_hohoemi1 at right
        show rainfront
        with t26
    elif rnd == 9:
        scene g1f_p1c
        show eva a11_odoroki2 at far_left
        show nat a11_majime1 at center
        show cla a11_komaru1 at far_right
        with t26
    elif rnd == 10:
        scene glob_1ar_bg
        show rainback
        show glob_1ar
        show goh a11_iiwake2 at left
        show geo a11k_majime3k at right
        with t24
    elif rnd == 11:
        scene letter1
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show enj a13_fuman2 at far_right
        show rg5 a11_komaru3 at far_left
        with t23
    if rnd <= 6:
        with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_worldend:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,3)
    if rnd == 1:
        scene white with t22
        scene portrait2 with t8
    elif rnd == 2:
        scene black with t22
        scene rose_1ar
        show rainback
        show rainfront
        show bea a31_warai1 dark at right behind rainfront
        with t24
    elif rnd == 3:
        scene black with t22
        scene portrait3 with t22
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
image bgm_tips1_2:
    Text("The one who obtains the key must then travel to the Golden Land in accordance with these rules.\n\nOn the first twilight, offer the six chosen by the key as sacrifices.\nOn the second twilight, those who remain shall tear apart the two who are close.\nOn the third twilight, those who remain shall praise my noble name.\nOn the fourth twilight, gouge the head and kill.\nOn the fifth twilight, gouge the chest and kill.\nOn the sixth twilight, gouge the stomach and kill.\nOn the seventh twilight, gouge the knee and kill.\nOn the eighth twilight, gouge the leg and kill.\nOn the ninth twilight, the witch shall revive, and none shall be left alive.\nOn the tenth twilight, the journey shall end, and you shall reach the capital where the gold dwells.",
    font = "times.ttf", size=40, outlines=[(1, "#000000", 0, 0)] )
    xalign 0.5 yalign 0.5
    size (850,745)
    
label bgm_mode_play:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,2)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        show bgm_tips1_2:
            xpos 0.5 ypos 0.5
    elif rnd == 2:
        scene mkit_1a_bg
        show rainback
        show mkit_1a
        show nan a1_komaru3 at far_left
        show gen a11_majime1 at center
        show goh a11_iiwake2 at far_right
    elif rnd == 3:
        scene blood_1a
        show bea a11_akuwarai1 at right
    elif rnd == 4:
        scene m_door1
        show jes a11_komaru1 at right
    elif rnd == 5:
        scene g2f_r1ar_bg
        show rainback
        show g2f_r1ar
        show but b11_kuyasigaru1 at left
        show mar a22_akuwarai1 at right
    with t6
    with Pause(4.0)
    if rnd == 1:
        with Pause(2.0)
        scene black with t2
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_system0:
    $ E_MA()
    scene black with None
    scene black with t22
    $ xtmp = [2]
    if renpy.seen_image('e0101 c'):
        $ xtmp.append(1)
    if persistent.UMINEKOEND >= 21:
        $ xtmp.append(3)
    if renpy.seen_image('c0205 c'):
        $ xtmp.append(4)
    $ rnd = renpy.random.choice(xtmp)
    if rnd == 1:
        scene mlib_1ar_bg
        show rainback
        show mlib_1ar
        show e0101_wall
        show e0101 c
    elif rnd == 2:
        scene mlib_1ar_bg
        show rainback
        show mlib_1ar
#        show nat a26_zutuu1 at left
        show nat a16_ikari1 at left
        show mar a22_def1 at right
    elif rnd == 3:
        scene m1f_r1a_bg
        show rainback
        show m1f_r1a
        show ros a14_ikari3 at left
        show sha a12_odoroki2 at right
    elif rnd == 4:
        scene m1f_r1a_bg
        show rainback
        show m1f_r1a
        show goh a11_komaru2 at far_right
        show c0205_wall
        show c0205 c
    with t28
    with Pause(30.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_voiceless:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,4)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,8)
    elif persistent.UMINEKOEND == 41:
        $ rnd = renpy.random.randint(1,9)
    else:
        $ rnd = renpy.random.randint(1,10)
    scene black with t22
    if rnd == 1:
        scene mlib_1er
    elif rnd == 2:
        scene garden_1af gray
        show geo a11_hohoemi1 gray at center
    elif rnd == 3:
        scene mkit_1cr
        show geo a11k_majime2k at far_left
        show gen a11_komaru1 at center
        show goh a11_komaru2 at far_right
    elif rnd == 4:
        scene m1f_s1dr
    elif rnd == 5:
        scene g2f_r1ar_bg
        show rainback
        show g2f_r1ar
        show jes a11_atya1 at left
        show geo a11_majime2 at right
    elif rnd == 6:
        scene rose_1a
        show rainback static
        show rainfront static
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_nayamu1 at right
    elif rnd == 7:
        scene glob_1e
    elif rnd == 8:
        scene g1f_s1bp
        show but b11_futeki1 at center
    elif rnd == 9:
        scene garden_1an
        show rainback
        show rainfront
        show but b11_nayamu1 dark behind rainfront at right
    elif rnd == 10:
        scene m_o1an
        show rainback
        show rainfront
    with t6
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_deadangle:       ## add scenes from episodes?
    $ E_MA()
    scene black with None
    scene black with t22
    scene butterfly_1a
    with t44
    with Pause(4.0)
    scene butterfly_3a
    with t44
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_orugann:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,7)
    elif persistent.UMINEKOEND == 31:
        $ rnd = renpy.random.randint(1,11)
    elif persistent.UMINEKOEND >= 32 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,12)
    else:
        $ rnd = renpy.random.randint(1,14)
    scene white with t22
    if rnd == 1:
        if persistent.UMINEKOEND < 20:
            $ rnd2 = 0
        else:
            $ rnd2 = renpy.random.randint(1,2)
        scene g1f_s1a
        if rnd2 == 1:
            scene different_space_1a
            show ber a11_def1 at left
        show bea a11_def1 at right
    elif rnd == 2:
        scene mhal_2ar_bg
        show rainback
        show mhal_2ar
        show sha a11_odoroki1 at left
        show bea a13_warai2 at right
    elif rnd == 3:
        scene rose_1an
        show bea a31_warai1 dark at left
        show kan a11_ikari1 dark at right
    elif rnd == 4:
        scene mvip_1a_bg
        show rainback
        show mvip_1a
        show kan a13_odoroki1 at left
        show bea b11_akuwarai1 at right
    elif rnd == 5:
        scene m1f_p1d_bg
        show rainback
        show m1f_p1d
        show bea b11_akuwarai1 at center
    elif rnd == 6:
        scene mjes_1a_bg
        show rainback
        show mjes_1a
        show butterfly_4sp2r
        show bea a14_akuwarai4 at right
    elif rnd == 7:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_kuyasigaru1 at right
        show bea a11_akuwarai2 at left
    elif rnd == 8:
        scene sky_1b
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b22_kuyasigaru1 at right
        show bea a14_akuwarai3 at left
    elif rnd == 9:
        scene g1f_s1bp
        show butterfly_4sp1
        show bea a21_akuwarai2 at center
    elif rnd == 10:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show bea a21_akuwarai2 at left
        show ron a23_warai2 at right
    elif rnd == 11:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show kan a13_ikari1 at left
        show bea a21_akuwarai5 at right
    elif rnd == 12:
        scene different_space_1a
        show bea a11_fukigen2 at far_left
        show ber a11_def2 at center
        show lam a11_akuwarai1 at far_right
    elif rnd == 13:
        scene g1f_s1ap
        show bea a31_akuwarai5 at center
    elif rnd == 14:
        scene mdin_1ar
        show kin a23_akuwarai2 at center
    with t6
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_rougoku:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 50:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene mhal_2cr
        show bea a14_warai2 at right
        show but b22_odoroki1 behind bea at left
    elif rnd == 2:
        scene m1f_r1a_bg
        show rainback static
        show m1f_r1a
        show ros a34_ikari4 at left
        show but b22_naku1 at right
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a31_akuwarai2 at center
    elif rnd == 3:
        scene sub_r1bp
        show ber a24_akuwarai1:
            xanchor 0 yanchor 0 xpos -(330.0/1920.0) ypos -(45.0/1080.0) zoom 2.0
        show lam b21_akuwarai6:
            xanchor 0 yanchor 0 xpos (800.0/1920.0) ypos -(40.0/1080.0) zoom 2.0
    with t28
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_ed:
    $ E_MA()
    scene black with None
    scene black with t22
    scene end_1b
    with t42
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_gc_01:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 12:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 12 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene g1f_s1a
    elif rnd == 2:
        scene different_space_1a
    elif rnd == 3:
        scene sub_r1a
    with t6
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_cage:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,6)
    else:
        $ rnd = renpy.random.randint(1,10)
    if rnd <= 3 or rnd >= 9:
        scene white with t22
    else:
        scene black with t22
    if rnd == 1:
        scene sky_1a
    elif rnd == 2 or rnd == 3:
        scene garden_1af
        show sha a12_odoroki2 at left
        show jes a11_warai1 at right
        if rnd == 3:
            show sha a11_tokui1
            show jes a11_akuwarai1
    elif rnd == 4:
        scene moon_1bn
    elif rnd == 5 or rnd == 6:
        scene garden_1cn
        if rnd == 6:
            scene garden_1an
            show kan a11_majime1 dark at left
        show jes a23_def1 dark at right
    elif rnd == 7:
        scene cit_3a
        show mar c21_warai2 dark at center
    elif rnd == 8:
        scene moon_2a
    elif rnd == 9:
        scene par_1c
        show rg4 b11_hohoemi1 at far_left
        show rg5 d31_warai1 at center
        show enj c11_warai2 at far_right
    elif rnd == 10:
        scene ship_s2a
        show rg5 d31_hohoemi1 at left
        show enj a11_nayamu1 at right
    with t6
    with Pause(10.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_ougon_no_kage:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 30:
        $ rnd = 1
    elif persistent.UMINEKOEND == 30:
        $ rnd = renpy.random.randint(1,2)
    elif persistent.UMINEKOEND >= 31:
        $ rnd = renpy.random.randint(1,3)
    if rnd == 1:
        $ bgm_mode_rnd_yomiage()
        $ rnd2 = renpy.random.randint(1,3)
        if rnd2 == 1:
            $ tmp_bg = 'tmp_null'
            $ tmp = 'mdin_1ar'
        elif rnd2 == 2:
            $ tmp = 'mdin_1er'
            $ tmp_bg = 'tmp_null'
        elif rnd2 == 3:
            $ tmp = 'mdin_1fr'
            $ tmp_bg = 'tmp_null'
    elif rnd == 3:
        $ bgm_mode_rnd_yomiage2()
        $ rnd2 = renpy.random.randint(1,3)
        if rnd2 == 1:
            $ tmp = 'different_spiral_1a'
            $ tmp_bg = 'tmp_null'
        elif rnd2 == 2:
            $ tmp = 'g1f_s1ap'
            $ tmp_bg = 'tmp_null'
        elif rnd2 == 3:
            $ tmp = 'g1f_s1bp'
            $ tmp_bg = 'tmp_null'
    elif rnd == 2:
        $ bgm_mode_rnd_yomiage3()
        $ rnd2 = renpy.random.randint(1,3)
        if rnd2 == 1:
            $ tmp = 'different_spiral_1a'
            $ tmp_bg = 'tmp_null'
        elif rnd2 == 2:
            $ tmp = 'different_space_1a'
            $ tmp_bg = 'tmp_null'
        elif rnd2 == 3:
            $ tmp = 'different_space_1c'
            $ tmp_bg = 'tmp_null'
    scene white with t22
    $ renpy.scene()
    $ renpy.show(tmp_bg,at_list=[center])
    $ renpy.show(tmp,at_list=[center])
    $ renpy.show(tmp1,at_list=[far_left])
    $ renpy.show(tmp2,at_list=[center])
    $ renpy.show(tmp3,at_list=[far_right],zorder=5)
    with t26
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_sasorinoharawata:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [1]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ xtmp = [1,2,4]
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ xtmp = [1,2,4,5]
    else:
        $ xtmp = [1,2,4,5,6]
    if renpy.seen_image('c0204 a'):
        $ xtmp.append(3)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene mlib_1cr_bg
        show mlib_1cr
        show kin a21_naku1 at center
    elif rnd == 2:
        scene mhal_1ar_bg
        show rainback
        show mhal_1ar
        show butterfly_4sp1r
    elif rnd == 3:
        scene c0204 a:
            yalign 0.0
        show no25_00059:
            additive 1.0
        show ep2_bea a11_futeki2:
            xpos (320.0/1920.0)
    elif rnd == 4:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show butterfly_4sp2r
        show bea b11_futeki1 at center
    elif rnd == 5:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show rg4 a12_fuman1 at far_left
        show rg3 a31_ikari1 at center
        show rg6 c21_akuwarai3 at far_right
    elif rnd == 6:
        scene mdin_1fr
        show kan a12_def2 at far_left
        show gen a11_def1 at far_right
        show kin a11_fukigen1 at center
        with t10
    if rnd < 6:
        with t6
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_sy:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene butterfly_3a
        if renpy.seen_image('goa a11'):
            show goa a11 at center
    elif rnd == 2:
        scene mlib_1br_bg
        show rainback
        show mlib_1br
        show rg1 a21_odoroki1 at center
        show rg7 a12_hohoemi1 behind rg1:
            xpos (210.0/1920.0)
        show rg6 a12_akuwarai1 behind rg1:
            xpos (510.0/1920.0)
        show rg5 a12_akuwarai2 behind rg1:
            xpos (810.0/1920.0)
        show rg4 a12_akuwarai1 behind rg1:
            xpos (1110.0/1920.0)
        show rg3 a12_fuman1 behind rg1:
            xpos (1410.0/1920.0)
        show rg2 a12_hohoemi1 behind rg1:
            xpos (1710.0/1920.0)
    with t6
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_where:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene butterfly_3a
        show goa a11b at right
        show kan a12b_ikari2 at left
    elif rnd == 2:
        scene mlib_1br_bg
        show rainback
        show mlib_1br
        show kan a12b_fuman1 at left
        show rg1 a12b_odoroki1 at right
    with t6
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Answer:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,4)
    scene white with None
    with Pause(0.03)
    if rnd == 1:
        scene g1f_s1bp
        show but b22_odoroki1 at left
        show bea a11_akuwarai1 at right
        with t6
    elif rnd == 2:
        scene g1f_s1bp
        show but b22_odoroki1 at left
        show bea a21_akuwarai5 at right
        with t6
    elif rnd == 3:
        scene g1f_s1ap
        show but b25_odoroki1 at right
        with t24
    elif rnd == 4:
        scene garden_r1an_bg
        show rainback
        show garden_r1an
        show geo a21k_majime4k at left
        show gap a11_warai2a at right
        with t22
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Answer_short:
    $ E_MA()
    scene black with None
    scene white with None
    with Pause(0.03)
    scene chess1
    with t6
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Read_Dread:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = renpy.random.randint(1,4)
    scene white with None
    with Pause(0.03)
    if rnd == 1:
        scene pumpkin2
    elif rnd == 2:
        scene cha_i1ar_bg
        show cha_i1ar
        show butterfly_4sp1
        show sha a11_komaru1 at center
    elif rnd == 3:
        scene cha_i1er
        show butterfly_4sp2r
#        show bea b21_akuwarai2 at center
        show bea b15_akuwarai3 at center
    elif rnd == 4:
        scene mkit_1ar_bg
        show mkit_1ar
        show goh a11_odoroki1 at center
    with t26
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_sirabe_oche:     ## add more from episodes?
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene portrait3 with t6
    elif rnd == 2:
        scene portrait4 with t6
    elif rnd == 3:
        scene air_out2b gray with t48
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Dread_grave:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [7,13]
    elif persistent.UMINEKOEND == 21:
        $ xtmp = [7,13,15]
    elif persistent.UMINEKOEND >= 22 and persistent.UMINEKOEND < 31:
        $ xtmp = [7,13,15,10]
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ xtmp = [7,13,15,10,1,2,3,4,5,6,8,9,11]
    else:
        $ xtmp = [7,13,15,10,1,2,3,4,5,6,8,9,11,12,16]
    if renpy.seen_image('e0103 a'):
        $ xtmp.append(14)
    $ rnd = renpy.random.choice(xtmp)
    scene white with None
    with Pause(0.03)
    if rnd == 1:
        scene m1f_s1a_bg
        show rainback static
        show m1f_s1a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_futeki3 at right
    elif rnd == 13:
        scene key1
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_futeki1 at center
    elif rnd == 14:
        scene map05
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b22_odoroki1 at center
        show e0103_wall
        show e0103 a
        show ep2_meta_1
    elif rnd == 2:
        scene map10
        show bea a11_akuwarai2 at left
        show ron a11_warai2 at right
    elif rnd == 3:
        scene map10
        show bea a11_akuwarai2 at left
    elif rnd == 4:
        scene letter1
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_majime1 at right
    elif rnd == 5:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_komaru2 at left
        show ron a11_def1 at right
    elif rnd == 6:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b22_oya1 at left
        show bea a11_akuwarai1 at right
    elif rnd == 7:
        scene map06
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_odoroki1 at right
    elif rnd == 8:
        scene g1f_s1bp
        show but b22_nayamu2 at left
        show bea a11_futeki1 at right
    elif rnd == 9:
        scene g1f_s1ap
        show but b22_futeki1 at left
        show ron a11_def1 at right
    elif rnd == 15:
        scene mjes_1a_bg
        show rainback
        show mjes_1a
        show ros a11_ikari3 at far_left
        show but b11_nayamu2 at far_right
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_futeki1 as bu2 at right
        show bea a11_futeki1 at left
    elif rnd == 10:
        scene g1f_s1ap
        show but b25_odoroki1 at right
    elif rnd == 11:
        scene map10b
    elif rnd == 12:
        scene black
#        show goa a11:
#            xanchor 0 yanchor 0 xpos -(533.0/1920.0) ypos -(352.0/1080.0) zoom 2.0
        show cla a11_komaru2:
#            xanchor 0 yanchor 0 xpos (756.0/1920.0) ypos -(44.0/1080.0) zoom 2.0
            xanchor 0 yanchor 0 xpos (845.0/1920.0) ypos -(150.0/1080.0) zoom 2.0
        show goa b11:
            xanchor 0 yanchor 0 xpos -(1100.0/1920.0) ypos -(565.0/1080.0) zoom 2.0
    elif rnd == 16:
        scene black
        show kir a25_futeki1:
            xanchor 0 yanchor 0 xpos -(245.0/1920.0) ypos -(80.0/1080.0) zoom 2.0
        show wal a11_komaru1:
            xanchor 0 yanchor 0 xpos (780.0/1920.0) ypos -(255.0/1080.0) zoom 2.0
    with None
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_moon:
    $ E_MA()
    scene black with None
    scene black with t22
    if persistent.UMINEKOEND < 21:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,5)
    else:
        $ rnd = renpy.random.randint(1,7)
    if rnd == 1:
        scene mjes_1a_bg
        show rainback
        show mjes_1a
        show kan a11_majime1 at left
        show jes a11_komaru1 at right
    elif rnd == 2:
        scene mjes_1c_bg
        show rainback
        show mjes_1c
        show kan a11_nayamu1:
            alpha (128.0/255.0)
            xpos (712.0/1920.0)
        show jes a11_naki1:
            alpha (128.0/255.0)
            xpos (1208.0/1920.0)
    elif rnd == 3:
        scene mnat_1ar_bg
        show rainback
        show mnat_1ar
        show butterfly_4sp1
        show barrier
        show sha a11_komaru1 at center
        show geo a21k_def1k behind sha at left
    elif rnd == 4:
        scene mlib_1br_bg
        show rainback
        show mlib_1br
        show sha a11_ikari1 at left
        show kan a11_ikari1 at right
        with t6
    elif rnd == 5:
        scene g1f_p1er
        show bea a11_iiwake1 at center:
            alpha (150.0/255.0)
        with t26
    elif rnd == 6:
        $ rnd2 = renpy.random.randint(1,2)
        scene pri_i1b
        show kir a11_nayamu1 dark at right
        if rnd2 == 2:
            show kir a13_majime1 dark
        show pri_i1a_2_sak
        show kin a11_fukigen1 dark at left
        with t4
    elif rnd == 7:
        scene mjes_1cr_bg
        show rainback
        show mjes_1cr
        show jes a11_majime1 at right
        show ron a11_akuwarai1 behind jes at left
        with t22
    if rnd <= 3:
        with t6
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Worldenddominator:
    $ E_MA()
    scene black with None
    scene black with None
    with Pause(0.03)
#    $ xtmp = [1,2,3,4,5,6,7,8,9,10,11,12]
    $ xtmp = [1,9]
    if renpy.seen_image('c0205 c') and persistent.UMINEKOEND >= 21:
        $ xtmp.extend([2,10,11,12])
    if persistent.UMINEKOEND >= 31:
        $ xtmp.extend([5,7,8,3,6,4])
        if renpy.seen_image('c_c0902_a') or renpy.seen_image('ep3_c0902 2') or renpy.seen_image('ep3_c0902 4') or renpy.seen_image('ep3_c0902_7') or renpy.seen_image('ep3_c0902 8'):
            pass
        else:
            $ xtmp.remove(8)
            $ xtmp.remove(3)
            $ xtmp.remove(6)
        if renpy.seen_image('c_c0901_a') or renpy.seen_image('ep3_c0901 4') or renpy.seen_image('ep3_c0901 5') or renpy.seen_image('c_c0901 ca'):
            pass
        else:
            $ xtmp.remove(4)
            $ xtmp.remove(8)
    $ rnd = renpy.random.choice(xtmp)
    if rnd == 1 or rnd == 9:
        scene m2f_p1br_bg
        show rainback
        show m2f_p1br
        show butterfly_4sp1
        show goa a11 at far_left
        show goa a11 as goa2 at center
        show goa a11 as goa3 at far_right
        show bea b33_futeki1 at center
    elif rnd == 2 or rnd == 10 or rnd == 11 or rnd == 12:
        scene moon_1bn
        show butterfly_4sp1
        show c0205 c
        show mar a11_ikari1 dark at far_right
    elif rnd == 3:
        scene m2f_p1a_bg
        show rainback
        show m2f_p1a
        show rg4 a12b_akuwarai1 at left
        show ep3_c0902 2:
            xpos (240.0/1920.0)
    elif rnd == 4:
        scene c_c0901_a
    elif rnd == 5:
        scene m1f_p1b_bg
        show rainback
        show m1f_p1b
        show rg2 a12b_akuwarai3 at left
        show kir a11_futeki1 at right
    elif rnd == 6:
        scene mhal_2b_bg
        show rainback
        show mhal_2b
        show rud a14_majime2 at left
        show ep3_c0902 5
    elif rnd == 7:
        scene blood_1b
        show rud a14_majime2 at left
        show rg4 a12_ikari1 at right
    elif rnd == 8:
        show ep3_c0901 5
        show ep3_c0902 8
    with t28
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_ririana:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 21:
        $ xtmp = [2]
    elif persistent.UMINEKOEND >= 21 and persistent.UMINEKOEND < 30:
        $ xtmp = [2,3]
    elif persistent.UMINEKOEND == 30:
        $ xtmp = [2,3,4]
    else:
        $ xtmp = [2,3,4,5,6,7,8,9]
    if renpy.seen_image('e0201'):
        $ xtmp.append(1)
    $ rnd = renpy.random.choice(xtmp)
    scene white with None
    with Pause(0.03)
    if rnd == 1:
        scene e0201
    elif rnd == 2:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show butterfly_4sp2
        show kin a11_warai2 at left
        show bea b11_futeki2 at right
    elif rnd == 3:
        scene mhal_2br_bg
        show rainback
        show mhal_2br
        show butterfly_4sp2
        show bea a11_def2 at center
    elif rnd == 4:
        scene different_space_1a
        show butterfly_4sp1
        show ber a11_def2 at far_left
        show lam a11_akuwarai1 at center
        show bea a13_def2 at far_right
    elif rnd == 5:
        scene g1f_s1ap
        show but b22_kuyasigaru1 at left
        show bea a11_akuwarai3 at right
        with t42
    elif rnd == 6:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show kan a12_ikari1 at center
        show rg1 a12_naku1:
            xpos (1330.0/1920.0)
        with t6
    elif rnd == 7:
        scene rose_1an
        show rainback
        show bea a12_aseru1 dark at center
        show wal a13_majime1 dark at far_right
        show rainfront
        with t26
    elif rnd == 8:
        scene glob_1d_bg
        show rainback static
        show glob_1d
        show geo a11_majime2 at far_left
        show eva a11_komaru1 at center
        show hid a11_fumu1 at far_right
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show ev2 a12_tokui1 at right
        with t2
    elif rnd == 9:
        scene m1f_p1br_bg
        show rainback
        show m1f_p1br
        show ev2 a11_akuwarai8 at right
        show nan a1_komaru3 behind ev2 at left
        with t24
    if rnd < 5:
        with t2
    with Pause(1.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_dokkyun:
    
label bgm_mode_turu_pettan:
    $ E_MA()
    scene black with None
    scene white with None
    with Pause(0.03)
    scene c0202_a with t28
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_turu_pettan2:
    $ E_MA()
    scene black with None
    scene white with t22
    scene no66_00000 with t28
    with Pause(1.323)
    scene white with None
    $ renpy.movie_cutscene("movie/no66.mkv", stop_music=False)
    $ renpy.pause(0.001, hard=True)
    scene c0202_b
    call bgm_jump
    return
    
label bgm_mode_kiyuusoku:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,4)
    scene white with t22
    if rnd == 1:
        scene g1f_s1bp
        show butterfly_4sp2
    elif rnd == 2:
        scene g1f_s1ap
        show butterfly_4sp2
        show bea a11_nayamu1 at center
    elif rnd == 3 or rnd == 4:
        scene sub_r1a with t2
        with Pause(2.0)
        scene sub_r1b
        if rnd == 4:
            show eva b24_komaru1 at right
        with t6
        with Pause(4.0)
    if rnd <= 2:
        with t2
        with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_hakujitunohate:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,3)
    scene white with t2
    if rnd == 1:
        scene different_spiral_1a
        show butterfly_4sp1
    elif rnd == 2:
        scene mlib_1ar_bg
        show rainback
        show mlib_1ar
        show gen a11_def1 at right
    elif rnd == 3:
        scene butterfly_3a sepia
        show wal a11_warai1 sepia at center
    with t10
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_sirabe_vocal:
    $ E_MA()
    scene black with None
    scene black with t2
    scene butterfly_4a
    with t2
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Over_the_sky:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,2)
    scene white with t2
    if rnd == 1:
        scene different_space_1a
        show ber a11_def2 at center
        with t48
    elif rnd == 2:
        scene g1f_s1ap
        show wal a11_warai1 at right
        show bea a11_fukigen2 behind wal at left
        with t26
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_hidamari:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,3)
    scene white with t2
    if rnd == 1:
        scene sehal_1a
        show wal a11_def1 at center
    elif rnd == 2:
        scene ros_m1ar
        show mar c11_warai1 at right
    elif rnd == 3:
        scene garden_se1b
        show bea a11_futeki2 at left
        show mar b22_warai2 at right
    with t48
    with Pause(6.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_org_remake:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,6)
    else:
        if not renpy.seen_image('e0406'):
            $ rnd = renpy.random.randint(1,8)
        else:
            $ rnd = renpy.random.randint(1,9)
    scene black with t22
    if rnd == 1 or rnd == 7:
        scene g1f_s1ap
        show bea a11_def1 at center
        if rnd == 7:
            show bea a31_akuwarai2 at left
            show but b11_majime4 at right
        with t26
    elif rnd == 2:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show kin a12_ikari1 at right
        with t22
    elif rnd == 3:
        scene blood_1a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b22_niramu1 at right
        show bea a11_akuwarai1 at left
        with t2
    elif rnd == 4:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show bea a31_warai1 at left
        show gen a21_kashikomari1 at right
        with t24
    elif rnd == 5:
        scene mhal_2a_bg
        show rainback
        show mhal_2a
        show butterfly_4sp2
        show ev2 a11_niramu1 at center
        with t22
    elif rnd == 6:
        scene rose_1ar
        show rainback
        show ev2 a11_akuwarai5 dark at center
        show rainfront
        with t24
    elif rnd == 8:
        scene pri_i1a
        show kin a11_akuwarai1 dark at center
        show pri_i1a_sak
        show kir a11_nayamu1 dark at far_right
        show nan a2_majime1 dark at far_left
        with t6
    elif rnd == 9:
        scene e0406 with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Haruka:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,4)
    else:
        $ rnd = renpy.random.randint(1,7)
    if rnd == 1:
        scene black with t22
        show ev2 b11_warai1 at center
    elif rnd == 7:
        scene white with t22
        scene g1f_s1bp
        show but b11_def2 at left
        show enj a11_fuman2 at right
    elif rnd == 5 or rnd == 6:
        scene white with t22
        scene car_i3c
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show enj a11_nayamu1 at right
        show ber a11_def1 at left
    else:
        $ rnd2 = renpy.random.randint(1,8)
        scene white with t22
        with Pause(1.5)
        if rnd2 == 1:
            scene forest_p2af
        elif rnd2 == 2:
            scene fence_1a
        elif rnd2 == 3:
            scene se_o1a
        elif rnd2 == 4:
            scene garden_se2b
        elif rnd2 == 5:
            scene garden_se1b
        elif rnd2 == 7:
            scene cliff_1a
            show bea a31_warai1:
                alpha (128.0/255.0)
        elif rnd2 == 8:
            scene garden_1a
            show rainback static
            show rainfront static
            show black:
                alpha (150.0/255.0)
            show hana1:
                alpha (180.0/255.0)
            show wal a11_def1 at left
            show but b11_komaru2 at right
        elif rnd2 == 6:
            scene g1f_p1er
            show black:
                alpha (150.0/255.0)
            show hana1:
                alpha (180.0/255.0)
            show bea a11_nayamu1 at left
            show geo a21_naki2 at right
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_psy_chorus_mx:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,4)
    if rnd == 1:
        $ rnd2 = renpy.random.randint(1,6)
        scene white with t22
        if rnd2 == 1:
            scene fence_1a:
                zoom 1.5 yalign 0.0 ypos -(503.0/720.0)
                pause 1.3
                easein 8.0 ypos -(100.0/720.0)
            with t6
            with Pause(8.5)
            scene fence_1a
        elif rnd2 == 2:
            scene forest_p1bf
        elif rnd2 == 3:
            scene se_o1a
        elif rnd2 == 4:
            scene garden_se2b
        elif rnd2 == 5:
            scene garden_se1b
        elif rnd2 == 6:
            scene garden_seaia
        with t2
    elif rnd == 2:
        scene black with t22
        scene text010c with t2
    else:
        scene white with t22
        with Pause(1.5)
        scene rose_1an
        show butterfly_4sp1
        show wal a11_def1 at center
        with t8
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_far:
    $ E_MA()
    scene black with None
    $ xtmp = [4]
    if renpy.seen_image('c0201_a'):
        $ xtmp.append(1)
    if renpy.seen_image('c0201_b'):
        $ xtmp.append(2)
    if renpy.seen_image('c0201_c'):
        $ xtmp.append(3)
    if persistent.UMINEKOEND >= 41:
        $ xtmp.extend([5,6])
    $ rnd = renpy.random.choice(xtmp)
    scene white with t22
    with Pause(1.5)
    if rnd == 1:
        scene c0201_a
    elif rnd == 2:
        scene c0201_b
    elif rnd == 3:
        scene c0201_c
    elif rnd == 4:
        scene garden_se2b
    elif rnd == 5:
        scene res_i3ar
        show mar c21_warai2 at left
        show ros c11_warai1 at right
    elif rnd == 6:
        scene garden_se1b
        show mar a22_niyari1 at left
        show bea a11_warai4 at right
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
image no38_bgm = Image("anime/no38_bgm.png", xalign=0.5, yalign=0.5)

label bgm_mode_akaikutu2:
    $ E_MA()
    scene black with None
    $ xtmp = [2,3,4,6,7]
    $ xtmp2 = []
    if renpy.seen_image("no01_00119"):
        $ xtmp.append(1)
    if renpy.seen_image("no55_00059") or renpy.seen_image("tower2r"):
        $ xtmp.append(5)
        $ xtmp.append(8)
    if renpy.seen_image("no55_00059"):
        $ xtmp2.append(1)
    if renpy.seen_image("tower2r"):
        $ xtmp2.append(2)
    $ rnd = renpy.random.choice(xtmp)
    if rnd == 5 or rnd == 8:
        $ rnd2 = renpy.random.choice(xtmp2)
    scene white with None
    with Pause(0.03)
    if rnd == 1:
        scene no01_00119
        show armor7b:
            alpha 0.8
    elif rnd == 2:
        scene no38_00149:
            rotate 180
    elif rnd == 3:
        scene no38_bgm
    elif rnd == 4:
        scene no57_00119
    elif rnd == 5:
        if rnd2 == 1:
            scene no55_00059
        elif rnd2 == 2:
            scene tower2r
    elif rnd == 6:
        scene rose_1an
        show bea a23_akuwarai5 at far_right
        show bea a23_akuwarai4 as bea2 behind bea at far_left
        show bea a32_akuwarai2 as bea3 behind bea at center
    elif rnd == 7:
        scene rose_g1an
        show barrier1p
        show wal a11_def1 at center
    elif rnd == 8:
        if rnd2 == 1:
            scene no55_00059
        elif rnd2 == 2:
            scene tower2r
        show bea a14_akuwarai4 at center
    with t28
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_mother:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 40:
        $ xtmp = [4,8]
    elif persistent.UMINEKOEND == 40:
        $ xtmp = [4,8,9,5]
    else:
        $ xtmp = [4,8,9,5,6,7]
    if renpy.seen_image('c0201_d'):
        $ xtmp.append(1)
    if renpy.seen_image('c0201_e'):
        $ xtmp.append(2)
    if renpy.seen_image('c0201_f'):
        $ xtmp.append(3)
    $ rnd = renpy.random.choice(xtmp)
    scene white with t22
    with Pause(1.5)
    if rnd == 1:
        scene c0201_d
    elif rnd == 2:
        scene c0201_e
    elif rnd == 3:
        scene c0201_f
    elif rnd == 4 or rnd == 8:
        scene rose_1an
        show butterfly_4sp1
        show rainback
        show rainfront
        show wal a11_majime1 dark at center
        show ss_1g
        if rnd == 8:
            hide ss_1g
            show wal a11_odoroki1 dark:
                alpha (155.0/255.0)             ## 140 ???
#            show bea a21_akuwarai2 dark behind rainfront at far_right
            show bea a33_warai1 dark behind rainfront at far_right
    elif rnd == 9:
        scene mhal_2c
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a11_komaru2 at right
        show wal a11_def1 at left
    elif rnd == 5:
        scene black
        show eva a11_warai1 gray at center
    elif rnd == 6:
        scene schr_r1ar
        show enj c11_naku1 at center
    elif rnd == 7:
        scene mlib_1cr_bg
        show rainback static
        show mlib_1cr
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a11_nayamu1 at right
        show but b11_komaru2 at left
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_haze:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 40:
        $ rnd = 1
    elif persistent.UMINEKOEND == 40:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,4)
    scene white with t22
    with Pause(1.5)
    if rnd == 1:
        scene rose_1an
        show rainback static
        show rainfront static
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_def1 at center
    elif rnd == 2:
        scene cit_2a
        show ber a11_def2 at center
    elif rnd == 3:
        scene g1f_s1ap
        show but b22_niramu2 at left
        show enj a11_def1 at right
    elif rnd == 4:
        scene cit_2a
        show enj a11_def1 at left
        show ber a11_def2 at right
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_ennkan:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,11)
    scene black with t22
    if rnd == 1:
        scene m1f_s1a_bg
        show rainback static
        show m1f_s1a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_futeki3 at right
    elif rnd == 2:
        scene map10
        show bea a11_akuwarai2 at left
        show ron a11_warai2 at right
    elif rnd == 3:
        scene map10
        show bea a11_akuwarai2 at left
    elif rnd == 4:
        scene letter1
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_majime1 at right
    elif rnd == 5:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show ron a11_def1 at right
        show but b11_komaru2 at left
    elif rnd == 6:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a11_akuwarai1 at right
        show but b22_oya1 at left
    elif rnd == 7:
        scene map06
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_odoroki1 at right
    elif rnd == 8:
        scene g1f_s1bp
        show but b22_nayamu2 at left
        show bea a11_futeki1 at right
    elif rnd == 9:
        scene g1f_s1ap
        show but b22_futeki1 at left
        show ron a11_def1 at right
    elif rnd == 10:
        scene g1f_s1ap
        show but b25_odoroki1 at right
    elif rnd == 11:
        scene map10b
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_dread_grave2:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,11)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,14)
    else:
        $ rnd = renpy.random.randint(1,15)
    scene black with t22
    if rnd == 1:
        scene m1f_s1a_bg
        show rainback static
        show m1f_s1a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_futeki3 at right
    elif rnd == 2:
        scene map10
        show bea a11_akuwarai2 at left
        show ron a11_warai2 at right
    elif rnd == 3:
        scene map10
        show bea a11_akuwarai2 at left
    elif rnd == 4:
        scene letter1
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_majime1 at right
    elif rnd == 5:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_komaru2 at left
        show ron a11_def1 at right
    elif rnd == 6:
        scene key2
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b22_oya1 at left
        show bea a11_akuwarai1 at right
    elif rnd == 7:
        scene map06
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b25_odoroki1 at right
    elif rnd == 8:
        scene g1f_s1bp
        show but b22_nayamu2 at left
        show bea a11_futeki1 at right
    elif rnd == 9:
        scene g1f_s1ap
        show but b22_futeki1 at left
        show ron a11_def1 at right
    elif rnd == 10:
        scene g1f_s1ap
        show but b25_odoroki1 at right
    elif rnd == 11:
        scene map10b
    elif rnd == 12:
        scene g1f_s1bp
        show but b25_odoroki1 at right
    elif rnd == 13:
        scene g1f_s1bp
        show ev2 a11_odoroki2 at left
        show but b25_majime4 at right
    elif rnd == 14:
        scene g1f_s1bp
        show ev2 a11_fukigen3 at left
        show but b25_majime4 at right
    elif rnd == 15:
        scene black
        show gap a11_akuwarai4:
            xanchor 0 yanchor 0 xpos (550.0/1920.0) ypos -(200.0/1080.0) zoom 2.0
        show geo a11k_majime5k:
            xanchor 0 yanchor 0 xpos -(380.0/1920.0) ypos -(80.0/1080.0) zoom 2.0
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_orugan_2okuban:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        scene g1f_s1bp
        show bea a11_nayamu2 at center
    elif rnd == 2:
        scene g1f_p1c
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a11_nayamu2 at right
        show ron a11_warai2 at left
    elif rnd == 3:
        scene mhal_2a_bg
        show rainback
        show mhal_2a
        show bea a11_komaru1 at left
        show ev2 a11_warai1 at right
    elif rnd == 4:
        scene g1f_s1ap
        show bea a11_warai2 at left
        show but b11_aseru1 at right
    elif rnd == 5:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show gap a12_warai2 at left
        show wal a14_komaru1 at right
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_rhythm_changer_mx:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,4)
    else:
        $ rnd2 = renpy.random.randint(1,7)
    if persistent.UMINEKOEND < 31:
        $ rnd2 = 1
    else:
        $ rnd2 = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        if rnd2 == 1:
            scene glob_1a_bg
            show rainback
            show glob_1a
        else:
            scene glob_1ar_bg
            show rainback
            show glob_1ar
    elif rnd == 2:
        if rnd2 == 1:
            scene glob_1d_bg
            show rainback
            show glob_1d
        else:
            scene glob_1dr_bg
            show rainback
            show glob_1dr
    elif rnd == 3:
        if rnd2 == 1:
            scene glob_1e
        else:
            scene glob_1er
    elif rnd == 4:
        scene glib_1a
    elif rnd == 5:
        scene pri_i1c
        show pri_i1c_sak
    elif rnd == 6:
        scene pri_i1b
        if rnd2 == 2:
            show pri_i1a_2_sak
    elif rnd == 7:
        scene pri_i1a
        if rnd2 == 2:
            show pri_i1a_sak
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_happiness_omake:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,4)
    scene white with t2
    with Pause(1.5)
    if rnd == 1:
        scene gold2 with t42
    elif rnd == 2:
        scene portrait4 with t6
    elif rnd == 3:
        scene mlib_1c_bg
        show mlib_1c
        show kin a11_akuwarai1 at center
        with t2
    elif rnd == 4:
        scene garden_r1an_bg
        show rainback
        show garden_r1an
        show geo a23k_majime4k at center
        with t46
    with Pause(5.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_happiness:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = renpy.random.randint(1,5)
    if rnd == 1:
        scene white with t22
        with Pause(1.5)
        scene mhal_ta1a
        show butterfly_4sp1
        show ev2 a11_hohoemi2 at center
        with t8
        with Pause(3.0)
    elif rnd == 2:
        scene white with t22
        with Pause(1.5)
        scene mhal_1a_bg
        show rainback
        show mhal_1a
        show butterfly_4sp1
        show ev2 a11_warai2 at center
        with t8
        with Pause(3.0)
    elif rnd == 3:
        $ rnd2 = renpy.random.randint(1,18)
        scene white with t22
        with Pause(1.0)
        if rnd2 == 1:
            scene different_space_1a
            show chain7r_sp
            show chain5r_sp
            show chain2r_sp
            show ev2 a11_akuwarai4 at right
            show chain6r_sp
            show chain4r_sp
            show chain3r_sp
            show chain2r_sp as chain2_2
            show but b22_kuyasigaru1 behind ev2 at left
        elif rnd2 == 2:
            scene different_space_1a
            show chain7r_sp
            show chain5r_sp
            show ev2 a11_akuwarai4 at center
            show chain6r_sp
            show chain4r_sp
            show chain3r_sp
        elif rnd2 == 3:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp2
            show gen a11_def1 at far_left
            show nat a11_warai1 at center
            show cla a11_def1 at far_right
        elif rnd2 == 4:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp2
            show kum a12_warai1 at far_left
            show mar a22_warai2 at center
            show ros a13_warai1 at right
        elif rnd2 == 5:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp2
            show geo a12_hohoemi1 at center
            show sha a11_warai1 behind geo at left
        elif rnd2 == 6:
            scene mhal_1c
            show butterfly_4sp2
            show nan a1_def1 at far_left
            show hid a11_odayaka1 at center
            show eva a11_warai1 at far_right
        elif rnd2 == 7:
            scene mhal_1c
            show butterfly_4sp2
            show goh a11_omakase2 at far_left
            show kir a11_def1 at center
            show rud a11_warai1 at far_right
        elif rnd2 == 8:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp2
            show kan a13_nayamu1 at center
            show jes a23_warai1 at right
        elif rnd2 == 9:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp2
            show nan a1_def1 at far_right
            show goh a11_hohoemi1 behind nan at center
            show rg6 d21_naku1 behind goh at far_left
        elif rnd2 == 10:
            scene mhal_1c
            show butterfly_4sp1
            show but b11_komaru1 at far_right
            show rg3 a11_hohoemi1 behind but at far_left
            show rg1 a11_hohoemi1 behind but at center
        elif rnd2 == 11:
            scene mhal_1c
            show butterfly_4sp2
            show sha a11_warai1 at center
            show geo a11_hohoemi1 at right
            show but b22_naku1 behind sha at far_left
        elif rnd2 == 12:
            scene mhal_1c
            show butterfly_4sp2
            show eva b32 at center
            show hid a11_odayaka1 behind eva at left
            show rg5 c21_hohoemi1 at far_right
        elif rnd2 == 13:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp1
            show rg7 d21_hohoemi1 at far_left
            show kan a12_nayamu1 at center
            show jes a23_tereru2 at right
        elif rnd2 == 14:
            scene mhal_1c
            show butterfly_4sp1
            show nat a43_naku1 at center
            show cla a11_akuwarai2 behind nat at left
            show eva b32 at right
        elif rnd2 == 15:
            scene mhal_1a_bg
            show mhal_1a
            show butterfly_4sp2
            show ros a13_warai1 at far_right
            show kir a11_komaru1 behind ros at far_left
            show rud a11_akuwarai1 behind ros at center
        elif rnd2 == 16:
            scene mhal_2a_bg
            show mhal_2a
            show butterfly_4sp2
            show mar a22_warai2 at right
            show but b22_odoroki2 behind mar at left
        elif rnd2 == 17:
            scene mhal_2a_bg
            show mhal_2a
            show butterfly_4sp2
            show s45 a11_majime1 at far_right
            show s41 a11_def1 behind s45 at far_left
            show mar a22_sakebu1 at center
        elif rnd2 == 18:
            scene mhal_1c
            show butterfly_4sp2
            show rg3 a21_odoroki1 at far_right
            show rg2 b12_naku1 behind rg3 at far_left
            show rg4 a32_akuwarai1 behind rg3 at center
        with t8
        with Pause(2.0)
    elif rnd == 4:
        scene white with t22
        with Pause(1.0)
        scene mdin_1cr_bg
        show rainback
        show mdin_1cr
        show kin a11_warai2 at left
        show ron a23_akuwarai1 at right
        with t23
        with Pause(2.0)
    elif rnd == 5:
        scene white with t22
        with Pause(1.0)
        scene black
        show bea a11_gaman6:
            xanchor 0 yanchor 0 xpos (350.0/1920.0) ypos -(150.0/1080.0) zoom 2.0
        show but b11_majime4:
            xanchor 0 yanchor 0 xpos -(450.0/1920.0) ypos -(172.0/1080.0) zoom 2.0
        with t2
        with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_tuki_usagi:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,10)
    scene black with t22
    if rnd <= 2:
        if persistent.UMINEKOEND < 31:
            $ rnd2 = 1
        else:
            $ rnd2 = renpy.random.randint(1,5)
        if rnd2 == 1:
            scene sky_3a
            show butterfly_4sp1
            show rainback
            show rainfront
            show ev2 a11_akuwarai5 behind rainfront at center
        elif rnd2 == 2:
            scene mhal_2c
            show butterfly_4sp2
            show s45 a11_def1 at left
            show s41 a11_def1 at right
        elif rnd2 == 3:
            scene mhal_2c
            show butterfly_4sp2
            show s45 a11_def1 at far_left
            show s41 a11_akuwarai1 at far_right
        elif rnd2 == 4:
            scene mhal_2c
            show butterfly_4sp2
            show s45 a11_komaru1 at far_left
            show s41 a11_def1 at far_right
            show ev2 a11_warai1 behind s41 at center
        elif rnd2 == 5:
            scene system5
            show s45 a11_odoroki1 at left
            show s41 a11_akuwarai1 at right
        with t26
        with Pause(2.0)
    elif rnd >= 3:
        $ bgm_mode_rnd_siesuta()
        $ rnd2 = renpy.random.randint(1,6)
        if rnd2 == 1:
            $ tmp_bg = 'tmp_null'
            $ tmp = 'system5'
        elif rnd2 == 2:
            $ tmp_bg = 'black'
            $ tmp = 'homing6'
        elif rnd2 == 3:
            $ tmp_bg = 'tmp_null'
            $ tmp = 'moon_1b'
        elif rnd2 == 4:
            $ tmp_bg = 'mhal_1ar_bg'
            $ tmp = 'mhal_1ar'
        elif rnd2 == 5:
            $ tmp_bg = 'tmp_null'
            $ tmp = 'sky_3a'
        elif rnd2 == 6:
            $ tmp_bg = 'tmp_null'
            $ tmp = 'butterfly_3a'
        $ renpy.scene()
        $ renpy.show(tmp_bg,at_list=[center])
        $ renpy.show(tmp,at_list=[center])
        $ renpy.show(tmp1,at_list=[far_left])
        $ renpy.show(tmp2,at_list=[center])
        $ renpy.show(tmp3,at_list=[far_right],zorder=5)
        with t26
        with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_melting_away:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = renpy.random.randint(1,4)
    scene black with t22
    if rnd == 1:
        scene mhal_2c
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a11_komaru2 at left
        show but b22_niramu1 at right
    elif rnd == 2:
        scene g2f_p1ar_bg
        show rainback
        show g2f_p1ar
        show bea a11_nayamu1 at right:
            alpha (180.0/255.0)
    elif rnd == 3:
        scene m1f_p1dr_bg
        show rainback
        show m1f_p1dr
        show ron a11_majime1 at far_right
        show bea a11_majime4 at center:
            alpha (180.0/255.0)
    elif rnd == 4:
        show mar b11_niyari1 at left
        show bea a12_hanbeso1 at right
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_soul_of_soul:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,3)
    elif persistent.UMINEKOEND >= 31 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,5)
    else:
        $ rnd = renpy.random.randint(1,8)
    scene black with t22
    if rnd == 1:
        scene butterfly_2a
    elif rnd == 2:
        scene different_garden1a
    elif rnd == 3:
        scene different_garden1b
    elif rnd == 4:
        scene m1f_r1ar_bg
        show rainback
        show m1f_r1ar
        show kan a11_nayamu1:
            alpha (160.0/255.0) xpos (810.0/1920.0)
    elif rnd == 5:
        show bea a11_komaru2 at left
        show but b11_nayamu1 at right
    elif rnd == 6:
        scene ship_s2af
        show layer master at ship_slow
        show rg5 a31_odoroki1 at far_left
        show sak a11_odoroki1 at center
    elif rnd == 7:
        scene ep4_meta_2
        show rainback static
        show rainfront static
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea b11_fuman2 at right
        show bea a11_majime1 as bea2 at left
    elif rnd == 8:
        scene rose_3ap
        show mar b23_naku1 at center
        show sak a11_warai1 behind mar at left
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_miragecoordinator:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 32:
        $ rnd = 5
    elif persistent.UMINEKOEND >= 32 and persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,5)
    else:
        $ rnd = renpy.random.randint(1,9)
    scene black with t22
    if rnd <= 4:
        show lam a11_akuwarai6 at center
    elif rnd == 5:
        scene g1f_s1ap
        show ev2 a11_niramu3 at center
    elif rnd == 6:
        scene different_space_1a
        show mar b11_def1k at center
        with t6
    elif rnd == 7:
        scene well_1bn
        show rainback
        show cla a11_ikari1 dark at far_left
        show nan a1_komaru3 dark at center
        show kir a11_sakebu1 dark at far_right
        show rainfront
        with t5
    elif rnd == 8:
        scene g1f_s1ap
        show but b22_odoroki2 at left
        show bea a11_majime4 at right
        with t26
    elif rnd == 9:
        scene hill_1b
        show butterfly_4sp1r
        show eva b24_futeki1 at left
        show enj a11_nayamu1 at right
        with t8
    if rnd <= 5:
        with t28
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_prison:
    $ E_MA()
    scene black with None
    $ xtmp = [1]
    if persistent.UMINEKOEND >= 31:
        $ xtmp.append(3)
    if renpy.seen_image('e0903_a'):
        $ xtmp.append(2)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene blood_2e
        show bea a11_iiwake3 at center
        with t26
    elif rnd == 2:
        scene e0903_a with t25
    elif rnd == 3:
        scene g1f_s1ap
        show ev2 a11_niramu3 at left
        show bea a11_gaman4 at right
        with t64
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_umare:
    $ E_MA()
    scene black with None
    $ xtmp = [1]
    if persistent.UMINEKOEND >= 31:
        $ xtmp.append(3)
    if persistent.UMINEKOEND >= 41:
        $ xtmp.extend([4,5,6,7,8])
    if renpy.seen_image('e0903_a'):
        $ xtmp.append(2)
    if renpy.seen_image('e0901_a'):
        $ xtmp.append(9)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene different_space_1a
        show bea a11_fukigen3 at left
        show but b22_naku2 at right
    elif rnd == 2:
        scene e0903_a
    elif rnd == 3:
        scene mhal_2br_bg
        show rainback
        show mhal_2br
        show but b11_nayamu3 at center
        show bea a12_hanbeso2 at far_right
    elif rnd == 4:
        scene ros_r1a gray
        show mar a22_warai2 gray:
            xanchor 0 yanchor 0 xpos -(384.0/1920.0) ypos -(32.0/1080.0) zoom 2.0
        show sak a11_warai1 gray:
            xanchor 0 yanchor 0 xpos (678.0/1920.0) ypos (156.0/1080.0) zoom 2.0
    elif rnd == 5 or rnd == 7:
        scene schr_r1ar
        show different_spiral_1a:
            alpha (128.0/255.0)
        show enj c11_hanbeso1 at center
        if rnd == 7:
            show enj c11_hanbeso2 at right
            show mar b23_komaru1 behind enj at center
            show sak a21_naku1 at left:
                alpha (175.0/255.0)
    elif rnd == 6:
        scene pri_i1b
        show sha a11_odoroki1 dark at center
        show pri_i1a_2_sak
    elif rnd == 8:
        scene hill_1a
        show sak a13_naku3 at right:
            alpha (135.0/255.0)
        show ev2 a12_akuwarai8 at left:
            alpha (135.0/255.0)
    elif rnd == 9:
        scene e0901_a
    with t8
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_tubasa:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = renpy.random.randint(1,7)
    else:
        $ rnd = renpy.random.randint(1,12)
    scene black with t22
    if rnd == 1:
        scene g1f_s1bp
        show but b25_odoroki1 at far_right
    elif rnd == 2:
        scene g1f_s1bp
        show but b25_odoroki1 at far_right
        show s41 a11_odoroki1 behind but at far_left
        show s45 a11_komaru1 behind but at center
    elif rnd == 3:
        scene g1f_s1bp
        show ev2 a11_odoroki2 at left
        show but b25_majime4 at right
    elif rnd == 4:
        scene g1f_s1ap
        show ev2 a11_niramu3 at left
        show bea a11_majime2 at right
    elif rnd == 5:
        scene g1f_s1bp
        show ev2 a11_fukigen3 at left
        show but b25_majime4 at right
    elif rnd == 6:
        scene mhal_2a_bg
        show rainback static
        show mhal_2a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_majime1 at right
        show but b11_majime4 at left
    elif rnd == 7:
        scene rose_1an
        show rainback static
        show rainfront static
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_majime1 at center
    elif rnd == 8:
        scene mhal_2c
        show enj a11_def1 at center
    elif rnd == 9:
        scene m2f_p1c_bg
        show m2f_p1c
        show bea a21_akuwarai4 at center
    elif rnd == 10:
        scene mhal_2a_bg
        show mhal_2a
        show butterfly_4sp2
        show enj a11_fuman1 at center
    elif rnd == 11:
        scene m2f_p1c_bg
        show m2f_p1c
        show but b11_kuyasigaru1 at left
        show bea a31_akuwarai2 at right
    elif rnd == 12:
        scene m2f_p1c_bg
        show m2f_p1c
        show but b22_niramu1 at left
        show enj a11_nayamu1 at right
    with t28
    with Pause(2.5)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_siturakuenn:
    $ E_MA()
    scene black with None
    $ xtmp = [2,3,4,6,7,8,9]
    if renpy.seen_image('g0301'):
        $ xtmp.append(1)
    if renpy.seen_image('g0302'):
        $ xtmp.append(5)
    $ rnd = renpy.random.randint(xtmp)
    scene black with t22
    if rnd == 1:
        scene g0301
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_def1 at center
    elif rnd == 2:
        scene g1f_s1bp
        show hid a11_def1 at center:
            alpha (155.0/255.0)
    elif rnd == 3:
        scene g1f_s1bp
        show ev2 a11_akuwarai4 at far_left
        show but b25_futeki3 at far_right
        show hid a11_fumu1 at center:
            alpha (155.0/255.0)
    elif rnd == 4:
        scene g1f_s1ap
        show but b25_odoroki1 at right
    elif rnd == 5:
        scene g0302
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show wal a11_def1 at right
        show but b11_futeki3 at left
    elif rnd == 6:
        scene g1f_s1bp
        show ev2 a11_fukigen3 at left
        show but b25_odoroki1 at right
    elif rnd == 7:
        scene g1f_s1ap
        show ron a11_akuwarai1 at left
        show wal a11_fuman1 at right
    elif rnd == 8:
        scene g1f_s1bp
        show ev2 a11_odoroki1 at left
    elif rnd == 9:
        scene g1f_s1ap
        show but b25_futeki1 at right
    with t26
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_wingless:
    $ E_MA()
    scene black with None
    $ xtmp = [1]
    if persistent.UMINEKOEND >= 41:
        $ xtmp.extend([3,4,5,6])
    if renpy.loadable('background/city/cit_2b.png'):
        $ xtmp.append(2)
    if renpy.seen_image('e0104_b'):
        $ xtmp.append(7)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        scene cit_2a
    elif rnd == 2:
        scene cit_2b
    elif rnd == 3:
        scene moon_2a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show mar a22_warai1 at right
        show enj a31_komaru3 at left
    elif rnd == 4:
        scene moon_1a
    elif rnd == 7:
        scene e0104_b
    elif rnd == 5:
        scene hill_1b
        show kas a21_akuwarai3 at center
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show enj a31_komaru3 at right
        show ev2 a11_niramu1 at left
    elif rnd == 6:
        scene sky_1b
    with t6
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_activepain:
    $ E_MA()
    scene black with None
    scene white with None
    with Pause(0.2)
    scene cit_2a
    with t28
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Dread_grave_rhythm:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene white with t22
    with Pause(0.1)
    if rnd == 1:
        scene m2f_p1c_bg
        show m2f_p1c
        show enj a31_fuman1 at left
        show bea a11_akuwarai3 at right
    elif rnd == 2:
        scene mhal_2a_bg
        show mhal_2a
        show butterfly_4sp2
        show enj a11_fuman1 at center
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_kururi:
    $ E_MA()
    scene black with None
    scene sub_r1bp
    with whirl_2000
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_discode:
    $ E_MA()
    scene black with None
    scene black with t22
    scene rose_2ap
    show butterfly_4sp1
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_dreamenddischarger:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,9)
    scene black with t22
    if rnd == 1:
        scene rose_2apr
    elif rnd == 2:
        scene rose_3apr
        show bea a11_akuwarai1 at right
        show but b11_niramu4 behind bea at left
    elif rnd == 3:
        show but b11_majime4:
            xanchor 0 yanchor 0 xpos -(426.0/1920.0) ypos -(166.0/1080.0) zoom 2.0
        show bea a11_akuwarai3:
            xanchor 0 yanchor 0 xpos (402.0/1920.0) ypos -(130.0/1080.0) zoom 2.0
    elif rnd == 4:
        scene rose_3apr
        show bea a14_def2 at center
    elif rnd == 5:
        scene rose_3apr
        show but b22_majime4 at center
    elif rnd == 6:
        scene rose_3apr
        show bea a11_akuwarai1 at right
        show but b22_niramu4 behind bea at left
    elif rnd == 7:
        scene rose_3apr
        show but b11_futeki3 at left
        show bea a11_fukigen1 at right
    elif rnd == 8:
        scene rose_1cpr
        show but b25_odoroki1 at right
    elif rnd == 9:
        scene rose_3apr
        show but b22_odoroki1 at center
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_e_nain:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 42:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,8)
    scene black with t22
    if rnd == 1:
        scene different_space_1a
        show but b22_sakebu2 at left
        show bea a11_akuwarai4 at right
    elif rnd == 2:
        scene rose_3apr
        show butterfly_4sp1
        show bea a14_majime2 at center
    elif rnd == 3:
        scene rose_3apr
        show butterfly_4sp1
        show bea a14_akuwarai3 at center
    elif rnd == 4:
        scene rose_3apr
        show butterfly_4sp2
        show but b22_odoroki1 at left
    elif rnd == 5:
        scene rose_3apr
        show butterfly_4sp1
        show but b11_futeki3 at left
        show bea a14_ikari1 at right
    elif rnd == 6:
        show but b22_odoroki1:
            xanchor 0 yanchor 0 xpos -(426.0/1920.0) ypos -(144.0/1080.0) zoom 2.0
        show bea a11_akuwarai3:
            xanchor 0 yanchor 0 xpos (402.0/1920.0) ypos -(130.0/1080.0) zoom 2.0
    elif rnd == 7:
        show but b11_futeki3:
            xanchor 0 yanchor 0 xpos -(426.0/1920.0) ypos -(166.0/1080.0) zoom 2.0
        show bea a11_ikari1:
            xanchor 0 yanchor 0 xpos (402.0/1920.0) ypos -(130.0/1080.0) zoom 2.0
    elif rnd == 8:
        scene rose_3apr
        show butterfly_4sp1
        show but b25_odoroki1 at center
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_dir:
    $ E_MA()
    scene black with None
    $ xtmp = [1]
    if persistent.UMINEKOEND >= 41:
        $ xtmp.extend([2,3,4])
    if persistent.UMINEKOEND >= 42:
        $ xtmp.append(6)
    if renpy.seen_image('e0407'):
        $ xtmp.append(5)
    $ rnd = renpy.random.choice(xtmp)
    scene white with t22
    if rnd == 1:
        scene rose_2ap
    elif rnd == 2:
        scene different_space_1a
        show enj a21_komaru4 at center
    elif rnd == 3:
        scene different_space_1a
        show butterfly_4sp1
        show enj a11_hanbeso3 at left
        show but b22_naku2 at center
    elif rnd == 4:
        scene different_space_1a
        show enj a11_ikari2 at center
    elif rnd == 5:
        scene e0407
    elif rnd == 6:
        scene mhal_2br_bg
        show rainback static
        show mhal_2br
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show bea a11_futeki2 at left
        show but b22_odoroki1 at right
    with t22
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_dive_to_emergency:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        scene hill_1a
        show rg1 a13b_ikari1 at center
        show rg5 b22_komaru2 at right:
            alpha (135.0/255.0)
    elif rnd == 2:
        scene hill_1b
        show enj a11_fuman2 at center
        show rg2 a22_akuwarai3 at far_right
    elif rnd == 3:
        scene hill_1a
        show rg3 a12b_akuwarai2 at center
        show enj a11_nayamu1 at far_right
    elif rnd == 4:
        scene hill_1b
        show enj a11_fuman2 at left
        show rg7 d21_akuwarai3 at right
    elif rnd == 5:
        scene hill_1a
        show enj a11_nayamu1 at left
        show rg5 a12_hohoemi1 at right
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_h_maria_uta:
    $ E_MA()
    scene black with None
    scene white with t22
    scene mlib_1br_bg
    show rainback
    show mlib_1br
    show bea b11_akuwarai2 at center
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_renngoku_kyousou:
    $ E_MA()
    scene black with None
    scene black with t22
    scene se1f_s1an
    show butterfly_4sp2
    show wal a11_akuwarai2 at center
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Revolt:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene sub_d1a
        show kir a11_majime1 at far_left
        show cla a11_komaru1 at far_right
        show sha a13_ikari1 at center
    elif rnd == 2:
        scene sub_d1a
        show sha a14_ikari1 at left
        show kan a12b_ikari2 at center
    elif rnd == 3:
        scene sub_d1a
        show goa a11 at far_left
        show goa a11 as goa2 at center
        show goa a11 as goa3 at far_right
        show pri_i1c_2_sak
        show kir a11_majime1 at left
        show cla a11_ikari1 at right
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Victima:
    $ E_MA()
    scene black with None
    $ xtmp = [2,3,4,5,6,7]
    if renpy.seen_image('c_c0402 c') or renpy.seen_image('c_c0402 lc') or renpy.seen_image('ep4_c0402 5'):
        $ xtmp.append(1)
    $ rnd = renpy.random.choice(xtmp)
    scene black with t22
    if rnd == 1:
        show c_c0402_wall:
            xalign 1.0
        show c_c0402 c:
            xalign 1.0
    elif rnd == 2:
        scene garden_1an
        show barrier
        show geo a11_majime5 at center
    elif rnd == 3:
        scene mjes_1cr_bg
        show rainback
        show mjes_1cr
        show barrier
        show jes a11_futeki2 at center
    elif rnd == 4:
        scene mjes_1ar_bg
        show rainback
        show mjes_1ar
        show jes a11_futeki2 at left
        show ron a12_akuwarai1 at right
    elif rnd == 5:
        scene moon_1b
        show geo a11_niramu1 at center
    elif rnd == 6:
        scene rose_1an
        show rainback
        show geo a11_majime5 at left
        show gap a11_akuwarai1a at right
        show rainfront
    elif rnd == 7:
        scene mjes_1ar_bg
        show rainback
        show mjes_1ar
        show jes a11_futeki2 at left
        show ron a12_akuwarai1 at right
    with t26
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_mortal:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 2
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        $ rnd2 = renpy.random.randint(1,3)
        scene rose_1an
        if rnd2 == 1:
            show geo a21_akuwarai1 dark at center
        elif rnd2 == 2:
            show geo a22_akuwarai1 dark at right
        elif rnd2 == 3:
            show geo a22k_akuwarai1k dark at right
    elif rnd == 2:
        scene mjes_1cr_bg
        show rainback
        show mjes_1cr
        show jes a11_akuwarai1 at left      ## futeki1
        show ron a12_odoroki1 at right      ## a11_
    elif rnd == 3:
        scene mjes_1ar_bg
        show rainback
        show mjes_1ar
        show jes a11_futeki2 at right
        show barrier1p
        show ron a11_majime2 at left
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_hibuta:
    $ E_MA()
    scene black with None
    scene black with t22
    scene mjes_1ar_bg
    show rainback
    show mjes_1ar
    show ron a11_def1 at left
    show jes a11_futeki2 at right
    with t6
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_death:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 3
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene bite
        show gap a11_akuwarai4:
            xanchor 0 yanchor 0 xpos (550.0/1920.0) ypos -(210.0/1080.0) zoom 2.0
    elif rnd == 2:
        scene sub_p1a_blur
        show goa a11 dark:
            xanchor 0 yanchor 0 xpos (150.0/1920.0) ypos (40.0/1080.0) zoom 1.5
        show wal a11_warai1 dark:
            xanchor 0 yanchor 0 xpos -(100.0/1920.0) ypos -(300.0/1080.0) zoom 1.2
    elif rnd == 3:
        scene rose_1an
        show gap a11_akuwarai4 dark at center
    with t28
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_Surrounding:     ## add hot_r1a?
    $ E_MA()
    scene black with None
    scene white with t22
    scene sky_1a
    with t8
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_kuonn:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 6
    elif persistent.UMINEKOEND == 41:
        $ rnd = renpy.random.randint(1,6)
    else:
        $ rnd = renpy.random.randint(1,7)
    scene black with t22
    if rnd == 1 or rnd == 4:
        scene moon_2a
        if rnd == 4:
            show black:
                alpha (150.0/255.0)
            show hana1:
                alpha (180.0/255.0)
            show mar a22_def1 at right
            show enj a11_hanbeso2 at left
    elif rnd == 2:
        scene ship_s2bf
        show layer master at ship_slow
        show enj a31_komaru3 at left
        show rg5 a11_def1 at right
    elif rnd == 3:
        scene different_space_p1a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show enj a11_ikari1 at right
        show mar a22_odoroki1 at left
    elif rnd == 5:
        scene cit_3a gray
        show mar c11_warai1 gray at center
    elif rnd == 6:
        scene gdin_1ad2 sepia
        show eva a11_majime1 sepia at right
    elif rnd == 7:
        scene rose_3apr
        show rainback
        show but b22_kuyasigaru1 at left
        show bea a11_hanbeso1 at right
        show rainfront
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_over:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        scene bui_o2b
        show enj a11_fuman2 at right
    elif rnd == 2:
        scene air_in1a
        show kas a11_warai1 at center
    elif rnd == 3:
        scene bui_inf1a
        show oko a11_warai2 at left
        show kas a11_warai1 at right
    elif rnd == 4:
        scene pro_o1a
        show kas a11_akuwarai1 at center
    elif rnd == 5:
        scene air_in1e
        show kas a11_akuwarai1 at right
    with t28
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_gc19:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene car_o2a
        show enj a11_fuman1 at left
    elif rnd == 2:
        scene car_i3c
        show ep4_car_enj a11_def1:
            xpos -(400.0/1920.0)
        show ep4_car_ama a11_akuwarai1:
            xpos (400.0/1920.0)
    elif rnd == 3:
        scene car_o2a
        show enj a11_fuman1 at left
        show ama a11_akuwarai1 at right
    with t26
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_f1_02:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        scene hot_r1a
        show mar b11_niyari1 at left
        show rg5 d21_warai1 at right
    elif rnd == 2:
        scene hot_r1a
        show rg7 a11_def1 at center:
            alpha (55.0/255.0)
    elif rnd == 3:
        show black as blk:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show rg5 a11_komaru3 at far_right
        show sak a11_odoroki1 at center
        show enj a31_komaru3 at far_left
    elif rnd == 4:
        scene pri_i1b
        show sha a11_majime3 dark at center
        show kan a11_nayamu1 dark at far_right
        show pri_i1a_2_sak
    elif rnd == 5:
        scene hill_1b
        show rg6 a12_hohoemi1:
            xpos (210.0/1920.0)
        show rg4 a12_akuwarai1:
            xpos (510.0/1920.0)
        show rg2 a12_def1:
            xpos (1110.0/1920.0)
        show rg3 a12_akuwarai2:
            xpos (1410.0/1920.0)
        show rg7 a12_warai1:
            xpos (1710.0/1920.0)
        show rg1 a12_akuwarai2:
            xpos (810.0/1920.0)
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_mclock:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    if rnd == 1:
        scene g1f_s1ap
        show bea a34_warai1 at center
    elif rnd == 2:
        scene car_i3c
    elif rnd == 3:
        scene car_i1a
    with t26
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_apathy:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ xtmp = [1,2]
    else:
        $ xtmp = [1,2,3,4,5,6,7,8,9,10,11,12]
    if renpy.seen_image('e0405'):
        $ xtmp.append(13)
    $ rnd = renpy.random.choice(xtmp)
    scene white with t22
    with Pause(1.5)
    if rnd == 1:
        scene schr_o2a
        show mar a22_def1 at center
    elif rnd == 13:
        scene e0405
    elif rnd == 2:
        scene sky_1a
    elif rnd == 3:
        scene ros_r1a
        show mar c11_warai1 at left
        show ros c11_warai1 at right
    elif rnd == 4:
        scene sakutaro2a
    elif rnd == 5:
        scene hot_r1a
        show enj a11_nayamu1 at left
        show mar b11_ikari1 at right
    elif rnd == 6:
        scene sakutaro2b
    elif rnd == 7:
        scene hill_1b
        show sak a11_warai1 at left
        show mar b11_def1 at right
    elif rnd == 8:
        scene sky_4b
        show mar b11_warai1 at center
        show sak a11_warai3 at far_right
    elif rnd == 9:
        scene sky_1a
        show enj c11_warai2 at right
    elif rnd == 10:
        scene sky_1a
        show rg5 d11_akuwarai1 at center
    elif rnd == 11:
        scene sky_1a
        show rg7 a12_hohoemi1:
            xpos (180.0/1920.0)
        show rg6 a12_akuwarai1:
            xpos (440.0/1920.0)
        show rg5 a12_akuwarai2:
            xpos (700.0/1920.0)
        show rg4 a12_def1:
            xpos (1220.0/1920.0)
        show rg3 a12_fuman1:
            xpos (1480.0/1920.0)
        show rg2 a12_hohoemi1:
            xpos (1740.0/1920.0)
        show rg1 a12_hohoemi1:
            xpos (960.0/1920.0)
    elif rnd == 12:
        scene con_i1a
        show sak a11_warai2 at left
        show mar c21_warai2 at right
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_forest:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,7)
    scene black with t22
    if rnd == 1:
        scene book1
    elif rnd == 2:
        scene tel1a
    elif rnd == 3:
        scene moon_2a
    elif rnd == 4:
        scene schr_r1a
        show enj c11_komaru1 at center
    elif rnd == 5:
        scene ros_m1ar
        show sak a21_naku1 at far_left
        show mar c23_naku1 at center
    elif rnd == 6:
        scene sakutaro2bb
    elif rnd == 7:
        scene ros_r1ar
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_mdoramu:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ xtmp = [5,6]
    else:
        $ xtmp = [1,2,3,4,5,6]
    if renpy.seen_image('e0404'):
        $ xtmp.append(7)
    $ rnd = renpy.random.choice(xtmp)
    scene white with t22
    with Pause(0.3)
    if rnd == 1:
        scene hill_1b
        show sak a11_warai1 at left
        show mar b11_def1 at right
    elif rnd == 2:
        scene sky_4b
        show mar b11_warai1 at center
        show sak a11_warai3 at far_right
    elif rnd == 3:
        scene sakutaro1bb
        show mar a22_warai1 at left
    elif rnd == 4:
        scene garden_se1b
        show sak a11_odoroki1 at center
    elif rnd == 5:
        scene sakutaro2ab
    elif rnd == 6:
        scene sakutaro2bb
    elif rnd == 7:
        scene e0404
    with t8
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_fs2:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,3)
    scene white with t22
    with Pause(1.5)
    if rnd == 1:
        scene hot_r1a
        show mar b11_niyari1 at center
    elif rnd == 2:
        scene hot_r1a
        show mar b11_warai1 at far_left
        show enj a11_nayamu1 at center
    elif rnd == 3:
        scene sky_4b
        show mar b11_def1 at far_left
        show sak a11_odoroki1 at center
        show enj c11_warai1 at far_right
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_org_kui:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = renpy.random.randint(1,6)
    scene black with t22
    if rnd == 1:
        scene hot_r1a
        show rg5 a21_fuman1 at right
    elif rnd == 2:
        scene hot_r1a
        show mar b11_warai1 at left
        show rg5 b11_komaru3 at right
    elif rnd == 3:
        scene hot_r1a
        show rg5 a31_akuwarai4 at left
        show enj a31_komaru3 at right
    elif rnd == 4:
        scene different_space_p1a
        show rg5 a31_akuwarai4 at left
        show enj a11_komaru1 at right
    elif rnd == 5:
        scene ep4_meta_1
        show rainback static
        show rainfront static
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show but b11_komaru2 at left
        show bea a11_majime4 at right
    elif rnd == 6:
        scene ep4_meta_1
        show rainback
        show rainfront
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_happy_maria:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 41:
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        scene mdin_1gr_bg
        show rainback
        show mdin_1gr
        show gap a11_akuwarai4:
            xanchor 0 yanchor 0 xpos (50.0/1920.0) ypos -(100.0/1080.0) zoom 2.0
    elif rnd == 2:
        scene mdin_1cr_bg
        show rainback
        show mdin_1cr
        show wal a11_def1 at far_left
        show gap a11_akuwarai1 at center
        show ron a11_akuwarai1 at far_right
    elif rnd == 3:
        scene garden_r1an_bg
        show rainback
        show garden_r1an
#        show gap a11_akuwarai5 at center
        show gap a11_warai2 at center
    elif rnd == 4:
        scene garden_r1an_bg
        show rainback
        show garden_r1an
#        show gap a11_warai2 at center
        show gap a11_akuwarai1 at center
    elif rnd == 5:
        scene blood_1ar
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show gap a11_warai3 at center
        show bea a21_akuwarai2 at far_left
    with t28
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_mbox:
    $ E_MA()
    scene black with None
    if persistent.UMINEKOEND < 31:
        $ rnd = 1
    else:
        $ rnd = renpy.random.randint(1,3)
    scene black with t22
    with Pause(5.6)
    if rnd == 1:
        scene mhal_1c
    elif rnd == 2:
        scene glob_1a_bg
        show glob_1a
    elif rnd == 3:
        scene glob_1e
    with t2
    with Pause(4.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_majoshima:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,3)
    if rnd == 1:
        scene white with t22
    else:
        scene black with t22
    if rnd == 1:
        scene g_o1cf with t28
        with Pause(2.0)
        show red_b:
            alpha 0.7
        with t2
    elif rnd == 2:
        scene forest_p1bf with t8
        with Pause(2.0)
        scene black with t2
        scene fence_1a with t6
    elif rnd == 3:
        scene kaw_r3bn
        show enj a31_komaru3 at center
        show ama a12_majime1 at far_right
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show sak a11_odoroki1 at far_right
        show rg5 a11_komaru3 at center
        show enj a11_komaru2 as enj2 at far_left
        with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_odayaka:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,4)
    scene black with t22
    if rnd == 1:
        scene beach_1a
        show kan a11_majime1 at left
        show sha a11_tokui1 at right
        with t6
    elif rnd == 2:
        scene schf_p1a with t6
    elif rnd == 3:
        scene schf_r1a with t5
    elif rnd == 4:
        scene m1f_s1ar_bg
        show rainback
        show m1f_s1ar
        show ros a13_warai1 at left
        show mar a11_niyari1 at right
        with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_shoujouningyou:          ## unused
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene sub_r1ap with t26
    elif rnd == 2:
        scene sub_r1bp with t26
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_oimotometa:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    scene mlib_1b_bg
    show mlib_1b
    if rnd == 1:
        show kin a11_naku2 at right
    elif rnd == 2:
        show kin a11_warai1 at right
    with t22
    with Pause(1.0)
    scene white onlayer meta with None
    with Pause(0.03)
    scene onlayer meta
    if rnd == 1:
        show kin a23_naku1
    elif rnd == 2:
        show kin a11_akuwarai1
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_haiyoru_fuan:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,6)
    scene black with t22
    if rnd == 1:
        scene mboi_1a
        show kan b32_nayamu1 dark at right
    elif rnd == 2:
        scene sea_1bn
        show rainback
        show rainfront
#        with t8
    elif rnd == 3:
        scene m1f_p1d_bg
        show rainback
        show m1f_p1d
        show bea b11_akuwarai5 at center
    elif rnd == 4:
        scene blood_1a
    elif rnd == 5:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show rg1 a32_def1 at left
        show bea a34_akuwarai1 at right
    elif rnd == 6:
        scene mlib_1cr_bg
        show rainback
        show mlib_1cr
        show ron a13_warai2 at far_left
        show rg1 a11_def1 at center
        show bea a13_warai2 at far_right
    with t2
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_akareta:
    $ E_MA()
    scene black with None
    scene black with t22
    if renpy.seen_image('g0201'):
        scene g0201 with t2
        with Pause(1.0)
    scene pumpkin2 with t22
    with Pause(0.5)
    scene black with None
    with Pause(0.03)
    scene sweet2 with t22
    with Pause(0.5)
    scene black with None
    with Pause(0.03)
    scene blood_1a with t22
    with Pause(0.5)
    scene blood_1ar with t2
    with Pause(1.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_koboreochiru:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,6)
    scene black with t22
    if rnd == 1:
        scene warehous_i1a_bg
        show rainback
        show warehous_i1a
        show geo a21_naki2 at left
        show hid a11_komaru2 at right
    elif rnd == 2:
        scene sta_1a
        show mar a22_naku1 at left
        show ros a25_ikari2 at right
    elif rnd == 3:
        scene rose_1ac
        show ros a25_ikari2 at center
        show mar a22_sakebu1 at right
    elif rnd == 4:
        scene m1f_r1a_bg
        show rainback
        show m1f_r1a
        show mar a11_fukigen2 at left
        show but b22_naku2 at right
    elif rnd == 5:
        scene schr_r1ar
        show different_spiral_1a:
            alpha (128.0/255.0)
        show sak a11_odoroki1 at left
        show mar b11_majime1 at center
    elif rnd == 6:
        scene different_space_1a
        show mar b11_fukigen2 at left
        show bea a11_majime1 at right
    with t5
    with Pause(3.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_yuutsunagogo:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd == 1:
        scene mlib_1e with t6
    elif rnd == 2:
        scene mlib_1c_bg
        show rainback
        show mlib_1c
        show kin a11_fumu1 at left
        show nat a11_tukare1 at right
        with t2
    elif rnd == 3:
        scene garden_1cn
        show jes a11_komaru1 dark at far_left
        show kan a11_ikari1 dark at center
        with t2
    elif rnd == 4:
        scene mhal_2c
        show ev2 a11_odoroki2 at center
        with t22
        with Pause(1.0)
        show hid a11_komaru2 at right with t23
    elif rnd == 5:
        scene white with None
        with Puase(0.03)
        scene schr_r1ar
        show different_spiral_1a:
            alpha (128.0/255.0)
        show enj c11_hanbeso3 at right
        show rg3 a12_naku1 at left:
            alpha (155.0/255.0)
        with t2
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_shizukana:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,7)
    scene black with t22
    if rnd == 1:
        scene g1f_p1er with t25
    elif rnd == 2:
        scene g2f_p1ar_bg
        show rainback
        show g2f_p1ar
        show bea a11_fukigen3:
            xpos (1160.0/1920.0) alpha (150.0/255.0)
        with t6
    elif rnd == 3:
        scene moon_2a with t8
    elif rnd == 4:
        scene ros_o1an
        show mar c21_sakebu1 dark at center
        with t23
        with Pause(1.0)
        show mar c23_naku1 dark with t80
        with quakey_3_400
    elif rnd == 5:
        scene mjes_1ar_bg
        show rainback
        show mjes_1ar
        show ron a11_def2 at center
        show jes a11_majime1 at far_right
        with t2
    elif rnd == 6:
        scene white with t8
        with Pause(0.1)
        scene hill_1a with t9
    elif rnd == 7:
        scene rose_3ap
        show bea a11_komaru4 at far_left
        show mar b11_komaru1 at center
        with t22
        with Pause(1.0)
        show mar b11_odoroki1 with t80
        with Pause(0.5)
        show bea a11_odoroki1 with t80
        with Pause(0.5)
#        hide mar with t64
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_shinounohomura:
    $ E_MA()
    scene black with None
    scene black with t22
    scene m1f_p1dr_bg
    show rainback
    show m1f_p1dr
    show ron a11_majime1 at far_right
    show bea a11_majime4 at center:
        alpha (180.0/255.0)
    with t26
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_ougon_no_hiai:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene different_space_1a
        show ev2 a11_fukigen3 at left   #far
        show bea a11_iiwake3 at right   #far
        with t22
    elif rnd == 2:
        scene hill_1a with t26
        show enj a11_nayamu1 at left with t2
        show rg5 b21_def1 at right with t22
        with Pause(2.0)
        scene sky_1b with t25
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_anryoku:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,6)
    scene black with t22
    if rnd == 1:
        scene rose_1ar with t22
        with Pause(1.0)
        show black:
            alpha (150.0/255.0)
        show ev2 b11_def1 at right
        with t42
    elif rnd == 2:
        scene mlib_1ar_bg
        show rainback
        show mlib_1ar
        show kan a13_nayamu1 at left
        show gen a11_def1 at right
        with t6
        with Pause(2.0)
        scene red_b with blood_2a_efe_2000
        with Pause(0.2)
        scene black with t22
    elif rnd == 3:
        scene g1f_s1ap
        show bea a11_akuwarai1 at left
        show but b22_naku1 at right
        with t2
        if renpy.seen_image('e0103 d'):
            with Pause(1.0)
            scene white onlayer meta with None
            with Pause(0.03)
            scene onlayer meta
            show e0103_wall
            show e0103 d
            with t22
            with quakex_3_300
    elif rnd == 6:
        scene g1f_s1ap
        show but b22_niramu1 at left
        show bea a11_hanbeso1 at right
        with t3
    elif rnd == 4:
        scene different_space_1c
        show mar b11_def1k at center
        with t22
        show bea a11_nayamu1 behind mar at far_left with t3
    elif rnd == 5:
        scene different_spiral_1a gray
        show eva b32 gray at center
        show ev2 a11_akuwarai8 gray at right:       ## xpos might be different
            alpha (135.0/255.0)
        with t8
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    if rnd == 2:
        scene mlib_1er
    call bgm_jump
    return
    
label bgm_mode_monocle:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene rose_1ar
        show rainback
        show ron a13_warai2 dark at left
        show bea a11_futeki1 dark at right
        show rainfront
    elif rnd == 2:
        scene g1f_s1ap
        show ev2 a11_akuwarai8 at center
    with t22
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_fukashigi:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene glob_1d_bg
        show rainback static
        show glob_1d
        show geo a11_majime2 at far_left
        show eva a11_komaru1 at center
        show hid a11_fumu1 at far_right
        show black:
            alpha (150.0/255.0)
        show ev2 a12_tokui1 at right
    elif rnd == 2:
        scene m1f_p1br_bg
        show rainback
        show m1f_p1br
        show nan a1_komaru3 at left
        show ev2 a11_akuwarai8 at right
    with t2
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_time_travel:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene cit_2a with t22
        show ber a11_def1 at center with t42
    elif rnd == 2:
        scene air_out2b gray with t48
        with Pause(0.5)
        show enj a11_komaru1 at right with t42
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_clown:
    $ E_MA()
    scene black with None
    if not renpy.seen_image('e0902'):
        $ rnd = renpy.random.randint(1,4)
    else:
        $ rnd = renpy.random.randint(1,5)
    scene black with t22
    if rnd < 3:
        scene portrait4
        if rnd == 2:
            show black:
                alpha (150.0/255.0)
            show hana1:
                alpha (180.0/255.0)
            show ron a11_warai2 at right
            show bea a11_def2 at left
    elif rnd == 3:
        scene different_space_1c
        show bea a11_fukigen1 at far_left
        show lam a11_futeki3 at right
    elif rnd == 4:
        scene sub_r1ap
    elif rnd == 5:
        scene white with t9
        with Pause(0.5)
        scene e0902
    with t22
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_yami_no_hohoemu:
    $ E_MA()
    scene black with None
    if not rnd == 5:
        $ rnd = renpy.random.randint(1,3)
    else:
        $ rnd = 1
    if rnd == 1:
        scene black with t22
        scene sky_4b
        show sak a11_def1 at center
        with t22
        show rg7 d21_warai1 at far_right with ImageDissolve("efe/breakup_urbl.png", 0.5, 4, reverse=True)
        show rg6 d21_warai2 behind sak at far_left with ImageDissolve("efe/breakup_urbl.png", 0.5, 4, reverse=True)
        show sak a11_odoroki1 with t80
    elif rnd == 2:
        scene white with None
        with Pause(0.03)
        scene g1f_s1ap
        show bea a34_warai1 at center
        with ImageDissolve("efe/breakup_urbl.png", 1.0, 1)
    elif rnd == 3:
        scene white with t22
        scene par_1c
        show rg4 b11_hohoemi1 at far_left
        show rg5 d31_warai1 at center
        show enj c11_warai2 at far_right
        with t26
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_chiisanasekai:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene res_i3ar
        show mar c21_warai2 at left
        show ros c11_warai1 at right
    elif rnd == 2:
        scene moon_2a
        show black:
            alpha (150.0/255.0)
        show hana1:
            alpha (180.0/255.0)
        show mar a22_niyari1 at right
        show enj a11_hanbeso1 at left
    with t2
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_tojitaheya:
    $ E_MA()
    scene black with None
    scene black with t22
    if not renpy.seen_image('c0301'):
        $ rnd = 2
    else:
        $ rnd = renpy.random.randint(1,2)
    scene white with t2
    if rnd == 1:
        scene c0301 with ImageDissolve("efe/breakup_ulbr.png", 2.0, 4)
    elif rnd == 2:
        scene rose_1an
        show rainback
        show ron a11_akuwarai1 dark at far_right behind rainfront
        show rainfront
        with ImageDissolve("efe/breakup_urbl.png", 1.5, 4, reverse=True)
        show kum a11_majime1 dark behind ron at far_left with t3
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_kudasarerushinpan:
    $ E_MA()
    scene black with None
    $ rnd = renpy.random.randint(1,2)
    scene black with t22
    if rnd == 1:
        scene garden_1an with t22
        show goa a11 dark at center with t65
        show goa a11 dark as goa2 behind goa at far_left with t65
        show goa a11 dark as goa3 at far_right with t65
        with Pause(1.0)
        scene white onlayer meta with None
        with Pause(0.03)
        scene onlayer meta
        show goa a11b dark
        show goa a11b dark as goa2
        show goa a11b dark as goa3
    elif rnd == 2:
        scene mjes_1ar_bg
        show rainback
        show mjes_1ar
        show jes a11_ikari1 at left
        show ron a11_akuwarai1 at right
        with t23
        with Pause(0.1)
        scene white onlayer meta with None
        with Pause(0.03)
        scene onlayer meta
        with t22
        scene white onlayer meta with None
        with Pause(0.03)
        scene onlayer meta
        with t22
        scene white onlayer meta with None
        with Pause(0.03)
        scene onlayer meta
    with t22
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label bgm_mode_tatakai:
    $ E_MA()
    scene black with None
    scene black with t22
    if renpy.seen_image('c_c0402 b') or renpy.seen_image('c_c0402 lb'):
        $ rnd = renpy.random.randint(1,2)
    else:
        $ rnd = 2
    scene white with None
    with Pause(0.03)
    if rnd == 1:
        scene black
        show c_c0402_wall:
            xpos 1.0 xanchor 1.0
        show c_c0402 b:
            xpos 1.0 xanchor 1.0
        show ep4_c0402 1
    elif rnd == 2:
        scene rose_3apr
        show butterfly_4sp1
        show bea a11_akuwarai4 at right
    with t2
    with Pause(2.0)
    $ renpy.pause(0.001, hard=True)
    call bgm_jump
    return
    
label old_bgm_mode_rnd_tati1:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1,4)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(but_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(jes_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(geo_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 4:
            $ tmp = renpy.random.choice(mar_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 4
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 4
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_tati_siyounin:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1, 5)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(gen_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(sha_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(kan_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 4:
            $ tmp = renpy.random.choice(goh_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 4
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 4
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 5:
            $ tmp = renpy.random.choice(kum_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 5
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 5
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_tati_4kyoudai:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1, 4)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(cla_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(eva_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(rud_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 4:
            $ tmp = renpy.random.choice(ros_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 4
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 4
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_yomiage:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1, 12)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(but_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(jes_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(geo_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 4:
            $ tmp = renpy.random.choice(mar_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 4
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 4
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 5:
            $ tmp = renpy.random.choice(cla_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 6:
            $ tmp = renpy.random.choice(nat_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 7:
            $ tmp = renpy.random.choice(eva_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 8:
            $ tmp = renpy.random.choice(hid_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 4
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 4
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 9:
            $ tmp = renpy.random.choice(rud_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 10:
            $ tmp = renpy.random.choice(kir_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 11:
            $ tmp = renpy.random.choice(ros_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 12:
            $ tmp = renpy.random.choice(nan_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 4
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 4
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_yomiage2:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1, 3)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(but_rnd2)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(bea_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(ron_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_yomiage3:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1, 3)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(ber_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(bea_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(lam_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_siesuta:
    $ tmp15 = 0
    while tmp15 <= 3:
        $ rand = renpy.random.randint(1, 3)
        if tmp15 == 2:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp16:
                $ tmp15-=1
                $ rand = 0
        if tmp15 == 3:
            if rand == tmp26:
                $ tmp15-=1
                $ rand = 0
#        if tmp15 == 1:
#            $ tmp1 = rand
#        if tmp15 == 2:
#            $ tmp2 = rand
        
        if rand == 1:
            $ tmp = renpy.random.choice(s00_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 1
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 1
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 2:
            $ tmp = renpy.random.choice(s45_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 2
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 2
            if tmp15 == 3:
                $ tmp3 = tmp
        
        if rand == 3:
            $ tmp = renpy.random.choice(s41_rnd1)
            if tmp15 == 1:
                $ tmp1 = tmp
                $ tmp16 = 3
            if tmp15 == 2:
                $ tmp2 = tmp
                $ tmp26 = 3
            if tmp15 == 3:
                $ tmp3 = tmp
        
        $ tmp15+=1
    return

label old_bgm_mode_rnd_bg1:
    $ rnd = renpy.random.randint(1,14)
    if rnd == 1:
        $ tmp = 'ship_p1a'
        $ tmp_bg = 'tmp_null'
    if rnd == 2:
        $ tmp = 'ship_p1c'
        $ tmp_bg = 'tmp_null'
    if rnd == 3:
        $ tmp = 'ship_s2af'
        $ tmp_bg = 'tmp_null'
    if rnd == 4:
        $ tmp = 'ship_s2bf'
        $ tmp_bg = 'tmp_null'
    if rnd == 5:
        $ tmp = 'rose_1af'
        $ tmp_bg = 'tmp_null'
    if rnd == 6:
        $ tmp = 'rose_1cf'
        $ tmp_bg = 'tmp_null'
    if rnd == 7:
        $ tmp = 'rose_g1c'
        $ tmp_bg = 'tmp_null'
    if rnd == 8:
        $ tmp = 'glob_1d_bg'
        $ tmp_bg = 'glob_1d'
    if rnd == 9:
        $ tmp = 'g2f_r1a_bg'
        $ tmp_bg = 'g2f_r1a'
    if rnd == 10:
        $ tmp = 'g2f_r1c_bg'
        $ tmp_bg = 'g2f_r1c'
    if rnd == 11:
        $ tmp = 'sky_2b'
        $ tmp_bg = 'tmp_null'
    if rnd == 12:
        $ tmp = 'sky_1a'
        $ tmp_bg = 'tmp_null'
    if rnd == 13:
        $ tmp = 'beach_1a'
        $ tmp_bg = 'tmp_null'
    if rnd == 14:
        $ tmp = 'beach_2a'
        $ tmp_bg = 'tmp_null'
    return

label old_bgm_mode_rnd_bg_mhal:
    $ rnd = renpy.random.randint(1,6)
    if rnd == 1:
        $ tmp = 'mhal_1c'
        $ tmp_bg = 'tmp_null'
    if rnd == 2:
        $ tmp = 'mhal_2a_bg'
        $ tmp_bg = 'mhal_2a'
    if rnd == 3:
        $ tmp = 'mdin_1e'
        $ tmp_bg = 'tmp_null'
    if rnd == 4:
        $ tmp = 'mlib_1e'
        $ tmp_bg = 'tmp_null'
    if rnd == 5:
        $ tmp = 'mnat_2g'
        $ tmp_bg = 'tmp_null'
    if rnd == 6:
        $ tmp = 'm2f_p1c_bg'
        $ tmp_bg = 'm2f_p1c'
    return

label old_bgm_mode_rnd_bg_mhal2:
    $ rnd = renpy.random.randint(1,12)
    if rnd == 1:
        $ tmp = 'mhal_1c'
        $ tmp_bg = 'tmp_null'
    if rnd == 2:
        $ tmp = 'mhal_2a_bg'
        $ tmp_bg = 'mhal_2a'
    if rnd == 3:
        $ tmp = 'mdin_1e'
        $ tmp_bg = 'tmp_null'
    if rnd == 4:
        $ tmp = 'mlib_1e'
        $ tmp_bg = 'tmp_null'
    if rnd == 5:
        $ tmp = 'mnat_2g'
        $ tmp_bg = 'tmp_null'
    if rnd == 6:
        $ tmp = 'm2f_p1c_bg'
        $ tmp_bg = 'm2f_p1c'
    if rnd == 7:
        $ tmp = 'm1f_p2b_bg'
        $ tmp_bg = 'm1f_p2b'
    if rnd == 8:
        $ tmp = 'm1f_s1a_bg'
        $ tmp_bg = 'm1f_s1a'
    if rnd == 9:
        $ tmp = 'm1f_s1c'
        $ tmp_bg = 'tmp_null'
#    if rnd == 10:
#        $ tmp = ''
#        $ tmp_bg = ''
    if rnd == 11:
        $ tmp = 'mlib_1b_bg'
        $ tmp_bg = 'mlib_1b'
    if rnd == 12:
        $ tmp = 'mlib_1c_bg'
        $ tmp_bg = 'mlib_1c'
    if rnd == 10:
        $ tmp = 'mlib_1a_bg'
        $ tmp_bg = 'mlib_1a'
    return

init python:
    
    def bgm_mode_rnd_tati1():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1,4)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                while True:
                    tmp = ("but " + renpy.random.choice(but_rnd1[0]) + renpy.random.choice(but_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("jes " + renpy.random.choice(jes_rnd1[0]) + renpy.random.choice(jes_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("geo " + renpy.random.choice(geo_rnd1[0]) + renpy.random.choice(geo_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 4:
                while True:
                    tmp = ("mar " + renpy.random.choice(mar_rnd1[0]) + renpy.random.choice(mar_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 4
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 4
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_tati_siyounin():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1, 5)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                while True:
                    tmp = ("gen " + renpy.random.choice(gen_rnd1[0]) + renpy.random.choice(gen_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("sha " + renpy.random.choice(sha_rnd1[0]) + renpy.random.choice(sha_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("kan " + renpy.random.choice(kan_rnd1[0]) + renpy.random.choice(kan_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 4:
                while True:
                    tmp = ("goh " + renpy.random.choice(goh_rnd1[0]) + renpy.random.choice(goh_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 4
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 4
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 5:
                while True:
                    tmp = ("kum " + renpy.random.choice(kum_rnd1[0]) + renpy.random.choice(kum_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 5
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 5
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_tati_4kyoudai():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1, 4)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                while True:
                    tmp = ("cla " + renpy.random.choice(cla_rnd1[0]) + renpy.random.choice(cla_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("eva " + renpy.random.choice(eva_rnd1[0]) + renpy.random.choice(eva_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("rud " + renpy.random.choice(rud_rnd1[0]) + renpy.random.choice(rud_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 4:
                tmp = renpy.random.choice(ros_rnd1)
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 4
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 4
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_yomiage():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1, 12)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                while True:
                    tmp = ("but " + renpy.random.choice(but_rnd1[0]) + renpy.random.choice(but_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("jes " + renpy.random.choice(jes_rnd1[0]) + renpy.random.choice(jes_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("geo " + renpy.random.choice(geo_rnd1[0]) + renpy.random.choice(geo_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 4:
                while True:
                    tmp = ("mar " + renpy.random.choice(mar_rnd1[0]) + renpy.random.choice(mar_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 4
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 4
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 5:
                while True:
                    tmp = ("cla " + renpy.random.choice(cla_rnd1[0]) + renpy.random.choice(cla_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 6:
                while True:
                    tmp = ("nat " + renpy.random.choice(nat_rnd1[0]) + renpy.random.choice(nat_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 7:
                while True:
                    tmp = ("eva " + renpy.random.choice(eva_rnd1[0]) + renpy.random.choice(eva_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 8:
                while True:
                    tmp = ("hid " + renpy.random.choice(hid_rnd1[0]) + renpy.random.choice(hid_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 4
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 4
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 9:
                while True:
                    tmp = ("rud " + renpy.random.choice(rud_rnd1[0]) + renpy.random.choice(rud_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 10:
                while True:
                    tmp = ("kir " + renpy.random.choice(kir_rnd1[0]) + renpy.random.choice(kir_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 11:
                while True:
                    tmp = ("ros " + renpy.random.choice(ros_rnd1[0]) + renpy.random.choice(ros_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 12:
                while True:
                    tmp = ("nan " + renpy.random.choice(nan_rnd1[0]) + renpy.random.choice(nan_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 4
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 4
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_yomiage2():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1, 3)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                while True:
                    tmp = ("but " + renpy.random.choice(but_rnd2[0]) + renpy.random.choice(but_rnd2[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("bea " + renpy.random.choice(bea_rnd1[0]) + renpy.random.choice(bea_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("ron " + renpy.random.choice(ron_rnd1[0]) + renpy.random.choice(ron_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_yomiage3():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1, 3)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                tmp = renpy.random.choice(ber_rnd1)
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("bea " + renpy.random.choice(bea_rnd1[0]) + renpy.random.choice(bea_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("lam " + renpy.random.choice(lam_rnd1[0]) + renpy.random.choice(lam_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_siesuta():
        global tmp1
        global tmp2
        global tmp3
        tmp15 = 1
        while tmp15 <= 3:
            rand = renpy.random.randint(1, 3)
            if tmp15 == 2:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
            elif tmp15 == 3:
                if rand == tmp16:
                    tmp15-=1
                    rand = 0
                elif rand == tmp26:
                    tmp15-=1
                    rand = 0
    #        if tmp15 == 1:
    #            tmp1 = rand
    #        if tmp15 == 2:
    #            tmp2 = rand
            
            if rand == 1:
                while True:
                    tmp = ("s00 " + renpy.random.choice(s00_rnd1[0]) + renpy.random.choice(s00_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 1
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 1
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 2:
                while True:
                    tmp = ("s45 " + renpy.random.choice(s45_rnd1[0]) + renpy.random.choice(s45_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 2
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 2
                elif tmp15 == 3:
                    tmp3 = tmp
            
            elif rand == 3:
                while True:
                    tmp = ("s41 " + renpy.random.choice(s41_rnd1[0]) + renpy.random.choice(s41_rnd1[1]))
                    if renpy.has_image(tmp):
                        break
                if tmp15 == 1:
                    tmp1 = tmp
                    tmp16 = 3
                elif tmp15 == 2:
                    tmp2 = tmp
                    tmp26 = 3
                elif tmp15 == 3:
                    tmp3 = tmp
            
            tmp15+=1
        return

    def bgm_mode_rnd_bg1():
        global tmp
        global tmp_bg
        rnd = renpy.random.randint(1,14)
        if rnd == 1:
            tmp = 'ship_p1a'
            tmp_bg = 'tmp_null'
        elif rnd == 2:
            tmp = 'ship_p1c'
            tmp_bg = 'tmp_null'
        elif rnd == 3:
            tmp = 'ship_s2af'
            tmp_bg = 'tmp_null'
        elif rnd == 4:
            tmp = 'ship_s2bf'
            tmp_bg = 'tmp_null'
        elif rnd == 5:
            tmp = 'rose_1af'
            tmp_bg = 'tmp_null'
        elif rnd == 6:
            tmp = 'rose_1cf'
            tmp_bg = 'tmp_null'
        elif rnd == 7:
            tmp = 'rose_g1c'
            tmp_bg = 'tmp_null'
        elif rnd == 8:
            tmp = 'glob_1d_bg'
            tmp_bg = 'glob_1d'
        elif rnd == 9:
            tmp = 'g2f_r1a_bg'
            tmp_bg = 'g2f_r1a'
        elif rnd == 10:
            tmp = 'g2f_r1c'
            tmp_bg = 'tmp_null'
        elif rnd == 11:
            tmp = 'sky_2b'
            tmp_bg = 'tmp_null'
        elif rnd == 12:
            tmp = 'sky_1a'
            tmp_bg = 'tmp_null'
        elif rnd == 13:
            tmp = 'beach_1a'
            tmp_bg = 'tmp_null'
        elif rnd == 14:
            tmp = 'beach_2a'
            tmp_bg = 'tmp_null'
        return

    def bgm_mode_rnd_bg_mhal():
        global tmp
        global tmp_bg
        rnd = renpy.random.randint(1,6)
        if rnd == 1:
            tmp = 'mhal_1c'
            tmp_bg = 'tmp_null'
        elif rnd == 2:
            tmp = 'mhal_2a_bg'
            tmp_bg = 'mhal_2a'
        elif rnd == 3:
            tmp = 'mdin_1e'
            tmp_bg = 'tmp_null'
        elif rnd == 4:
            tmp = 'mlib_1e'
            tmp_bg = 'tmp_null'
        elif rnd == 5:
            tmp = 'mnat_2g'
            tmp_bg = 'tmp_null'
        elif rnd == 6:
            tmp = 'm2f_p1c_bg'
            tmp_bg = 'm2f_p1c'
        return

    def bgm_mode_rnd_bg_mhal2():
        global tmp
        global tmp_bg
        rnd = renpy.random.randint(1,13)
        if rnd == 1:
            tmp = 'mhal_1c'
            tmp_bg = 'tmp_null'
        elif rnd == 2:
            tmp = 'mhal_2a_bg'
            tmp_bg = 'mhal_2a'
        elif rnd == 3:
            tmp = 'mdin_1e'
            tmp_bg = 'tmp_null'
        elif rnd == 4:
            tmp = 'mlib_1e'
            tmp_bg = 'tmp_null'
        elif rnd == 5:
            tmp = 'mnat_2g'
            tmp_bg = 'tmp_null'
        elif rnd == 6:
            tmp = 'm2f_p1c_bg'
            tmp_bg = 'm2f_p1c'
        elif rnd == 7:
            tmp = 'm1f_p2b_bg'
            tmp_bg = 'm1f_p2b'
        elif rnd == 8:
            tmp = 'm1f_s1a_bg'
            tmp_bg = 'm1f_s1a'
        elif rnd == 9:
            tmp = 'm1f_s1c'
            tmp_bg = 'tmp_null'
        elif rnd == 10:
            tmp = 'mlib_1b_bg'
            tmp_bg = 'mlib_1b'
        elif rnd == 11:
            tmp = 'mlib_1c_bg'
            tmp_bg = 'mlib_1c'
        elif rnd == 12:
            tmp = 'mlib_1a_bg'
            tmp_bg = 'mlib_1a'
        elif rnd == 13:
            tmp = 'msta_1b_bg'
            tmp_bg = 'msta_1b'
        return


## sound effects

image tmp_null = "saveload/load_null.png"

define se01 = "se/A5_06196.ogg"
define se02 = "se/A5_02047.ogg"
define se03 = "se/A1_16258.ogg"
define se04 = "se/A1_17270.ogg"
define se05 = "se/A5_08263.ogg"
define se06 = "se/A1_07130.ogg"
define se07 = "se/A1_07131.ogg"
define se08 = "se/A1_07132.ogg"
define se09 = "se/A1_07133.ogg"
define se10 = "se/A5_04105.ogg"
define se11 = "se/A5_04107.ogg"
define se12 = "se/A5_10316.ogg"
define se13 = "se/A5_10317.ogg"
define se14 = "se/A1_21333.ogg"
define se15 = "se/A5_01023.ogg"
define se16 = "se/door_slam2.ogg"
define se17 = "se/A5_07201.ogg"
define se18 = "se/A5_07202.ogg"
define se19 = "se/knock2.ogg"
define se20 = "se/A5_10315.ogg"
define se21 = "se/distant_thunder2.ogg"
define se22 = "se/horror.ogg"
define se23 = "se/clock_grand_fathers3.ogg"
define se24 = "se/07_se_umi.ogg"
define se25 = "se/A6_24636.ogg"
define se26 = "se/05_se_umi.ogg"
define se27 = "se/lightning3.ogg"
define se28 = "se/SE4.ogg"
define se29 = "me/telephone2_far.ogg"
define se30 = "se/reload_fast.ogg"
define se31 = "se/key_ring2.ogg"
define se32 = "se/chain.ogg"
define se33 = "se/02se_umi.ogg"
define se34 = "se/01se_umi.ogg"
define se35 = "se/blood4.ogg"
define se36 = "se/clash.ogg"
define se37 = "se/ahaha.ogg"
define se38 = "se/lowclick.ogg"
define se39 = "se/dropped_hatchet.ogg"
define se40 = "se/metal_pipe_hit.ogg"
define se41 = "se/metal_pipe_hitB.ogg"
define se42 = "se/metal_pipe_hitC.ogg"
define se43 = "se/reload_slow.ogg"
define se44 = "se/auto_lock5.ogg"
define se45 = "se/03se_umi.ogg"
define se46 = "se/raihuru3d.ogg"
define se47 = "se/B1.ogg"
define se48 = "se/B5.ogg"
define se49 = "se/shutter_reverb1.ogg"
define se50 = "se/shutter_close_reverb1.ogg"
define se51 = "se/bell1.ogg"
define se52 = "se/teleport1.ogg"
define se53 = "se/phone_hangup.ogg"
define se54 = "se/applause1.ogg"
define se55 = "se/river_(evap2).ogg"
define se56 = "se/Z1.ogg"
define se57 = "se/barrier_deploy_03.ogg"
define se58 = "se/close_game.ogg"
define se59 = "se/barrier_deploy_02.ogg"

define se60 = "se/heavy_impact1.ogg"
define se61 = "se/heavy_impact2.ogg"
define se62 = "se/heavy_impact3.ogg"
define se63 = "se/impact.ogg"
define se64 = "se/B4.ogg"
define se65 = "se/B_long.ogg"

define se66 = "se/approaching_barrage.ogg"
define se67 = "se/04_se_umi.ogg"

define se68 = "se/car_skid.ogg"
define se69 = "se/school_bell.ogg"
define se70 = "se/ping_pong2.ogg"
define se71 = "se/24hour_chime.ogg"

define se72 = "se/large_sword_slash_01.ogg"
define se73 = "se/large_sword_slash_02.ogg"
define se74 = "se/large_sword_slash_03.ogg"
define se75 = "se/teleportation_06.ogg"

define se76 = "se/applause.ogg"
define se77 = "se/spotlights1.ogg"
define se78 = "se/gorilla3_d.ogg"
define se79 = "se/shattering_jewels1.ogg"
define se80 = "se/shattering_jewels5.ogg"
define se81 = "se/shutter_d.ogg"

define se1000 = "sys_se/zyosys7.ogg"
define se1001 = "sys_se/zyosys1.ogg"
define se1002 = "sys_se/zyosys0.ogg"

define se1005 = "sys_se/zyosys3.ogg"
define se1006 = "sys_se/ZS1.ogg"

define se1010 = "sys_se/page.ogg"

define se1020 = "sys_se/ZS1.ogg"
define se1021 = "sys_se/one_re.ogg"
define se1022 = "sys_se/ZS1.ogg"
define se1023 = "sys_se/Z2.ogg"

define se1030 = "sys_se/mizu_d.ogg"
define se1031 = "sys_se/mizu_d2.ogg"

define se1040 = "sys_se/da_kane.ogg"

define se1050 = "sys_se/clock_ticking.ogg"
define se1051 = "sys_se/screw.ogg"
define se1052 = "sys_se/da_kane2.ogg"

define se1060 = "sys_se/KT1.ogg"
define se1061 = "sys_se/mizu_ijou.ogg"
define se1062 = "sys_se/KT1.ogg"
define se1063 = "sys_se/mizu_ijou.ogg"

define se_ex01 = "se/umise_ex01.ogg"
define se_ex02 = "se/umise_ex02.ogg"
define se_ex03 = "se/umise_ex03.ogg"


## music effects

define me01 = "me/A1_03052.ogg"
define me02 = "me/A3_05051.ogg"
define me03 = "me/A3_05045.ogg"
define me04 = "me/A1_03055.ogg"
define me05 = "me/A3_01005.ogg"
define me06 = "me/A3_02012.ogg"
define me07 = "me/A5_01033.ogg"
define me08 = "me/A1_12222.ogg"
#define me09 = "me/A5_08234.ogg"
#define me10 = "me/A5_14445.ogg"
define me11 = "me/clock_L4.ogg"
define me12 = "me/rain2.ogg"
define me13 = "me/Rain4_Long.ogg"
define me14 = "me/STORM2.ogg"
define me15 = "me/clock_grand.ogg"
define me16 = "me/A5_14446.ogg"
define me17 = "me/flangingstorm.ogg"
define me18 = "me/flangingwind.ogg"
define me19 = "me/clock_flanging3.ogg"
define me20 = "me/boiler.ogg"
define me21 = "me/flangefemale.ogg"
define me22 = "me/telephone2_far.ogg"
define me23 = "me/telephone2.ogg"
define me24 = "me/crowd.ogg"
define me25 = "me/train3.ogg"
define me26 = "me/waterdrops_cave.ogg"
define me27 = "me/waterflow_cave.ogg"

define me55 = "se/river_(evap2).ogg"

define me28 = "me/wind_break.ogg"
define me29 = "me/city_traffic.ogg"
define me30 = "me/city_traffic2.ogg"

define me1050 = "sys_se/clock_ticking.ogg"
define me1051 = "sys_se/screw.ogg"
define me1052 = "sys_se/clock_bell_wall.ogg"
define me1053 = "sys_se/clock_bell_wall2.ogg"



init:
    python:
        
        play_i = im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,0,80,50)), im.matrix.colorize("#000","#969696"))
        play_h = im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,0,80,50)), im.matrix.colorize("#000","#f00"))
        play_s_i = im.Crop("bgmmode/buttons.png", (0,0,80,50))
        
        stop_i = im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,50,80,50)), im.matrix.colorize("#000","#969696"))
        stop_h = im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,50,80,50)), im.matrix.colorize("#000","#f00"))
        stop_s_i = im.Crop("bgmmode/buttons.png", (0,50,80,50))
        
        shuffle_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,100,115,50)), im.matrix.colorize("#000","#969696")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,100,224,50)), im.matrix.colorize("#000","#969696")))
        shuffle_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,100,115,50)), im.matrix.colorize("#000","#f00")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,100,224,50)), im.matrix.colorize("#000","#f00")))
        shuffle_s_i = ConditionSwitch("_preferences.language == None", im.Crop("bgmmode/buttons.png", (0,100,115,50)), "_preferences.language == 'japanese'", im.Crop("bgmmode/buttons.png", (0,100,224,50)))
        
        repeat_1_i = im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,150,205,50)), im.matrix.colorize("#000","#969696"))
        repeat_1_h = im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,150,205,50)), im.matrix.colorize("#000","#f00"))
        repeat_1_s_i = im.Crop("bgmmode/buttons.png", (0,150,205,50))
        
        repeat_a_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,200,235,50)), im.matrix.colorize("#000","#969696")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,200,224,50)), im.matrix.colorize("#000","#969696")))
        repeat_a_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,200,235,50)), im.matrix.colorize("#000","#f00")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,200,224,50)), im.matrix.colorize("#000","#f00")))
        repeat_a_s_i = ConditionSwitch("_preferences.language == None", im.Crop("bgmmode/buttons.png", (0,200,235,50)), "_preferences.language == 'japanese'", im.Crop("bgmmode/buttons.png", (0,200,224,50)))
        
        all_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,250,140,50)), im.matrix.colorize("#000","#969696")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,250,152,50)), im.matrix.colorize("#000","#969696")))
        all_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,250,140,50)), im.matrix.colorize("#000","#f00")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (0,250,152,50)), im.matrix.colorize("#000","#f00")))
        all_s_i = ConditionSwitch("_preferences.language == None", im.Crop("bgmmode/buttons.png", (0,250,140,50)), "_preferences.language == 'japanese'", im.Crop("bgmmode/buttons.png", (0,250,152,50)))
        
        back_i = ConditionSwitch("_preferences.language == None", im.Crop("bgmmode/buttons.png", (160,0,208,50)), "_preferences.language == 'japanese'", im.Crop("bgmmode/buttons.png", (124,0,244,50)))
        back_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (160,0,208,50)), im.matrix.colorize("#000","#f00")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (124,0,244,50)), im.matrix.colorize("#000","#f00")))
        
        next_i = ConditionSwitch("_preferences.language == None", im.Crop("bgmmode/buttons.png", (154,50,214,50)), "_preferences.language == 'japanese'", im.Crop("bgmmode/buttons.png", (124,50,244,50)))
        next_h = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("bgmmode/buttons.png", (154,50,214,50)), im.matrix.colorize("#000","#f00")), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("bgmmode/buttons.png", (124,50,244,50)), im.matrix.colorize("#000","#f00")))
        
        bgm_exit_i = im.MatrixColor(im.Crop("bgmmode/buttons.png", (288,250,80,50)), im.matrix.colorize("#000","#969696"))
        bgm_exit_h = im.MatrixColor(im.Crop("bgmmode/buttons.png", (288,250,80,50)), im.matrix.colorize("#000","#f00"))
        bgm_exit_s_i = im.Crop("bgmmode/buttons.png", (288,250,80,50))
        