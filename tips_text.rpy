screen r_hyouji_cha_ep1_text:
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nThe aged head of the Ushiromiya family.  Even though it has already been announced that he has just a few months left to live, he is brimming with energy.\nThough he amassed a vast fortune in the past, he never made any announcements about his inheritance, which worries his children.\n\nHe is strongly influenced by the West and is a rabid fan of the occult.\nHis study is packed with mysterious grimoires.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nDisappeared from his study unnoticed.\nKinzo's study has everything from a bed to a toilet to a bathtub, so it is extremely rare for him to go outside.\n\nHowever, he does occasionally go out for a walk on a whim without telling anybody, and his disappearance invariably leads to a huge uproar throughout the house.\nHe usually comes back as soon as he gets hungry...usually...")
        if r[r_hyouji_cha][condition] == 3:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nBurned in the incinerator, with a weapon resembling an ice-pick rammed into his forehead.\n\nThe old sorcerer's wish vanished before it could be granted.\nHe always knew that this was one possible result of his risky gamble.")
    
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nKinzo's first child.\nAs the oldest of the four siblings, he leads the family conference.\nHowever, the other siblings think that he is trying to get all of the inheritance for himself, and this further strains the tensions between them.\n\nHe is a real estate investor and has put a lot of money into the development of a resort.\nHowever, his results have been harshly criticized.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nHis corpse was found inside the rose garden storehouse.\nThe direct cause of death is unknown, but it seems the side of his head was smashed after his death.\n\nThis is the beginning of everything.")
    
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nKrauss' wife.\nShe manages the household of the Ushiromiya head family in place of her husband, who takes little interest in such matters.\nShe was in charge of all preparations and arrangements for this family conference.\n\nShe possesses a strong sense of responsibility and a great deal of pride.\nHowever, neither her husband nor his siblings understand her very well, so her position is far from enviable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nFound shot to death in front of the witch's portrait.\n\nHow impudent of her to challenge a witch with nothing but a mere gun.  Of course she'd end up like this.\nKihihihihihihihihihi.")
    
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nKrauss and Natsuhi's daughter.\nIn the absence of any irregularities, it is thought that she will eventually inherit the headship of the Ushiromiya family (or rather, her husband will).  However, she seems to have no interest in all of this.\n\nShe was born with weak bronchi and is sometimes assailed by sudden asthma attacks.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nMissing.\n\nEven though she was given a precious invitation to the Golden Land, a single fool refused to believe in the witch, and all of the magic disappeared.\n\nShe was then chewed to bits by demons and went to hell.")
    
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nKinzo's second child.\nShe is hostile towards her brother Krauss and opposes him whenever she can, from issues dealing with the family fortune to the question of who will succeed the family headship.\n\nNormally, she would have lost her place in the Ushiromiya family register upon her marriage, but she managed to forcibly overcome this by having her husband take her family name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nFound on the bed of a guest room inside the mansion, with a weapon resembling an ice-pick rammed into her forehead.\n\nThe windows and door to the room were locked from the inside, and even the chain was set.\nThere was no way for a human being to have killed her.")
    
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nEva's husband.\nHe took his wife's name upon their marriage and became a member of the Ushiromiya family.\nHe therefore does not possess the spiteful genes passed down through Ushiromiya family members, and his bright smile is very refreshing at the family conferences.\n\nHe started his business from scratch and now works as the president of a medium-sized restaurant chain.\nThis chain seems to be growing and performing extremely well.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nFound in the bathroom of the same guest room the Eva was found in.  Like Eva, there was a weapon resembling an ice-pick rammed into his forehead.\n\nYou can't see either of them by looking through the gap of the door while the chain is set.\nYou can't see them, so you can't reach them.\nHey, how could a human possibly kill them?\nKihihihihihihihihihihihi.")
    
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nEva and Hideyoshi's son.\nAn affable yound man liked by everyone in the family.\nHe is currently studying as an assistant for his father's company, and it seems he dreams of making it on his own one day.\n\nAs the oldest of the four cousins, he acts as their leader and arbitrator.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nMissing.\n\nEven though everyone was finally getting along so well after being reunited in the Golden Land, all of the magic came to nothing because of a certain hardheaded fool.\n\nAfterwards, the demons chewed him to the bone and he went to hell.")
    
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nKinzo's third child.\nAlong with his sister, Eva, he intends to make his voice heard during the family conference to prevent their oldest sibling, Krauss, from keeping all of their father's wealth for himself.\n\nHis former wife, Asumu, passed away six years ago, and he married his current wife, Kyrie, shortly after that.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nHis corpse was found inside the rose garden storehouse.\nHis face seems to have been smashed after his death.\n\nHe has the right to lament his ill fortune.")
    
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nRudolf's second wife.\nShe had already worked alongside him for some time before the death of his first wife, at which time she openly took the position of his wife.\n\nShe has served as Rudolf's right hand in several shady pieces of business, guiding them to success.\nShe is quick-thinking and well-trusted by her husband.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nHer corpse was found inside the rose garden storehouse.\nHer face seems to have been smashed after her death.\n\nShe was chosen by the Demons' Roulette.\nThat's all there is to it.")
    
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nThe son of Rodolf and his first wife, Asumu.\nWhen his father married a second wife shortly after Asumu's death, Battler rebelled and went to live with his grandparents on his mother's side.\nHowever, both of these grandparents passed away, and he has now returned to the Ushiromiya family after six years.\n\nThis family conference is a chance for him to renew his friendship with his cousins after a six year gap.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nMissing.\n\nThis fool made the world where everyone could be happy all come to nothing.\n\nThough Beatrice is extremely angry, she also seems to be enjoying herself immensely.\nIt's almost as though she's waited a thousand years to get her hands on a toy as fun as this one.\n\nHopefully, even this fool will be able to see you before too long...")
    
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nThe leader of the servants who work for the Ushiromiya family.\nHe has served Kinzo longer than any other and has formed a strong bond of trust with the old man.\n\nSince he serves Kinzo directly, Krauss and Natsuhi suspect him of being Kinzo's spy.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nFound in the parlor.  His stomach had been pierced by a weapon resembling an ice-pick, and his face had been smashed.\n\nOn the sixth twilight, gouge the stomach and kill.")
    
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nKinzo's fourth child.\nShe is by far the youngest of the four siblings.  It seems that this gives her a weaker position at the family conference.\n\nShe manages a design company, but she has yet to start taking it seriously, and its financial situation is far from favorable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nHer corpse was found inside the rose garden storehouse.\nHer face seems to have been smashed after her death.\n\nWe'll be able to see her again.  No need to feel lonely.")
    
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nRosa's daughter.  Her father's identity is unknown.\nShe can't shake off the habit of speaking like a young child, which often earns her a scolding.\n\nShe has no interest in studying or making friends, but is very interested in things concerning the occult and black magic.  Thanks to her excellent powers of memorization, she knows all kinds of obscure trivia.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nMissing.\n\nKihihihihihihihihihihihi.")
    
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nKinzo's attending physician and long time friend.\nHe once ran a hospital on Niijima, but he turned it over to his son and now enjoys his old age is peace.\n\nNow that Kinzo's constant suspicion has reached extraordinary heights, Nanjo is one of the very few people he trusts.\nThanks to Nanjo's big-hearted nature, he has been able to continue his friendship with Kinzo despite the latter's tendency to fly into a rage at the slightest provocation.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nFound in the parlor.  His thigh had been pierced by a weapon resembling an ice-pick, and his face had been smashed.\n\nOn the seventh twilight, gouge the knee and kill.")
    
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Shannon{/size}\n\nA young but experienced servant.\nShe's normally calm and performs her job flawlessly, but she messes up when she gets nervous.\n\nFurthermore, Shannon is nothing more than a pseudonym that she uses when on duty, not her real name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Shannon{/size}\n\nHer corpse was found inside the rose garden storehouse.\nIt seems the side of her head was smashed after her death.\n\nDon't worry.  Everyone will be revived in the Golden Land.")
    
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kanon{/size}\n\nA young servant.\nHe performs his duties silently and diligently, but is not so highly regarded as a servant due to his unsociable nature.\n\nThere are serval other servants with the chracter \"{font=default.ttf}音{/font}\" in their pseudonyms.  He and Shannon just happened to be the ones on duty that day.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kanon{/size}\n\nFound in the boiler room with a weapon resembling and ice-pick rammed into his chest.\n\nHow presumptuous for such lowly funiture.")
    
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nThe servant employed as the family chef.\nHe hasn't served this family long, but through his earlier jobs and previous experience, he has cultivated a talent for entertaining guests.  Because of this, he is very highly regarded as a servant.\n\nGohda was hired by Krauss and his wife, so he is more trusted than those servants who have served the family longer and who are suspected of being Kinzo's spies.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nHis corpse was found inside the rose garden storehouse.\nHis face seems to have been smashed after his death.\n\nHow unfortunate.  Apparently, he was actually supposed to be on duty in the guesthouse.")
    
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nThis elderly woman is a part-timer who, though she has quit her job several times along the way, has served the family for a great many years in total.\n\nShe is crafty and more than competent when it comes to performing her duties, but because of her chattiness and love of rumors, she is not highly regarded as a servant.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nFound in the parlor.  Her calf had been pierced by a weapon resembling an ice-pick, and her face had been smashed.\n\nOn the eighth twilight, gouge the leg and kill.")
    
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Golden Witch who has lived for a thousand years.\nShe has surpassed the limits of humans and will, just as demons do, appear in response to a human's summons to lend them her power for a price.\n\nShe likes black tea and ice cream.\nShe hates boredom and people who deny her existence.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Beatrice{/size}\n\nIt is utterly useless to try and kill me, foolish human.\nEven if you fire bullets at me, they will merely bounce back as though by a mirror and strike you down.\n\nHowever, there is one single way to kill me.\nYou grasp this method in the palm of your hand.\nStill, I doubt a mediocre fool like you could ever do it.\n\nKihihihihihihihihihihihi!\n*cackle*cackle*cackle*cackle*!")
    
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of the Fragments who has lived a thousand years.\nIt is said that she lives in a world where concepts like fate and possibility can be visualized.\nShe observes the fate of humans and sometimes interferes.\n\nIn other words, sometimes she is both you..and also your closest friend.  ......Understand?\n\nShe likes wine and spicy foods.\nShe hates boredom and people who never learn.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nIf I continue to think, I will live on for all eternity.\nIn other words, if I stop thinking, I can die at any time.\nHowever, once I start thinking again, I will revive no matter what.\n\nThat's why I'm fickle and whimsical.\nI live as I want to, die as I want to, and revive as I want to.")
    
    side "c r":
        area (190, 180, 995, 740)        ## was area (190, 180, 995, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
    
screen r_hyouji_cha_ep1_2_text:
    
    if r_hyouji_cha_ma == ma_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Golden Witch who has lived for a thousand years.\nShe has surpassed the limits of humans and will, just as demons do, appear in response to a human's summons to lend them her power for a price.\n\nShe likes black tea and ice cream.\nShe hates boredom and people who deny her existence.")
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            $ r_text = _("{size=60}Beatrice{/size}\n\nIt is utterly useless to try and kill me, foolish human.\nEven if you fire bullets at me, they will merely bounce back as though by a mirror and strike you down.\n\nHowever, there is one single way to kill me.\nYou grasp this method in the palm of your hand.\nStill, I doubt a mediocre fool like you could ever do it.\n\nKihihihihihihihihihihihi!\n*cackle*cackle*cackle*cackle*!")
    
    elif r_hyouji_cha_ma == ma_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of the Fragments who has lived a thousand years.\nIt is said that she lives in a world where concepts like fate and possibility can be visualized.\nShe observes the fate of humans and sometimes interferes.\n\nIn other words, sometimes she is both you..and also your closest friend.  ......Understand?\n\nShe likes wine and spicy foods.\nShe hates boredom and people who never learn.")
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nIf I continue to think, I will live on for all eternity.\nIn other words, if I stop thinking, I can die at any time.\nHowever, once I start thinking again, I will revive no matter what.\n\nThat's why I'm fickle and whimsical.\nI live as I want to, die as I want to, and revive as I want to.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep2_text:
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nThe aged head of the Ushiromiya family.  Even though it has already been announced that he has just a few months left to live, he is brimming with energy.\nThough he amassed a vast fortune in the past, he never made any announcements about his inheritance, which worries his children.\n\nHe is strongly influenced by the West and is a rabid fan of the occult.\nHis study is packed with mysterious grimoires.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nMissing.\n\nHe finally reached the Golden Land he so desired to see.\nHowever, since a certain fool was once again unwilling to acknowledge it, the magic vanished once again.\n\nEven so, he was probably happy.\nAfter all, he managed to be reunited with the Golden Witch, if only for a brief time.\n\nAfterwards, he was torn to pieces and eaten by the demons as he went to hell.")
    
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nKinzo's first child.\nAs the oldest of the four siblings, he leads the family conference.\nHowever, the other siblings think that he is trying to get all of the inheritance for himself, and this further strains the tensions between them.\n\nHe is a real estate investor and has put a lot of money into the development of a resort.\nHowever, his results have been harshly criticized.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nHis corpse was found in the chapel.\nThe direct cause of death is unknown, but it seems his stomach was cut open and his intestines pulled out after his death.\nOn top of that, sweets and candies were packed into his stomach.\n\nWelcome Maria.\nHappy Halloween.")
    
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nKrauss' wife.\nShe manages the household of the Ushiromiya head family in place of her husband, who takes little interest in such matters.\nShe was in charge of all preparations and arrangements for this family conference.\n\nShe possesses a strong sense of responsibility and a great deal of pride.\nHowever, neither her husband nor his siblings understand her very well, so her position is far from enviable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nHer corpse was found in the chapel.\nThe direct cause of death is unknown, but it seems her stomach was cut open and her intestines pulled out after her death.\nOn top of that, sweets and candies were packed into her stomach.\n\nDidn't I tell you that her stomach would be filled with candy?")
    
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nKrauss and Natsuhi's daughter.\nIn the absence of any irregularities, it is thought that she will eventually inherit the headship of the Ushiromiya family (or rather, her husband will).  However, she seems to have no interest in all of this.\n\nShe was born with weak bronchi and is sometimes assailed by sudden asthma attacks.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nFound in her own room in the mansion with a weapon shaped like a stake rammed into her back.\n\nFinally, at the very end, she got to be with the person she loved.\nShe must have been happy.")
    
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nKinzo's second child.\nShe is hostile towards her brother Krauss and opposes him whenever she can, from issues dealing with the family fortune to the question of who will succeed the family headship.\n\nNormally, she would have lost her place in the Ushiromiya family register upon her marriage, but she managed to forcibly overcome this by having her husband take her family name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nHer corpse was found in the chapel.\nThe direct cause of death is unknown, but it seems her stomach was cut open and her intestines pulled out after her death.\nOn top of that, sweets and candies were packed into her stomach.\n\nAll stomachs are filled with sweet dreams.")
    
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nEva's husband.\nHe took his wife's name upon their marriage and became a member of the Ushiromiya family.\nHe therefore does not possess the spiteful genes passed down through Ushiromiya family members, and his bright smile is very refreshing at the family conferences.\n\nHe started his business from scratch and now works as the president of a medium-sized restaurant chain.\nThis chain seems to be growing and performing extremely well.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nHis corpse was found in the chapel.\nThe direct cause of death is unknown, but it seems his stomach was cut open and his intestines pulled out after his death.\nOn top of that, sweets and candies were packed into his stomach.\n\nWhat's so filthy about the inside of a stomach?")
    
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nEva and Hideyoshi's son.\nAn affable yound man liked by everyone in the family.\nHe is currently studying as an assistant for his father's company, and it seems he dreams of making it on his own one day.\n\nAs the oldest of the four cousins, he acts as their leader and arbitrator.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nDied in Natsuhi's room, with his stomach pierced by a weapon shaped like a stake.\n\nOn the sixth twilight, gouge the stomach and kill.\n\nThese two might have ended up as the second twilight.")
    
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nKinzo's third child.\nAlong with his sister, Eva, he intends to make his voice heard during the family conference to prevent their oldest sibling, Krauss, from keeping all of their father's wealth for himself.\n\nHis former wife, Asumu, passed away six years ago, and he married his current wife, Kyrie, shortly after that.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nHis corpse was found in the chapel.\nThe direct cause of death is unknown, but it seems his stomach was cut open and his intestines pulled out after his death.\nOn top of that, sweets and candies were packed into his stomach.\n\nThis is why we want to be as sweet and innocent as candy.")
    
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nRudolf's second wife.\nShe had already worked alongside him for some time before the death of his first wife, at which time she openly took the position of his wife.\n\nShe has served as Rudolf's right hand in several shady pieces of business, guiding them to success.\nShe is quick-thinking and well-trusted by her husband.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nHer corpse was found in the chapel.\nThe direct cause of death is unknown, but it seems her stomach was cut open and her intestines pulled out after her death.\nOn top of that, sweets and candies were packed into her stomach.\n\nAnd so, I give you the land of dreams.\nHappy Halloween.")
    
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nThe son of Rodolf and his first wife, Asumu.\nWhen his father married a second wife shortly after Asumu's death, Battler rebelled and went to live with his grandparents on his mother's side.\nHowever, both of these grandparents passed away, and he has now returned to the Ushiromiya family after six years.\n\nThis family conference is a chance for him to renew his friendship with his cousins after a six year gap.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nMissing.\n\nHe did surrender to the witch at one point, but he pulled himself together and regained his will to fight.\n\nI see, so witches enjoy breaking a toy like Battler?\nSo that's why she breaks him again all the time.\n\nTorture is meaningless if you kill the subject.\nYou have to alternate between causing pain and letting them rest.")
    
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nThe leader of the servants who work for the Ushiromiya family.\nHe has served Kinzo longer than any other and has formed a strong bond of trust with the old man.\n\nSince he serves Kinzo directly, Krauss and Natsuhi suspect him of being Kinzo's spy.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nMissing.\n\nUnselfish furniture seeks nothing but repose in the Golden Land.\nHowever, since a certain fool obstinately blocks the way to the Golden Land, his repose is unlikely to come anytime soon.\n\nAfterwards, he was torn to pieces and eaten by the demons as he went to hell.")
    
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nKinzo's fourth child.\nShe is by far the youngest of the four siblings.  It seems that this gives her a weaker position at the family conference.\n\nShe manages a design company, but she has yet to start taking it seriously, and its financial situation is far from favorable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nMissing.\n\nIn the Golden Land, she finally found a treasure more precious than gold.\nHowever, it only lasted a brief time.\nBecause of a certain fool, she was forced to once again lose what she had finally found.\n\nAfterwards, she was chewed into a pulp by the demons as she went to hell.")
    
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nRosa's daughter.  Her father's identity is unknown.\nShe can't shake off the habit of speaking like a young child, which often earns her a scolding.\n\nShe has no interest in studying or making friends, but is very interested in things concerning the occult and black magic.  Thanks to her excellent powers of memorization, she knows all kinds of obscure trivia.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nMissing.\n\nIn the Golden Land, she saw that her mother still truly loved her.\n\nAt least for now, she is satisfied.")
    
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nKinzo's attending physician and long time friend.\nHe once ran a hospital on Niijima, but he turned it over to his son and now enjoys his old age is peace.\n\nNow that Kinzo's constant suspicion has reached extraordinary heights, Nanjo is one of the very few people he trusts.\nThanks to Nanjo's big-hearted nature, he has been able to continue his friendship with Kinzo despite the latter's tendency to fly into a rage at the slightest provocation.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nDied in the servant room, his throat sliced open by a sharp blade or something similar.\n\nHowever, this alone isn't enough.")
        if r[r_hyouji_cha][condition] == 3:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nHis corpse, which had gone missing, was later found in the courtyard.\nAt that time, it had a weapon shaped like a stake rammed into its knee.\n\nWith this, the seventh twilight is finished.")
    
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Shannon{/size}\n\nA young but experienced servant.\nShe's normally calm and performs her job flawlessly, but she messes up when she gets nervous.\n\nFurthermore, Shannon is nothing more than a pseudonym that she uses when on duty, not her real name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Shannon{/size}\n\nDied in Natsuhi's room, with her forehead pierced by a weapon shaped like a stake.\n\nOn the fourth twilight, gouge the head and kill.\n\nShe got to spend her last moments with the man she loved.")
    
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kanon{/size}\n\nA young servant.\nHe performs his duties silently and diligently, but is not so highly regarded as a servant due to his unsociable nature.\n\nThere are serval other servants with the chracter \"{font=default.ttf}音{/font}\" in their pseudonyms.  He and Shannon just happened to be the ones on duty that day.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kanon{/size}\n\nMissing.\n\nThe witch erased his corpse for fun.\nThat alone caused an incredible uneasiness among the survivors.\n\nThat which exists is of the human world, but things that do not exist are naught but illusions.\n\nThe illusion takes the form of the things they fear.")
        if r[r_hyouji_cha][condition] == 3:
            $ r_text = _("{size=60}Kanon{/size}\n\nThere is no corpse.  And yet, he is dead.\n\nThe witch said so in red.\nTherefore, he is definitely dead, even if there is no corpse.")
    
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nThe servant employed as the family chef.\nHe hasn't served this family long, but through his earlier jobs and previous experience, he has cultivated a talent for entertaining guests.  Because of this, he is very highly regarded as a servant.\n\nGohda was hired by Krauss and his wife, so he is more trusted than those servants who have served the family longer and who are suspected of being Kinzo's spies.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nDied in Natsuhi's room, with his chest pierced by a weapon shaped like a stake.\n\nOn the fifth twilight, gouge the chest and kill.\n\nThe cook was cooked.\nKihihihihi.")
    
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nThis elderly woman is a part-timer who, though she has quit her job several times along the way, has served the family for a great many years in total.\n\nShe is crafty and more than competent when it comes to performing her duties, but because of her chattiness and love of rumors, she is not highly regarded as a servant.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nDied in the servant room, her throat sliced open by a sharp blade or something similar.\n\nThe finishing touches are yet to come.")
        if r[r_hyouji_cha][condition] == 3:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nHer corpse, which had gone missing, was later found in the courtyard.\nAt that time, it had a weapon shaped like a stake rammed into its ankle.\n\nWith this, even the eighth twilight is finished.")
    
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Golden Witch who has lived for a thousand years.\nShe has surpassed the limits of humans and will, just as demons do, appear in response to a human's summons to lend them her power for a price.\n\nShe likes black tea and ice cream.\nShe hates boredom and people who deny her existence.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe mysterious visitor and the 19th person who appeared on the day of the family conference.\nShe uses the same name as the Golden Witch who gave the gold to Kinzo.\n\nHer reasons for coming to the island are unknown.\n\nShe was ushered into the VIP room, which no one had been allowed to use in the past.")
        if r[r_hyouji_cha][condition] == 3:
            $ r_text = _("{size=60}Beatrice{/size}\n\nIt is utterly useless to try and kill me, foolish human.\nEven if you fire bullets at me, they will merely bounce back as though by a mirror and strike you down.\n\nHowever, there is one single way to kill me.\nYou grasp this method in the palm of your hand.\nStill, I doubt a mediocre fool like you could ever do it.\n\nKihihihihihihihihihihihi!\n*cackle*cackle*cackle*cackle*!")
    
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of the Fragments who has lived a thousand years.\nIt is said that she lives in a world where concepts like fate and possibility can be visualized.\nShe observes the fate of humans and sometimes interferes.\n\nIn other words, sometimes she is both you..and also your closest friend.  ......Understand?\n\nShe likes wine and spicy foods.\nShe hates boredom and people who never learn.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep2_2_text:
    
    if r_hyouji_cha_ma == ma_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Endless Witch who has lived for a thousand years.\nShe is known for being exceptionally cruel, even among witches.\n\nShe loves bullying the weak and is capable of using trial-and-error endlessly to find the cruelest fate they can possibly be given.\nAnd she toys with her victims even further by piling on one after another.\n\nThis witch is extremely powerful, but word has it that she sometimes becomes obsessed with the art of creating certain patterns, so that her means end up becoming her goals.")
    
    elif r_hyouji_cha_ma == ma_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of Miracles who lived for a thousand years.\nHer vast power is capable of creating all kinds of miracles, but her heart has broken a bit as a result.\n\nBack when she was a human, Lambdadelta once imprisoned her within a cruel fate, toying with her the whole time.  It seems that she's unable to abandon others who are caught within a similar fate.\n\nIn theory, she holds the strongest power of any witch, but in practice, that is no more realistic than folding a piece of paper a hundred times so that it reaches the moon.\n\nYet, she did fold it a hundred times.")
    
    elif r_hyouji_cha_ma == ma_but:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nAn unfortunate young man whom Beatrice has taken a liking to.\nA human who inherited the black blood from Kinzo.\n\nThe massive resistance to magical power that Kinzo was born with was passed on to Battler.  Ironically, it was this trait that made it so hard for Kinzo to succeed as a magician.\n\nA massive defense power against magic can be very useful in a battle against a witch.\n\nKinzo has begun to lose this power with age, but Battler's power is still on the rise.\n\nPerhaps it's understandable why Beatrice tried to crush it as soon as possible.")
    
    elif r_hyouji_cha_ma == ma_gen:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Genji{/size}\n\nKinzo's earliest furniture, which he created to serve him and him alone with complete loyalty.\n\nThough he was Kinzo's first creation, he was made with the help of a high-class demon, so though there were several defects in his intial specifications, he conceals a great potential within himself.\n\nIn the many years following that, he began to mature and compensate for his many deficiencies, turning himself into the nearly flawless butler furniture that he is now.\n\nHe is approaching the limit of his service life, but the magical power he can unleash for an instant rivals Kinzo's.")
    
    elif r_hyouji_cha_ma == ma_kan:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Kanon{/size}\n\nSo far, he is the last furniture created by Kinzo.\n\nMaking use of all his previous experience, Kinzo managed to implement a set flawless specs.\nKanon was also given a heart, but it was much weaker than Shannon's.\n\nPerhaps because Kinzo felt a sense of approaching personal danger related to his fortune as he neared the end of his life, he bestowed Kanon with the rare power to fight and protect.\n\nHowever, he hasn't yet matured very far and is unable to control his own power and speed.")
    
    elif r_hyouji_cha_ma == ma_kin:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nA self-taught human sorcerer.\nHis natural talent and level of knowledge are nothing special, but when his insane powers of concentration and dedication were transformed into magical power, he awakened as a great sorcerer.\n\nHis power is at least great enough that he was able to summon Beatrice and form a contract with her.\n\nThough his power is great, it is also extremely limited.  He specializes in summoning and barriers, so perhaps it is fitting to call him a summoner.")
    
    elif r_hyouji_cha_ma == ma_lam:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Lambdadelta{/size}\n\nThe Witch of Certainty who has lived for a thousand years.\nShe embodies the idea that \"hard workers are rewarded\" and is highly respected even by humans.\n\nThough she is a witch, she does not stray far from the concepts of humans.  For that reason, her power as one worshiped by humans is incalculable.\n\nHowever, she is fickle about whose efforts she chooses to reward, and in many cases, she bestows her favor upon those who please her the most.\n\nHer massive, swift and terrifying power can cause any witch to surrender in an instant.\n\nHowever, she is often reckless, and Bernkastel was able to take full advantage of that.")
    
    elif r_hyouji_cha_ma == ma_mar:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nA little magician who has inherited the black blood from Kinzo.\n\nUnlike Knizo, she was gifted with talent and has begun to tread the path of the magician from a young age.\nHowever, her power is still weak, and she is no more than an apprentice.\n\nHowever, she is skilled with enchantments, which bestow magical power upon objects, and the magical items she creates are all master class.")
    
    elif r_hyouji_cha_ma == ma_sha:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Shannon{/size}\n\nShannon is, in the truest sense, Kinzo's handmade furniture, which he created without borrowing the power of demons.\n\nThough there were a few problems with her intial specifications, she was given a very rare and precious thing: a heart.\nIt seems that, as a result of his long personal experience, Kinzo came to believe that the power created by the heart contains within it a strong magic.\n\nIn the lengthy span of time following that, she began to mature, becoming exceptionally skilled with powers of a protective or repulsive nature, such as magical barriers.\n\nBecause of this, in the realm of barriers alone, she possesses an immense, magician-class power.")
    
    elif r_hyouji_cha_ma == ma_rg1:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Lucifer the Eldest Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nHaughty and arrogant.\nHowever, she actually feels pleasure from submission.")
    
    elif r_hyouji_cha_ma == ma_rg2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Leviathan the Second Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nNothing but a jealous crybaby.\nShe'll do whatever it takes to get what she wants.")
    
    elif r_hyouji_cha_ma == ma_rg3:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Satan the Third Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nVery quick to anger.\nHowever, she actually wants others to be angry at her.")
    
    elif r_hyouji_cha_ma == ma_rg4:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Belphegor the Fourth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nSensible and reliable.\nBecause of this, she corrupts her masters.")
    
    elif r_hyouji_cha_ma == ma_rg5:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Mammon the Fifth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nVery greedy.\nOnce she decides she wants something, she will sacrifice anything and everything to get it.")
    
    elif r_hyouji_cha_ma == ma_rg6:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Beelzebub the Sixth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nA true gourmet.\nShe would use any ingredients to make a good meal, even her own body.")
    
    elif r_hyouji_cha_ma == ma_rg7:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Asmodeus the Seventh Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\nThey can act by their own will, but they cannot disobey the orders of their master.\n\nThey are quite powerful while in their human forms, but when they return to their true forms as the Seven Stakes of Purgatory and fly at the enemy at high-speeds, they display their full, terrifying potential.\n\nA girl at that age where they want a boyfriend.\nShe would give up her life for love.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep3_text:
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nThe aged head of the Ushiromiya family.  Even though it has already been announced that he has just a few months left to live, he is brimming with energy.\nThough he amassed a vast fortune in the past, he never made any announcements about his inheritance, which worries his children.\n\nHe is strongly influenced by the West and is a rabid fan of the occult.\nHis study is packed with mysterious grimoires.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nHis body was found burnt to death in the incinerator in the underground boiler room.\n\nBecause there was no evidence found inside the incinerator, it is probably appropriate to think that he was burned after he was murdered.\n\nToo bad this time.\nIt was game over right from the start.")
    
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nKinzo's first child.\nAs the oldest of the four siblings, he leads the family conference.\nHowever, the other siblings think that he is trying to get all of the inheritance for himself, and this further strains the tensions between them.\n\nHe is a real estate investor and has put a lot of money into the development of a resort.\nHowever, his results have been harshly criticized.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nHis corpse was found in the arbor of the rose garden.\nIt is assumed that the cause of death was strangling by a thin object.\nA stake-shaped weapon was sticking out of his thigh.\n\nIf only there wasn't that stupid epitaph, I wouldn't have needed a stake.  What a pain.")
    
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nKrauss' wife.\nShe manages the household of the Ushiromiya head family in place of her husband, who takes little interest in such matters.\nShe was in charge of all preparations and arrangements for this family conference.\n\nShe possesses a strong sense of responsibility and a great deal of pride.\nHowever, neither her husband nor his siblings understand her very well, so her position is far from enviable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nHer corpse was found in the arbor of the rose garden.\nIt is assumed that the cause of death was strangling by a thin object.\nA stake-shaped weapon was sticking out of her calf.\n\nWhy follow the epitaph in the first place?  A game?")
    
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nKrauss and Natsuhi's daughter.\nIn the absence of any irregularities, it is thought that she will eventually inherit the headship of the Ushiromiya family (or rather, her husband will).  However, she seems to have no interest in all of this.\n\nShe was born with weak bronchi and is sometimes assailed by sudden asthma attacks.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nMissing.\n\nShe was surely joined with Kanon in the Golden Land.\nThey both apologized for their cowardice, and communicated their true and honest feelings.\nAnd they hugged each other until the last moment.\n\nAfterwards, she was chewed to pieces by the demons, and went to hell.\nIt's alright.  Kanon is with her.")
    
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nKinzo's second child.\nShe is hostile towards her brother Krauss and opposes him whenever she can, from issues dealing with the family fortune to the question of who will succeed the family headship.\n\nNormally, she would have lost her place in the Ushiromiya family register upon her marriage, but she managed to forcibly overcome this by having her husband take her family name.")
    
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nEva's husband.\nHe took his wife's name upon their marriage and became a member of the Ushiromiya family.\nHe therefore does not possess the spiteful genes passed down through Ushiromiya family members, and his bright smile is very refreshing at the family conferences.\n\nHe started his business from scratch and now works as the president of a medium-sized restaurant chain.\nThis chain seems to be growing and performing extremely well.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nDied in the hall of the mansion, his chest pierced by a stake-shaped weapon.\n\nHow careless.  He was still living......")
    
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nEva and Hideyoshi's son.\nAn affable yound man liked by everyone in the family.\nHe is currently studying as an assistant for his father's company, and it seems he dreams of making it on his own one day.\n\nAs the oldest of the four cousins, he acts as their leader and arbitrator.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nHis corpse was found in the mansion's parlor.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nIn exchange for his soul, the witch gave 8 numbers.\n\n07151129\nIf you say it, a small Golden Land will be opened.")
    
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nKinzo's third child.\nAlong with his sister, Eva, he intends to make his voice heard during the family conference to prevent their oldest sibling, Krauss, from keeping all of their father's wealth for himself.\n\nHis former wife, Asumu, passed away six years ago, and he married his current wife, Kyrie, shortly after that.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nDied in the hall of the mansion, his forehead pierced by a stake-shaped weapon.\n\nFrom here on, a stake must be the finishing blow.  How vulgar.")
    
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nRudolf's second wife.\nShe had already worked alongside him for some time before the death of his first wife, at which time she openly took the position of his wife.\n\nShe has served as Rudolf's right hand in several shady pieces of business, guiding them to success.\nShe is quick-thinking and well-trusted by her husband.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nDied in the hall of the mansion, her stomach pierced by a stake-shaped weapon.\n\nThe stomach isn't a very lethal spot.\nIs it OK to kill in a different way and stick the stake in the corpse?")
    
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nThe son of Rodolf and his first wife, Asumu.\nWhen his father married a second wife shortly after Asumu's death, Battler rebelled and went to live with his grandparents on his mother's side.\nHowever, both of these grandparents passed away, and he has now returned to the Ushiromiya family after six years.\n\nThis family conference is a chance for him to renew his friendship with his cousins after a six year gap.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nWas shot to death by Ushiromiya Eva inside the mansion.\nThe weapon was a Winchester from Knzo's collection.\n\nJessica lost her eyesight.  Battler was with her.\nWolf and sheep puzzle.")
    
    elif r_hyouji_cha == r_enj:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Ange{/size}\n\nRudolf and Kyrie's daughter.  Battler's younger sister from a different mother.\nShe hasn't come in contact with Battler often, but is extremely close to him and respects him.\n\nBecause she was sick and absent during the family conference, she always survives in solitude.\n\nUnluckily, her heart has been laid waste.\nHas a bad habit of always walking around with a massive amount of cash, throwing it out to whoever comes first.")
    
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nThe leader of the servants who work for the Ushiromiya family.\nHe has served Kinzo longer than any other and has formed a strong bond of trust with the old man.\n\nSince he serves Kinzo directly, Krauss and Natsuhi suspect him of being Kinzo's spy.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nHis body was found in the VIP room on the second floor.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nGenji worked for many years of service, so let's let him sleep in the honored guests room.")
    
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nKinzo's fourth child.\nShe is by far the youngest of the four siblings.  It seems that this gives her a weaker position at the family conference.\n\nShe manages a design company, but she has yet to start taking it seriously, and its financial situation is far from favorable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nDied in the rose garden, her medulla oblongata was pierced by the spear-shaped part of the fence.\nIf Maria hadn't been killed by another person, you might suspect that Rosa died in an accident.\n\nShe was the sacrifice for the birth of the new witch.")
    
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nRosa's daughter.  Her father's identity is unknown.\nShe can't shake off the habit of speaking like a young child, which often earns her a scolding.\n\nShe has no interest in studying or making friends, but is very interested in things concerning the occult and black magic.  Thanks to her excellent powers of memorization, she knows all kinds of obscure trivia.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nHer corpse was found in the rose garden.\nThe cause of death was strangling.  Probably with bare hands.\nJudging by the situation, it is probably appropriate to think that she was killed after Rosa.\n\nThen her blood became the red ink for the witch's oath.")
    
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nKinzo's attending physician and long time friend.\nHe once ran a hospital on Niijima, but he turned it over to his son and now enjoys his old age is peace.\n\nNow that Kinzo's constant suspicion has reached extraordinary heights, Nanjo is one of the very few people he trusts.\nThanks to Nanjo's big-hearted nature, he has been able to continue his friendship with Kinzo despite the latter's tendency to fly into a rage at the slightest provocation.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nHis corpse was found in the hallway in fron of the mansion's servants room.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nJust a little longer, and he probably would have been able to return alive.\nHowever, in the very end, the witch did not permit that.")
    
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Shannon{/size}\n\nA young but experienced servant.\nShe's normally calm and performs her job flawlessly, but she messes up when she gets nervous.\n\nFurthermore, Shannon is nothing more than a pseudonym that she uses when on duty, not her real name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Shannon{/size}\n\nHer corpse was found in the parlor on the first floor.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nFor Shannon, the parlor, with its wonderful view of the rose garden on sunny days.")
    
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kanon{/size}\n\nA young servant.\nHe performs his duties silently and diligently, but is not so highly regarded as a servant due to his unsociable nature.\n\nThere are serval other servants with the chracter \"{font=default.ttf}音{/font}\" in their pseudonyms.  He and Shannon just happened to be the ones on duty that day.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kanon{/size}\n\nHis corpse was found in the chapel.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nFor Kanon, the chapel.  Now that he's dead, let him continue to protect the place important to the Lord.")
    
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nThe servant employed as the family chef.\nHe hasn't served this family long, but through his earlier jobs and previous experience, he has cultivated a talent for entertaining guests.  Because of this, he is very highly regarded as a servant.\n\nGohda was hired by Krauss and his wife, so he is more trusted than those servants who have served the family longer and who are suspected of being Kinzo's spies.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nHis corpse was found in the waiting room on the third floor.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nThe room next to the study is fitting for him, since he wanted Knizo to like him.")
    
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nThis elderly woman is a part-timer who, though she has quit her job several times along the way, has served the family for a great many years in total.\n\nShe is crafty and more than competent when it comes to performing her duties, but because of her chattiness and love of rumors, she is not highly regarded as a servant.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nHer corpse was found in the guest room on the second floor.\nThe weapon is assumed to be a gun or a spear-shaped object.\n\nThis seldom-used second floor guest room was her secret napping room.")
    
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Golden Witch who has lived for a thousand years.\nShe has surpassed the limits of humans and will, just as demons do, appear in response to a human's summons to lend them her power for a price.\n\nShe likes black tea and ice cream.\nShe hates boredom and people who deny her existence.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Beatrice{/size}\n\nIt is utterly useless to try and kill me, foolish human.\nEven if you fire bullets at me, they will merely bounce back as though by a mirror and strike you down.\n\nHowever, there is one single way to kill me.\nYou grasp this method in the palm of your hand.\nStill, I doubt a mediocre fool like you could ever do it.\n\nKihihihihihihihihihihihi!\n*cackle*cackle*cackle*cackle*!")
    
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\A Witch of the Kakera who has lived for a thousand years.\nIt is said that she lives in a world where concepts like fate and possibility can be visualized.\nShe appreciates the fate of humans in an aesthetic sense, and sometimes interferes.\n\nIn other words, sometimes she is you; and she's also your only friend.  ......Do you understand?\n\nShe likes wine and spicy food.\nShe hates boredom and people who don't learn.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep3_2_text:
    
    if r_hyouji_cha_ma == ma3_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Endless Witch who has lived for a thousand years.\nShe is known for being exceptionally cruel, even among witches.\n\nShe loves bullying the weak and is capable of using trial-and-error endlessly to find the cruelest fate they can possibly be given.\nAnd she toys with her victims even further by piling on one after another.\n\nThis witch is extremely powerful, but word has it that she sometimes becomes obsessed with the art of creating certain patterns, so that her means end up becoming her goals.")
    
    elif r_hyouji_cha_ma == ma3_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of Miracles who lived for a thousand years.\nHer vast power is capable of creating all kinds of miracles, but her heart has broken a bit as a result.\n\nBack when she was a human, Lambdadelta once imprisoned her within a cruel fate, toying with her the whole time.  It seems that she's unable to abandon others who are caught within a similar fate.\n\nIn theory, she holds the strongest power of any witch, but in practice, that is no more realistic than folding a piece of paper a hundred times so that it reaches the moon.\n\nYet, she did fold it a hundred times.")
    
    elif r_hyouji_cha_ma == ma3_enj:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}ANGE-Beatrice{/size}\n\nThe final witch, born in 1998.\nNamed by EVA as her successor and was accepted, with Bernkastel as her guardian.\n\nAs a witch, she had to start out from zero, but because she became one 12 years in the future, she gained and extreme magical resistence power which would prevent her from being the target of any of Beatrice's magic.\n\nFurthermore, completely unlike her older brother's magical resistence, she has a natural ability to attack anything of a magical nature.\nHer potential in both attack and defense is of the highest level.  But the distance is great.  12 years really is.")
    
    elif r_hyouji_cha_ma == ma3_ev2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}EVA-Beatrice{/size}\n\nSolved the riddle of the witch's epitaph, and was welcomed as the new Endless Witch.\nShe has a natural ability in magic, and is expected to grow into an extraordinary Great Witch.\n\nThe genius witch often indulged in her own power during her younger days.\nThis is a test permitted only geniuses, and if she succeeds, her name will probably be listed in the history of Endless Witches.\n\nWill she be able to overcome the test which defeated her predecessors?")
    
    elif r_hyouji_cha_ma == ma3_goa:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}All of the Goats{/size}\n\nThey are low-level furniture that serve Beatrice.\n\nThere are many of them, but they are silent, with no personality.  They obey their Master's orders faithfully.\n\nTheir sensitivity is closer to an animal's than a human's, and they sometimes misunderstand their orders surprisingly foolishly.\nBy nature, they have a huge build like a minotaur, and incredible superhuman strength.\n\nThey are low-level as furniture, but can be very convenient since an inexhaustible supply of them can be summoned.")
    
    elif r_hyouji_cha_ma == ma3_lam:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Lambdadelta{/size}\n\nThe Witch of Certainty who has lived for a thousand years.\nShe embodies the idea that \"hard workers are rewarded\" and is highly respected even by humans.\n\nThough she is a witch, she does not stray far from the concepts of humans.  For that reason, her power as one worshiped by humans is incalculable.\n\nHowever, she is fickle about whose efforts she chooses to reward, and in many cases, she bestows her favor upon those who please her the most.\n\nHer massive, swift and terrifying power can cause any witch to surrender in an instant.\n\nHowever, she is often reckless, and Bernkastel was able to take full advantage of that.")
    
    elif r_hyouji_cha_ma == ma3_rg1:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Lucifer the Eldest Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nLucifer is the oldest of the sisters and therefore their leader.\n\nBecause of this, she claims to be the strongest of the sisters, but she's secretly aware that she's actually the least talented.\n\nHowever, she has always acted arrogantly in an attempt to hide this fact from the others.\nHer great fear is that her sisters would sneer at her if they ever found out.")
    
    elif r_hyouji_cha_ma == ma3_rg2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Leviathan the Second Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nLeviathan often speaks to Lucifer on behalf of the youngest sisters.\n\nAt her best, she has a brutal, deeply envious nature and is adept at spotting people's weaknesses.\n\nHowever, she is usually nothing more than a selfish crybaby.\n\nFor some reason, she's not a very quick thinker, and she often comes in last among the sisters, ends up with the short end of the stick, and cries.")
    
    elif r_hyouji_cha_ma == ma3_rg3:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Satan the Third Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nSatan takes on the role of the constantly angry class president among the sisters.\n\nShe is known for giving out rapid-fire scoldings, which makes the other sisters scared of her.\nBecause of this, no one is willing to talk back to her, which means she is surprisingly lonely.\n\nShe'll sometimes intentionally try to do things that should anger the other sisters, but they never scold her back, which leaves her even more lonely.")
    
    elif r_hyouji_cha_ma == ma3_rg4:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Belphegor the Fourth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nBelphegor is well trusted and known for being a reticent, serious, and responsible piece of furniture.\n\nHowever, this is all because of demonic desire to turn her masters into useless, lazy pigs.\nIn this sense, she might be the most demon-like of all the sisters.\n\nShe is serious to a fault, and not at all comfortable with being the one treated kindly instead of the other way around.")
    
    elif r_hyouji_cha_ma == ma3_rg5:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Mammon the Fifth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nMammon is quick to grab whatever she wants, without any concern for her sisters.\n\nHer motto is \"monopolize through greed.\"  Therefore, she is usually the main cause of any arguments between the sisters.\n\nHowever, among the sisters, she is the most honest about her own feelings, and the one most likely to try and please the opposite sex.\n\nShe is greedy, but a hard worker, and will stop at nothing to capture her target's affections for all eternity.")
    
    elif r_hyouji_cha_ma == ma3_rg6:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Beelzebub the Sixth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nBeelzebub is the gourmet of the sisters and is known for being a big and picky eater.\n\nHer personality is similar to Mammon's and the two sisters often fight over the same thing.\n\nShe's always talking about food, which makes her a calming influence among the sisters.\n\nHowever, she also has that disturbing desire to kidnap pretty boys and store them in the food cellar...")
    
    elif r_hyouji_cha_ma == ma3_rg7:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Asmodeus the Seventh Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nAs the youngest of the sisters, Asmodeus is always doted upon.\nThis might be why she alone is kept out of way whenever an even slightly lewd topic comes up.\n\nShe's always looking for a boyfriend in the hopes that her sisters will finally accpet her as an adult.\n\nHowever, she keeps aiming too high and whiles away each day dreaming of the prince who will never come.")
    
    elif r_hyouji_cha_ma == ma3_ron:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Ronove{/size}\n\nOne of the Great Demons of the 72 pillars.  Works for a Master in exchange for various forms of compensation.\nHe currently has a contract with Beatrice as her butler (head furniture).\n\nHe has become proficient at housekeeping after serving in many households, so his ability as a butler is very high.\n\nIn the high society of witches, employing him has become a kind of status.\nFurthermore, the cookies he bakes are superb, and witches will often form a line demanding them.\n\nHe should hold a tremendous magical power, but since he is always serving his master, his battle abilities are unknown.")
    
    elif r_hyouji_cha_ma == ma3_s41:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Chiester 410 (Yonichimaru){/size}\n\nA weapon in contract with Beatrice.\n\n410 is a kid whose personality tends to cause her to speak arrogantly.\n\nShe has a hobby of laughing at people who are serious or not relaxed, which is why she likes 45 and Lucifer.\n\nShe speaks roughly, but she loves company and easily succumbs to loneliness.\nShe gets depressed if she isn't always being looked after by someone.\n\n410 has excellent capabilities in firing control, and exhibits matchless battle power even at close quarters fighting.")
    
    elif r_hyouji_cha_ma == ma3_s45:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Chiester 45 (Yonjuugo){/size}\n\nA weapon in contract with Beatrice.\n\n45 has a very methodical and timid personality, and her persecution complex is somehwat strong.\nThis makes her compensate well for the weakness of 410's rough personality when they work as a pair.\n\nSince she cannot stand silence, she sometimes becomes emotionally insecure if she isn't always being ordered by someone.\n\n45 has excellent capabilities in searching for the enemy and deciding orders.  The sisters' battle power is multiplied by her support.")
    
    elif r_hyouji_cha_ma == ma3_wal:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Virgilia{/size}\n\nAs a now-retired Endless Witch, she was Beatrice's teacher.\nShe used the Endless Magic properly, and devoted her life to the smiles and happiness of many people.\n\nShe taught Beatrice the Endless Magic, and retired, believing that Beatrice would also devote herself to the people.\n\nAt the same time that she was Beatrice's teacher, she also served as the magician of Beatrice's home.\nBecause of that, Virgilia had come in contact with her with the position of a servant.\nIt is said that this became her downfall, and invited Beatrice's arrogance and recklessness.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep4_text:
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nThe aged head of the Ushiromiya family.  Even though it has already been announced that he has just a few months left to live, he is brimming with energy.\nThough he amassed a vast fortune in the past, he never made any announcements about his inheritance, which worries his children.\n\nHe is strongly influenced by the West and is a rabid fan of the occult.\nHis study is packed with mysterious grimoires.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kinzo{/size}\n\nHis body was found burnt to death in the incinerator in the underground boiler room.\n\nBecause there was no evidence found inside the incinerator, it is probably appropriate to think that he was burned after he was murdered.\n\nDust to Dust.  Ashes to ashes.  The dead to the dead.")
    
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nKinzo's first child.\nAs the oldest of the four siblings, he leads the family conference.\nHowever, the other siblings think that he is trying to get all of the inheritance for himself, and this further strains the tensions between them.\n\nHe is a real estate investor and has put a lot of money into the development of a resort.\nHowever, his results have been harshly criticized.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Krauss{/size}\n\nHis body was found in the vicinity of the back door to the mansion.\nHis head was half destroyed.  It is probably appropriate to think that he was murdered with something like a powerful gun.\n\nA demon stake was buried into the damaged area.\n\nNo one can escape from the Chiesters' golden arrows.")
    
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nKrauss' wife.\nShe manages the household of the Ushiromiya head family in place of her husband, who takes little interest in such matters.\nShe was in charge of all preparations and arrangements for this family conference.\n\nShe possesses a strong sense of responsibility and a great deal of pride.\nHowever, neither her husband nor his siblings understand her very well, so her position is far from enviable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Natsuhi{/size}\n\nHer body was found in the dinning hall.\nHer head was half destroyed.  It is probably appropriate to think that she was murdered with something like a powerful gun.\n\nHowever, the witnesses don't believe that she was killed with a gun...")
    
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nKrauss and Natsuhi's daughter.\nIn the absence of any irregularities, it is thought that she will eventually inherit the headship of the Ushiromiya family (or rather, her husband will).  However, she seems to have no interest in all of this.\n\nShe was born with weak bronchi and is sometimes assailed by sudden asthma attacks.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Jessica{/size}\n\nHer body was found in her room on the second floor of the mansion.\nHer head was half destroyed.  It is probably appropriate to think that she was murdered with something like a powerful gun.\n\nShe was smashed by her own attack due to George's counter-offensive specialized barrier.")
    
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nKinzo's second child.\nShe is hostile towards her brother Krauss and opposes him whenever she can, from issues dealing with the family fortune to the question of who will succeed the family headship.\n\nNormally, she would have lost her place in the Ushiromiya family register upon her marriage, but she managed to forcibly overcome this by having her husband take her family name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nHer body was found in the dinning hall.\nHer head was half destroyed.  It is probably appropriate to think that she was murdered with something like a powerful gun.\n\nHowever, the witnesses don't believe that she was killed with a gun...")
    
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nEva's husband.\nHe took his wife's name upon their marriage and became a member of the Ushiromiya family.\nHe therefore does not possess the spiteful genes passed down through Ushiromiya family members, and his bright smile is very refreshing at the family conferences.\n\nHe started his business from scratch and now works as the president of a medium-sized restaurant chain.\nThis chain seems to be growing and performing extremely well.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Hideyoshi{/size}\n\nHis body was found in the dinning hall.\nHis head was half destroyed.  It is probably appropriate to think that he was murdered with something like a powerful gun.\n\nHowever, the witnesses don't believe that he was killed with a gun...")
    
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nEva and Hideyoshi's son.\nAn affable yound man liked by everyone in the family.\nHe is currently studying as an assistant for his father's company, and it seems he dreams of making it on his own one day.\n\nAs the oldest of the four cousins, he acts as their leader and arbitrator.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya George{/size}\n\nHis body was found by the arbor of the rose garden.\nThere was a single hole right in the center of his forehead.  It is probably appropriate to think that he was shot with a gun or something.\n\nThat was a brand of disgrace marking his loss to Gaap.")
    
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nKinzo's third child.\nAlong with his sister, Eva, he intends to make his voice heard during the family conference to prevent their oldest sibling, Krauss, from keeping all of their father's wealth for himself.\n\nHis former wife, Asumu, passed away six years ago, and he married his current wife, Kyrie, shortly after that.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rudolf{/size}\n\nHis body was found in the dinning hall.\nHis head was half destroyed.  It is probably appropriate to think that he was murdered with something like a powerful gun.\n\nHowever, the witnesses don't believe that he was killed with a gun...")
    
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nRudolf's second wife.\nShe had already worked alongside him for some time before the death of his first wife, at which time she openly took the position of his wife.\n\nShe has served as Rudolf's right hand in several shady pieces of business, guiding them to success.\nShe is quick-thinking and well-trusted by her husband.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Kyrie{/size}\n\nHer body was found in a guest room inside the mansion.\nThere was a single hole right in the center of her forehead.  It is probably appropriate to think that she was shot with a gun or something.\n\nA demon stake was buried in the hole in her forehead, but it is hard to imagine that this was the cause of death.\n\nIt didn't miss.  It missed on purpose to tease her, nyeh...!")
    
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nThe son of Rodolf and his first wife, Asumu.\nWhen his father married a second wife shortly after Asumu's death, Battler rebelled and went to live with his grandparents on his mother's side.\nHowever, both of these grandparents passed away, and he has now returned to the Ushiromiya family after six years.\n\nThis family conference is a chance for him to renew his friendship with his cousins after a six year gap.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Battler{/size}\n\nMissing.\n\nAs he was held by the witch, he went to hell.\nBut to the witch, that hell was the Golden Land.")
    
    elif r_hyouji_cha == r_enj:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Ange{/size}\n\nRudolf and Kyrie's daughter.  Battler's younger sister from a different mother.\nShe hasn't come in contact with Battler often, but is extremely close to him and respects him.\n\nBecause she was sick and absent during the family conference, she always survives in solitude.\n\nUnluckily, her heart has been laid waste.\nHas a bad habit of always walking around with a massive amount of cash, throwing it out to whoever comes first.")
    
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nThe leader of the servants who work for the Ushiromiya family.\nHe has served Kinzo longer than any other and has formed a strong bond of trust with the old man.\n\nSince he serves Kinzo directly, Krauss and Natsuhi suspect him of being Kinzo's spy.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ronoue Genji{/size}\n\nHis body was found in the dinning hall.\nHis head was half destroyed.  It is probably appropriate to think that he was murdered with something like a powerful gun.\n\nHowever, the witnesses don't believe that he was killed with a gun...")
    
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nKinzo's fourth child.\nShe is by far the youngest of the four siblings.  It seems that this gives her a weaker position at the family conference.\n\nShe manages a design company, but she has yet to start taking it seriously, and its financial situation is far from favorable.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Rosa{/size}\n\nHer body was found in the dinning hall.\nHer head was half destroyed.  It is probably appropriate to think that she was murdered with something like a powerful gun.\n\nHowever, the witnesses don't believe that she was killed with a gun...")
    
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nRosa's daughter.  Her father's identity is unknown.\nShe can't shake off the habit of speaking like a young child, which often earns her a scolding.\n\nShe has no interest in studying or making friends, but is very interested in things concerning the occult and black magic.  Thanks to her excellent powers of memorization, she knows all kinds of obscure trivia.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nHer body was found in the dinning hall.\nUnable to notice any particular external wounds, Battler hypothesized that there might have been some kind of poison.\n\nThe most peaceful form of invitation to the Golden Land.")
    
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nKinzo's attending physician and long time friend.\nHe once ran a hospital on Niijima, but he turned it over to his son and now enjoys his old age is peace.\n\nNow that Kinzo's constant suspicion has reached extraordinary heights, Nanjo is one of the very few people he trusts.\nThanks to Nanjo's big-hearted nature, he has been able to continue his friendship with Kinzo despite the latter's tendency to fly into a rage at the slightest provocation.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Nanjo Terumasa{/size}\n\nHis body was found behind the mansion.\nHis head was half destroyed.  It is probably appropriate to think that he was show with a gun or something.\n\nA demon stake had fallen near the body.")
    
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Shannon{/size}\n\nA young but experienced servant.\nShe's normally calm and performs her job flawlessly, but she messes up when she gets nervous.\n\nFurthermore, Shannon is nothing more than a pseudonym that she uses when on duty, not her real name.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Shannon{/size}\n\nHer body was found behind the mansion.\nHer head was half destroyed.  It is probably appropriate to think that she was show with a gun or something.\nA demon stake had fallen near the body.\n\nThe witnesses at least realize that the stake did not kill her.")
    
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kanon{/size}\n\nA young servant.\nHe performs his duties silently and diligently, but is not so highly regarded as a servant due to his unsociable nature.\n\nThere are serval other servants with the chracter \"{font=default.ttf}音{/font}\" in their pseudonyms.  He and Shannon just happened to be the ones on duty that day.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kanon{/size}\n\nBattler was not able to find his body.\n\nNo matter how he's killed with magic, without a corpse, he's a definite suspect.\nThis is truly anti-fantasy.\n\n{color=#ff0000}Therefore, I will guarentee his death with the red truth.{/color}\n\nThis is truly anti-mystery...!")
    
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nThe servant employed as the family chef.\nHe hasn't served this family long, but through his earlier jobs and previous experience, he has cultivated a talent for entertaining guests.  Because of this, he is very highly regarded as a servant.\n\nGohda was hired by Krauss and his wife, so he is more trusted than those servants who have served the family longer and who are suspected of being Kinzo's spies.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Gohda Toshiro{/size}\n\nHis body was found in the rose garden storehouse.\nIt is hypothesized that after being shot in the forehead, he was hung by his neck.\n\nThey put loops around their own necks.\nIt's an interesting experience every now and then.")
    
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nThis elderly woman is a part-timer who, though she has quit her job several times along the way, has served the family for a great many years in total.\n\nShe is crafty and more than competent when it comes to performing her duties, but because of her chattiness and love of rumors, she is not highly regarded as a servant.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Kumasawa Chiyo{/size}\n\nHer body was found in the rose garden storehouse.\nIt is hypothesized that after being shot in the forehead, she was hung by her neck.\n\nAs long as a closed room murder could be constructed, nothing else mattered.")
    
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Endless Witch who has lived for a thousand years.\nShe is known for being the cruelest among the witches.\n\nShe loves bullying the weak and is capable of using trial-and-error infinitely to see what kind of fate is the cruelest to give.\nAnd she plays even more with what she's built up.\n\nShe is an extremely powerful witch, but since she is particular about a certain kind of pattern, it seems that her means occasionally end up becoming her goals.")
        if r[r_hyouji_cha][condition] == 2:
            $ r_text = _("{size=60}Beatrice{/size}\n\nIt's a useless dream to try to kill me with a human body.\nEven if you shoot lead bullets, they will just rebound to your pitiful body, as from a mirror.\n\nHowever, there is only one way to kill me.\nIt is possible for you to grasp that way with your hands.\nBut it's most likely impossible for a simple man like you, I suppose?\n\nKihihihihihihihihihihihi!\n*cackle* *cackle* *cackle*!")
    
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of the Kakera who has lived a thousand years.\nIt is said that she lives in a world where concepts like fate and possibility can be visualized.\nShe appreciates the aestheticism in the fate of humans, and sometimes she interferes.\n\nIn other words, sometimes she is you; and she's also your only friend.  ......Do you understand?\n\nThe things she likes are wine and spicy things.\nThe things she hates are boredom and people who will not learn.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep4_2_text:
    
    if r_hyouji_cha_ma == ma4_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Endless Witch who has lived for a thousand years.\nShe is known for being exceptionally cruel, even among witches.\n\nShe loves bullying the weak and is capable of using trial-and-error endlessly to find the cruelest fate they can possibly be given.\nAnd she toys with her victims even further by piling on one after another.\n\nThis witch is extremely powerful, but word has it that she sometimes becomes obsessed with the art of creating certain patterns, so that her means end up becoming her goals.")
        if r_ma[r_hyouji_cha_ma][condition] == 2:
            $ r_text = _("{size=60}Beatrice{/size}\n\nThe Endless Witch who has lived for a thousand years.\nShe holds the fatherly magical power to give endless evolution to the sea.\n\nHowever, that magical power is meaningless.\nNo matter how many times you multiply something in the sea of zero, it is nothing more than zero.\n\nHowever, when she benefited from a miracle where 1 was born in that sea, her world became endless.\n\nWhen she was joined with the Witch of Origins through Mariage Sorcière, their magical compendium gained an endless span, as well as endless power.")
    
    elif r_hyouji_cha_ma == ma4_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of Miracles who lived for a thousand years.\nTo defeat Beatrice in her game, she threw in the piece called ANGE.\n\nThe Voyager witches who cross the sea of kakera are beings far superior to the witches who cannot leave their own territories.\n\nInside this territory, they may be on an even footing, but her magical power fundamentally far surpasses that of Beatrice.\n\nWhat does she who continually voyages to escape boredom seek on her journey......?")
    
    elif r_hyouji_cha_ma == ma4_enj:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}ANGE{/size}\n\nThe Endless Witch, who will life for one thousand years in the future.\nOr perhaps she is a witch hunter, who will fell all witches.\n\nWithout understanding witches, they cannot be felled.\nEven after understanding witches, they cannot be felled.\n\nShe understands, and denies witches.\nOnly the power of that contradiction can give her a sword with which to fell witches.")
    
    elif r_hyouji_cha_ma == ma4_gap:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Gaap{/size}\n\nOne of the 72 Great Demons.  Also Beatrice's friend.\nIn response to a magician's demands, she gives the power of instant movement.\n\nShe always uses this wonderful power for pranks.\n\nHiding keys and bags during busy mornings is her specialty.\n\nHowever, this power becomes a final weapon which can easily strike the finishing blow in closed room mysteries.\nHer queen bee-like attack would probably pierce all famous detectives, making them surrender.")
    
    elif r_hyouji_cha_ma == ma4_goa:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}All of the Goats{/size}\n\nThey are low-level furniture that serve Beatrice.\n\nThere are many of them, but they are silent, with no personality.  They obey their Master's orders faithfully.\n\nTheir sensitivity is closer to an animal's than a human's, and they sometimes misunderstand their orders surprisingly foolishly.\nBy nature, they have a huge build like a minotaur, and incredible superhuman strength.\n\nThey are low-level as furniture, but can be very convenient since an inexhaustible supply of them can be summoned.")
    
    elif r_hyouji_cha_ma == ma4_kin:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Goldsmith{/size}\n\nKinzo's name as a sorcerer is Goldsmith.\nHis skill as a summoner is legendary for the current era.\nHis summoning ability surpasses even Beatrice's.\n\nHowever, he is very mismatched, and while he does excel in some areas, he is fatally lacking as a sorcerer in others.\n\nHe can't even use enough magic to reheat black tea, but it is possible for him to summon demons that can use enough magic to boil the sea.\n\nThe source of his magic is found in arithmetic miracles, and his magical compendium is unique.\nLater on, Beatrice also took notice of this and rearranged her own magical compendium.")
    
    elif r_hyouji_cha_ma == ma4_lam:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Lambdadelta{/size}\n\nThe Witch of Certainty who has lived for a thousand years.\nShe likens Beatrice's game to a bird cage enclosing Bernkastel.\nHer goal is an eternal tie.\n\nShe is fundamentally Beatrice's ally, but she will support Battler if it looks like he is about to retire.\nOn the other hand, if Beatrice starts to get cornered, she will support Beatrice.\n\nCompared to the endless, which just repeats idly, certainty has a much greater power of will...")
    
    elif r_hyouji_cha_ma == ma4_mar:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Maria{/size}\n\nA little magician who inherited the black blood from Kinzo.\n\nShe has a natural talent Kinzo didn't have, and even though she's very young, she reaches the level of magician.\nNonetheless, her powers are still very weak, and she is just an apprentice.\n\nHowever, her enchanting ability to give magical power to tools is a natural gift, and the magical items she makes are a match even for the master class.")
        if r_ma[r_hyouji_cha_ma][condition] == 2:
            $ r_text = _("{size=60}MARIA{/size}\n\nThe Witch of Origins, who will live for one thousand years in the future.\nShe holds the motherly magical power to give birth to 1 from the sea of zero.\n\nAt a glance, this magical power is frail.\nBut no matter how many times you multiply 0, it doesn't become anything but 0.\nBut the 1 that she gives birth to could eventually surpass the heavens.\n\nShe is loyally protected by Beatrice, who understands her true worth.\nShe is in an alliance with Beatrice.")
    
    elif r_hyouji_cha_ma == ma4_rg1:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Lucifer the Eldest Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nLucifer is the oldest of the sisters and therefore their leader.\n\nBecause of this, she claims to be the strongest of the sisters, but she's secretly aware that she's actually the least talented.\n\nHowever, she has always acted arrogantly in an attempt to hide this fact from the others.\nHer great fear is that her sisters would sneer at her if they ever found out.")
    
    elif r_hyouji_cha_ma == ma4_rg2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Leviathan the Second Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nLeviathan often speaks to Lucifer on behalf of the youngest sisters.\n\nAt her best, she has a brutal, deeply envious nature and is adept at spotting people's weaknesses.\n\nHowever, she is usually nothing more than a selfish crybaby.\n\nFor some reason, she's not a very quick thinker, and she often comes in last among the sisters, ends up with the short end of the stick, and cries.")
    
    elif r_hyouji_cha_ma == ma4_rg3:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Satan the Third Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nSatan takes on the role of the constantly angry class president among the sisters.\n\nShe is known for giving out rapid-fire scoldings, which makes the other sisters scared of her.\nBecause of this, no one is willing to talk back to her, which means she is surprisingly lonely.\n\nShe'll sometimes intentionally try to do things that should anger the other sisters, but they never scold her back, which leaves her even more lonely.")
    
    elif r_hyouji_cha_ma == ma4_rg4:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Belphegor the Fourth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nBelphegor is well trusted and known for being a reticent, serious, and responsible piece of furniture.\n\nHowever, this is all because of demonic desire to turn her masters into useless, lazy pigs.\nIn this sense, she might be the most demon-like of all the sisters.\n\nShe is serious to a fault, and not at all comfortable with being the one treated kindly instead of the other way around.")
    
    elif r_hyouji_cha_ma == ma4_rg5:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Mammon the Fifth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nMammon is quick to grab whatever she wants, without any concern for her sisters.\n\nHer motto is \"monopolize through greed.\"  Therefore, she is usually the main cause of any arguments between the sisters.\n\nHowever, among the sisters, she is the most honest about her own feelings, and the one most likely to try and please the opposite sex.\n\nShe is greedy, but a hard worker, and will stop at nothing to capture her target's affections for all eternity.")
    
    elif r_hyouji_cha_ma == ma4_rg6:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Beelzebub the Sixth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nBeelzebub is the gourmet of the sisters and is known for being a big and picky eater.\n\nHer personality is similar to Mammon's and the two sisters often fight over the same thing.\n\nShe's always talking about food, which makes her a calming influence among the sisters.\n\nHowever, she also has that disturbing desire to kidnap pretty boys and store them in the food cellar...")
    
    elif r_hyouji_cha_ma == ma4_rg7:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Asmodeus the Seventh Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nAs the youngest of the sisters, Asmodeus is always doted upon.\nThis might be why she alone is kept out of way whenever an even slightly lewd topic comes up.\n\nShe's always looking for a boyfriend in the hopes that her sisters will finally accpet her as an adult.\n\nHowever, she keeps aiming too high and whiles away each day dreaming of the prince who will never come.")
    
    elif r_hyouji_cha_ma == ma4_ron:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Ronove{/size}\n\nOne of the Great Demons of the 72 pillars.  Works for a Master in exchange for various forms of compensation.\nHe currently has a contract with Beatrice as her butler (head furniture).\n\nHe has become proficient at housekeeping after serving in many households, so his ability as a butler is very high.\n\nIn the high society of witches, employing him has become a kind of status.\nFurthermore, the cookies he bakes are superb, and witches will often form a line demanding them.\n\nHe should hold a tremendous magical power, but since he is always serving his master, his battle abilities are unknown.")
    
    elif r_hyouji_cha_ma == ma4_s00:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Chiester 00 (Double oh){/size}\n\nA weapon of the Sister's Calvary, which serves Pendragon.\n\n00 has the position as their calm and composed leader.\nHowever, while that is the position demanded of her, she actually has a weaker composition.\n\n00 excels in reconnaissance and as an advanced guard, possessing extreme supremacy in encounters.\n\nHowever, her excess fighting power is criticized as being inhuman, and it is not rare for her to be lynched and abused when she surrenders on the battlefield.\n\nHer one eye silently tells of that.")
    
    elif r_hyouji_cha_ma == ma4_s41:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Chiester 410 (Yonichimaru){/size}\n\nA weapon in contract with Beatrice.\n\n410 is a kid whose personality tends to cause her to speak arrogantly.\n\nShe has a hobby of laughing at people who are serious or not relaxed, which is why she likes 45 and Lucifer.\n\nShe speaks roughly, but she loves company and easily succumbs to loneliness.\nShe gets depressed if she isn't always being looked after by someone.\n\n410 has excellent capabilities in firing control, and exhibits matchless battle power even at close quarters fighting.")
    
    elif r_hyouji_cha_ma == ma4_s45:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Chiester 45 (Yonjuugo){/size}\n\nA weapon in contract with Beatrice.\n\n45 has a very methodical and timid personality, and her persecution complex is somehwat strong.\nThis makes her compensate well for the weakness of 410's rough personality when they work as a pair.\n\nSince she cannot stand silence, she sometimes becomes emotionally insecure if she isn't always being ordered by someone.\n\n45 has excellent capabilities in searching for the enemy and deciding orders.  The sisters' battle power is multiplied by her support.")
    
    elif r_hyouji_cha_ma == ma4_s55:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Chiester 556 (Go-go-roku){/size}\n\nA quiet girl who is a-lways teased by everybody.\nBut that is because she is loved by everyone.\n\nThe trumpet is her specialty.\nEveryone skips to her lively tone.")
        if r_ma[r_hyouji_cha_ma][condition] == 2:
            $ r_text = _("{size=60}Chiester 556 (Go-go-roku){/size}\n\nA weapon of the Sister's Calvary, which serves Pendragon.\n\n556 was a quiet and teased character, but she was loved by everyone.\nHowever, her luck was always bad, and she met a tragic end in battle with the black witch.\n\nShe was the latest style of weapon, and unique in the Sisters' Cavalry, which had a strong tint as an honor guard.\n\n556 was in charge of squad fire support.  She shot not to kill, but to protect her allies.")
    
    elif r_hyouji_cha_ma == ma4_sak:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Sakutarou{/size}\n\nThe beloved furniture of the witch of Mariage Sorcière, Lady MARIA.\n\nHis existence is Lady MARIA's white heart itself.\nYou could even say that he is another Lady MARIA and he is an irreplaceable existence to her.\n\nHe holds a decoration as a diplomat, and all witches, weapons and furniture in the alliance, as well as demons and divine spirits who are in a contract with the alliance, are not permitted to take aim at him.")
        if r_ma[r_hyouji_cha_ma][condition] == 2:
            $ r_text = _("{size=60}Sakutarou{/size}\n\nLady MARIA's white heart, which was torn apart.\n\nHis broken vessel can only be regenerated by the Meister who created him, ROSA.\n\nHowever, ROSA disposed of the vessel's fragments, and even lost the pattern paper.\nOn top of that, because his existence was denied by the Meister herself, his resurrection is impossible.\n\nThe Meister died in the year 1986, and his resurrection disappeared for all time.\n\nHis resurrection is even impossible for the Endless Witch, Beatrice......")
    
    elif r_hyouji_cha_ma == ma4_wal:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            $ r_text = _("{size=60}Virgilia{/size}\n\nAs a now-retired Endless Witch, she was Beatrice's teacher.\nShe used the Endless Magic properly, and devoted her life to the smiles and happiness of many people.\n\nShe taught Beatrice the Endless Magic, and retired, believing that Beatrice would also devote herself to the people.\n\nAt the same time that she was Beatrice's teacher, she also served as the magician of Beatrice's home.\nBecause of that, Virgilia had come in contact with her with the position of a servant.\nIt is said that this became her downfall, and invited Beatrice's arrogance and recklessness.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_hyouji_cha_ep4_3_text:
    
    if r_hyouji_cha_enj == enj_ama:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Amakusa Juuza{/size}\n\nA former guard of Eva's.\nHis guiding principle is of undertaking dangerous jobs for little money and performing with extreme skill.\n\nAt one point, he did work as a guard for Ange, but after repeatedly breaking Eva's strict order not to talk to her, he became disliked in the end and was fired.\n\nAnge isn't as dissatisfied as she might seem at having him as a person to talk to.\n\nThis man, who has traveled between the Japan Self-Defense Force, the Foreign Legion, and non-government military companies, has skill in counter-sniping and VIP escorting.")
    
    elif r_hyouji_cha_enj == enj_ber:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Bernkastel{/size}\n\nThe Witch of Miracles who lived for a thousand years.\nTo defeat Beatrice in her game, she threw in the piece called ANGE.\n\nThe Voyager witches who cross the sea of kakera are beings far superior to the witches who cannot leave their own territories.\n\nInside this territory, they may be on an even footing, but her magical power fundamentally far surpasses that of Beatrice.\n\nWhat does she who continually voyages to escape boredom seek on her journey......?")
    
    elif r_hyouji_cha_enj == enj_enj:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Ange{/size}\n\nEven after throwing herself off the top of a skyscraper, she miraculously survived unharmed.\nAfter that mysterious experience, she threw away everything, and went on a journey by herself to learn her past.\n\nCan she, who is positioned in the future 12 years after, break through Beatrice's magic...?")
    
    elif r_hyouji_cha_enj == enj_eva:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Ushiromiya Eva{/size}\n\nAfter being repeatedly hospitalized from psychogenic stress, she is already dead in the world of 1998 due to acute heart failure.\n\nShe lived her later years isolated with no one to understand her, and is the only survivor from Rokkenjima.  The media gave her the name \"Queen of Suspicion.\"\n\nShe continued to make reckless expansions of management like Kinzo had done in the past, creating many enemies.\n\nIn her later years, as though she enjoyed it, she no longer continued for economic reasons, but did it simply to harass.\n\nAnd that was all for the sake of Ange who would eventually succeed her.")
    
    elif r_hyouji_cha_enj == enj_kas:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Sumadera Kasumi{/size}\n\nDaughter of the declining noble family Sumadera.  Ushiromiya Kyrie's younger sister.\n\nShe hates her sister Kyrie so much that she loathes everything about her, so she also strongly hates Ange.\n\nShe is the opposite of the freewheeling person Kyrie once was and holds appearance in high regard, possessing a strong ambition for philanthropy.\nHowever, that is nothing more than a sign that her complex towards her sister causes her to crave the limelight.\n\nThere are several opposing factions in the Sumadera family, and they are constantly engaged in a secret feud over who will control the vast wealth Ange holds.")
    
    elif r_hyouji_cha_enj == enj_kwa:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Captain Kawabata{/size}\n\nAn old man who used to be a captain of a high-speed boat that went to Rokkenjima and back.\n\nIt is at least certain that of those who currently survive, he is the one who knows the most about Rokkenjima.\n\nThe media hoped that he might have known the details of the situation inside the Ushiromiya family from various discussions with servants going to and from the island.\n\nHowever, because he didn't say anything, they eventually began to forget this old man...")
    
    elif r_hyouji_cha_enj == enj_mar:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}MARIA{/size}\n\nThe Witch of Origins, who will live for one thousand years in the future.\nShe holds the motherly magical power to give birth to 1 from the sea of zero.\n\nAt a glance, this magical power is frail.\nBut no matter how many times you multiply 0, it doesn't become anything but 0.\nBut the 1 that she gives birth to could eventually surpass the heavens.\n\nShe is loyally protected by Beatrice, who understands her true worth.\nShe is in an alliance with Beatrice.")
    
    elif r_hyouji_cha_enj == enj_mas:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Nanjo Masayuki{/size}\n\nNanjo's son.  Inherited the Nanjo Clinic.\nUnlike Nanjo, he gives a slightly sobered, indifferent impression.\n\nAfter the rampage surrounding Rokkenjima, he grew to completely despise the press, and never again did he attempt to speak of what had happened at the time.\n\nIn the past, he had a daughter afflicted with an incurable disease, but unfortunately, she wasn't able to live out her natural lifespan.")
    
    elif r_hyouji_cha_enj == enj_oko:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Okonogi Tetsurou{/size}\n\nLeader of the Ushiromiya Group.\nAfter Eva's death and until Ange succeeds the group, he and his ministers are the ones managing it.\n\nHowever, since Ange has no desire to do so, the group is on the brink of internal discord, putting him in a difficult position as well.\n\nHe was previously the president of a foodstuff distribution company, and had an intimate relationship with Hideyoshi's company.\n\nBecause of that long-lasting association, Eva particularly trusted him, and he was appointed to a significant post in the group.")
    
    elif r_hyouji_cha_enj == enj_pro:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Professor Ootsuki{/size}\n\nA professor at a certain college, well-known as an authority on the study of western folklore.\n\nHe is also famous for his hobby of researching the Rokkenjima Witch Legend, as one of the Witch Hunters.\n\nThe Witch Hunt is primarily focused on the straining of occult superstitions to explain the truth of the Rokkenjima crime rather than doing so scientifically, and its dilettantes and enthusiasts of the mystical primarily view it as a mental game.")
    
    elif r_hyouji_cha_enj == enj_sab:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Kumasawa Sabakichi{/size}\n\nKumasawa's son.  Working at the Niijima Fishing Harbor.\nHe must have gotten his carefree, big-hearted personality from Kumasawa.\n\nMany of Kumasawa's sons were fisherman often separated from land.\nBecause he was involved with the fishing harbor, it was possible to encounter him by coincidence.\n\nIt was expected that he might have heard that talker Kumasawa let something important slip, but...")
    
    elif r_hyouji_cha_enj == enj_sak:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}Sakutarou{/size}\n\nMaria onee-chan's precious friend.\nVery simple, warm and kind.\n\nTends to say \"Uryu.\"\n\nDidn't Maria onee-chan also have a habit of saying this, long ago?")
    
    elif r_hyouji_cha_enj == enj_rg1:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Lucifer the Eldest Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nLucifer is the oldest of the sisters and therefore their leader.\n\nBecause of this, she claims to be the strongest of the sisters, but she's secretly aware that she's actually the least talented.\n\nHowever, she has always acted arrogantly in an attempt to hide this fact from the others.\nHer great fear is that her sisters would sneer at her if they ever found out.")
    
    elif r_hyouji_cha_enj == enj_rg2:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Leviathan the Second Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nLeviathan often speaks to Lucifer on behalf of the youngest sisters.\n\nAt her best, she has a brutal, deeply envious nature and is adept at spotting people's weaknesses.\n\nHowever, she is usually nothing more than a selfish crybaby.\n\nFor some reason, she's not a very quick thinker, and she often comes in last among the sisters, ends up with the short end of the stick, and cries.")
    
    elif r_hyouji_cha_enj == enj_rg3:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Satan the Third Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nSatan takes on the role of the constantly angry class president among the sisters.\n\nShe is known for giving out rapid-fire scoldings, which makes the other sisters scared of her.\nBecause of this, no one is willing to talk back to her, which means she is surprisingly lonely.\n\nShe'll sometimes intentionally try to do things that should anger the other sisters, but they never scold her back, which leaves her even more lonely.")
    
    elif r_hyouji_cha_enj == enj_rg4:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Belphegor the Fourth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nBelphegor is well trusted and known for being a reticent, serious, and responsible piece of furniture.\n\nHowever, this is all because of demonic desire to turn her masters into useless, lazy pigs.\nIn this sense, she might be the most demon-like of all the sisters.\n\nShe is serious to a fault, and not at all comfortable with being the one treated kindly instead of the other way around.")
    
    elif r_hyouji_cha_enj == enj_rg5:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Mammon the Fifth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nMammon is the first furniture to become Ange's friend.\n\nShe stayed by Ange's side throughout her training period, greedily encouraging her master to become a full, true witch.\n\nA very special person, even among the seven sisters.")
    
    elif r_hyouji_cha_enj == enj_rg6:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Beelzebub the Sixth Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nBeelzebub is the gourmet of the sisters and is known for being a big and picky eater.\n\nHer personality is similar to Mammon's and the two sisters often fight over the same thing.\n\nShe's always talking about food, which makes her a calming influence among the sisters.\n\nHowever, she also has that disturbing desire to kidnap pretty boys and store them in the food cellar...")
    
    elif r_hyouji_cha_enj == enj_rg7:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            $ r_text = _("{size=60}The Seven Sisters of Purgatory\n  Asmodeus the Seventh Daughter{/size}\n\nAdvanced-level furniture created by Beatrice.\n\nAs the youngest of the sisters, Asmodeus is always doted upon.\nThis might be why she alone is kept out of way whenever an even slightly lewd topic comes up.\n\nShe's always looking for a boyfriend in the hopes that her sisters will finally accpet her as an adult.\n\nHowever, she keeps aiming too high and whiles away each day dreaming of the prince who will never come.")
    
    side "c r":
        area (190, 180, 995, 740)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_text style style.chr_text
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 740 xpos (1200.0/1920.0) ypos (180.0/1080.0)
        
screen r_cha_hyouji_ep1():
    
    if r[r_hyouji_cha][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/kin.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/kin_m.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/kin_d.png" at chars_tati
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/kla.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/kla_d.png" at chars_tati
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/nat.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/nat_d.png" at chars_tati
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/jes.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/jes_d.png" at chars_tati
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/eva.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/eva_d.png" at chars_tati
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/hid.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/hid_d.png" at chars_tati
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/geo.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/geo_d.png" at chars_tati
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/rud.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/rud_d.png" at chars_tati
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/kir.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/kir_d.png" at chars_tati
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/but.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/but_d.png" at chars_tati
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/gen.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/gen_d.png" at chars_tati
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ros.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ros_d.png" at chars_tati
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/mar.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/mar_d.png" at chars_tati
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/nan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/nan_d.png" at chars_tati
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/sha.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/sha_d.png" at chars_tati
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/kan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/kan_d.png" at chars_tati
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/goh.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/goh_d.png" at chars_tati
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/kum.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/kum_d.png" at chars_tati
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/bea.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/bea_d.png" at chars_tati
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ber.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ber_d.png" at chars_tati
    
screen r_cha_hyouji_ep1_2():
    
    if r_ma[r_hyouji_cha_ma][condition] == 0:
        add Null() at chars_tati
    
    elif r_hyouji_cha_ma == ma_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/bea.png" at chars_tati
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            add "r_click/chars/cha_tati/bea_d.png" at chars_tati
    elif r_hyouji_cha_ma == ma_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ber.png" at chars_tati
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            add "r_click/chars/cha_tati/ber_d.png" at chars_tati
    
screen r_cha_hyouji_ep2():
    
    if r[r_hyouji_cha][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/kin.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/kin_d.png" at chars_tati
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/kla.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/kla_d.png" at chars_tati
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/nat.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/nat_d.png" at chars_tati
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/jes.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/jes_d.png" at chars_tati
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/eva.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/eva_d.png" at chars_tati
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/hid.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/hid_d.png" at chars_tati
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep2/geo2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep2/geo.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/geo_d.png" at chars_tati
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/rud.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/rud_d.png" at chars_tati
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/kir.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/kir_d.png" at chars_tati
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/but.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/but_d.png" at chars_tati
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/gen.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/gen_d.png" at chars_tati
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/ros.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/ros_d.png" at chars_tati
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/mar.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/mar_d.png" at chars_tati
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/nan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/nan_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep2/nan_d2.png" at chars_tati
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep2/sha2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep2/sha.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/sha_d.png" at chars_tati
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep2/kan2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep2/kan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/kan_m.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep2/kan_d.png" at chars_tati
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/goh.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/goh_d.png" at chars_tati
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/kum.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/kum_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep2/kum_d2.png" at chars_tati
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/bea.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/bea2.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep2/bea_d.png" at chars_tati
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/ber.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep2/ber_d.png" at chars_tati
    elif r_hyouji_cha == r_lam:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep2/lam.png" at chars_tati
    
    ### EP2 META ###
screen r_cha_hyouji_ep2_2():
    
    if r_ma[r_hyouji_cha_ma][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha_ma == ma_kin:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/kin.png" at chars_tati
    elif r_hyouji_cha_ma == ma_but:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/but.png" at chars_tati
    elif r_hyouji_cha_ma == ma_gen:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/gen.png" at chars_tati
    elif r_hyouji_cha_ma == ma_mar:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/mar.png" at chars_tati
    elif r_hyouji_cha_ma == ma_sha:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/sha.png" at chars_tati
    elif r_hyouji_cha_ma == ma_kan:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/kan.png" at chars_tati
    elif r_hyouji_cha_ma == ma_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/bea.png" at chars_tati
    elif r_hyouji_cha_ma == ma_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/ber.png" at chars_tati
    elif r_hyouji_cha_ma == ma_lam:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/lam.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg1:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg1.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg2.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg3:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg3.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg4:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg4.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg5:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg5.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg6:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg6.png" at chars_tati
    elif r_hyouji_cha_ma == ma_rg7:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep2_2/rg7.png" at chars_tati
    
screen r_cha_hyouji_ep3():
    
    if r[r_hyouji_cha][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/kin.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/kin_d.png" at chars_tati
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/kla.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/kla_d.png" at chars_tati
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/nat.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/nat_d.png" at chars_tati
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/jes.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/jes_d.png" at chars_tati
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/eva.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/eva_d.png" at chars_tati
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/hid.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/hid_d.png" at chars_tati
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep3/geo2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep3/geo.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/geo_d.png" at chars_tati
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/rud.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/rud_d.png" at chars_tati
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/kir.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/kir_d.png" at chars_tati
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/but.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/but_d.png" at chars_tati
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/gen.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/gen_d.png" at chars_tati
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/ros.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/ros_d.png" at chars_tati
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/mar.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/mar_d.png" at chars_tati
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/nan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/nan_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep3/nan_d2.png" at chars_tati
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep3/sha2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep3/sha.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/sha_d.png" at chars_tati
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep3/kan2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep3/kan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/kan_d.png" at chars_tati
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/goh.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/goh_d.png" at chars_tati
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/kum.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/kum_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep3/kum_d2.png" at chars_tati
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/bea.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/bea_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep3/bea_d.png" at chars_tati
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/ber.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep3/ber_d.png" at chars_tati
    elif r_hyouji_cha == r_lam:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/lam.png" at chars_tati
    elif r_hyouji_cha == r_enj:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep3/enj.png" at chars_tati
    
    ### ep3 META ###
screen r_cha_hyouji_ep3_2():
    if r_ma[r_hyouji_cha_ma][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha_ma == ma3_bea:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/bea.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/ber.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_lam:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/lam.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_goa:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/goa.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_wal:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/wal.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_ron:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/ron.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_ev2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            if r_ma[r_hyouji_cha_ma][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep3_2/ev2_2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep3_2/ev2.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_enj:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/enj.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_s41:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/s41.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_s45:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/s45.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg1:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg1.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg2.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg3:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg3.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg4:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg4.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg5:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg5.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg6:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg6.png" at chars_tati
    elif r_hyouji_cha_ma == ma3_rg7:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep3_2/rg7.png" at chars_tati
    
    
    
    
screen r_cha_hyouji_ep4():
    
    if r[r_hyouji_cha][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha == r_kin:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/kin.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/kin_d.png" at chars_tati
    elif r_hyouji_cha == r_kla:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/kla.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/kla_d.png" at chars_tati
    elif r_hyouji_cha == r_nat:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/nat.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/nat_d.png" at chars_tati
    elif r_hyouji_cha == r_jes:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/jes.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/jes_d.png" at chars_tati
    elif r_hyouji_cha == r_eva:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/eva.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/eva_d.png" at chars_tati
    elif r_hyouji_cha == r_hid:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/hid.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/hid_d.png" at chars_tati
    elif r_hyouji_cha == r_geo:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep4/geo2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep4/geo.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/geo_d.png" at chars_tati
    elif r_hyouji_cha == r_rud:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/rud.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/rud_d.png" at chars_tati
    elif r_hyouji_cha == r_kir:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/kir.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/kir_d.png" at chars_tati
    elif r_hyouji_cha == r_but:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/but.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/but_d.png" at chars_tati
    elif r_hyouji_cha == r_gen:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/gen.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/gen_d.png" at chars_tati
    elif r_hyouji_cha == r_ros:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/ros.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/ros_d.png" at chars_tati
    elif r_hyouji_cha == r_mar:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/mar.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/mar_d.png" at chars_tati
    elif r_hyouji_cha == r_nan:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/nan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/nan_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep4/nan_d2.png" at chars_tati
    elif r_hyouji_cha == r_sha:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep4/sha2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep4/sha.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/sha_d.png" at chars_tati
    elif r_hyouji_cha == r_kan:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep4/kan2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep4/kan.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/kan_d.png" at chars_tati
    elif r_hyouji_cha == r_goh:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/goh.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/goh_d.png" at chars_tati
    elif r_hyouji_cha == r_kum:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/kum.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/kum_d.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 3:
            add "r_click/chars/cha_tati/ep4/kum_d2.png" at chars_tati
    elif r_hyouji_cha == r_bea:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/bea.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/bea_d.png" at chars_tati
    elif r_hyouji_cha == r_ber:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/ber.png" at chars_tati
        elif r[r_hyouji_cha][condition] == 2:
            add "r_click/chars/cha_tati/ep4/ber_d.png" at chars_tati
    elif r_hyouji_cha == r_lam:
        if r[r_hyouji_cha][condition] == 1:
            add "r_click/chars/cha_tati/ep4/lam.png" at chars_tati
    elif r_hyouji_cha == r_enj:
        if r[r_hyouji_cha][condition] == 1:
            if r[r_hyouji_cha][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep4/enj_2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep4/enj.png" at chars_tati
    
    
    ### ep4 META ###
screen r_cha_hyouji_ep4_2():
    
    if r_ma[r_hyouji_cha_ma][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha_ma == ma4_lam:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/lam.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_ber:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/ber.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_bea:
        if r_ma[r_hyouji_cha_ma][condition] >= 1:
            add "r_click/chars/cha_tati/ep4_2/bea.png" at chars_tati                                ## psp version doesn't reload tati
#        elif r_ma[r_hyouji_cha_ma][condition] == 2:
#            add "r_click/chars/cha_tati/ep4_2/bea.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_mar:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/mar.png" at chars_tati
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            add "r_click/chars/cha_tati/ep4_2/mar_2.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_enj:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/enj.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_kin:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/kin.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_sak:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/sak.png" at chars_tati
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            add "r_click/chars/cha_tati/ep4_2/sak_d.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_wal:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/wal.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_ron:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/ron.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_gap:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/gap.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_s00:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/s00.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_s41:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/s41.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_s45:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/s45.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_s55:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/s55.png" at chars_tati
        elif r_ma[r_hyouji_cha_ma][condition] == 2:
            add "r_click/chars/cha_tati/ep4_2/s55_d.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg1:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg1.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg2:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg2.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg3:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg3.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg4:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg4.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg5:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg5.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg6:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg6.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_rg7:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/rg7.png" at chars_tati
    elif r_hyouji_cha_ma == ma4_goa:
        if r_ma[r_hyouji_cha_ma][condition] == 1:
            add "r_click/chars/cha_tati/ep4_2/goa.png" at chars_tati
    
    

screen r_cha_hyouji_ep4_3():
    
    if r_enj_ma[r_hyouji_cha_enj][condition] == 0:
        add Null() at chars_tati
    
    if r_hyouji_cha_enj == enj_eva:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/eva.png" at chars_tati
    elif r_hyouji_cha_enj == enj_oko:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/oko.png" at chars_tati
    elif r_hyouji_cha_enj == enj_kas:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/kas.png" at chars_tati
    elif r_hyouji_cha_enj == enj_enj:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            if r_enj_ma[r_hyouji_cha_enj][r_ishou] == 2:
                add "r_click/chars/cha_tati/ep4_3/enj_2.png" at chars_tati
            else:
                add "r_click/chars/cha_tati/ep4_3/enj.png" at chars_tati
    elif r_hyouji_cha_enj == enj_ama:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/ama.png" at chars_tati
    elif r_hyouji_cha_enj == enj_sak:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/sak.png" at chars_tati
    elif r_hyouji_cha_enj == enj_mar:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/mar.png" at chars_tati
        elif r_enj_ma[r_hyouji_cha_enj][condition] == 2:
            add "r_click/chars/cha_tati/ep4_3/mar_2.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg1:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg1.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg2:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg2.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg3:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg3.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg4:
        if r_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg4.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg5:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg5.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg6:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg6.png" at chars_tati
    elif r_hyouji_cha_enj == enj_rg7:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/rg7.png" at chars_tati
    elif r_hyouji_cha_enj == enj_pro:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/pro.png" at chars_tati
    elif r_hyouji_cha_enj == enj_mas:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/mas.png" at chars_tati
    elif r_hyouji_cha_enj == enj_sab:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/sab.png" at chars_tati
    elif r_hyouji_cha_enj == enj_kwa:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/kwa.png" at chars_tati
    elif r_hyouji_cha_enj == enj_ber:
        if r_enj_ma[r_hyouji_cha_enj][condition] == 1:
            add "r_click/chars/cha_tati/ep4_3/ber.png" at chars_tati
    


screen tips_text_ep1():
    if r_hyouji_tips == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_tips == 1:
        $ r_tips_text = _("Behold the sweetfish river running through my beloved hometown.\nYou who seek the Golden Land, follow its path downstream in search of the key.\n\nAs you travel down it, you will see a village.\nIn that village, look for the shore the two will tell you of.\nThere sleeps the key to the Golden Land.\n\nThe one who obtains the key must then travel to the Golden Land in accordance with these rules.\n\nOn the first twilight, offer the six chosen by the key as sacrifices.\nOn the second twilight, those who remain shall tear apart the two who are close.\nOn the third twilight, those who remain shall praise my noble name.\nOn the fourth twilight, gouge the head and kill.\nOn the fifth twilight, gouge the chest and kill.\nOn the sixth twilight, gouge the stomach and kill.\nOn the seventh twilight, gouge the knee and kill.\nOn the eighth twilight, gouge the leg and kill.\nOn the ninth twilight, the witch shall revive, and none shall be left alive.\nOn the tenth twilight, the journey shall end, and you shall reach the capital where the gold dwells.\n\nThe witch shall praise the wise and bestow four treasures.\n\nOne shall be all the gold from the Golden Land.\nOne shall be the resurrection of all the dead souls.\nOne shall be the resurrection of the love that was lost.\nOne shall be to put the witch to sleep for all time.\n\nSleep peacefully, my most beloved witch, Beatrice.")
    elif r_hyouji_tips == 2:
        $ r_tips_text = _("Welcome to Rokkenjima, members of the Ushiromiya family.\nI am Beatrice, the alchemist, for this family employed by Kinzo-sama, himself.\nI have served him for many years in accordance with our cantract, but on this day, Kinzo-sama has announced the final suspension of that contract.\nTherefore, I ask that you acknowledge my resignation from the position of famiy alchemist from this day forth.\n\nAnd now, there is one part of the contract that must be explained to all present.\nI, Beatrice, lent Kinzo-sama a vast quantity of gold under certain terms.  One of these terms specifies that all the gold is to be returned to me upon the termination of the contract.\nFurthermore, I am to receive everything of the Ushiromiya family as interest.\n\nAfter hearing this, you may feel as though Knizo-sama has been savagely ruthless.\nHowever, Kinzo-sama did append a special clause to the contract so that you would have a chance to preserve your wealth and honor.\nIf and only if that special clause is fulfilled, I will lose my rights to the gold and the interest for all eternity.\n\nSpecial Clause: Beatrice retains the right to collect the gold and accumulated interest upon the termination of the contract.\nHowever, if someone is able to discover the hidden gold of this contract, Beatrice must abandon the rights for all time.\n\nThe collection of the interest will proceed shortly, but if any one of you fulfills the terms of this special clause, I shall return everything, including the portion that has already been collected.\nFurthermore, as the first step in this collection of Kinzo-sama's debt, I have taken possession of the Ushiromiya family \"Head's Ring,\" which signifies the passage of the Ushiromiya family headship from one individual to another.\nI ask that you confirm this for yourselves by examining the imprint on the wax seal.\n\nKinzo-sama has already publicly displayed the location of the hidden gold within the epitaph under my portrait.\nThe rules apply equally to all who can read the epitaph.\nIf you discover the gold, I shall return everything to you.\nTonight, I ask that you enjoy your battle of wits with Kinzo-sama to the fullest.  I sincerely pray that this night will be both intellectual and elegant.\n\n------Beatrice the Golden.")
    elif r_hyouji_tips == 3:
        $ r_tips_text = _("Praise my name.")
    elif r_hyouji_tips == 4:
        $ r_tips_text = _("Are you enjoying the riddle of Kinzo-sama's epitaph?\nAs you are all probably aware, you have very little time remaining.\nPlease abandon any naive hopes of escaping after the storm passes.\nThis game can only end with my victory or yours.\nWhen the time runs out, I will win by default.  There will be no ties.\nMake sure that you do not misunderstand your current situation.")
    elif r_hyouji_tips == 5:
        $ r_tips_text = _("Ushiromiya Krauss\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Rudolf\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Kyrie\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Rosa\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Shannon\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Gohda\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Eva\n    Died on the second twilight.\n    Pierced through the forehead by the 'Stake of Asmodeus.'\n\nUshiromiya Hideyoshi\n    Died on the second twilight.\n    Pierced through the forehead by the 'Stake of Beelzebub.'\n\nUshiromiya Kinzo\n    Died on the fourth twilight.\n    Forehead gouged by the 'Stake of Mammon.'\n\nServant Kanon\n    Died on the fifth twilight.\n    Chest gouged by the 'Stake of Satan.'\n\nServant Genji\n    Died on the sixth twilight.\n    Stomach gougede by the 'Stake of Lucifer.'\n\nAttending Physician Nanjo\n    Died on the seventh twilight.\n    Knee gouged by the 'Stake of Belphegor.'\n\nServant Kumasawa\n    Died on the eighth twilight.\n    Leg gouged by the 'Stake of Leviathan.'\n\nThe Witch Beatrice\n    Revived at the ninth twilight.\n    Finally opens the door to the Golden Land.\n\nUshiromiya Natsuhi\n    Died on the ninth twilight.\n    her the honor of a duel.\n\nUshiromiya George\n    Missing on the tenth twilight.\n    After he acknowledged the existence of the witch and prostrated himself, the witch invited him to the Golden Land.\n\nUshiromiya Jessica\n    Missing on the tenth twilight.\n    After she acknowledged the existence of the witch and prostrated herself, the witch invited her to the Golden Land.\n\nUshiromiya Maria\n    Missing on the tenth twilight.\n    After she acknowledged the existence of the witch and prostrated herself, the witch invited her to the Golden Land.\n\nUshiromiya Battler\n    Missing on the tenth twilight.\n    Will the witch invite this man, who denied her existence, to the Golden Land?")
    elif r_hyouji_tips == 6:
        $ r_tips_text = _("Winchester M1894 Sawed off\n\nA sawed-off custom version of a riffle manufactured during the golden age of Winchesters.\nThis special model more than makes up for its shorter lethal range by its portability and old-time cool factor.  It can even be fired as quickly as a pistol if one works the lever action skillfully enough.\nFuthermore, any true lover of the old western dramas can't help but be attracted to the one-handed reload made possible by its characteristic lever handle.\n\nTo match with Kinzo's personal preferences, it was made to handle .45 long-colt bullets.\n")
    elif r_hyouji_tips == 7:
        $ r_tips_text = _("The Seven Stakes of Purgatory\n\nStakes containing the seven magics that represent the seven deadly sins.\nIn accordance with thier user's orders, they bury themselves into the desired location of the desired target with perfect accuracy.\nBecause they flit about at ultra-high speeds and change their trajectories at will by bouncing off walls and the like, they have no blind spots, and will hit their targets without fail no matter what form of cover they might be hiding behind.  Furthermore, it is possible to change the force they hit with depending on the part of the body at which they strike.\n\nThey are extremely powerful as weapons, but they cannot target pure people who have not committed one of the seven deadly sins or people who have a strong resistance to magical power.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen tips_text_ep2():
    if r_hyouji_tips == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_tips == 1:
        $ r_tips_text = _("Behold the sweetfish river running through my beloved hometown.\nYou who seek the Golden Land, follow its path downstream in search of the key.\n\nAs you travel down it, you will see a village.\nIn that village, look for the shore the two will tell you of.\nThere sleeps the key to the Golden Land.\n\nThe one who obtains the key must then travel to the Golden Land in accordance with these rules.\n\nOn the first twilight, offer the six chosen by the key as sacrifices.\nOn the second twilight, those who remain shall tear apart the two who are close.\nOn the third twilight, those who remain shall praise my noble name.\nOn the fourth twilight, gouge the head and kill.\nOn the fifth twilight, gouge the chest and kill.\nOn the sixth twilight, gouge the stomach and kill.\nOn the seventh twilight, gouge the knee and kill.\nOn the eighth twilight, gouge the leg and kill.\nOn the ninth twilight, the witch shall revive, and none shall be left alive.\nOn the tenth twilight, the journey shall end, and you shall reach the capital where the gold dwells.\n\nThe witch shall praise the wise and bestow four treasures.\n\nOne shall be all the gold from the Golden Land.\nOne shall be the resurrection of all the dead souls.\nOne shall be the resurrection of the love that was lost.\nOne shall be to put the witch to sleep for all time.\n\nSleep peacefully, my most beloved witch, Beatrice.")
    elif r_hyouji_tips == 2:
        $ r_tips_text = _("Welcome to Rokkenjima, members of the Ushiromiya family.\nI am Beatrice, the alchemist, for this family employed by Kinzo-sama, himself.\nI have served him for many years in accordance with our cantract, but on this day, Kinzo-sama has announced the final suspension of that contract.\nTherefore, I ask that you acknowledge my resignation from the position of famiy alchemist from this day forth.\n\nAnd now, there is one part of the contract that must be explained to all present.\nI, Beatrice, lent Kinzo-sama a vast quantity of gold under certain terms.  One of these terms specifies that all the gold is to be returned to me upon the termination of the contract.\nFurthermore, I am to receive everything of the Ushiromiya family as interest.\n\nAfter hearing this, you may feel as though Knizo-sama has been savagely ruthless.\nHowever, Kinzo-sama did append a special clause to the contract so that you would have a chance to preserve your wealth and honor.\nIf and only if that special clause is fulfilled, I will lose my rights to the gold and the interest for all eternity.\n\nSpecial Clause: Beatrice retains the right to collect the gold and accumulated interest upon the termination of the contract.\nHowever, if someone is able to discover the hidden gold of this contract, Beatrice must abandon the rights for all time.\n\nThe collection of the interest will proceed shortly, but if any one of you fulfills the terms of this special clause, I shall return everything, including the portion that has already been collected.\nFurthermore, as the first step in this collection of Kinzo-sama's debt, I have taken possession of the Ushiromiya family \"Head's Ring,\" which signifies the passage of the Ushiromiya family headship from one individual to another.\nI ask that you confirm this for yourselves by examining the imprint on the wax seal.\n\nKinzo-sama has already publicly displayed the location of the hidden gold within the epitaph under my portrait.\nThe rules apply equally to all who can read the epitaph.\nIf you discover the gold, I shall return everything to you.\nTonight, I ask that you enjoy your battle of wits with Kinzo-sama to the fullest.  I sincerely pray that this night will be both intellectual and elegant.\n\n------Beatrice the Golden.")
    elif r_hyouji_tips == 3:
        $ r_tips_text = _("Do you think I'd be that senile, to wait comfortably in this plave for you to barge into here?\nYou're too wild to be suitable for this intellectual night.\nWhat kind of faces did your parents, who raised you to be so stupid, make?  Yeah, I saw them, they had a truly stupid look just like you.\nNow, their bellies are full in the land of sweets!")
    elif r_hyouji_tips == 4:
        $ r_tips_text = _("Everyone of the Ushiromiya family.  I wonder if you have finally reached a climax solving the epitaph's riddle for the gold.\nThe only way you all can stop me is by solving the riddle of the epitaph.\nNo matter which other methods you use, you won't be able to stop the ritual and me.\nTake care that you don't mistake everyone's goal, I'm counting with you.\nEven if you try to search for me, it's useless.  Even if you try to escape from me, it's useless.\nEven if you try to deny me, that's also useless.\n\n------Beatrice the Golden.\n\nP.S.\nI borrowed two corpses for the ritual.\nI'll return them later, so please forgive me.\n...Furthermore, since these keys belong to all of you, I'm returning them.")
    elif r_hyouji_tips == 5:
        $ r_tips_text = _("Are you making progress solving the riddle of the epitaph?\nVery, very soon, you'll run out of time.\n")
    elif r_hyouji_tips == 6:
        $ r_tips_text = _("Ushiromiya Krauss\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Natsuhi\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Eva\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Hideyoshi\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Rudolf\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Kyrie\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Jessica\n    Died on the second twilight.\n    Pierced through the back by the 'Stake of Asmodeus'.\n\nServant Kanon\n    Died on the second twilight.\n    Pierced through the chest by the 'Stake of Satan'.\n\nServant Shannon\n    Died on the fourth twilight.\n    Forehead gouged by the 'Stake of Mammon'.\n\nServant Ghoda\n    Died on the fifth twilight.\n    Chest gouged by the 'Stake of Beelzebub'.\n\nUshiromiya George\n    Died on the sixth twilight.\n    Stomach gouged by the 'Stake of Lucifer'.\n\nAttending Physician Nanjo\n    Died on the seventh twilight.\n    Knee gouged by the 'Stake of Belphegor'.\n\nServant Kumasawa\n    Died on the eighth twilight.\n    Leg gouged by the 'Stake of Leviathan'.\n\nThe Witch Beatrice\n    Revived at the ninth twilight.\n    Finally opens the door to the Golden Land.\n\nUshiromiya Kinzo\n    Missing on the tenth twilight.\n    After he acknowledged the existence of the witch and prostrated himself, the witch invited him to the Golden Land.\n\nUshiromiya Rosa\n    Missing on the tenth twilight.\n    This witch did not invite this woman, who had denied the witch's existence, to the Golden Land.\n\nUshiromiya Maria\n    Missing on the tenth twilight.\n    After she acknowledged the existence of the witch and prostrated herself, the witch invited her to the Golden Land.\n\nServant Genji\n    Missing on the tenth twilight.\n    After he acknowledged the existence of the witch and prostrated himself, the witch invited him to the Golden Land.\n\nUshiromiya Battler Missing on the tenth twilight.\n    Will he acknowledge the existence of the witch and be beckoned to the Golden Land?")
    elif r_hyouji_tips == 7:
        $ r_tips_text = _("Golden Butterfly Brooch\n\nIn order to mediate the relationship between the opposite sex, it brings all fates together favorably and mediates that relationship.\nSince it only brings things together favorably, large differences can be seen in its effects depending on the individual.\n\nHence, if the Witch giving this item does not measure with care whether the target she will give it will be able to use this item effectively or not, it's likely that she will be called a liar.  The initial cost is enormous, and to many human beings, it's no more useful than a mere brooch.\n\nHowever, blind love will easily pay this enormous cost.  The more good will there is from the other partner, the more dramatic the effects will become.\nIronically, the more dramatic the effects are, the original need of such a brooch lessens.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen tips_text_ep3():
    if r_hyouji_tips == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_tips == 1:
        $ r_tips_text = _("Behold the sweetfish river running through my beloved hometown.\nYou who seek the Golden Land, follow its path downstream in search of the key.\n\nAs you travel down it, you will see a village.\nIn that village, look for the shore the two will tell you of.\nThere sleeps the key to the Golden Land.\n\nThe one who obtains the key must then travel to the Golden Land in accordance with these rules.\n\nOn the first twilight, offer the six chosen by the key as sacrifices.\nOn the second twilight, those who remain shall tear apart the two who are close.\nOn the third twilight, those who remain shall praise my noble name.\nOn the fourth twilight, gouge the head and kill.\nOn the fifth twilight, gouge the chest and kill.\nOn the sixth twilight, gouge the stomach and kill.\nOn the seventh twilight, gouge the knee and kill.\nOn the eighth twilight, gouge the leg and kill.\nOn the ninth twilight, the witch shall revive, and none shall be left alive.\nOn the tenth twilight, the journey shall end, and you shall reach the capital where the gold dwells.\n\nThe witch shall praise the wise and bestow four treasures.\n\nOne shall be all the gold from the Golden Land.\nOne shall be the resurrection of all the dead souls.\nOne shall be the resurrection of the love that was lost.\nOne shall be to put the witch to sleep for all time.\n\nSleep peacefully, my most beloved witch, Beatrice.")
    elif r_hyouji_tips == 2:
        $ r_tips_text = _("So that there will be no misunderstandings.\nThe game I seek is for everyone to try and solve the riddle of the epitaph, not for you to try and catch me.\n\nIf you don't solve the riddle of the epitaph, the pitiful sacrifices will further increase in number.  It would be more wise to spend your time solving the epitaph than searching for me.\nIf no one can solve the riddle of the epitaph, no one will survive.\n\nIf a person appears who can miraculously solve the riddle of the epitaph, I will give them all the gold of the Golden Land, the Ushiromiya family inheritance, and all of my power.\nI was the one who succeeded the Ushiromiya family inheritance from Kinzo-sama.  And, I look forward to seeing who will receive the inheritance from me.\n\n――Beatrice The Golden.")     ##------The Golden Witch, Beatrice.")
    elif r_hyouji_tips == 3:
        $ r_tips_text = _("Ushiromiya Kinzo\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Genji\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Shannon\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Kanon\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Gohda\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nServant Kumasawa\n    Died on the first twilight.\n    Chosen by the key of the Golden Land and offered up as sacrifice.\n\nUshiromiya Rosa\n    Died on the second twilight.\n    Offered up as a sacrifice for the new witch. \n\nUshiromiya Maria\n    Died on the second twilight.\n    Offered up as a sacrifice for the new witch.\n\nUshiromiya Rudolf\n    Died on the fourth twilight.\n    Forehead gouged by the 'Stake  of Asmodeus'.\n\nUshiromiya Hideyoshi\n    Died on the fifth twilight.\n    Chest gouged by the 'Stake of Beelzebub'.\n\nUshiromiya Kyrie\n    Died on the sixth twilight.\n    Stomach gouged by the 'Stake of Mammon'.\n\nUshiromiya Krauss\n    Died on the seventh twilight.\n    Stomach gouged by the 'Stake of Lucifer'.\n\nUshiromiya Natsuhi\n    Died on the eighth twilight.\n    Foot gouged by the 'Stake of Satan'.\n\nThe Witch Beatrice\n    Revived at the ninth twilight.\n    This time, she awakened as a true Golden Witch.\n\nUshiromiya George\n    Died at the ninth twilight.\n    The new witch will not let anyone survive.\n\nAttending Physician Nanjo\n    Died on the ninth twilight.\n    The new witch will not let anyone survive.\n\nUshiromiya Battler\n    Died on the ninth twilight.\n    The new witch will not let anyone survive.\n\nUshiromiya Jessica\n    Missing on the tenth twilight.\n    After she acknowledged the existence of the witch and prostrated herself, the witch invited her to the Golden Land.\n\nUshiromiya Eva\n    Solved the riddle of the epitaph.  Returned from Rokkenjima alive.\n    The witch praised her victory, and gave her all of the gold and magic.")
    elif r_hyouji_tips == 4:
        $ r_tips_text = _("Chiester Sisters Imperial Guard Corps\n\nAn Imperial Guard Corps formed by the Dragon King Pendragon in memory of the red dragon and composed only of sisters.\nThey were originally subordinates of the Dragon King, but because of a long relationship with the successive generations of Beatrice's, it was permitted that two Imperial Guard soldiers be lent out.\n\nThe sisters are beings with false life, created by magic.  For that reason, sisters with a great variety of personalities are still being created as their numbers continue to increase.\n\nManifesting into the human world requires a great cost, and even setting aside their tremendous power, summoning them is difficult.\nFor this reason, they are often summoned as guards in special ceremonies.")
    elif r_hyouji_tips == 5:
        $ r_tips_text = _("The Chiesters' Golden Bow\n\nOne of the Chiester Sisters Imperial Guard Corps' sniping equipment.\nThe arrow's trajectory can be controlled at will, but it takes a special talent and special training to master its true potential.  Therefore, the equipment itself is a sign of high-class sniper's prestige.\nIt is a masterpiece anti-armor sniping bow, capable of penetrating a wide variety of armors and barriers, and with a rich type of ammunition selected as the arrow's warhead.\n\nFuthermore, the ones primarily used throughout the play were Wire-Guided Winged Piercing Rounds.\nBecause they are wire-guided, they are capable of highly deceptive long-distance precision sniping in complicated indoor terrain battles.")
    elif r_hyouji_tips == 6:
        $ r_tips_text = _("Regarding the Succession of the Witch\n\nIn the noble families of witches, family secrets are often inherited by a single child to prevent the propagation of hidden arts and the decline of quality.\nIt is the same with the Endless Witches, where the greatest hidden art goes to a single child, so that the hidden art does not propagate even after the retirement following the inheritance.\n\nCustom dictates that a witch from another sect must make a recommendation for the succession.\nLambdadelta recommended EVA.\nBernkastel recommended ANGE.\nIt is Unkown who recommended Beato.\n\nFuthermore, during the play, Beatrice had also inherited that name, but this custom only began recently.\nThe Predecessor was the original Beatrice, and all Endless Witches before her had different names.\nAfter that, it became customary that the name was also inherited, and EVA, following that tradition, gave ANGE the name of Beatrice.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen tips_text_ep4():
    if r_hyouji_tips == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_tips == 1:
        $ r_tips_text = _("Mariage Socière\n\nAn alliance of witches formed by the Witch of Origins, Lady MARIA, and the Endless Witch, Lady Beatrice.\nFrom them, a groundbreaking magical compendium was created, and Beatrice, whose magical power had declined, was given an immense new magical power.\n\nYou could probably say that through the formation of this alliance, Beatrice gained the Endless Power in the true sense.\n\nThe first clause was that witches accept each other, and respect each other's magic.\nAt one point, young Ange was invited into the alliance, but she was later excommunicated.")
    elif r_hyouji_tips == 2:
        $ r_tips_text = _("Magical Compendium\n\nA foundation that gives birth to magic.\nIn particular, it refers to a system by which magic can be automatically gained through shared use.\nYou could say that writing down their own magical compendium and leaving it for future generations is one of a witch's life works.\n\nHowever, magical compendiums of terrific magical power become proportionally difficult to comprehend, and shared use becomes troublesome.  As a result, it becomes so that the bearer was never born.\n\nIf it is of a easy to learn magical power, it may also be easy to share it, but as a result, it comes to ruin as a magical compendium with no greater effect than a simple good luck charm and is forgotten in the end.\n\nLeaving a magical compendium for later generations while simultaneously keeping that balance is the epitome of socery.")
    elif r_hyouji_tips == 3:
        $ r_tips_text = _("Grimoire\n\nIn short, a grimoire is that upon which a magical compendium is written down and transmitted to later generations.\n\nIt is said that today, the most famous grimoire in the world has a history of over 2000 years, is currently still in circulation, and continues to aquire new alliance members even now.\n\nIt is forbidden to speak the true name of that grimoire, and it is simply called \"Book\".")
    elif r_hyouji_tips == 4:
        $ r_tips_text = _("Beatrice's Titles\n\nAs a witch, Beatrice holds the two titles of \"Golden\" and \"Endless.\"  Because these were originally titles from separate magical compendiums, it can be said that she holds two magical compendiums.\n\nThe Endless Witch has its foundation in \"Endless Creation,\" and is the root of her unmatched endless magical power.\nThe Golden Witch has its foundation in \"Magic Realization,\" and the magical power to make precious metals materialize gives the miracle of materialization to all faint forms of magic.\n\nThe two of these were polished even further through Mariage Sorciere, leading to the sublimation of \"Endless Realization.\"\n\nIn that sense, she should now be called neither the Endless nor Golden Witch, but by a new title that is a fusion of the two.")
    elif r_hyouji_tips == 5:
        $ r_tips_text = _("Regarding Witches\n\nThe definition of a witch is vague, but the general theory is that at the point when one gains a power surpassing humans and is able to use it at will, that person is a witch.\n\nAnd the world, or possibly kakera, in which that can be used freely is called their territory.\nMost witches cannot leave this territory, but those who can leave it freely and migrate through the kakera are called Vaoyagers.\n\nIn the story, Bernkastel and Lambdadelta were these.")
    elif r_hyouji_tips == 6:
        $ r_tips_text = _("Regarding Voyagers\n\nWorlds of different fates and circumstances are called kakera, and witches who are able to cross the ocean of endless kakera are called Voyagers.\nIt is also a pseudonym for high-order witches, and witches who cannot leave their territories cannot compare with their power.\n\nHowever, perhaps because they do not have specific territories, their sense of worth is unstable, and it is easy for their souls to become faint.\nAs a result, it is not rare for Voyagers to become scraps of seaweed in the ocean of kakera and disappear.\n\nTheir voyage has no endpoint, and perhaps you could even say that it is a journey to escape an endpoint.\n\nWitches of a higher order than Voyagers are called Creators.")
    elif r_hyouji_tips == 7:
        $ r_tips_text = _("Regarding Creators\n\nCreators are scared beings who can create 1 out of the sea of nothingness.\nThey can give birth to 1 from 0, give birth to the endless, and then return it to 0 again in a flash.\nThey are freed from all restrictions, and the Voyagers sometimes even call them gods.\n\nIn that sense, perhaps the Witch of Origins, MARIA, is a chosen girl, bound to become a Creator......\n\nVoyagers are frightened that the ends of their own journeys mean becoming a Creator.\nAs to why they would be frightened of advancing to become a higher-order being, none can understand except they themselves.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen grim_text_ep1():
    if r_hyouji_grim == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_grim == 1:
        $ r_tips_text = _("Welcome to the Witch Hunt's in-game translation notes. \n\nAs you progress through the game, you will see some words colored {color=#86ef9c}green{/color}.  This coloring means that a new translation note is available on this screen, which you can check on at any time during the current episode.\n\nFor more in-depth notes about the game, please check the Grimoire doc files included in this patch, or visit our {a=http://www.witch-hunt.com}website{/a}. \n\nScroll down to learn about the Japanese suffixes and honorifics that are used frequently in this game. \n\n\n{size=60}Japanese Honorifics{/size}\n\nIn Japanese, honorifics are often used following names to convey respect.  Different honorifics are used in different relationships, and forgetting to say an honorific can either be rude, or mean that both people have a close relationship. \n\nsan ({font=default.ttf}さん{/font}):   Neutral honorific, this suffix is a generic word for Mr./Mrs./Ms. \n\nkun ({font=default.ttf}くん{/font}):   Used on a person of lesser age, usually male, denotes affection. \n\nchan ({font=default.ttf}ちゃん{/font}):    Used on a person of lesser age, usually female, denotes affection/close relationship, youth and cuteness. \n\nsama({font=default.ttf}さま{/font}):   Denotes high respect towards one person or used for someone of a higher status.  A very formal and polite suffix. \n\n\n{size=60}Familiar Terms/suffixes{/size}\n\nThese are used similarly to and sometimes together with honorifics. \n\naniki ({font=default.ttf}兄貴{/font}):   Older brother, \"yakuza\"-like honorific.  This word can used either as a stand-alone, or a suffix for someone's name. \n\naneki ({font=default.ttf}姉貴{/font}):   Older sister, \"yakuza\"-like honorific (rarer) \n\n(o)nii ({font=default.ttf}兄{/font}):    Older brother.  This word (and the following ones) usually have a proper honorific attached to them in order to refer to someone with them. Similar to aniki, you don't have to include the person's first name with it.  In fact, the word by itself is enough most of the time.  Note this word can also be used to refer to a young man, not necessarily a sibling. In such case, it denotes some familiarity.\n\n(o)nee ({font=default.ttf}姉{/font}):    Older sister.  Female counterpart of (o)nii in every way, this word can be used to refer to a young woman, not necessarily blood related. \n\noba ({font=default.ttf}伯母{/font}):   Aunt.  Note this word also means \"middle aged woman\" while its pronunciation is pretty close to \"obaa\" which means \"old woman.\"  This is the reason why in many manga and anime series, some characters tend not to call their aunt like this, otherwise they might have \"some\" trouble... \n\noji ({font=default.ttf}伯父{/font}):   Uncle.  Pretty much like oba, this can also be used for \"middle aged man.\" \n\n(o)ka ({font=default.ttf}お母{/font}):   Mother.  This is always with an honorific, generally san. \n\n(o)tou ({font=default.ttf}お父{/font}):   Father. \n\nSenpai ({font=default.ttf}先輩{/font}):   Often translated as \"senior.\" This word, pretty much like the previous ones, can be used as a stand alone or associated with one's name.\nIt is used for someone that is in a particular group or organization longer than you.\n(example: an upperclassman at school, someone with a higher rank in a sport, etc.)")
    elif r_hyouji_grim == 2:
        $ r_tips_text = _("{size=60}Western Names{/size}\n\nThe names of many characters in this game sound very foreign.  Normally, foreign words are written in katakana (phonetic characters) instead of the more common kanji.\n\nHowever, several members of the Ushiromiya family have foreign-sounding names written in Kanji (characters that have a meaning, but may be pronounced in several different way), which is very strange in Japan, though not unheard of.\n\nBattler's name is pronounced 'Batora,' but the characters it is written with would usually be pronounced like Sento or something similar.")
    elif r_hyouji_grim == 3:
        $ r_tips_text = _("{size=60}Namunamunamu{/size}\n\nDerived from \"Namu Amida Butsu,\" a buddhist prayer, literally \"I believe in the Amida Buddha.\"\nRecited to get into Amida's paradise.\n\nIn other words, Battler says something like \"Rest in peace, old bastard.\"")
    elif r_hyouji_grim == 4:
        $ r_tips_text = _("{size=60}Jessica's Speech{/size}\n\nIn Japanese, men and women speak slightly differently.  This difference is much larger than what you find in English.\n\nSimply put, Jessica speaks like a guy, which makes her sound bolder and ruder than you'd expect from a girl of her age, regardless of what she's actually saying.\n\nThis doesn't translate too well in all situations, so bear in mind that Jessica's speech is almost always casual and not particularly polite.")
    elif r_hyouji_grim == 5:
        $ r_tips_text = _("{size=60}Toriis and Tutelary Gods{/size}\n\nA torii is a ceremonial entry gate to a Shinto shrine, painted red.\n\nThe word 'tutelary god' was originally {font=default.ttf}鎮守様{/font}, which means the god of a region or a place.")
    elif r_hyouji_grim == 6:
        $ r_tips_text = _("{size=60}Yakitori{/size}\n\nA Japanese skewered chicken dish.  Literally means 'grilled bird.'")
    elif r_hyouji_grim == 7:
        $ r_tips_text = _("{size=60}Kotatsu{/size}\n\nA table frame covered by either a futon or a blanket, which is itself covered by a table top, and has a heat source beneath that is often built into the table itself.\nKotatsu is a reliable way to keep yourself warm, since heat is expensive in Japan due to poor insulation of housing in general.\n\nThe heat source and the blanket/futon can be removed, so the kotatsu can be used like a regular table.")
    elif r_hyouji_grim == 8:
        $ r_tips_text = _("{size=60}Kikurage{/size}\n\nLiterally \"tree-jellyfish,\" this mushroom is also known as \"Auricularia auricula-judae,\" or the Juads' ear fungus.\n\nThis species is often used in Asian cooking.")
    elif r_hyouji_grim == 9:
        $ r_tips_text = _("{size=60}Sogakishi{/size}\n\nThe word shore is composed of one kanji, {font=default.ttf}岸{/font} (kishi).\nThis kanji also used as a suffix for place names near the shore, such as Sogakishi ({font=default.ttf}曽我岸{/font}).")
    elif r_hyouji_grim == 10:
        $ r_tips_text = _("{size=60}Inari Shrines and Kitsune-sama{/size}\n\nInari ({font=default.ttf}稲荷{/font}) is the shinto god of fertility, rice and foxes and one of the most revered Shinto gods in Japan.\nThis is made apparent by the sheer amount of shrines dedicated to her, along with torii and many statues of kitsune (foxes).\n\nThe kitsune are white foxes that are her benevolent messengers.\nHowever, they can be malicious and generate grave disasters.")
    elif r_hyouji_grim == 11:
        $ r_tips_text = _("{size=60}Kakera{/size}\n\nThe Japanese word 'kakera' means 'shard,' 'piece' or 'fragment.'\nIt has a very special meaning in both Umineko and Higurashi.\nMore details can be found in Higurashi no {color=#ff0000}Na{/color}ku Koro ni.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen grim_text_ep2():
    if r_hyouji_grim == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_grim == 1:
        $ r_tips_text = _("Welcome to the Witch Hunt's in-game translation notes. \n\nAs you progress through the game, you will see some words colored {color=#86ef9c}green{/color}.  This coloring means that a new translation note is available on this screen, which you can check on at any time during the current episode.\n\nFor more in-depth notes about the game, please check the Grimoire doc files included in this patch, or visit our {a=http://www.witch-hunt.com}website{/a}. \n\nScroll down to learn about the Japanese suffixes and honorifics that are used frequently in this game. \n\n\n{size=60}Japanese Honorifics{/size}\n\nIn Japanese, honorifics are often used following names to convey respect.  Different honorifics are used in different relationships, and forgetting to say an honorific can either be rude, or mean that both people have a close relationship. \n\nsan ({font=default.ttf}さん{/font}):   Neutral honorific, this suffix is a generic word for Mr./Mrs./Ms. \n\nkun ({font=default.ttf}くん{/font}):   Used on a person of lesser age, usually male, denotes affection. \n\nchan ({font=default.ttf}ちゃん{/font}):    Used on a person of lesser age, usually female, denotes affection/close relationship, youth and cuteness. \n\nsama({font=default.ttf}さま{/font}):   Denotes high respect towards one person or used for someone of a higher status.  A very formal and polite suffix. \n\n\n{size=60}Familiar Terms/suffixes{/size}\n\nThese are used similarly to and sometimes together with honorifics. \n\naniki ({font=default.ttf}兄貴{/font}):   Older brother, \"yakuza\"-like honorific.  This word can used either as a stand-alone, or a suffix for someone's name. \n\naneki ({font=default.ttf}姉貴{/font}):   Older sister, \"yakuza\"-like honorific (rarer) \n\n(o)nii ({font=default.ttf}兄{/font}):    Older brother.  This word (and the following ones) usually have a proper honorific attached to them in order to refer to someone with them. Similar to aniki, you don't have to include the person's first name with it.  In fact, the word by itself is enough most of the time.  Note this word can also be used to refer to a young man, not necessarily a sibling. In such case, it denotes some familiarity.\n\n(o)nee ({font=default.ttf}姉{/font}):    Older sister.  Female counterpart of (o)nii in every way, this word can be used to refer to a young woman, not necessarily blood related. \n\noba ({font=default.ttf}伯母{/font}):   Aunt.  Note this word also means \"middle aged woman\" while its pronunciation is pretty close to \"obaa\" which means \"old woman.\"  This is the reason why in many manga and anime series, some characters tend not to call their aunt like this, otherwise they might have \"some\" trouble... \n\noji ({font=default.ttf}伯父{/font}):   Uncle.  Pretty much like oba, this can also be used for \"middle aged man.\" \n\n(o)ka ({font=default.ttf}お母{/font}):   Mother.  This is always with an honorific, generally san. \n\n(o)tou ({font=default.ttf}お父{/font}):   Father. \n\nSenpai ({font=default.ttf}先輩{/font}):   Often translated as \"senior.\" This word, pretty much like the previous ones, can be used as a stand alone or associated with one's name.\nIt is used for someone that is in a particular group or organization longer than you.\n(example: an upperclassman at school, someone with a higher rank in a sport, etc.)")
    elif r_hyouji_grim == 2:
        $ r_tips_text = _("{size=60}Tsundora{/size}\n\nRomaji reading for \"Tundra\" which is often used as a pun and reference to the term \"Tsundere\" ({font=default.ttf}ツンデレ{/font}), which has become increasingly popular in recent decades.\n\n\nThis Japanese term is composed by two words, \"tsuntsun\" and \"deredere,\" meaning respectively \"aloof or cranky\" and \"lovestruck.\"\nIt is mainly used for characters that demonstrate an aggressive and/or cold behavior (tsuntsun) but then become all lovey-dovey (deredere) under some circumstances.")
    elif r_hyouji_grim == 3:
        $ r_tips_text = _("{size=60}Boku/omgomg{/size}\n\n'Boku' ({font=default.ttf}僕/ぼく{/font}) is the pronoun for \"I.\"  This is often used by yound boys and can have a slightly cute feel to it.\nIt is less often used by teenagers and adults who would rather use 'ore' ({font=default.ttf}俺/おれ{/font}) or a neutral pronoun like 'watashi' ({font=default.ttf}私{/font}), and implies casual deference.\n\nThe Japanese 'word' for omgomg was 'ktkr,' an abbreviation for \"kita kore\" ({font=default.ttf}キタコレ{/font}), which literally means \"it's coming.\"\nThis Japanese online slang usually shows excitement or expectation and is often seen in the ASCII art shown below.\n\n{font=default.ttf}キタ━━━━━(・∀・)━━━━━━━━━!!!!{/font}")
    elif r_hyouji_grim == 4:
        $ r_tips_text = _("{size=60}Tsurupettan{/size}\n\nIn the non-FMV version of the scene, the name of the song Jessica's band plays is Tsurupettan, which was actually composed by Silver Forest and is one of the most popular songs related to the characters from the Touhou Project, a famous doujin danmaku shoot'em up created by ZUN.\n\nThe cross reference is doubled with Jessica's costume, which is Marisa's, one of the main characters of the Touhou franchise, along with Reimu.\n\n\nFinally, the colorful comments and ASCII art you see all over the screen is actually a reference to Nico Nico Douga ({font=default.ttf}ニコニコ動画{/font}), a Japanese streaming site, which is often considered the Japanese counterpart of Youtube.\n\nThe main original feature of this site was the ability for viewers to type comments that appear on the video itself and playback with the video at the moment they write the comment.")
    elif r_hyouji_grim == 5:
        $ r_tips_text = _("{size=60}Devil's Proof{/size}\n\nThis 'Devil's Proof' ({font=default.ttf}悪魔の証明{/font}) is actually the legal requirement used in court, known as Probatio Diabolica.")
    elif r_hyouji_grim == 6:
        $ r_tips_text = _("{size=60}Locus{/size}\n\nA locus is basically a curved line or surface.\n\nThe Japanese word used here can also mean a trace or track, and is pronounced the same as 'miracle' (kiseki).")
    elif r_hyouji_grim == 7:
        $ r_tips_text = _("{size=60}6x9=42{/size}\n\nReference to Hitchhiker's Guide to the Galaxy.\n\nThe Answer to the Ultimate Question of Life, the Universe and Everything.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen grim_text_ep3():
    if r_hyouji_grim == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_grim == 1:
        $ r_tips_text = _("Welcome to the Witch Hunt's in-game translation notes. \n\nAs you progress through the game, you will see some words colored {color=#86ef9c}green{/color}.  This coloring means that a new translation note is available on this screen, which you can check on at any time during the current episode.\n\nFor more in-depth notes about the game, please check the Grimoire doc files included in this patch, or visit our {a=http://www.witch-hunt.com}website{/a}. \n\nScroll down to learn about the Japanese suffixes and honorifics that are used frequently in this game. \n\n\n{size=60}Japanese Honorifics{/size}\n\nIn Japanese, honorifics are often used following names to convey respect.  Different honorifics are used in different relationships, and forgetting to say an honorific can either be rude, or mean that both people have a close relationship. \n\nsan ({font=default.ttf}さん{/font}):   Neutral honorific, this suffix is a generic word for Mr./Mrs./Ms. \n\nkun ({font=default.ttf}くん{/font}):   Used on a person of lesser age, usually male, denotes affection. \n\nchan ({font=default.ttf}ちゃん{/font}):    Used on a person of lesser age, usually female, denotes affection/close relationship, youth and cuteness. \n\nsama({font=default.ttf}さま{/font}):   Denotes high respect towards one person or used for someone of a higher status.  A very formal and polite suffix. \n\n\n{size=60}Familiar Terms/suffixes{/size}\n\nThese are used similarly to and sometimes together with honorifics. \n\naniki ({font=default.ttf}兄貴{/font}):   Older brother, \"yakuza\"-like honorific.  This word can used either as a stand-alone, or a suffix for someone's name. \n\naneki ({font=default.ttf}姉貴{/font}):   Older sister, \"yakuza\"-like honorific (rarer) \n\n(o)nii ({font=default.ttf}兄{/font}):    Older brother.  This word (and the following ones) usually have a proper honorific attached to them in order to refer to someone with them. Similar to aniki, you don't have to include the person's first name with it.  In fact, the word by itself is enough most of the time.  Note this word can also be used to refer to a young man, not necessarily a sibling. In such case, it denotes some familiarity.\n\n(o)nee ({font=default.ttf}姉{/font}):    Older sister.  Female counterpart of (o)nii in every way, this word can be used to refer to a young woman, not necessarily blood related. \n\noba ({font=default.ttf}伯母{/font}):   Aunt.  Note this word also means \"middle aged woman\" while its pronunciation is pretty close to \"obaa\" which means \"old woman.\"  This is the reason why in many manga and anime series, some characters tend not to call their aunt like this, otherwise they might have \"some\" trouble... \n\noji ({font=default.ttf}伯父{/font}):   Uncle.  Pretty much like oba, this can also be used for \"middle aged man.\" \n\n(o)ka ({font=default.ttf}お母{/font}):   Mother.  This is always with an honorific, generally san. \n\n(o)tou ({font=default.ttf}お父{/font}):   Father. \n\nSenpai ({font=default.ttf}先輩{/font}):   Often translated as \"senior.\" This word, pretty much like the previous ones, can be used as a stand alone or associated with one's name.\nIt is used for someone that is in a particular group or organization longer than you.\n(example: an upperclassman at school, someone with a higher rank in a sport, etc.)")
    elif r_hyouji_grim == 2:
        $ r_tips_text = _("{size=60}Ore/Watashi{/size}\n\nOre ({font=default.ttf}俺/オレ{/font}) is a pronoun used by boys and young men is general, an informal \"I\" that denotes familiarity among friends and family, but also masculinity and superiority towards their peers or people of lower status.\nWatashi ({font=default.ttf}私{/font}) is the neutral and formal pronoun for \"I,\" that can be used by anyone, regardless their gender or status.\n\nSwitching from ore to watashi may be sign that the person is trying to sound more serious, rather than simply masculine.")
    elif r_hyouji_grim == 3:
        $ r_tips_text = _("{size=60}Give up and die{/size}\n\nThis line was originally 'bite your belly-button and die,' pronounced 'heso kande shinjiaeba.'\n\nThe first part is a set phrase meanin something hopeless and isn't meant literally, but the literal meaning may end up becoming important as well...")
    elif r_hyouji_grim == 4:
        $ r_tips_text = _("{size=60}Lines in English{/size}\n\nSome lines in Umineko were written in katakana English, meaning the phonetic Japanese characters were used to sound out English.\nThese lines will be enclosed in < >, like <See you again.>\n\nBecause they're written in katakana, they would be pronounced a little different than what you might expect.  e.g. Shii yuu ah-gain.")
    elif r_hyouji_grim == 5:
        $ r_tips_text = _("{size=60}Merute{/size}\n\nThis word is probably related to a fictional unit of length measurement from 'Nausicaa of the Valley of the Wind', which seems to be about one meter long.")
    elif r_hyouji_grim == 6:
        $ r_tips_text = _("{size=60}Valkyria{/size}\n\nThe Japanese pronunciations for Virgilia (Warugiria) and Valkyira (Warukyura) are almost the same, which is why Battler mentions it.")
    elif r_hyouji_grim == 7:
        $ r_tips_text = _("{size=60}Village of Gold{/size}\n\nOne of the puzzles of the epitaph is the meaning of the word 'Golden Land': {font=default.ttf}黄金{/font}(gold)+{font=default.ttf}郷{/font}(land/country)={font=default.ttf}黄金郷{/font}(Golden Land).\n\nIn the line about the tenth twilight, it is written slightly differently: {font=default.ttf}黄金の郷{/font}.\nIn this sense '{font=default.ttf}の{/font}' (pronounced no) particle is similar to the English word 'of', in that the first word describes the second.\nThe difference between {font=default.ttf}黄金郷{/font} and {font=default.ttf}黄金の郷{/font} could be as simple as 'golden land' and 'land of gold'...in other words, no real difference.\n\nBut when the {font=default.ttf}郷{/font} character is by itself, it is often pronounced differently and may refer to a village or hometown.")
    elif r_hyouji_grim == 8:
        $ r_tips_text = _("{size=60}Pinning{/size}\n\nA pin in chess is a situation where a piece is unable to move because it would expose a more valuable piece otherwise.\n\nAn absolute pin is when the pinned piece is defending the king, and it is therefore impossible to move the pinned piece as it would leave the king in check (illegal move).")
    elif r_hyouji_grim == 9:
        $ r_tips_text = _("{size=60}Don't use Katakana!{/size}\n\nKatakana is the phonetic script used in Japanese, which usually used to write foreign names and is the way Beatrice's name is written every time during the game ({font=default.ttf}ベアトリーチェ{/font}).\n\nApparently Beatrice doesn't sign her name with the Roman alphabet and sticks with the katakana.")
    elif r_hyouji_grim == 10:
        $ r_tips_text = _("{size=60}Naniwa-bushis{/size}\n\nA kind of theatrical narrative and singing focused on human feelings and stories of loyalty.")
    elif r_hyouji_grim == 11:
        $ r_tips_text = _("{size=60}Galge{/size}\n\nContraction for Gal Games (Girl games).  This is a synonym for the archetype of games in Japan, known as Bishoujo games, which involve beautiful girls as the name implies.")
    elif r_hyouji_grim == 12:
        $ r_tips_text = _("{size=60}Ebaaah{/size}\n\nAs mentioned in an earlier tip, a certain catch-phrase is pronounced 'heso kande shinjia{color=#ff0000}eba{/color}'...")
    elif r_hyouji_grim == 13:
        $ r_tips_text = _("{size=60}The Names of Witches{/size}\n\nIn certain parts of the story, the names of some characters are written in Katakana instead of the normal Kanji.\nIn this translation, those names have been written in all-caps.\n\nThe reason for this is still shrouded in darkness, but you may spot a pattern as you read...")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
screen grim_text_ep4():
    if r_hyouji_grim == 0:
        $ r_tips_text = _("")
    
    if r_hyouji_grim == 1:
        $ r_tips_text = _("Welcome to the Witch Hunt's in-game translation notes. \n\nAs you progress through the game, you will see some words colored {color=#86ef9c}green{/color}.  This coloring means that a new translation note is available on this screen, which you can check on at any time during the current episode.\n\nFor more in-depth notes about the game, please check the Grimoire doc files included in this patch, or visit our {a=http://www.witch-hunt.com}website{/a}. \n\nScroll down to learn about the Japanese suffixes and honorifics that are used frequently in this game. \n\n\n{size=60}Japanese Honorifics{/size}\n\nIn Japanese, honorifics are often used following names to convey respect.  Different honorifics are used in different relationships, and forgetting to say an honorific can either be rude, or mean that both people have a close relationship. \n\nsan ({font=default.ttf}さん{/font}):   Neutral honorific, this suffix is a generic word for Mr./Mrs./Ms. \n\nkun ({font=default.ttf}くん{/font}):   Used on a person of lesser age, usually male, denotes affection. \n\nchan ({font=default.ttf}ちゃん{/font}):    Used on a person of lesser age, usually female, denotes affection/close relationship, youth and cuteness. \n\nsama({font=default.ttf}さま{/font}):   Denotes high respect towards one person or used for someone of a higher status.  A very formal and polite suffix. \n\n\n{size=60}Familiar Terms/suffixes{/size}\n\nThese are used similarly to and sometimes together with honorifics. \n\naniki ({font=default.ttf}兄貴{/font}):   Older brother, \"yakuza\"-like honorific.  This word can used either as a stand-alone, or a suffix for someone's name. \n\naneki ({font=default.ttf}姉貴{/font}):   Older sister, \"yakuza\"-like honorific (rarer) \n\n(o)nii ({font=default.ttf}兄{/font}):    Older brother.  This word (and the following ones) usually have a proper honorific attached to them in order to refer to someone with them. Similar to aniki, you don't have to include the person's first name with it.  In fact, the word by itself is enough most of the time.  Note this word can also be used to refer to a young man, not necessarily a sibling. In such case, it denotes some familiarity.\n\n(o)nee ({font=default.ttf}姉{/font}):    Older sister.  Female counterpart of (o)nii in every way, this word can be used to refer to a young woman, not necessarily blood related. \n\noba ({font=default.ttf}伯母{/font}):   Aunt.  Note this word also means \"middle aged woman\" while its pronunciation is pretty close to \"obaa\" which means \"old woman.\"  This is the reason why in many manga and anime series, some characters tend not to call their aunt like this, otherwise they might have \"some\" trouble... \n\noji ({font=default.ttf}伯父{/font}):   Uncle.  Pretty much like oba, this can also be used for \"middle aged man.\" \n\n(o)ka ({font=default.ttf}お母{/font}):   Mother.  This is always with an honorific, generally san. \n\n(o)tou ({font=default.ttf}お父{/font}):   Father. \n\nSenpai ({font=default.ttf}先輩{/font}):   Often translated as \"senior.\" This word, pretty much like the previous ones, can be used as a stand alone or associated with one's name.\nIt is used for someone that is in a particular group or organization longer than you.\n(example: an upperclassman at school, someone with a higher rank in a sport, etc.)")
    elif r_hyouji_grim == 2:
        $ r_tips_text = _("{size=60}Lines in English{/size}\n\nSome lines in Umineko were written in katakana English, meaning the phonetic Japanese characters were used to sound out English.\nThese lines will be enclosed in < >, like <Have a nice dream>.\n\nBecause they're written in katakana, they would be pronounced a little different than what you might expect.  e.g. Ha ba naisu doriimu.")
    elif r_hyouji_grim == 3:
        $ r_tips_text = _("{size=60}Shotoku Taishi{/size}\n\nThe man whose face was on the 10,000 yen note from 1957 to 1984 (about 55 dollars at that time).")
    elif r_hyouji_grim == 4:
        $ r_tips_text = _("{size=60}'Demon' Kasumi{/size}\n\nThe word translated demon here is actually 'Hannya', a type of mask common in Japanese Noh Theater that represents a jealous, female demon.")
    elif r_hyouji_grim == 5:
        $ r_tips_text = _("{size=60}Vessel{/size}\n\nThe Japanese word used here is 'yorishiro'.\n\nA yorishiro is an object or person that acts as a physical entity for a spirit or god to dwell in.")
    elif r_hyouji_grim == 6:
        $ r_tips_text = _("{size=60}Rifle/Teppou{/size}\n\nThe first characters kids learn to write in Japan are Hiragana, which is a phonetic set like Katakana but used mainly for Japanese words instead of foreign ones.\n\nFor example, Katakana is used to pronounce the foreign word 'rifle', while the Japanese word for gun, 'teppou', would be written in Kanji, or else hiragana if the writer was a kid who hadn't learned Kanji yet.\n\nThere are several thousand Kanji in common use in Japan, so students keep on learning more and more of them from elementary school until high school.")
    elif r_hyouji_grim == 7:
        $ r_tips_text = _("{size=60}Shiritori{/size}\n\nThis is a Japanese game where players take turns saying words that start with the last syllable of the previous word.\nAnytime someone says a word that ends with nn ({font=default.ttf}ん{/font}), they lose, because no Japanese word starts with that sound.\n\nE.G.  Ootsuki->Kyrie->Ange->Jessica->Kanon\n\nThe person who said 'Kanon' loses.")
    elif r_hyouji_grim == 8:
        $ r_tips_text = _("{size=60}110{/size}\n\nThis is the number for calling the police in Japan.")
    elif r_hyouji_grim == 9:
        $ r_tips_text = _("{size=60}Kyukyukyukyu{/size}\n\nThe Japanese word for 9 is pronounced 'kyuu'.")
    elif r_hyouji_grim == 10:
        $ r_tips_text = _("{size=60}IME{/size}\n\nInput Method Editor.  This is a computer term which means a way to write characters that don't appear on a keyboard.  Often used to input Japanese text.  This term is only used by Microsoft.")
    elif r_hyouji_grim == 11:
        $ r_tips_text = _("{size=60}Loser Flag{/size}\n\nParody of the usual \"love/event/bad end/etc.\" flags you can find in most visual novels.\n\nPeople say something is a 'death flag' or 'loser flag' to refer to a cliché that is almost always followed by death or total failure for a character in a story.")
    elif r_hyouji_grim == 12:
        $ r_tips_text = _("{size=60}Minmeishobou{/size}\n\nA parody of a fictional series of books from an old manga that explains fighting moves and the like with ridiculous, fake explanations that may sound somewhat believable.\n\nThe scene with the 'triple cross' is probably a parody of the very famous and long-running boxing manga, Ashita no Joe, which had the same explanation for the move.")
    
    side "c r":
        area (864, 174, 850, 745)
        viewport id "chr_txt":
            draggable True
            mousewheel True
            text r_tips_text style style.tips_text
#        vbar value YScrollValue("chr_txt")
    vbar value YScrollValue("chr_txt") xmaximum 20 ymaximum 745 xpos (1729.0/1920.0) ypos (174.0/1080.0)
#    add "r_click/chars/vscrollbar.png" xpos (1698.0/1920.0) ypos (126.0/1080.0)
    
init:
    python:
        
        f_hana = im.MatrixColor("r_click/chars/hana.png", im.matrix.colorize("#000","#898989"))
        h_hana = im.MatrixColor("r_click/chars/hana.png", im.matrix.colorize("#000","#a60000"))
        w_hana = im.MatrixColor("r_click/chars/hana.png", im.matrix.colorize("#000","#945c00"))
        
        btn_char_change_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,0,312,64)), im.matrix.brightness(-0.5))
        btn_char_change_h = im.Crop("r_click/chars/button_chars.png", (0,0,312,64))
        
        btn_char_exec_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,64,170,64)), im.matrix.brightness(-0.5))
        btn_char_exec_h = im.Crop("r_click/chars/button_chars.png", (0,64,170,64))
        
        btn_char_resur_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,128,206,64)), im.matrix.brightness(-0.5))
        btn_char_resur_h = im.Crop("r_click/chars/button_chars.png", (0,128,206,64))
        
        btn_char_side_0_i = im.MatrixColor(im.Crop("r_click/chars/side.png", (0,0,200,48)), im.matrix.brightness(-0.5))
        btn_char_side_0_h = im.Crop("r_click/chars/side.png", (0,0,200,48))
        btn_char_side_1_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("r_click/chars/side.png", (0,48,180,48)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("r_click/chars/side.png", (0,48,200,48)), im.matrix.brightness(-0.5)))
        btn_char_side_1_h = ConditionSwitch("_preferences.language == None", im.Crop("r_click/chars/side.png", (0,48,180,48)), "_preferences.language == 'japanese'", im.Crop("r_click/chars/side.png", (0,48,200,48)))
        btn_char_side_2_i = ConditionSwitch("_preferences.language == None", im.MatrixColor(im.Crop("r_click/chars/side.png", (0,96,188,48)), im.matrix.brightness(-0.5)), "_preferences.language == 'japanese'", im.MatrixColor(im.Crop("r_click/chars/side.png", (0,96,200,48)), im.matrix.brightness(-0.5)))
        btn_char_side_2_h = ConditionSwitch("_preferences.language == None", im.Crop("r_click/chars/side.png", (0,96,188,48)), "_preferences.language == 'japanese'", im.Crop("r_click/chars/side.png", (0,96,200,48)))
        
        btn_char_ep1_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,192,96,64)), im.matrix.brightness(-0.5))
        btn_char_ep1_h = im.Crop("r_click/chars/button_chars.png", (0,192,96,64))
        btn_char_ep2_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,256,96,64)), im.matrix.brightness(-0.5))
        btn_char_ep2_h = im.Crop("r_click/chars/button_chars.png", (0,256,96,64))
        btn_char_ep3_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,320,96,64)), im.matrix.brightness(-0.5))
        btn_char_ep3_h = im.Crop("r_click/chars/button_chars.png", (0,320,96,64))
        btn_char_ep4_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (0,384,96,64)), im.matrix.brightness(-0.5))
        btn_char_ep4_h = im.Crop("r_click/chars/button_chars.png", (0,384,96,64))
        btn_char_ep5_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (112,192,96,64)), im.matrix.brightness(-0.5))
        btn_char_ep5_h = im.Crop("r_click/chars/button_chars.png", (112,192,96,64))
        btn_char_ep6_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (112,256,98,64)), im.matrix.brightness(-0.5))
        btn_char_ep6_h = im.Crop("r_click/chars/button_chars.png", (112,256,98,64))
        btn_char_ep7_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (112,320,99,64)), im.matrix.brightness(-0.5))
        btn_char_ep7_h = im.Crop("r_click/chars/button_chars.png", (112,320,99,64))
        btn_char_ep8_i = im.MatrixColor(im.Crop("r_click/chars/button_chars.png", (112,384,97,64)), im.matrix.brightness(-0.5))
        btn_char_ep8_h = im.Crop("r_click/chars/button_chars.png", (112,384,97,64))
        
        line_01r = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,36,32,36)), im.matrix.colorize("#000","#9c1143"))    # 480 - f90101
        line_01g = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,36,32,36)), im.matrix.colorize("#000","#cfbe3a"))    # 480 - f9ce01
        line_01b = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,36,32,36)), im.matrix.colorize("#000","#3d16af"))    # 480 - 0253f8
        
        line_02r = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,72,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_02g = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,72,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_02b = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,72,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_03r = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,108,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_03g = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,108,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_03b = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,108,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_04r = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,0,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_04g = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,0,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_04b = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,0,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_05r = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,36,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_05g = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,36,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_05b = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,36,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_06r = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,72,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_06g = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,72,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_06b = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,72,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_07r = im.MatrixColor(im.Crop("r_click/chars/line.png", (0,108,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_07g = im.MatrixColor(im.Crop("r_click/chars/line.png", (0,108,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_07b = im.MatrixColor(im.Crop("r_click/chars/line.png", (0,108,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_08r = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,108,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_08g = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,108,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_08b = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,108,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_09r = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,36,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_09g = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,36,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_09b = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,36,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_10r = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,72,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_10g = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,72,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_10b = im.MatrixColor(im.Crop("r_click/chars/line.png", (96,72,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_11r = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,108,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_11g = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,108,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_11b = im.MatrixColor(im.Crop("r_click/chars/line.png", (64,108,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        line_12r = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,0,32,36)), im.matrix.colorize("#000","#9c1143"))
        line_12g = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,0,32,36)), im.matrix.colorize("#000","#cfbe3a"))
        line_12b = im.MatrixColor(im.Crop("r_click/chars/line.png", (32,0,32,36)), im.matrix.colorize("#000","#3d16af"))
        
        cha_back = LiveComposite((848,792), (208,52), line_08r, (336,52), line_01r, (464,52), line_01r
                    , (208,88), line_02r, (208,124), line_02r, (208,160), line_02r
                    , (208,196), line_11r, (336,196), line_01r, (464,196), line_01r
                    , (208,232), line_02r, (208,268), line_02r, (208,304), line_02r
                    , (208,340), line_11r, (336,340), line_01r, (464,340), line_01r
                    , (208,376), line_02r, (208,412), line_02r, (208,448), line_02r
                    , (208,484), line_05r, (336,484), line_01r, (368,484), line_01r, (400,484), line_01r, (432,484), line_01r, (464,484), line_01r
                    , (208,628), line_01b, (336,628), line_01b, (464,628), line_01b, (592,628), line_01b)
        
        cha_back3 = LiveComposite((848,792), (384,340), line_01g, (416,340), line_01g)
        
        cha_back_ma = LiveComposite((848,792), (128,124), line_01g, (256,124), line_01g, (544,124), line_01r, (672,124), line_01r
                    , (64,196), line_02b, (480,196), line_02b, (480,340), line_02b, (480,484), line_02b)
        
        cha_back10 = LiveComposite((848,792), (192,286), line_07b, (224,286), line_01b, (256,286), line_01b, (288,286), line_01b, (320,286), line_01b, (352,286), line_01b, (384,286), line_01b, (416,286), line_10b)
        
        cha_back11 = LiveComposite((848,792), (192,358), line_07b, (224,358), line_01b, (256,358), line_01b, (288,358), line_01b, (320,358), line_01b, (352,358), line_01b, (384,358), line_01b, (416,358), line_10b, (416,214), line_02b)
        
        cha_back12 = LiveComposite((848,792), (352,142), line_01g
                    , (192,358), line_07b, (224,358), line_01b, (256,358), line_01b, (288,358), line_01b, (320,358), line_01b, (352,358), line_01b, (384,358), line_01b, (416,358), line_10b, (416,214), line_02b)
        
        cha_back13 = LiveComposite((848,792), (240,142), line_01g, (368,142), line_01g
                    , (208,358), line_07b, (240,358), line_01b, (272,358), line_01b, (304,358), line_01b, (336,358), line_01b, (368,358), line_01b, (400,358), line_01b, (432,358), line_10b, (432,214), line_02b)
        cha_back13_2 = LiveComposite((848,792), (240,70), line_01g, (368,70), line_01g
                    , (208,286), line_07b, (240,286), line_01b, (272,286), line_01b, (304,286), line_01b, (336,286), line_01b, (368,286), line_01b, (400,286), line_01b, (432,286), line_10b, (432,142), line_02b)
        
        cha_back14 = LiveComposite((848,792), (224,142), line_01g, (352,142), line_01g
                    , (192,358), line_07b, (224,358), line_01b, (256,358), line_01b, (288,358), line_01b, (320,358), line_01b, (352,358), line_01b, (384,358), line_01b, (416,358), line_10b
                    , (416,214), line_11b, (448,214), line_01b, (480,214), line_01b, (512,214), line_01b, (544,214), line_06b)
        cha_back14_2 = LiveComposite((848,792), (224,70), line_01g, (352,70), line_01g
                    , (192,286), line_07b, (224,286), line_01b, (256,286), line_01b, (288,286), line_01b, (320,286), line_01b, (352,286), line_01b, (384,286), line_01b, (416,286), line_10b
                    , (416,142), line_11b, (448,142), line_01b, (480,142), line_01b, (512,142), line_01b, (544,142), line_06b)
        
        cha_back4 = LiveComposite((848,792), (208,52), line_08r, (336,52), line_01r, (464,52), line_01r
                    , (208,88), line_02r, (208,124), line_02r, (208,160), line_02r
                    , (208,196), line_11r, (336,196), line_01r, (464,196), line_01r
                    , (208,232), line_02r, (208,268), line_02r, (208,304), line_02r
                    , (208,340), line_11r, (336,340), line_01r, (464,340), line_01r, (592,340), line_01r
                    , (208,376), line_02r, (208,412), line_02r, (208,448), line_02r
                    , (208,484), line_05r, (336,484), line_01r, (368,484), line_01r, (400,484), line_01r, (432,484), line_01r, (464,484), line_01r
                    , (208,628), line_01b, (336,628), line_01b, (464,628), line_01b, (592,628), line_01b)
        
        cha_back15 = LiveComposite((848,792), (208,70), line_01g, (336,70), line_01g, (464,70), line_01g, (496,70), line_01g, (528,70), line_01g, (560,70), line_01g, (592,70), line_01g
                    , (192,286), line_07b, (224,286), line_01b, (256,286), line_01b, (288,286), line_01b, (320,286), line_01b, (352,286), line_01b, (384,286), line_01b, (416,286), line_10b
                    , (416,142), line_11b, (448,142), line_01b, (480,142), line_01b, (512,142), line_01b, (544,142), line_06b)
        
        cha_back16 = LiveComposite((848,792), (208,52), line_08r, (336,52), line_01r, (464,52), line_01r
                    , (208,88), line_02r, (208,124), line_02r, (208,160), line_02r
                    , (208,196), line_11r, (336,196), line_01r, (464,196), line_01r
                    , (208,232), line_02r, (208,268), line_02r, (208,304), line_02r
                    , (208,340), line_11r, (336,340), line_01r
                    , (208,376), line_02r, (208,412), line_02r, (208,448), line_02r
                    , (208,484), line_05r, (336,484), line_01r, (368,484), line_01r, (400,484), line_01r, (432,484), line_01r, (464,484), line_01r
                    , (208,628), line_01b, (336,628), line_01b, (464,628), line_01b, (592,628), line_01b)
        
        ba4_2_0 = LiveComposite((848,792), (272,340), line_02g, (528,340), line_02g, (336,412), line_01g, (464,412), line_01g)
        
        ba4_2_1 = LiveComposite((848,792), (272,268), line_02g, (528,268), line_02g
                    , (336,340), line_01g, (464,340), line_01g, (272,412), line_02g)
        
        ba4_2_2 = LiveComposite((848,792), (272,268), line_02g, (528,268), line_02g
                    , (336,340), line_01g, (464,340), line_01g
                    , (272,412), line_02g, (400,412), line_02b)
        
        ba4_2_4 = LiveComposite((848,792), (320,196), line_02g, (576,196), line_02g
                    , (384,268), line_01g, (512,268), line_01g
                    , (320,340), line_02g, (448,340), line_02b
                    , (320,484), line_02b)
        
        ba4_2_5 = LiveComposite((848,792), (240,196), line_02g, (496,196), line_02g
                    , (304,268), line_01g, (432,268), line_01g
                    , (240,340), line_02g, (368,340), line_02b
                    , (240,484), line_11b, (272,484), line_01b, (304,484), line_01b, (336,484), line_01b, (368,484), line_01b, (400,484), line_01b, (432,484), line_01b, (464,484), line_06b)
        
        ba4_2_6 = LiveComposite((848,792), (304,124), line_02g, (560,124), line_02g
                    , (368,196), line_01g, (496,196), line_01g
                    , (304,268), line_02g, (432,268), line_02b
                    , (176,412), line_07b, (208,412), line_01b, (240,412), line_01b, (272,412), line_01b, (304,412), line_03b, (336,412), line_01b, (368,412), line_01b, (400,412), line_01b, (432,412), line_01b, (464,412), line_01b, (496,412), line_01b, (528,412), line_06b
                    , (48,556), line_07b, (80,556), line_01b, (112,556), line_01b, (144,556), line_01b, (176,556), line_09b, (208,556), line_01b, (240,556), line_01b, (272,556), line_01b, (304,556), line_09b, (336,556), line_01b, (368,556), line_01b, (400,556), line_01b, (432,556), line_01b, (464,556), line_06b)
        
        ba4_2_7 = LiveComposite((848,792), (240,124), line_02g, (496,124), line_02g
                    , (304,196), line_01g, (432,196), line_01g
                    , (240,268), line_02g, (368,268), line_02b
                    , (112,412), line_07b, (144,412), line_01b, (176,412), line_01b, (208,412), line_01b, (240,412), line_03b, (272,412), line_01b, (304,412), line_01b, (336,412), line_01b, (368,412), line_08b, (400,412), line_01b, (432,412), line_01b, (464,412), line_01b, (496,412), line_01b, (528,412), line_01b, (560,412), line_01b, (592,412), line_06b
                    , (48,556), line_07b, (80,556), line_01b, (112,556), line_09b, (144,556), line_01b, (176,556), line_01b, (208,556), line_01b, (240,556), line_09b, (272,556), line_01b, (304,556), line_01b, (336,556), line_01b, (368,556), line_01b, (400,556), line_01b, (432,556), line_01b, (464,556), line_06b)
        
        ba4_2_7_2 = LiveComposite((848,792), (304,124), line_02g, (560,124), line_02g            # for use on title
                    , (368,196), line_01g, (496,196), line_01g
                    , (304,268), line_02g, (432,268), line_02b
                    , (48,412), line_07b, (80,412), line_01b, (112,412), line_01b, (144,412), line_01b, (176,412), line_08b, (208,412), line_01b, (240,412), line_01b, (272,412), line_01b, (304,412), line_03b, (336,412), line_01b, (368,412), line_01b, (400,412), line_01b, (432,412), line_01b, (464,412), line_01b, (496,412), line_01b, (528,412), line_06b
                    , (48,556), line_11b, (80,556), line_01b, (112,556), line_01b, (144,556), line_01b, (176,556), line_09b, (208,556), line_01b, (240,556), line_01b, (272,556), line_01b, (304,556), line_01b, (336,556), line_01b, (368,556), line_01b, (400,556), line_01b, (432,556), line_01b, (464,556), line_06b)
        
        ba4_3_0 = LiveComposite((848,792), (400,340), line_02r)
        
        ba4_3_1 = LiveComposite((848,792), (336,340), line_02r, (400,268), line_01b)
        
        ba4_3_2 = LiveComposite((848,792), (464,340), line_02r, (528,268), line_01b
                    , (272,412), line_01r, (304,412), line_01r, (336,412), line_01r, (368,412), line_01r, (400,412), line_01r)
        
        ba4_3_3 = LiveComposite((848,792), (528,268), line_01b
                    , (464,340), line_02r , (592,340), line_02b
                    , (272,412), line_01r, (304,412), line_01r, (336,412), line_01r, (368,412), line_01r, (400,412), line_01r, (528,412), line_01b)
        
        ba4_3_3_2 = LiveComposite((848,792), (528,196), line_01b
                    , (464,268), line_02r , (592,268), line_02b
                    , (272,340), line_01r, (304,340), line_01r, (336,340), line_01r, (368,340), line_01r, (400,340), line_01r, (528,340), line_01b)
        
        ba4_3_5 = LiveComposite((848,792), (528,124), line_01b
                    , (464,196), line_02r , (592,196), line_02b
                    , (272,268), line_01r, (304,268), line_01r, (336,268), line_01r, (368,268), line_01r, (400,268), line_01r, (528,268), line_01b
                    , (464,340), line_02g)
        
        ba4_3_6 = LiveComposite((848,792), (496,70), line_01b
                    , (432,142), line_02r , (560,142), line_02b
                    , (240,214), line_01r, (272,214), line_01r, (304,214), line_01r, (336,214), line_01r, (368,214), line_01r, (496,214), line_01b
                    , (208,286), line_07g, (240,286), line_01g, (272,286), line_01g, (304,286), line_01g, (336,286), line_01g, (368,286), line_01g, (400,286), line_01g, (432,286), line_10g)
        
        ba4_3_7 = LiveComposite((848,792), (512,70), line_01b
                    , (448,142), line_02r , (576,142), line_02b
                    , (256,214), line_01r, (288,214), line_01r, (320,214), line_01r, (352,214), line_01r, (384,214), line_01r, (512,214), line_01b
                    , (128,286), line_07g, (160,286), line_01g, (192,286), line_01g, (224,286), line_01g, (256,286), line_08g, (288,286), line_01g, (320,286), line_01g, (352,286), line_01g, (384,286), line_01g, (416,286), line_01g, (448,286), line_09g, (480,286), line_06g)
        
        
