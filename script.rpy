# This prevents the {nw} tag from waiting for voices
define config.nw_voice = False

# You can place the script of your game in this file.

init:
    
    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
        
        class Shakex(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, xanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), 0)
                
        def _Shakx(start, time, child=None, dist=100.0, **properties):

            move = Shakex(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shakx = renpy.curry(_Shakx)
        
        class Shakey(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                ypos = ypos - yanchor
                
                nx = 0
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shaky(start, time, child=None, dist=100.0, **properties):

            move = Shakey(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shaky = renpy.curry(_Shaky)
        
    ##random noise
        class NonUniformRandom(object):
            def __init__(self, list_of_values_and_probabilities):
                """
                expects a list of [ (value, probability), (value, probability),...]
                """
                self.the_list = list_of_values_and_probabilities
                self.the_sum = sum([ v[1] for v in list_of_values_and_probabilities])

            def pick(self):
                """
                return a random value taking into account the probabilities
                """
                import random
                r = random.uniform(0, self.the_sum)
                s = 0.0
                for k, w in self.the_list:
                    s += w
                    if r < s: return k
                return k
                
#        se1100 = NonUniformRandom( [('sys_se/ZS1.ogg', 6), ('sys_se/ZS2.ogg',5), ('sys_se/ZS3.ogg',4), ('sys_se/ZS4.ogg',3), ('sys_se/ZS5.ogg',2), ('sys_se/ZS6.ogg',1)] )        
        se1100 = NonUniformRandom( [('sys_se/ZS1.ogg', 3), ('sys_se/ZS2.ogg',3), ('sys_se/ZS3.ogg',3), ('sys_se/ZS4.ogg',3), ('sys_se/ZS5.ogg',3), ('sys_se/ZS6.ogg',3)] )
    #
    
    $ config.layer_clipping['cg2'] = (0, 235, 1920, 615)
    $ config.layer_clipping['cg3'] = (0, 235, 1920, 610)
    
#    $ left = Position(xpos=(590.0/1920.0))
#    $ far_left = Position(xpos=(410.0/1920.0))
#    $ center = Position(xpos=0.5)
#    $ right = Position(xpos=(1330.0/1920.0))
#    $ far_right = Position(xpos=(1510.0/1920.0))
    #$ top = Position(xpos=0.5, xanchor='center', ypos=0.0,
    #               yanchor='top')
    
    $ clock_reg = False
    $ clock_large = False
    $ button_show = False
    $ BtnRes = 0
    $ scenario_Number = 0
    $ config_pg = 1
    $ skip_id = 0
    $ rain_static = 0
    $ easter_egg = 0
    
    $ ep_unlock = 0
    $ min3 = 0
    $ clock_size = 0
    $ clock_x = 0
    $ clock_y = 0
    $ clock_reverse = 0
    $ clock_special = 0
    
    $ config_msgwnd = 0
    
    # Define some new transitions here.
    $ t2 = Dissolve(1.0)
    $ t22 = Dissolve(0.4)
    $ t42 = Dissolve(3.0)
    $ t62 = Dissolve(0.2)
    $ t80 = Dissolve(0.2)
    
    $ t3 = ImageDissolve("efe/right.png", 1.3, 256)
    $ t23 = ImageDissolve("efe/right.png", 0.5, 256)
    $ t43 = ImageDissolve("efe/right.png", 3.0, 256)
    $ t63 = ImageDissolve("efe/right.png", 0.3, 64)
    $ t83 = ImageDissolve("efe/right.png", 0.005, 64)
    
    $ t4 = ImageDissolve("efe/left.png", 1.3, 256)
    $ t24 = ImageDissolve("efe/left.png", 0.5, 256)
    $ t44 = ImageDissolve("efe/left.png", 3.0, 256)
    $ t64 = ImageDissolve("efe/left.png", 0.3, 64)
    $ t84 = ImageDissolve("efe/left.png", 0.005, 64)
    
    $ t5 = ImageDissolve("efe/down.png", 1.3, 256)
    $ t25 = ImageDissolve("efe/down.png", 0.5, 256)
    $ t45 = ImageDissolve("efe/down.png", 3.0, 256)
    $ t65 = ImageDissolve("efe/down.png", 0.3, 64)
    $ t85 = ImageDissolve("efe/down.png", 0.005, 64)
    
    $ t6 = ImageDissolve("efe/up.png", 1.3, 256)
    $ t26 = ImageDissolve("efe/up.png", 0.5, 256)
    $ t46 = ImageDissolve("efe/up.png", 3.0, 256)
    $ t66 = ImageDissolve("efe/up.png", 0.3, 64)
    $ t86 = ImageDissolve("efe/up.png", 0.005, 64)
    
    $ t7 = ImageDissolve("efe/x.png", 1.3, 256, reverse=True)
    $ t27 = ImageDissolve("efe/x.png", 0.5, 256, reverse=True)
    $ t47 = ImageDissolve("efe/x.png", 3.0, 256, reverse=True)
    $ t67 = ImageDissolve("efe/x.png", 0.3, 64, reverse=True)
    
    $ t8 = ImageDissolve("efe/c.png", 1.3, 256, reverse=True)
    $ t28 = ImageDissolve("efe/c.png", 0.5, 256, reverse=True)
    $ t48 = ImageDissolve("efe/c.png", 3.0, 256, reverse=True)
    $ t68 = ImageDissolve("efe/c.png", 0.3, 64, reverse=True)
    $ t88 = ImageDissolve("efe/c.png", 0.001, 256, reverse=True)
    
    $ t9 = ImageDissolve("efe/m1.png", 1.3, 256, reverse=True)
    $ t29 = ImageDissolve("efe/m1.png", 0.5, 256, reverse=True)
    $ t49 = ImageDissolve("efe/m1.png", 3.0, 256, reverse=True)
    $ t69 = ImageDissolve("efe/m1.png", 0.3, 64, reverse=True)
    
    $ t10 = ImageDissolve("efe/1.png", 3.0, 256, reverse=True)
    $ t30 = ImageDissolve("efe/1.png", 0.3, 256, reverse=True)
    $ t50 = ImageDissolve("efe/1.png", 3.0, 256, reverse=True)
    $ t18 = ImageDissolve("efe/1.png", 1.2, 256, reverse=True)          ## remove this?
    
    $ t11 = ImageDissolve("efe/2.png", 3.0, 256, reverse=True)
    $ t31 = ImageDissolve("efe/2.png", 0.3, 256, reverse=True)
    
    $ tquit = ImageDissolve("title/kannon_r.png", 3.0, 256, reverse=True)
    
    $ blood_2a_efe = ImageDissolve("efe/blood_2a_efe.png", 1.0, 256, reverse=True)                ## change to 1?
    $ blood_2a_efe_2000 = ImageDissolve("efe/blood_2a_efe.png", 2.0, 256, reverse=True)
    $ blood_2a_efe_3000 = ImageDissolve("efe/blood_2a_efe.png", 3.0, 256, reverse=True)
    $ blood_2a_efe_5000 = ImageDissolve("efe/blood_2a_efe.png", 5.0, 256, reverse=True)
    $ blood_2a_efe_300 = ImageDissolve("efe/blood_2a_efe.png", 0.3, 256, reverse=True)
    
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    # Imagedissolve Transitions.
    $ circlewipe = ImageDissolve("efe/id_circlewipe.png", 1.0, 32)
    $ dream = ImageDissolve("efe/id_dream.png", 2.0, 256)
    $ teleport = ImageDissolve("efe/id_teleport.png", 1.0, 0)
    $ wipedown_slow = CropMove(1.5, "wipedown_slow")
    $ wipeup_slow = CropMove(1.5, "wipeup_slow")
    $ slideup = CropMove(0.3, "slideup")
    $ spiral = ImageDissolve("efe/id_cholfingers.png", 3.0, 256)
    $ whirl_700 = ImageDissolve("efe/id_cholfingers.png", 0.7, 256)
    $ whirl_2000 = ImageDissolve("efe/id_cholfingers.png", 2.0, 256)
    $ whirl_3000 = ImageDissolve("efe/id_cholfingers.png", 3.0, 256)
    $ whirl_5000 = ImageDissolve("efe/id_cholfingers.png", 5.0, 256)
    $ breakup_300 = ImageDissolve(im.Tile("efe/noisetile.png"), 0.3, 1)
    $ breakup_500 = ImageDissolve(im.Tile("efe/noisetile.png"), 0.5, 1)
    $ breakup_700 = ImageDissolve(im.Tile("efe/noisetile.png"), 0.7, 1)
    $ breakup_1000 = ImageDissolve(im.Tile("efe/noisetile.png"), 1.0, 1)
    $ breakup_1500 = ImageDissolve(im.Tile("efe/noisetile.png"), 1.5, 1)
    $ breakup_2000 = ImageDissolve(im.Tile("efe/noisetile.png"), 2.0, 1)
    $ breakup_2500 = ImageDissolve(im.Tile("efe/noisetile.png"), 2.5, 1)
    $ breakup_3000 = ImageDissolve(im.Tile("efe/noisetile.png"), 3.0, 1)
    $ breakup_3500 = ImageDissolve(im.Tile("efe/noisetile.png"), 3.5, 1)
    $ breakup_4000 = ImageDissolve(im.Tile("efe/noisetile.png"), 4.0, 1)
    $ breakup_5000 = ImageDissolve(im.Tile("efe/noisetile.png"), 5.0, 1)
    $ breakup_6000 = ImageDissolve(im.Tile("efe/noisetile.png"), 6.0, 1)
    $ breakup_8000 = ImageDissolve(im.Tile("efe/noisetile.png"), 8.0, 1)
#    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
#    $ quakey_5_600 = Move((0, 50), (0, -50), 0.6, bounce=True, repeat=False)
#    $ quakey_5_1000 = Move((0, 50), (0, -50), 1.0, bounce=True, repeat=False)
#    $ quakey_3_300 = Move((0, 30), (0, -30), 0.3, bounce=True, repeat=False)
#    $ quakey_3_500 = Move((0, 30), (0, -30), 0.5, bounce=True, repeat=False)
#    $ quakey_3_600 = Move((0, 30), (0, -30), 0.6, bounce=True, repeat=False)
#    $ quakey_4_800 = Move((0, 40), (0, -40), 0.8, bounce=True, repeat=False)
    
#    $ quakex_4_600 = Move((40, 0), (-40, 0), 0.6, bounce=True, repeat=False)
    
    $ quakey_1_50 = Shaky((0, 0, 0, 0), 0.05, dist=10)
    $ quakey_1_100 = Shaky((0, 0, 0, 0), 0.1, dist=10)
    $ quakey_1_200 = Shaky((0, 0, 0, 0), 0.2, dist=10)
    $ quakey_1_300 = Shaky((0, 0, 0, 0), 0.3, dist=10)
    $ quakey_1_400 = Shaky((0, 0, 0, 0), 0.4, dist=10)
    $ quakey_1_700 = Shaky((0, 0, 0, 0), 0.7, dist=10)
    $ quakey_2_100 = Shaky((0, 0, 0, 0), 0.1, dist=45)
    $ quakey_2_150 = Shaky((0, 0, 0, 0), 0.15, dist=45)
    $ quakey_2_200 = Shaky((0, 0, 0, 0), 0.2, dist=45)
    $ quakey_2_250 = Shaky((0, 0, 0, 0), 0.25, dist=45)
    $ quakey_2_300 = Shaky((0, 0, 0, 0), 0.3, dist=45)
    $ quakey_2_400 = Shaky((0, 0, 0, 0), 0.4, dist=45)
    $ quakey_2_500 = Shaky((0, 0, 0, 0), 0.5, dist=45)
    $ quakey_2_600 = Shaky((0, 0, 0, 0), 0.6, dist=45)
    $ quakey_2_700 = Shaky((0, 0, 0, 0), 0.7, dist=45)
    $ quakey_3_050 = Shaky((0, 0, 0, 0), 0.05, dist=67)
    $ quakey_3_100 = Shaky((0, 0, 0, 0), 0.1, dist=67)
    $ quakey_3_200 = Shaky((0, 0, 0, 0), 0.2, dist=67)
    $ quakey_3_300 = Shaky((0, 0, 0, 0), 0.3, dist=67)
    $ quakey_3_400 = Shaky((0, 0, 0, 0), 0.4, dist=67)
    $ quakey_3_500 = Shaky((0, 0, 0, 0), 0.5, dist=67)
    $ quakey_3_600 = Shaky((0, 0, 0, 0), 0.6, dist=67)
    $ quakey_3_700 = Shaky((0, 0, 0, 0), 0.7, dist=67)
    $ quakey_3_800 = Shaky((0, 0, 0, 0), 0.8, dist=67)
    $ quakey_3_900 = Shaky((0, 0, 0, 0), 0.9, dist=67)
    $ quakey_3_1000 = Shaky((0, 0, 0, 0), 1.0, dist=67)
    $ quakey_4_200 = Shaky((0, 0, 0, 0), 0.2, dist=90)
    $ quakey_4_300 = Shaky((0, 0, 0, 0), 0.3, dist=90)
    $ quakey_4_400 = Shaky((0, 0, 0, 0), 0.4, dist=90)
    $ quakey_4_500 = Shaky((0, 0, 0, 0), 0.5, dist=90)
    $ quakey_4_600 = Shaky((0, 0, 0, 0), 0.6, dist=90)
    $ quakey_4_700 = Shaky((0, 0, 0, 0), 0.7, dist=90)
    $ quakey_4_800 = Shaky((0, 0, 0, 0), 0.8, dist=90)
    $ quakey_4_900 = Shaky((0, 0, 0, 0), 0.9, dist=90)
    $ quakey_4_1000 = Shaky((0, 0, 0, 0), 1.0, dist=90)
    $ quakey_4_1200 = Shaky((0, 0, 0, 0), 1.2, dist=90)
    $ quakey_4_1500 = Shaky((0, 0, 0, 0), 1.5, dist=90)
    $ quakey_5_200 = Shaky((0, 0, 0, 0), 0.2, dist=112)
    $ quakey_5_300 = Shaky((0, 0, 0, 0), 0.3, dist=112)
    $ quakey_5_400 = Shaky((0, 0, 0, 0), 0.4, dist=112)
    $ quakey_5_500 = Shaky((0, 0, 0, 0), 0.5, dist=112)
    $ quakey_5_600 = Shaky((0, 0, 0, 0), 0.6, dist=112)
    $ quakey_5_700 = Shaky((0, 0, 0, 0), 0.7, dist=112)
    $ quakey_5_800 = Shaky((0, 0, 0, 0), 0.8, dist=112)
    $ quakey_5_900 = Shaky((0, 0, 0, 0), 0.9, dist=112)
    $ quakey_5_1000 = Shaky((0, 0, 0, 0), 1.0, dist=112)
    $ quakey_5_1200 = Shaky((0, 0, 0, 0), 1.2, dist=112)
    $ quakey_6_400 = Shaky((0, 0, 0, 0), 0.4, dist=135)
    $ quakey_6_500 = Shaky((0, 0, 0, 0), 0.5, dist=135)
    $ quakey_6_600 = Shaky((0, 0, 0, 0), 0.6, dist=135)
    $ quakey_6_700 = Shaky((0, 0, 0, 0), 0.7, dist=135)
    $ quakey_6_800 = Shaky((0, 0, 0, 0), 0.8, dist=135)
    $ quakey_6_900 = Shaky((0, 0, 0, 0), 0.9, dist=135)
    $ quakey_6_1000 = Shaky((0, 0, 0, 0), 1.0, dist=135)
    $ quakey_6_1200 = Shaky((0, 0, 0, 0), 1.2, dist=135)
    $ quakey_7_200 = Shaky((0, 0, 0, 0), 0.2, dist=157)
    $ quakey_7_600 = Shaky((0, 0, 0, 0), 0.6, dist=157)
    $ quakey_7_800 = Shaky((0, 0, 0, 0), 0.8, dist=157)
    $ quakey_7_1000 = Shaky((0, 0, 0, 0), 1.0, dist=157)
    $ quakey_7_1200 = Shaky((0, 0, 0, 0), 1.2, dist=157)
    $ quakey_7_1500 = Shaky((0, 0, 0, 0), 1.5, dist=157)
    $ quakey_8_500 = Shaky((0, 0, 0, 0), 0.5, dist=180)
    $ quakey_8_600 = Shaky((0, 0, 0, 0), 0.6, dist=180)
    $ quakey_8_700 = Shaky((0, 0, 0, 0), 0.7, dist=180)
    $ quakey_8_800 = Shaky((0, 0, 0, 0), 0.8, dist=180)
    $ quakey_8_1000 = Shaky((0, 0, 0, 0), 1.0, dist=180)
    $ quakey_8_1200 = Shaky((0, 0, 0, 0), 1.2, dist=180)
    $ quakey_8_1500 = Shaky((0, 0, 0, 0), 1.5, dist=180)
    $ quakey_9_800 = Shaky((0, 0, 0, 0), 0.8, dist=202)
    $ quakey_9_1200 = Shaky((0, 0, 0, 0), 1.2, dist=202)
    $ quakey_9_1500 = Shaky((0, 0, 0, 0), 1.5, dist=202)
    $ quakey_10_1200 = Shaky((0, 0, 0, 0), 1.2, dist=225)
    $ quakey_12_1500 = Shaky((0, 0, 0, 0), 1.5, dist=270)
    $ quakey_12_2000 = Shaky((0, 0, 0, 0), 2.0, dist=270)
    
    $ quakex_1_50 = Shakx((0, 0), 0.05, dist=10)
    $ quakex_1_100 = Shakx((0, 0), 0.1, dist=10)
    $ quakex_1_200 = Shakx((0, 0), 0.2, dist=10)
    $ quakex_1_300 = Shakx((0, 0), 0.3, dist=10)
    $ quakex_1_400 = Shakx((0, 0), 0.4, dist=10)
    $ quakex_2_100 = Shakx((0, 0), 0.1, dist=45)
    $ quakex_2_200 = Shakx((0, 0), 0.2, dist=45)
    $ quakex_2_250 = Shakx((0, 0), 0.25, dist=45)
    $ quakex_2_300 = Shakx((0, 0), 0.3, dist=45)
    $ quakex_2_400 = Shakx((0, 0), 0.4, dist=45)
    $ quakex_2_500 = Shakx((0, 0), 0.5, dist=45)
    $ quakex_2_600 = Shakx((0, 0), 0.6, dist=45)
    $ quakex_2_800 = Shakx((0, 0), 0.8, dist=45)
    $ quakex_3_100 = Shakx((0, 0), 0.1, dist=67)
    $ quakex_3_200 = Shakx((0, 0), 0.2, dist=67)
    $ quakex_3_300 = Shakx((0, 0), 0.3, dist=67)
    $ quakex_3_400 = Shakx((0, 0), 0.4, dist=67)
    $ quakex_3_500 = Shakx((0, 0), 0.5, dist=67)
    $ quakex_3_600 = Shakx((0, 0), 0.6, dist=67)
    $ quakex_3_700 = Shakx((0, 0), 0.6, dist=67)
    $ quakex_3_800 = Shakx((0, 0), 0.8, dist=67)
    $ quakex_4_200 = Shakx((0, 0), 0.2, dist=90)
    $ quakex_4_300 = Shakx((0, 0), 0.3, dist=90)
    $ quakex_4_400 = Shakx((0, 0), 0.4, dist=90)
    $ quakex_4_500 = Shakx((0, 0), 0.5, dist=90)
    $ quakex_4_600 = Shakx((0, 0), 0.6, dist=90)
    $ quakex_4_700 = Shakx((0, 0), 0.7, dist=90)
    $ quakex_4_800 = Shakx((0, 0), 0.8, dist=90)
    $ quakex_4_900 = Shakx((0, 0), 0.9, dist=90)
    $ quakex_4_1000 = Shakx((0, 0), 1.0, dist=90)
    $ quakex_4_1200 = Shakx((0, 0), 1.2, dist=90)
    $ quakex_5_100 = Shakx((0, 0), 0.1, dist=112)
    $ quakex_5_300 = Shakx((0, 0), 0.3, dist=112)
    $ quakex_5_400 = Shakx((0, 0), 0.4, dist=112)
    $ quakex_5_500 = Shakx((0, 0), 0.5, dist=112)
    $ quakex_5_600 = Shakx((0, 0), 0.6, dist=112)
    $ quakex_5_700 = Shakx((0, 0), 0.7, dist=112)
    $ quakex_5_800 = Shakx((0, 0), 0.8, dist=112)
    $ quakex_5_900 = Shakx((0, 0), 0.9, dist=112)
    $ quakex_5_1000 = Shakx((0, 0), 1.0, dist=112)
    $ quakex_5_1200 = Shakx((0, 0), 1.2, dist=112)
    $ quakex_6_400 = Shakx((0, 0), 0.4, dist=135)
    $ quakex_6_500 = Shakx((0, 0), 0.5, dist=135)
    $ quakex_6_600 = Shakx((0, 0), 0.6, dist=135)
    $ quakex_6_800 = Shakx((0, 0), 0.8, dist=135)
    $ quakex_6_900 = Shakx((0, 0), 0.9, dist=135)
    $ quakex_6_1000 = Shakx((0, 0), 1.0, dist=135)
    $ quakex_6_1200 = Shakx((0, 0), 1.2, dist=135)
    $ quakex_6_1400 = Shakx((0, 0), 1.4, dist=135)
    $ quakex_6_1500 = Shakx((0, 0), 1.5, dist=135)
    $ quakex_7_500 = Shakx((0, 0), 0.5, dist=157)
    $ quakex_7_600 = Shakx((0, 0), 0.6, dist=157)
    $ quakex_7_800 = Shakx((0, 0), 0.8, dist=157)
    $ quakex_7_1000 = Shakx((0, 0), 1.0, dist=157)
    $ quakex_7_1200 = Shakx((0, 0), 1.2, dist=157)
    $ quakex_8_500 = Shakx((0, 0), 0.5, dist=180)
    $ quakex_8_1200 = Shakx((0, 0), 1.2, dist=180)
    $ quakex_8_1400 = Shakx((0, 0), 1.4, dist=180)
    $ quakex_8_2000 = Shakx((0, 0), 2.0, dist=180)
    $ quakex_9_700 = Shakx((0, 0), 0.7, dist=202)
    $ quakex_9_1200 = Shakx((0, 0), 1.2, dist=202)
    $ quakex_10_600 = Shakx((0, 0), 0.6, dist=225)
    $ quakex_10_900 = Shakx((0, 0), 0.9, dist=225)
    $ quakex_10_1200 = Shakx((0, 0), 1.2, dist=225)
    $ quakex_10_1500 = Shakx((0, 0), 1.5, dist=225)
    
    $ quake_2_300 = Shake((0, 0, 0, 0), 0.3, dist=45)
    
    ## V use these old ones for 480p ? V
    
#    $ quakey_2_100 = Shaky((0, 0, 0, 0), 0.1, dist=20)
#    $ quakey_2_200 = Shaky((0, 0, 0, 0), 0.2, dist=20)
#    $ quakey_2_300 = Shaky((0, 0, 0, 0), 0.3, dist=20)
#    $ quakey_2_400 = Shaky((0, 0, 0, 0), 0.4, dist=20)
#    $ quakey_2_500 = Shaky((0, 0, 0, 0), 0.5, dist=20)
#    $ quakey_2_600 = Shaky((0, 0, 0, 0), 0.6, dist=20)
#    $ quakey_3_200 = Shaky((0, 0, 0, 0), 0.2, dist=30)
#    $ quakey_3_300 = Shaky((0, 0, 0, 0), 0.3, dist=30)
#    $ quakey_3_400 = Shaky((0, 0, 0, 0), 0.4, dist=30)
#    $ quakey_3_500 = Shaky((0, 0, 0, 0), 0.5, dist=30)
#    $ quakey_3_600 = Shaky((0, 0, 0, 0), 0.6, dist=30)
#    $ quakey_3_700 = Shaky((0, 0, 0, 0), 0.7, dist=30)
#    $ quakey_3_800 = Shaky((0, 0, 0, 0), 0.8, dist=30)
#    $ quakey_3_900 = Shaky((0, 0, 0, 0), 0.9, dist=30)
#    $ quakey_3_1000 = Shaky((0, 0, 0, 0), 1.0, dist=30)
#    $ quakey_4_200 = Shaky((0, 0, 0, 0), 0.2, dist=40)
#    $ quakey_4_300 = Shaky((0, 0, 0, 0), 0.3, dist=40)
#    $ quakey_4_400 = Shaky((0, 0, 0, 0), 0.4, dist=40)
#    $ quakey_4_500 = Shaky((0, 0, 0, 0), 0.5, dist=40)
#    $ quakey_4_600 = Shaky((0, 0, 0, 0), 0.6, dist=40)
#    $ quakey_4_700 = Shaky((0, 0, 0, 0), 0.7, dist=40)
#    $ quakey_4_800 = Shaky((0, 0, 0, 0), 0.8, dist=40)
#    $ quakey_4_900 = Shaky((0, 0, 0, 0), 0.9, dist=40)
#    $ quakey_4_1000 = Shaky((0, 0, 0, 0), 1.0, dist=40)
#    $ quakey_4_1200 = Shaky((0, 0, 0, 0), 1.2, dist=40)
#    $ quakey_4_1500 = Shaky((0, 0, 0, 0), 1.5, dist=40)
#    $ quakey_5_300 = Shaky((0, 0, 0, 0), 0.3, dist=50)
#    $ quakey_5_400 = Shaky((0, 0, 0, 0), 0.4, dist=50)
#    $ quakey_5_500 = Shaky((0, 0, 0, 0), 0.5, dist=50)
#    $ quakey_5_600 = Shaky((0, 0, 0, 0), 0.6, dist=50)
#    $ quakey_5_700 = Shaky((0, 0, 0, 0), 0.7, dist=50)
#    $ quakey_5_800 = Shaky((0, 0, 0, 0), 0.8, dist=50)
#    $ quakey_5_900 = Shaky((0, 0, 0, 0), 0.9, dist=50)
#    $ quakey_5_1000 = Shaky((0, 0, 0, 0), 1.0, dist=50)
#    $ quakey_5_1200 = Shaky((0, 0, 0, 0), 1.2, dist=50)
#    $ quakey_6_400 = Shaky((0, 0, 0, 0), 0.4, dist=60)
#    $ quakey_6_500 = Shaky((0, 0, 0, 0), 0.5, dist=60)
#    $ quakey_6_600 = Shaky((0, 0, 0, 0), 0.6, dist=60)
#    $ quakey_6_700 = Shaky((0, 0, 0, 0), 0.7, dist=60)
#    $ quakey_6_800 = Shaky((0, 0, 0, 0), 0.8, dist=60)
#    $ quakey_6_900 = Shaky((0, 0, 0, 0), 0.9, dist=60)
#    $ quakey_6_1000 = Shaky((0, 0, 0, 0), 1.0, dist=60)
#    $ quakey_6_1200 = Shaky((0, 0, 0, 0), 1.2, dist=60)
#    $ quakey_7_600 = Shaky((0, 0, 0, 0), 0.6, dist=70)
#    $ quakey_7_1000 = Shaky((0, 0, 0, 0), 1.0, dist=70)
#    $ quakey_8_600 = Shaky((0, 0, 0, 0), 0.6, dist=80)
#    $ quakey_8_700 = Shaky((0, 0, 0, 0), 0.7, dist=80)
#    $ quakey_8_800 = Shaky((0, 0, 0, 0), 0.8, dist=80)
#    $ quakey_8_1000 = Shaky((0, 0, 0, 0), 1.0, dist=80)
#    $ quakey_8_1200 = Shaky((0, 0, 0, 0), 1.2, dist=80)
#    $ quakey_9_800 = Shaky((0, 0, 0, 0), 0.8, dist=90)
#    $ quakey_9_1200 = Shaky((0, 0, 0, 0), 1.2, dist=90)
#    $ quakey_12_1500 = Shaky((0, 0, 0, 0), 1.5, dist=120)
#    $ quakey_12_2000 = Shaky((0, 0, 0, 0), 2.0, dist=120)
    
#    $ quakex_1_100 = Shakx((0, 0), 0.1, dist=10)
#    $ quakex_2_200 = Shakx((0, 0), 0.2, dist=20)
#    $ quakex_2_300 = Shakx((0, 0), 0.3, dist=20)
#    $ quakex_2_400 = Shakx((0, 0), 0.4, dist=20)
#    $ quakex_2_600 = Shakx((0, 0), 0.6, dist=20)
#    $ quakex_3_200 = Shakx((0, 0), 0.2, dist=30)
#    $ quakex_3_300 = Shakx((0, 0), 0.3, dist=30)
#    $ quakex_3_400 = Shakx((0, 0), 0.4, dist=30)
#    $ quakex_3_500 = Shakx((0, 0), 0.5, dist=30)
#    $ quakex_3_600 = Shakx((0, 0), 0.6, dist=30)
#    $ quakex_3_800 = Shakx((0, 0), 0.8, dist=30)
#    $ quakex_4_300 = Shakx((0, 0), 0.3, dist=40)
#    $ quakex_4_400 = Shakx((0, 0), 0.4, dist=40)
#    $ quakex_4_500 = Shakx((0, 0), 0.5, dist=40)
#    $ quakex_4_600 = Shakx((0, 0), 0.6, dist=40)
#    $ quakex_4_700 = Shakx((0, 0), 0.7, dist=40)
#    $ quakex_4_800 = Shakx((0, 0), 0.8, dist=40)
#    $ quakex_4_900 = Shakx((0, 0), 0.9, dist=40)
#    $ quakex_4_1000 = Shakx((0, 0), 1.0, dist=40)
#    $ quakex_4_1200 = Shakx((0, 0), 1.2, dist=40)
#    $ quakex_5_300 = Shakx((0, 0), 0.3, dist=50)
#    $ quakex_5_400 = Shakx((0, 0), 0.4, dist=50)
#    $ quakex_5_500 = Shakx((0, 0), 0.5, dist=50)
#    $ quakex_5_600 = Shakx((0, 0), 0.6, dist=50)
#    $ quakex_5_700 = Shakx((0, 0), 0.7, dist=50)
#    $ quakex_5_800 = Shakx((0, 0), 0.8, dist=50)
#    $ quakex_5_900 = Shakx((0, 0), 0.9, dist=50)
#    $ quakex_5_1000 = Shakx((0, 0), 1.0, dist=50)
#    $ quakex_5_1200 = Shakx((0, 0), 1.2, dist=50)
#    $ quakex_6_400 = Shakx((0, 0), 0.4, dist=60)
#    $ quakex_6_500 = Shakx((0, 0), 0.5, dist=60)
#    $ quakex_6_600 = Shakx((0, 0), 0.6, dist=60)
#    $ quakex_6_800 = Shakx((0, 0), 0.8, dist=60)
#    $ quakex_6_900 = Shakx((0, 0), 0.9, dist=60)
#    $ quakex_6_1000 = Shakx((0, 0), 1.0, dist=60)
#    $ quakex_6_1200 = Shakx((0, 0), 1.2, dist=60)
#    $ quakex_6_1400 = Shakx((0, 0), 1.4, dist=60)
#    $ quakex_7_600 = Shakx((0, 0), 0.6, dist=70)
#    $ quakex_7_800 = Shakx((0, 0), 0.8, dist=70)
#    $ quakex_7_1000 = Shakx((0, 0), 1.0, dist=70)
#    $ quakex_8_500 = Shakx((0, 0), 0.5, dist=80)
#    $ quakex_8_1200 = Shakx((0, 0), 1.2, dist=80)
#    $ quakex_9_1200 = Shakx((0, 0), 1.2, dist=90)
#    $ quakex_10_600 = Shakx((0, 0), 0.6, dist=100)
#    $ quakex_10_900 = Shakx((0, 0), 0.9, dist=100)
    
    $ narrator = Character(None, ctc="keywait", ctc_position="nestled")
    $ nvlnar = NVLCharacter(kind=nvl, ctc="keywait", ctc_position="nestled")
    $ centered = Character(None,
                          what_size=46, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.25, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          what_outlines=[(1, "#000000", 0, 0)],
                          what_font="default.ttf",
                          what_drop_shadow=[(2,2)],
                          #Gives an outline
                          #what_slow_cps=20, #Speed at which the text appears (slow)
                          ctc="keywait", 
                          ctc_position="nestled")
    
    $ r_click_chp = "Undefined"
    
    image bg circleiris = "efe/id_circleiris1.png"
    image bg teleport = "efe/id_teleport.png"



# This defines the far sheet of the rain.
# You show that one /behind/ character sprites.
#image rainback scroll:
#    # Distant drops
#    contains:
#        im.Tile("efe/rain2b.png", size=(2556, 1440))
#        alpha (0.5/3)
#        anchor (0.0,0.0)
#        subpixel True
#        pos (0.0,-2.0)
#        parallel:
#            ypos -1.0
#            linear RainYF ypos 0.0
#            repeat
#        parallel:
#            xpos 0
#            linear RainXF xpos -1.0
#            repeat
#    # Medium drops
#    contains:
#        im.Tile("efe/rain3b.png", size=(2556, 1440))
#        alpha RainLayerAlpha
#        anchor (0.0,0.0)
#        subpixel True
#        pos (0.0,-2.0)
#        parallel:
#            ypos -1.0
#            linear RainYM ypos 0.0
#            repeat
#        parallel:
#            xpos 0
#            linear RainXM xpos -1.0
#            repeat
#    # Front drops

## This is the front sheet of the rain, it goes /above/ the 
## character sprites.
#image rainfront scroll:    
#    contains:
#        im.Tile("efe/rain1.png", size=(2556, 1440))
#        anchor (0.0,0.0)
#        alpha RainLayerAlpha
#        subpixel True
#        pos (0.0,-2.0)
#        parallel:
#            ypos -1.0
#            linear RainY ypos 0.0
#            repeat
#        parallel:
#            xpos 0
#            linear RainX xpos -1.0
#            repeat
#image rainback static:
#    contains:
#        alpha (0.6/3)
#        im.Tile("efe/rain2b.png", size=(1280, 720))
#    contains:
#        alpha RainLayerAlpha
#        im.Tile("efe/rain3b.png", size=(1280, 720))
#image rainfront static:        
#    contains:
#        alpha RainLayerAlpha
#        im.Tile("efe/rain1.png", size=(1280, 720))


transform far_left:
    xpos (410.0/1920.0)
transform left:
    xpos (590.0/1920.0)
transform center:
    xpos 0.5
transform right:
    xpos (1330.0/1920.0)
transform far_right:
    xpos (1510.0/1920.0)


# Declare characters used by this game.
define nan = Character('Nanjo Terumasa', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="#ffffff"
define kin = Character('Ushiromiya Kinzo', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="e3e6ec"
define gen = Character('Ronoue Genji', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="b4b1b1"
define but = Character('Ushiromiya Battler', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="9D4A4A"
define geo = Character('Ushiromiya George', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="DEDE9F"
define hid = Character('Ushiromiya Hideyoshi', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="a89152"
define eva = Character('Ushiromiya Eva', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="4f3443"
define kir = Character('Ushiromiya Kyrie', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="dee1e8"
define rud = Character('Ushiromiya Rudolf', show_two_window=True, ctc="keywait", ctc_position="nestled")
define mar = Character('Ushiromiya Maria', show_two_window=True, ctc="keywait", ctc_position="nestled")
define ros = Character('Ushiromiya Rosa', show_two_window=True, ctc="keywait", ctc_position="nestled")
define jes = Character('Ushiromiya Jessica', show_two_window=True, ctc="keywait", ctc_position="nestled")
define kum = Character('Kumasawa Chiyo', show_two_window=True, ctc="keywait", ctc_position="nestled")
define goh = Character('Gohda Toshiro', show_two_window=True, ctc="keywait", ctc_position="nestled")
define kan = Character('Kanon', show_two_window=True, ctc="keywait", ctc_position="nestled")
define nat = Character('Ushiromiya Natsuhi', show_two_window=True, ctc="keywait", ctc_position="nestled")
define sha = Character('Shannon', show_two_window=True, ctc="keywait", ctc_position="nestled")
define cla = Character('Ushiromiya Krauss', show_two_window=True, ctc="keywait", ctc_position="nestled")
define bea = Character('Beatrice', show_two_window=True, ctc="keywait", ctc_position="nestled")
define ber = Character('Bernkastel', show_two_window=True, ctc="keywait", ctc_position="nestled")
define goa = Character('Goat Attendant', show_two_window=True, ctc="keywait", ctc_position="nestled")           ## name = 山羊の従者
define rg1 = Character('Lucifer', show_two_window=True, ctc="keywait", ctc_position="nestled")                  ## name = ルシファ
define rg2 = Character('Leviathan', show_two_window=True, ctc="keywait", ctc_position="nestled")                ## name = レヴィア
define rg3 = Character('Satan', show_two_window=True, ctc="keywait", ctc_position="nestled")                    ## name = サタン
define rg4 = Character('Belphegor', show_two_window=True, ctc="keywait", ctc_position="nestled")                ## name = ベルフェ
define rg5 = Character('Mammon', show_two_window=True, ctc="keywait", ctc_position="nestled")                   ## name = マモン
define rg6 = Character('Beelzebub', show_two_window=True, ctc="keywait", ctc_position="nestled")                ## name = ベルゼ
define rg7 = Character('Asmodeus', show_two_window=True, ctc="keywait", ctc_position="nestled")                 ## name = アスモ
define lam = Character('Lambdadelta', show_two_window=True, ctc="keywait", ctc_position="nestled")
define wal = Character('Virgilia', show_two_window=True, ctc="keywait", ctc_position="nestled")
define ron = Character('Ronove', show_two_window=True, ctc="keywait", ctc_position="nestled")
define ev2 = Character('EVA-Beatrice', show_two_window=True, ctc="keywait", ctc_position="nestled")             ## name = エヴァ・ベアトリーチェ
define s41 = Character('Chiester 410', show_two_window=True, ctc="keywait", ctc_position="nestled")
define s45 = Character('Chiester 45', show_two_window=True, ctc="keywait", ctc_position="nestled")
define s00 = Character('Chiester 00', show_two_window=True, ctc="keywait", ctc_position="nestled")
define enj = Character('Ushiromiya Ange', show_two_window=True, ctc="keywait", ctc_position="nestled")
define sak = Character('Sakutarou', show_two_window=True, ctc="keywait", ctc_position="nestled")                ## name = さくたろう (take off the last character for 'Sakutaro')
define oko = Character('Okonogi Tetsurou', show_two_window=True, ctc="keywait", ctc_position="nestled")
define kas = Character('Sumadera Kasumi', show_two_window=True, ctc="keywait", ctc_position="nestled")
define ama = Character('Amakusa Juuza', show_two_window=True, ctc="keywait", ctc_position="nestled")
define pro = Character('Professor Ootsuki', show_two_window=True, ctc="keywait", ctc_position="nestled")
define gap = Character('Gaap', show_two_window=True, ctc="keywait", ctc_position="nestled")
define na2 = Character('Nanjo Masayuki', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="#ffffff"
define ku2 = Character('Kumasawa Sabakichi', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="#ffffff"
define kaw = Character('Captain Kawabata', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="#ffffff"
define eri = Character('Furudo Erika', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="#ffffff"
define fea = Character('Hachijo Tohya', show_two_window=True, ctc="keywait", ctc_position="nestled")#, color="#ffffff"

define nvlcenter = Character(None, kind=nvl, ctc="keywait", ctc_position="nestled", what_text_align=0.5, what_xalign=0.5, what_minwidth=1500)

image clock = "clock/clock_m.png" # Short Clockhand
image clock_1 = "clock/clock_h.png" # Long Clockhand
image clock_2 = "clock/clock.png" # Clockface
image clock_c = "clock/clock_c.png"


init python:
    import sys
    import time
    
    def check_infinite_loop():
        global il_statements

        il_statements += 1

        if il_statements <= 1000:
            return

        il_statements = 0

        global il_time

        if time.time() > il_time:
            il_time = time.time() + 60
        #    raise Exception("Possible infinite loop.")

        return
    
    overriding_on = None
    def overriding_overlay():
        if not overriding_on:
            return
        ui.keymap(mousedown_1=ui.returns(None))
        ui.keymap(mouseup_1=ui.returns(None))
        ui.keymap(I=ui.returns('False'))
        

    config.overlay_functions.append(overriding_overlay) 
    
    if not persistent.runtime:
        persistent.runtime = 0
    persistent.curr_play = 0

    def calc_total_run():
        global curr_play
        persistent.runtime += renpy.get_game_runtime()
        persistent.curr_play += renpy.get_game_runtime()
        renpy.clear_game_runtime()
    time_calc = renpy.curry(calc_total_run)
    
    def cps_time(say_length, voice_time, quake_tmp=None):
        global cps_wait
        if not _preferences.text_cps == 0:
            tmp1 = (say_length*1.0) / (_preferences.text_cps*1.0)
            cps_wait = voice_time - tmp1
        else:
            cps_wait = voice_time
        if quake_tmp:
            cps_wait = cps_wait - quake_tmp
        
    def cps_time2(say_length, voice_time, quake_tmp=None):
        global cps_wait2
        if not _preferences.text_cps == 0:
            tmp1 = (say_length*1.0) / (_preferences.text_cps*1.0)
            cps_wait2 = voice_time - tmp1
        else:
            cps_wait2 = voice_time
        if quake_tmp:
            cps_wait2 = cps_wait - quake_tmp
        
    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random number's we'll generate.
    import random
    
    # initialize random numbers
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=400, speed=5050, wind=0, xborder=(0,10), yborder=(50,50), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)
        
        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.
        
        @parm {int} max_particles:
            The maximum number of particles at once in the screen.
            
        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1
            
        @parm {float} wind:
            The max wind force that'll be applyed to the particles.
            
        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.
            
        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """            
            # the maximum number of particles we can have on screen at once
            self.max_particles = max_particles
            
            # the particle's speed
            self.speed = speed
            
            # the wind's speed
            self.wind = wind
            
            # the horizontal/vertical range to create particles
            self.xborder = xborder
            self.yborder = yborder
            
            # the maximum depth of the screen. Higher values lead to more varying particles size,
            # but it also uses more memory. Default value is 10 and it should be okay for most
            # games, since particles sizes are calculated as percentage of this value.
            self.depth = kwargs.get("depth", 10)
            
            # initialize the images
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            # if we can create a new particle...
            if particles is None or len(particles) < self.max_particles:
                
                # generate a random depth for the particle
                depth = random.randint(1, self.depth)
                
                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.            
            """
            rv = [ ]
            
            # generate the array of images for each possible depth value.
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind's speed
            self.wind = wind
            
            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None
            
            # the horizontal/vertical positions of this particle            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            # calculate lag
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            # update the position
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            # verify if the particle went out of the screen so we can destroy it.
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ##  print "Dead"
                return None
                
            # returns the particle as a Tuple (xpos, ypos, time, image)
            # since it expects horizontal and vertical positions to be integers, we have to convert
            # it (internal positions use float for smooth movements =D)
            return int(self.xpos), int(self.ypos), st, self.image
    
    
    def text_box_window(st, at):
        return persistent.msgwnd, None

    style.window.background = Frame(DynamicDisplayable(text_box_window), 25, 25)
    
    def name_box_window(st, at):
        return persistent.chrwnd, None

    style.say_who_window.background = Frame(DynamicDisplayable(name_box_window), 25, 25)
    
    style.say_two_window_vbox.order_reverse=True
    
    style.default.layout = "greedy"
    style.default.language = "western"
    
transform rotateshort:
    subpixel True
    xanchor 0.5
    yanchor 0.5
#    size (856*2.25*clock_size, 856*2.25*clock_size)
    block:
        rotate (min1*6)
        pause 2.0
    #    rotate (minutes*6)
        linear clock_speed rotate (min2*6)
    
transform rotatelong:
    subpixel True
    xanchor 0.5
    yanchor 0.5
#    size (856*2.25*clock_size, 856*2.25*clock_size)
    block:
        rotate (min1*0.5)
        pause 2.0
    #    rotate (minutes*0.5)
        linear clock_speed rotate (min2*0.5)

transform alpha_dissolve:
    alpha 0.0
    linear 1.0 alpha 1.0
#    on hide:
#        linear 1.0 alpha 0
    # This is to fade in the clock.

screen clock:
    frame at alpha_dissolve:
#        xmaximum 350 # X size of clock graphic
#        ymaximum 350 # Y size of clock graphic
        xpos clock_x # X placement on screen
        ypos clock_y # Y placement on screen
        background "saveload/load_null.png"
        add "clock_2" xanchor 0.5 yanchor 0.5 size (856*2.25*clock_size, 856*2.25*clock_size)
        add "clock_1" size (856*2.25*clock_size, 856*2.25*clock_size) at rotatelong                ## these are switch around in PS3 version (as in, like an actual clock)
        add "clock" size (856*2.25*clock_size, 856*2.25*clock_size) at rotateshort                 ## these are switch around in PS3 version (as in, like an actual clock)
        add "clock_c" xanchor 0.5 yanchor 0.5 size (856*2.25*clock_size, 856*2.25*clock_size)

label cps_time(say_length, voice_time, quake_tmp=None):
    if not _preferences.text_cps == 0:
        $ tmp1 = (say_length*1.0) / (_preferences.text_cps*1.0)
        $ cps_wait = voice_time - tmp1
    else:
        $ cps_wait = voice_time
    if quake_tmp:
        $ cps_wait = cps_wait - quake_tmp
    return


label splashscreen:
    python:
        if not persistent.first_run:
            persistent.first_run = True
            _preferences.volumes['music'] = 0.6
            _preferences.volumes['sfx'] = 0.7
            _preferences.volumes['voice'] = 0.9
            _preferences.afm_time = 3
            
            persistent.bgm_text = True
            persistent.fmv = True
            persistent.ach_toggle = True
            persistent.anime_bgm2 = False
    if not persistent.msgwnd:
        $ persistent.msgwnd = "efe/msgwnd.png"
        $ persistent.config_msgwnd = 3
    if not persistent.chrwnd:
        $ persistent.chrwnd = "efe/chrwnd.png"
    if not persistent.bgm_lang:
        $ persistent.bgm_lang = 0
    if not persistent.anime_bgm:
        $ persistent.anime_bgm = False
    if not persistent.tsuru_flg:
        $ persistent.tsuru_flg = False
        $ persistent.tsurupettan = False
    
    $ persistent.op_demo = 0
    
    #$ renpy.pause(0)
    scene black 
    with Pause(0.5)
    
    $ se1("title/clock_bell_wall2.ogg")
    show splash
    with dissolve
    with Pause(2.5)
    
    scene black with dissolve
    
   # play sound "sys_se/mizu_d2.ogg"
    show splash2
   # with teleport
    with dissolve
    with Pause(2.5)
    
    scene black with dissolve
    
    show splash3
    with dissolve
    with Pause(2.5)
    
    scene black with dissolve
    
    show splash4 with dissolve
    with Pause(2.5)
    
    scene black 
    with dissolve
    with Pause(1.0)
    
    $ E_A()
    
    $ renpy.movie_cutscene("movie/umineko_op.mkv")
    $ persistent.op_demo += 1
    
    scene black
    with Pause(1.0)
    
label splash2:
    if persistent.UMINEKOEND < 50:
        play music "bgm/umilse_002.ogg"
        $ config.main_menu_music = "bgm/umilse_002.ogg"
    elif persistent.UMINEKOEND >= 50:
        play music "bgm4/umilse_016.ogg"
        $ config.main_menu_music = "bgm4/umilse_016.ogg"
    
    $ bgmvol(default_vol)
    if not _skipping:
        $ _skipping = True
    $ bgm_counter()
    $ cg_counter()
    
    scene black
    with Pause(1.0)
    
    if persistent.UMINEKOEND < 20:
        show title1
    elif persistent.UMINEKOEND == 20 or persistent.UMINEKOEND == 21 or persistent.UMINEKOEND == 22:
        show title2
    elif persistent.UMINEKOEND == 30 or persistent.UMINEKOEND == 31 or persistent.UMINEKOEND == 32:
        show title3
    elif persistent.UMINEKOEND == 40 or persistent.UMINEKOEND == 41 or persistent.UMINEKOEND == 42:
        show title4
    elif persistent.UMINEKOEND >= 50:
        show title5
    with t23
    
    show title_logo at logo with t2#2
    
    $ tmp = 0
#    $ x=(1320.0/1920.0)
    $ x=1320.0
    $ y=420.0
    $ y+=2.0
    show title_start at ep_start(x,y):
#        xpos x ypos (y/1080.0)
        alpha 0.0
        linear 0.2 alpha 1.0
    if persistent.UMINEKOEND_flg == 20 or persistent.UMINEKOEND_flg == 30 or persistent.UMINEKOEND_flg == 40:
        show title_new at new_title(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            linear 0.2 alpha 1.0
    
    if persistent.UMINEKOEND >= 11:
        $ tmp +=0.1
        $ y+=60.0
        show title_tea at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_flg == 11 or persistent.UMINEKOEND_flg == 21 or persistent.UMINEKOEND_flg == 31 or persistent.UMINEKOEND_flg == 41:
            show title_new at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
    if persistent.UMINEKOEND >= 12:
        $ tmp +=0.1
        $ y+=60.0
        show title_ura at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_flg == 12 or persistent.UMINEKOEND_flg == 22 or persistent.UMINEKOEND_flg == 32 or persistent.UMINEKOEND_flg == 42:
            show title_new at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
    
#    if persistent.UMINEKOEND < 5:
#        $ tmp +=0.1
#        $ y+=60.0
#        show title_config1 at ep_start(x,y):
##            xpos x ypos (y/1080.0)
#            alpha 0.0
#            pause tmp
#            linear 0.2 alpha 1.0
#        $ tmp +=0.1
#        $ y+=60.0
#        show title_exit1 at ep_start(x,y):
##            xpos x ypos (y/1080.0)
#            alpha 0.0
#            pause tmp
#            linear 0.2 alpha 1.0
    if persistent.UMINEKOEND < 11:
        $ tmp +=0.1
        $ y+=60.0
        show title_continue1 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_load1 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_config2 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_exit2 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
    elif persistent.UMINEKOEND == 11:
        $ tmp +=0.1
        $ y+=60.0
        show title_continue2 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_load2 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_config3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_picture1 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_CG_flg == 1:
            show title_new as title_new2 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_music1 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_BGM_flg == 1:
            show title_new as title_new3 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_exit3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
    elif persistent.UMINEKOEND == 12:
        $ tmp +=0.1
        $ y+=60.0
        show title_continue3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_load3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_config4 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_picture2 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_CG_flg == 1:
            show title_new as title_new2 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_music2 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_BGM_flg == 1:
            show title_new as title_new3 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_exit4 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
    elif persistent.UMINEKOEND >= 20:
        $ tmp +=0.1
        $ y+=60.0
        show title_continue3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_load3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_chars at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_CHARS1_flg == 1 or persistent.UMINEKOEND_CHARS2_flg == 1 or persistent.UMINEKOEND_CHARS3_flg == 1 or persistent.UMINEKOEND_CHARS4_flg == 1:
            show title_new as title_new2 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_tips at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_TIPS1_flg == 1 or persistent.UMINEKOEND_TIPS2_flg == 1 or persistent.UMINEKOEND_TIPS3_flg == 1 or persistent.UMINEKOEND_TIPS4_flg == 1:
            show title_new as title_new3 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_config5 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_picture3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_CG_flg == 1:
            show title_new as title_new4 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_music3 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
        if persistent.UMINEKOEND_BGM_flg == 1:
            show title_new as title_new5 at new_title(x,y):
#                xpos x ypos (y/1080.0)
                alpha 0.0
                pause tmp
                linear 0.2 alpha 1.0
        $ tmp +=0.1
        $ y+=60.0
        show title_exit5 at ep_start(x,y):
#            xpos x ypos (y/1080.0)
            alpha 0.0
            pause tmp
            linear 0.2 alpha 1.0
    with Pause(tmp + 0.2)
    return
    
label eye1:
    show screen disable_keys
    ##example of clock to use is script: 7:30AM to 10:00PM in 8 seconds
    
#    $ clock_special = 0
#    $ min1 = 450 # first and second number
#    $ min2 = 870 # third and fourth number
#    $ clock_speed = 10.0 # fifth to last number, 11 is equivilent to 2.3 seconds?
#    $ clock_reverse = 0 # fourth to last number
#    $ clock_x = (510.0/640.0) # third to last number
#    $ clock_y = (340.0/480.0) # second to last number
#    $ clock_size = 0.25 # %clock_kakudai (last number) is scale factor percentage
#    call eye1
    
    # 12:00 MN - 0
    # 1:00  AM - 60
    # 2:00  AM - 120
    # 3:00  AM - 180
    # 4:00  AM - 240
    # 5:00  AM - 300
    # 6:00  AM - 360
    # 7:00  AM - 420
    # 8:00  AM - 480
    # 9:00  AM - 540
    # 10:00 AM - 600
    # 11:00 AM - 660
    # 12:00 NN - 720 
    # 1:00  PM - 780
    # 2:00  PM - 840
    # 3:00  PM - 900
    # 4:00  PM - 960
    # 5:00  PM - 1020
    # 6:00  PM - 1080
    # 7:00  PM - 1140
    # 8:00  PM - 1200
    # 9:00  PM - 1260
    # 10:00 PM - 1320
    # 11:00 PM - 1380
    # 12:00 MN - 1440
    
    ## 24-HR
    
    # 13:00 PM - 780
    # 14:00 PM - 840
    # 15:00 PM - 900
    # 16:00 PM - 960
    # 17:00 PM - 1020
    # 18:00 PM - 1080
    # 19:00 PM - 1140
    # 20:00 PM - 1200
    # 21:00 PM - 1260
    # 22:00 PM - 1320
    # 23:00 PM - 1380
    # 24:00    - 1440
    
    # 25:00    - 1500
    # 26:00    - 1560
    # 27:00    - 1620
    # 28:00    - 1680
    # 29:00    - 1740
    # 30:00    - 1800
    # 31:00    - 1860
    # 32:00    - 1920
    # 33:00    - 1980
    # 34:00    - 2040
    # 35:00    - 2100
    # 36:00    - 2160
    # 37:00    - 2220
    # 38:00    - 2280
    # 39:00    - 2340
    # 40:00    - 2400
    # 41:00    - 2460
    # 42:00    - 2520
    # 43:00    - 2580
    # 44:00    - 2640
    # 45:00    - 2700
    # 46:00    - 2760
    # 47:00    - 2820
    # 48:00    - 2880
    
    
    $ _game_menu_screen = None
    $ rain_static = 1
    scene black onlayer cinema:
        alpha (150.0/255.0)
    show ware onlayer cinema
    with None
    
    #show rainback static
    #show rainfront static
    
    $ E_A()
    
    $ seplay(9,se1022)
    
    with Pause(1.0)
    
    show cinema logo onlayer cinema2:
        xanchor 0.5
        yanchor 0.5
        xpos (1460.0/1920.0)
        ypos (870.0/1080.0)
#        ypos (410.0/480.0)
#        xalign 1.0
#        yanchor 0.5
##        xpos 0.734375
#        ypos 0.8287037037037037037037037037037
    with t5
    
    $ minutes = min1
#    $ min3 = 0
    $ min3 = clock_speed
    show screen clock
    with t2
    with Pause(1.0)
    
    if clock_reverse == 0:
        $ me5(me1050)
    elif clock_reverse ==1:
        $ me5(me1051)
#    $ min3 = clock_speed
#    $ minutes += min2
#    with t2          ##fix rotating problem
#    with Pause(clock_speed-2.0)
    with Pause(clock_speed)
    
    $ E_M5()
    if clock_special == 0:
        $ se3(se30)
        with Pause(4.0)
    elif clock_special == "umi1_end":
        $ seplay(9,se1052)
        with Pause(20.0)
    elif clock_special == "umi3_5":
        $ seplay(9,se1052)
        with Pause(20.0)
    
    scene black
    scene onlayer cinema
    scene onlayer cg
    scene onlayer meta
    hide screen clock
    hide cinema onlayer cinema2
    with t2
    $ renpy.free_memory()
    
    $ fede(0,2.0)
    
    $ rain_static = 0
    hide screen disable_keys
    return
    
label eye2:
    show screen disable_keys
    $ _game_menu_screen = None
    $ rain_static = 1
    show hana1_ onlayer cinema:            ##keep alpha???
        alpha (180.0/255.0)
    with t7
    
    show cinema logo 2 onlayer cinema2:
        xanchor 0.5
        yanchor 0.5
        xpos (1460.0/1920.0)
        ypos (870.0/1080.0)
#        ypos (410.0/480.0)
#        xalign 1.0
#        yanchor 0.5
#        ypos 0.8287037037037037037037037037037
    with t5
    
    with Pause(6.0)
    
    scene black
    scene onlayer meta
    scene onlayer cinema
    with t2
    
    with Pause(2.0)
    
#    $ minutes = min1
#    $ min3 = 0
#    $ min3 = clock_speed
    show screen clock
    with t2
    with Pause(1.0)
    
    if clock_reverse == 0:
        $ me5(me1050)
    elif clock_reverse ==1:
        $ me5(me1051)
#    $ min3 = clock_speed
#    $ minutes += min2
#    with t2          ##fix rotating problem
    with Pause(clock_speed)
#    with Pause(clock_speed-2.0)
    
    $ E_M5()
    if clock_special == 0:
        $ se3(se30)
        with Pause(4.0)
    elif clock_special == "umi1_end":
        $ seplay(9,se1052)
        with Pause(20.0)
    elif clock_special == "umi3_5":
        $ seplay(9,se1052)
        with Pause(20.0)
    
    scene black
    scene onlayer cinema
    scene onlayer cg
    scene onlayer meta
    hide screen clock
    hide cinema onlayer cinema2
    with t2
    $ renpy.free_memory()
    
    $ fede(0,2.0)
    
    $ rain_static = 0
    hide screen disable_keys
    return
    
label eye3:
    
    ##work on this
    
    return
    
label eye11:
    show screen disable_keys
    $ _game_menu_screen = None
    $ rain_static = 1
    scene black onlayer cinema:
        alpha (150.0/255.0)
    with None
    
    show ware onlayer cinema with None
    $ E_A()
    $ seplay(9,se1022)
    with Pause(1.0)
    
    show cinema logo onlayer cinema2:
        xanchor 0.5
        yanchor 0.5
        xpos (1460.0/1920.0)
        ypos (870.0/1080.0)
#        ypos (410.0/480.0)
    with t5
    
    with Pause(2.0)
    
    scene black
    scene onlayer cinema
    scene onlayer cg
    scene onlayer meta
    with t2
    with Pause(4.0)
    
    scene onlayer cinema2
    with t2
    $ renpy.free_memory()
    
    $ fede(0,2.0)
    $ rain_static = 0
    hide screen disable_keys
    return
    
label eye12:
    show screen disable_keys
    $ _game_menu_screen = None
    $ rain_static = 1
    show hana1_ onlayer cinema:            ##keep alpha???
        alpha (180.0/255.0)
    with t7
    
    show cinema logo 2 onlayer cinema2:
        xanchor 0.5
        yanchor 0.5
        xpos (1460.0/1920.0)
        ypos (870.0/1080.0)
#        ypos (410.0/480.0)
    with t5
    
    with Pause(6.0)
    
#    with Pause(2.0)
    
    scene black
    scene onlayer cinema
    scene onlayer cg
    scene onlayer meta
    with t2
    with Pause(2.0)
    
    scene onlayer cinema2
    with t2
    $ renpy.free_memory()
    
    $ fede(0,2.0)
    $ rain_static = 0
    hide screen disable_keys
    return
    
label meta_set:
    call mset
    return

label mset:
    
    $ rain_static = 1
    show black onlayer meta zorder -1:
        alpha (150.0/255.0)
    with t22
    
    show hana1 onlayer meta zorder -1:            ##keep alpha???
        alpha (180.0/255.0)
    with t28
    with Pause(1.0)
    
    return

label meta_set2:
    call mset2
    return

label mset2:
    
    $ rain_static = 1
    show black onlayer meta zorder -1:
        alpha (150.0/255.0)
    with t22
    with Pause(1.0)
    
    return
    
label meta_end:
    call mend
    return

label mend:
    scene onlayer meta
    $ rain_static = 0
    with t8
    return

label meta_set_ef(tmp11=0,tmp12=0):
    call msetef(tmp11,tmp12)
    return

label msetef(tmp11=0,tmp12=0):
    $ rain_static = 1
    show black onlayer meta zorder -1:
        alpha (150.0/255.0)
    if tmp11 == 0:
        pass
    else:
        with tmp11
    
    show hana1 onlayer meta zorder -1:            ##keep alpha???
        alpha (180.0/255.0)
    if tmp12 == 0:
        pass
    else:
        with tmp12
#    with Pause(1.0)
    return

label meta_set2_ef(tmp11=0):
    call mset2ef(tmp11)
    return

label mset2ef(tmp11=0):
    $ rain_static = 1
    show black onlayer meta zorder -1:
        alpha (150.0/255.0)
    if tmp11 == 0:
        pass
    else:
        with tmp11
    return

label meta_end_ef(tmp11=0):
    call mendef(tmp11)
    return

label mendef(tmp11=0):
    scene onlayer meta
    $ rain_static = 0
    if tmp11 == 0:
        pass
    else:
        with tmp11
    return

transform ship_slow:
    parallel:
        xalign (0.5)
        xpos ((960.0-10.0)/1920.0)
        ease 1.0 xpos ((960.0+10.0)/1920.0)
        pause 0.3
        ease 1.0 xpos ((960.0-10.0)/1920.0)
        pause 0.3
        repeat
    parallel:
        yalign (0.5)
        ypos ((540.0-40.0)/1080.0)
        ease 1.0 ypos ((540.0+40.0)/1080.0)
        ease 1.0 ypos ((540.0-40.0)/1080.0)
        repeat
    
transform ship_fast:            ## increase speed ??? https://youtu.be/vQWPKMIQnfY?t=20m4s
    parallel:
        xalign (0.5)
        xpos ((960.0-10.0)/1920.0)
        ease 0.26 xpos ((960.0+10.0)/1920.0)
        ease 0.26 xpos ((960.0-10.0)/1920.0)
        repeat
    parallel:
        yalign (0.5)
        ypos ((540.0-50.0)/1080.0)
        ease 0.16 ypos ((540.0+50.0)/1080.0)
        ease 0.16 ypos ((540.0-50.0)/1080.0)
        repeat
    
transform ship_stop:
    parallel:
        xalign (0.5)
        xpos ((960.0-10.0)/1920.0)
        ease 2.2 xpos ((960.0+10.0)/1920.0)
        ease 2.2 xpos ((960.0-10.0)/1920.0)
        ease 2.0 xpos 0.5
    parallel:
        yalign (0.5)
        ypos ((540.0-40.0)/1080.0)
        ease 1.1 ypos ((540.0+40.0)/1080.0)
        ease 1.1 ypos ((540.0-40.0)/1080.0)
        ease 2.0 ypos 0.5
    
init -2:
    transform character_bob:
        ypos 1.0
        linear 0.25 ypos 1.1
        linear 0.25 ypos 1.0