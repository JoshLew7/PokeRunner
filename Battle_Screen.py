# import PokeStats

def setup():
    from random import  randint
    
    # BulbaTrap's Attacks
    global growl, tackle, vinewhip, toxic
    
    # Cha Fuego's Attacks
    global scratch, slash, ember, firespin
    
    # Lil Squirt's Attacks
    global headbutt, tailwhip, bubble, watergun
    
    # health bars
    global enemyHealth, Health
    
    # starter health
    global bulbNum, chaNum, sqNum
    
    global bulb, cha, lil
    
    global enemypicturelist, enemy
    
    global run
    
    
    # Characters
    bulb = True
    cha = False
    lil = False
   
     # Background
    size(600, 600)
    img = loadImage("BattleScreen copy.jpg")
    image(img, 0, 0, 600, 600)
    
    enemyHealth = 500
    Health = 1000
    
    enemypicturelist = [ loadImage("1-Bulbasaur copy.png"), loadImage("squirtle3 copy.png"), 
                loadImage("charmandere3 copy.png"), loadImage("pika7.png")]
    
    enemy = (enemypicturelist[randint(0,3)])
    
    # (enemypicturelist[randint(0,2)])

    
    # BulbaTrap's Attacks
    growl = 0
    tackle = 0
    vinewhip = 0
    toxic = 0
    
    # Cha Fuego's Attacks
    scratch = 0
    slash = 0
    ember = 0
    firespin = 0
    
    # Lil Squirt's Attacks
    headbutt = 0
    tailwhip = 0
    bubble = 0
    watergun = 0
    
    # bulbNum = int(1000)
    # chaNum = int(1000)
    # sqNum = int(1000)
    
    # health bars
    # bulbHealth = bulbNum
    # chaHealth = 1000
    # squHealth = 1000
    
    
    # fill(255)
    # rect(0, 0, 100, 50)
    # fill(0)
    # text("Health: ", 10, 25)
   
    
    # set's bulbatrap's attacks in the boxes
    if bulb == True:
      

        fill(255)
        rect(30, 450, 150, 50)
        fill(0)
        textSize(40)
        text("Tackle", 40, 490)
        tackle = 40
       
        # vine whip
        fill(255)
        rect(205, 450, 150, 50)
        fill(0)
        textSize(30)
        text("Vine Whip", 208, 487)
        vinewhip = 40
        
        # toxic
        fill(255)
        rect(205, 510, 150, 50)
        fill(0)
        textSize(40)
        text("Toxic", 225, 550)
        toxic = 50 
        
        # growl
        fill(255)
        rect(30, 510, 150, 50)
        fill(0)
        textSize(40)
        text("Growl", 45, 550)
        growl = 25
        
        # run
        fill(255)
        rect(410, 480, 140, 52)
        fill(0)
        textSize(50)
        text("Run", 435, 525) 
        enemyattacklist=[90,80,40]
        
        #these work
        fill(255)
        rect(10, 15, 205, 50)
        textSize(36) 
        fill(0)
        text("Health: " + str(enemyHealth), 10, 57)
        
        
        fill(255)
        rect(380, 295, 215, 50)
        fill(0)
        text("Health: " + str(Health), 387, 340)
        
   
    # set's cha fuego's attacks in the boxes
    if cha == True:
        
        # scratch
        fill(255)
        rect(30, 510, 150, 50)
        fill(0)
        textSize(40)
        text("Scratch", 35, 550)
        scratch = 40
       
       # slash
        fill(255)
        rect(30, 450, 150, 50)
        fill(0)
        textSize(50)
        text("Slash", 43, 495)
        slash = 70
        
        #ember
        fill(255)
        rect(205, 450, 150, 50)
        fill(0)
        textSize(45)
        text("Ember", 212, 493)
        ember = 40
       
       # fire spin
        fill(255)
        rect(205, 510, 150, 50)
        fill(0)
        textSize(35)
        text("Fire Spin", 207, 550)
        firespin = 35
       
       # run
        fill(255)
        rect(410, 480, 140, 52)
        fill(0)
        textSize(50)
        text("Run", 432, 523)
        
        textSize(36)
        fill(255)
        rect(10, 15, 205, 50)
        textSize(36) 
        fill(0)
        text("Health: " + str(enemyHealth), 10, 57)
        
        
        fill(255)
        rect(380, 295, 215, 50)
        fill(0)
        text("Health: " + str(Health), 387, 340)
  

   
    # set's lil squirt's attacks in the boxes
    if lil == True:
         
        # headbutt
        fill(255)
        rect(30, 510, 150, 50)
        fill(0)
        textSize(32)
        text("Headbutt", 33, 550)
        headbutt = 10
        
        # tail whip
        fill(255)
        rect(30, 450, 150, 50)
        fill(0)
        textSize(33)
        text("Tail Whip", 32, 490)
        tailwhip = 35
       
        # bubble
        fill(255)
        rect(205, 450, 150, 50)
        fill(0)
        textSize(45)
        text("Bubble", 206, 494)
        bubble = 40
        
        # water gun
        fill(255)
        rect(205, 510, 150, 50)
        fill(0)
        textSize(29)
        text("Water Gun", 208, 550)
        watergun = 70
        
        # run
        fill(255)
        rect(410, 480, 140, 52)
        fill(0)
        textSize(52)
        text("Run", 435, 525)
        
        run = False

        
    
def draw():
    from random import  randint
    
    img = loadImage("BattleScreen copy.jpg")
    image(img, 0, 0, 600, 600)
    
    # img2 = loadImage("gold-silver-back.png")
    # image(img2, 100, 350, 100, 100)
    
    
      # BulbaTrap's Attacks
    global growl, tackle, vinewhip, toxic
    
    # Cha Fuego's Attacks
    global scratch, slash, ember, firespin
    
     # Lil Squirt's Attacks
    global headbutt, tailwhip, bubble, watergun
    
    # health bars
    global enemyHealth, Health
    
    global enemyattacklist
    
    # characters
    global bulb, cha, lil
    
    global enemypicturelist, enemy
    
    global run
    
   

    enemyattacklist=[90,80,40]
    


    
    # bulbaTrap's attacks
    if bulb == True:
        
        #(enemypicturelist[randint(0,2)])
        img2 = loadImage("gold-silver-back.png")
        image(img2, 95, 325, 120, 120)
    
        # img = enemy
        image(enemy, 395, 115, 150, 150)
        


 
        # growl
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            print("growl")
            enemyHealth = enemyHealth - 25
            Health-=(enemyattacklist[randint(0,2)])
            
            #tackle  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            print("tackle")
            enemyHealth = enemyHealth - 30
            Health-=(enemyattacklist[randint(0,2)])
            print(enemyHealth)
            #rect(0,0,600,80)
            
            # else:
            #     bulbHealth = 100
            # vine whip
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            print("vine whip")
            enemyHealth = enemyHealth - 45
            Health-=(enemyattacklist[randint(0,2)])
                
                
            # toxic
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            print("toxic")
            enemyHealth = enemyHealth - 50
            Health-=(enemyattacklist[randint(0,2)])
            
            enemyattacklist=[90,80,40]
            
        textSize(36) 
        fill(255)
        rect(10, 15, 205, 50)
        textSize(36) 
        fill(0)   
        text("Health: " + str(enemyHealth), 10, 57)
       
        fill(255)
        rect(380, 295, 215, 50)
        fill(0)
        text("Health: " + str(Health), 387, 340)
            
            #run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            print("run")
            run = True
            
            # if run == True:
                
                
                # make it go back to the adventure screen
                
                # set's bulbatrap's attacks in the boxes
        if bulb == True:
        
               # tackle
            fill(255)
            rect(30, 450, 150, 50)
            fill(0)
            textSize(40)
            text("Tackle", 40, 490)
            tackle = 40
                
                    # vine whip
            fill(255)
            rect(205, 450, 150, 50)
            fill(0)
            textSize(30)
            text("Vine Whip", 208, 487)
            vinewhip = 40
                
                    # toxic
            fill(255)
            rect(205, 510, 150, 50)
            fill(0)
            textSize(40)
            text("Toxic", 225, 550)
            toxic = 50 
                    
                    # growl
            fill(255)
            rect(30, 510, 150, 50)
            fill(0)
            textSize(40)
            text("Growl", 45, 550)
            growl = 25
                    
                    # run
            fill(255)
            rect(410, 480, 140, 52)
            fill(0)
            textSize(50)
            text("Run", 435, 525) 
            
            # text("Health: " + str(enemyHealth), 10, 57)
            # text("Health: " + str(enemyHealth), 10, 500)
            
        
     
     
      # cha fuego's attacks       
    if cha == True:
        img = enemy
        image(img, 395, 115, 150, 150)
        img2 = loadImage("charback.png")
        image(img2, 100, 350, 100, 100)
        
         
           # scratch
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            print("scratch")
            #bulbAttack = bulbHealth - 30
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
        
        
           # slash  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            print("slash")
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
        
        
        
           # ember
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            print("ember")
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
    
        
        
           # fire spin
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            print("fire spin")
            enemyHealth = enemyHealth - 35
            Health-=(enemyattacklist[randint(0,2)])
        
       
        
           # run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            print("run")
          
        textSize(36)  
        fill(255)
        rect(10, 15, 205, 50)
        textSize(36) 
        fill(0)    
        text("Health: " + str(enemyHealth), 10, 57)
        
        
        fill(255)
        rect(380, 295, 215, 50)
        fill(0)
        text("Health: " + str(Health), 387, 340)
            
       
        
        # set's cha fuego's attacks in the boxes
        if cha == True:
        
               # scratch
            fill(255)
            rect(30, 510, 150, 50)
            fill(0)
            textSize(40)
            text("Scratch", 35, 550)
            scratch = 40
        
               # slash
            fill(255)
            rect(30, 450, 150, 50)
            fill(0)
            textSize(50)
            text("Slash", 43, 495)
            slash = 70
            
               #ember
            fill(255)
            rect(205, 450, 150, 50)
            fill(0)
            textSize(45)
            text("Ember", 212, 493)
            ember = 40
        
               # fire spin
            fill(255)
            rect(205, 510, 150, 50)
            fill(0)
            textSize(35)
            text("Fire Spin", 207, 550)
            firespin = 35
        
               # run
            fill(255)
            rect(410, 480, 140, 52)
            fill(0)
            textSize(50)
            text("Run", 432, 523)
            
            fill(255)
            rect(10, 15, 205, 50)
            textSize(36) 
            fill(0)
            textSize(36)
            text("Health: " + str(enemyHealth), 10, 57)
            
            
            fill(255)
            rect(380, 295, 215, 50)
            fill(0)
            text("Health: " + str(Health), 387, 340)
        
     
    # lil squirt attacks       
    if lil == True:
        img2 = loadImage("squback.png")
        image(img2, 100, 310, 160, 160)
        img = enemy
        image(img, 395, 115, 150, 150)
        
        
        fill(255)
        rect(10, 15, 205, 50)
        textSize(36) 
        fill(0)
        textSize(36)
        text("Health: " + str(enemyHealth), 10, 57)
        
        
        fill(255)
        rect(380, 295, 215, 50)
        fill(0)
        text("Health: " + str(Health), 387, 340)
        
        # img = loadImage("pika7.png")
        # image(img, 395, 115, 150, 150)
    
         
         
         # headbutt
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            print("headbutt")
            #bulbAttack = bulbHealth - 30
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
       
        
          # tail whip  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            print("tail whip")
            enemyHealth = enemyHealth - 35
            Health-=(enemyattacklist[randint(0,2)])
        
        
        
        # bubble
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            print("bubble")
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
    
       
        
          # water gun
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            print("water gun")
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
        
       
        
          #run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            print("run")
            
        # set's lil squirt's attacks in the boxes
        if lil == True:
            
               # headbutt
            fill(255)
            rect(30, 510, 150, 50)
            fill(0)
            textSize(32)
            text("Headbutt", 33, 550)
            headbutt = 10
            
               # tail whip
            fill(255)
            rect(30, 450, 150, 50)
            fill(0)
            textSize(33)
            text("Tail Whip", 32, 490)
            tailwhip = 35
        
               # bubble
            fill(255)
            rect(205, 450, 150, 50)
            fill(0)
            textSize(45)
            text("Bubble", 206, 494)
            bubble = 40
            
               # water gun
            fill(255)
            rect(205, 510, 150, 50)
            fill(0)
            textSize(29)
            text("Water Gun", 208, 550)
            watergun = 70
            
               # run
            fill(255)
            rect(410, 480, 140, 52)
            fill(0)
            textSize(52)
            text("Run", 435, 525)
print ("orange")

    



# def mouseClicked():
    
#     # BulbaTrap's Attacks
#     global growl, tackle, vinewhip, toxic
    
#     # Cha Fuego's Attacks
#     global scratch, slash, ember, firespin
    
#      # Lil Squirt's Attacks
#     global headbutt, tailwhip, bubble, watergun
    
#     # health bars
#     global bulbHealth, chaHealth, squHealth
    
#     global bulbNum, chaNum, sqNum
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
