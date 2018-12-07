## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 1920
    config.screen_height = 1080

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Umineko no Naku Koro ni"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "A Ren'Py Game"
    config.version = "0.0"
    
    config.layers = [ 'master', 'transient', 'cg', 'cg2', 'cg3', 'meta', 'meta2', 'cinema', 'screens', 'cinema2', 'overlay' ]
    

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

#    theme.tv(
#        ## Theme: TV
#        ## Color scheme: Dramatic Flesh
                                    
#        ## The color of an idle widget face.
#        widget = "#BF7C51",

#        ## The color of a focused widget face.
#        widget_hover = "#dda570",

#        ## The color of the text in a widget.
#        widget_text = "#E5DFDF",

#        ## The color of the text in a selected widget. (For
#        ## example, the current value of a preference.)
#        widget_selected = "#ffffff",

#        ## The color of a disabled widget face. 
#        disabled = "#ab6038",

#        ## The color of disabled widget text.
#        disabled_text = "#BF7C51",

#        ## The color of informational labels.
#        label = "#ffffff",

#        ## The color of a frame containing widgets.
#        frame = "#49271b",

#        ## The background of the main menu. This can be a color
#        ## beginning with '#', or an image filename. The latter
#        ## should take up the full height and width of the screen.
#        mm_root = "efe/Untitled2.png",

#        ## The background of the game menu. This can be a color
#        ## beginning with '#', or an image filename. The latter
#        ## should take up the full height and width of the screen.
##        gm_root = "efe/Untitled.png",
#        gm_root = Null(),

#        ## If this is True, the in-game window is rounded. If False,
#        ## the in-game window is square.
#        rounded_window = False,

#        ## And we're done with the theme. The theme will customize
#        ## various styles, so if we want to change them, we should
#        ## do so below.            
#        )
    theme.ancient()

#    theme.outline(
#        inside="#fff",
#        idle="#e66",
#        hover="#48f",
#        selected="#84f",
#        insensitive="#ccc",
#        label="#484",
#        prompt="#484",
#        background="#fee",
#        large_button="#fff8f8",
#        text_size=40,
#        small_text_size=40
#        )

    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

#    if persistent.msgwnd == 1:
#        style.window.background = Frame("efe/msgwnd.png", 25, 25)
#    elif persistent.msgwnd == 4:
#        style.window.background = Frame("efe/msgwnd4.png", 25, 25)
#    style.window.background = Frame("efe/msgwnd.png", 16, 16)
#    style.say_who_window.background = Frame("efe/chrwnd3.png", 25, 25)
    style.nvl_window.background = Frame("efe/Untitled2.png", 25, 25)
#    style.nvl_window.background = Image("efe/Untitled.png", xalign=0.5, yalign=0.5)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

#    style.window.left_margin = 113
#    style.window.right_margin = 113
##    style.window.top_margin = 6
#    style.window.bottom_margin = 0
    
    style.nvl_window.left_margin = 150
    style.nvl_window.right_margin = 150
    style.nvl_window.top_margin = 165
    
#    style.say_who_window.left_margin = 150
    

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 150
    style.window.right_padding = 150
    style.window.top_padding = 25
    style.window.bottom_padding = 25
    
    style.nvl_window.left_padding = 10
    style.nvl_window.right_padding = 10
    style.nvl_window.top_padding = 6
    
    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 390
    style.say_who_window.yminimum = 0
    style.say_who_window.ypos = 140
    style.nvl_window.ypos = -0.1
    


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

#    style.default.font = "msgothic.ttc"

    ## The default size of text.

#    style.default.size = 40

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.
    
#    style.default.drop_shadow = [(1, 1)]
    
    style.button_text.color = "#b7b7b7"
    style.button_text.hover_color = "#ff1d1d"
    style.button_text.insensitive_color = (192, 192, 192, 255)
    style.button_text.size = 40
    style.button_text.drop_shadow = (2, 2)
    style.button_text.drop_shadow_color = "#000"

    style.button_text.selected_color = "#ffffff"
    style.button_text.selected_hover_color = "#ff1d1d"
    style.button_text.font = "msgothic.ttc"
    


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.ogg"
    # style.imagemap.activate_sound = "click.ogg"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.ogg"
    # config.exit_sound = "click.ogg"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.ogg"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"
    #config.main_menu_music = "ME/A3_05051.ogg"
    
    if persistent.UMINEKOEND < 50:
        config.main_menu_music = "bgm/umilse_002.ogg"
    elif persistent.UMINEKOEND >= 50:
        config.main_menu_music = "bgm4/umilse_016.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = ImageDissolve("efe/right.png", 0.5, 256)    ## 386?

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = ImageDissolve("efe/right.png", 0.5, 256)

    ## Used when the window is shown.
    config.window_show_transition = Dissolve(.16)                #Dissolve(.25)

    ## Used when the window is hidden.
    config.window_hide_transition = Dissolve(.16)                #Dissolve(.25)
    
    config.imagemap_cache = False
#    config.imagemap_cache = True                ## change to false if cache gets bloated?
    
#    config.thumbnail_height = 150     ## for original saveload slots
#    config.thumbnail_width = 267      ## for original saveload slots
#    config.thumbnail_height = 161     ## for new saveload slots
#    config.thumbnail_width = 286      ## for new saveload slots
    config.thumbnail_height = 180      ## for PS3 saveload slots
    config.thumbnail_width = 320       ## for PS3 saveload slots
#    config.load_save_empty_thumbnail = "saveload/nodata.png"


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "Umineko no Naku Koro ni-1365047857"

init:
    style say_who_window:
        xminimum 200
        yminimum 34
        xfill True
        xalign 0
        
init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 50                ##default = 0
    
    config.emphasize_audio_channels = [ 'dummy' ]
    config.emphasize_audio_time = 0.3
    config.emphasize_audio_volume = 0.5
    config.autosave_on_quit = False
    config.autosave_slots = 1
    
#    config.default_afm_time = ???
#    _preferences.set_volume("music", 0.75)              ## might be a potential problem? and refer to splashscreen python

    #########################################
    ## More customizations can go here.
    
    style.say_dialogue.outlines = [(1, "#000000", 0, 0)]
    style.say_thought.outlines = [(1, "#000000", 0, 0)]
    style.say_label.outlines = [(1, "#000000", 0, 0)]
    style.nvl_dialogue.outlines = [(1, "#000000", 0, 0)]
    
    style.say_label.bold = False
    
    style.say_dialogue.size = 46
    style.say_thought.size = 46
    style.say_label.size = 46
    style.nvl_dialogue.size = 46
    
    style.say_dialogue.font = "default.ttf"
    style.say_thought.font = "default.ttf"
    style.say_label.font = "default.ttf"
    style.nvl_dialogue.font = "default.ttf"
    
#    style.say_dialogue.color = "#e0e0e0"
#    style.say_thought.color = "#e0e0e0"
#    style.say_label.color = "#e0e0e0"
#    style.nvl_dialogue.color = "#e0e0e0"
    
    style.say_dialogue.color = "#ffffff"
    style.say_thought.color = "#ffffff"
    style.say_label.color = "#ffffff"
    style.nvl_dialogue.color = "#ffffff"
    
    style.say_dialogue.drop_shadow = [(2,2)]
    style.say_thought.drop_shadow = [(2,2)]
    style.say_label.drop_shadow = [(2,2)]
    style.nvl_dialogue.drop_shadow = [(2,2)]
    
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 46
    style.ruby_style.yoffset = -30
    style.ruby_style.line_leading = 12
    
    ### use this · for ruby instead? ###

    
    style.default.ruby_style = style.ruby_style
    style.ruby_style.font = "default.ttf"
    
    config.window_icon = "icon.png"
    config.voice_filename_format = "voice/{filename}.ogg"
    config.has_autosave = False
#    config.mouse = { 'default' : [ ('mouse.png', 0, 0)] }
    config.mouse = { 'default' : [ ('mouse_aero.png', 0, 0)] }
#    config.nvl_page_ctc = "keywait2"
    
init python:

#    style.button_text['chp_choice'].color = "#808080"
#    style.button_text['chp_choice'].hover_color = "#ffffff"
#    style.button_text['chp_choice'].insensitive_color = (255, 255, 255, 255)
#    style.button_text['chp_choice'].size = 60
#    style.button_text['chp_choice'].drop_shadow = (2, 2)
#    style.button_text['chp_choice'].drop_shadow_color = "#000"

#    style.button_text['chp_choice'].selected_color = "#ffffff"
#    style.button_text['chp_choice'].selected_hover_color = "#ff1d1d"
#    style.button_text['chp_choice'].font = "default.ttf"
#    style.button_text['chp_choice'].xalign = 0.0
#    style.button_text['chp_choice'].text_align = 0.0
    
#    style.button_text['chp_sel'].color = "#808080"
#    style.button_text['chp_sel'].hover_color = "#ffffff"
#    style.button_text['chp_sel'].size = 40
#    style.button_text['chp_sel'].drop_shadow = (2, 2)
#    style.button_text['chp_sel'].drop_shadow_color = "#000"

#    style.button_text['chp_sel'].font = "default.ttf"
#    style.button_text['chp_sel'].xalign = 0.0
#    style.button_text['chp_sel'].text_align = 0.0
    
#    style.button_text['tips'].color = "#525252"
#    style.button_text['tips'].hover_color = "#ffffff"
#    style.button_text['tips'].insensitive_color = (82, 82, 82, 255)
#    style.button_text['tips'].size = 45
#    style.button_text['tips'].drop_shadow = (2, 2)
##    style.button_text['tips'].drop_shadow_color = "#000"
#    style.button_text['tips'].outlines = [(2, "#000000", 2, 2)]
#    style.button_text['tips'].selected_color = "#ffffff"
#    style.button_text['tips'].selected_hover_color = "#ffffff"
#    style.button_text['tips'].font = "times.ttf"
#    style.button_text['tips'].xalign = 0.0
#    style.button_text['tips'].text_align = 0.0
    
    style.vscrollbar.xmaximum = 20
    style.vscrollbar.top_bar = "#29162b"
    style.vscrollbar.bottom_bar = "#29162b"
    style.vscrollbar.thumb = "#6a6376"
    style.vscrollbar.thumb_offset = 0
    style.vscrollbar.thumb_shadow = None
    style.vscrollbar.unscrollable = "hide"
    
#    style.vscrollbar.xmaximum = 22
#    style.vscrollbar.top_bar = Solid("#0008")
#    style.vscrollbar.bottom_bar = Solid("#0008")
#    style.vscrollbar.thumb = Solid("#e8a04a")
#    style.vscrollbar.thumb_offset = 0
#    style.vscrollbar.thumb_shadow = None


#style default:    ## copied over from portable 1, can't remember what it's for
#    size 25


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Umineko no Naku Koro ni-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Umineko no Naku Koro ni"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    