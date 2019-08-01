# import PokeStats
import PokeSelection
import Adventure
import StartMenu

def setupScreen():
    from random import  randint
    
    # BulbaTrap's Attacks
    global growl, tackle, vinewhip, toxic
    
    # Cha Fuego's Attacks
    global scratch, slash, ember, firespin
    
    # Lil Squirt's Attacks
    global headbutt, tailwhip, bubble, watergun
    
    # health bars
    global enemyHealth, Health

    global bulb, cha, lil
    
    global enemypicturelist, enemy
    
    global run
    
    global setAdventureState
    
    def setAdventureState(state):
        global modeState
        modeState = state
        
    def getModeState():
        return modeState
    
    # def setAdventureState(state):
    #     global modeState
    #     modeState = state
        
    
    setAdventureState = False
    
    # Characters
    if PokeSelection.pokemon == "bulbasaur":
        bulb = True
        # print("bulb")
    else:
        bulb = False
        # print("no bulb")
        
    if PokeSelection.pokemon == "charmander":
        cha = True
        # print("cha")
    else:
        cha = False
        # print("no cha")
        
    if PokeSelection.pokemon == "squirtle":
        lil = True
        # print("lil")
    else:
        lil = False
        # print("no lil")
   
     # Background
    img = loadImage("BattleScreen.jpg")
    image(img, 0, 0, 600, 600)
    
    enemyHealth = 500
    Health = 500        
    
    enemypicturelist = [ loadImage("1-Bulbasaur.png"), loadImage("squirtle3.png"), 
                loadImage("charmandere3.png"), loadImage("pika7.png")]
    
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


def setBattleState(state):
    global modeState
    modeState = state
        
def getModeState():
    return modeState 
    
def drawScreen():
    from random import  randint
    global Health,enemyHealth
    
    img = loadImage("BattleScreen.jpg")
    image(img, 0, 0, 600, 600)
    
    if enemyHealth <= 0:
        Adventure.setupScreen()
        StartMenu.setStartState(False)
        PokeSelection.setSelectionState(False)
        setBattleState(False)
        Adventure.setAdventureState(True) 
                    
    if Health <= 0:
        StartMenu.setupScreen()
        StartMenu.setStartState(True)
        PokeSelection.setSelectionState(False)
        setBattleState(False)
        Adventure.setAdventureState(False)
    

    
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
    
    global setAdventureState
    
    # def setAdventureState(state):
    #     global modeState
    #     modeState = state
        
    
   

    enemyattacklist=[70,60,10]
    


    
    # bulbaTrap's attacks
    if bulb == True:
        
        #(enemypicturelist[randint(0,2)])
        img2 = loadImage("gold-silver-back.png")
        image(img2, 95, 325, 120, 120)
    
        # img = enemy
        image(enemy, 395, 115, 150, 150)
    
        # growl
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            # print("growl")
            enemyHealth = enemyHealth - 25
            Health-=(enemyattacklist[randint(0,2)])

            #tackle  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            # print("tackle")
            enemyHealth = enemyHealth - 30
            Health-=(enemyattacklist[randint(0,2)])
            print(enemyHealth)
           
            # vine whip
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            # print("vine whip")
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
            # if Health <= 0:
            #     StartMenu.setStartState(True)
        # if  <= 0:
        #     Adventure.setupScreen()
        #     Adventure.setAdventureState(True)
            
        # if Health <= 0:
        #     StartMenu.setStartState(True)
            
            
        

                
            # toxic
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            # print("toxic")
            enemyHealth = enemyHealth - 50
            Health-=(enemyattacklist[randint(0,2)])
        
        # if Health <= 0:
        #      StartMenu.setStartState(True)
            
        # if enemyHealth <= 0:
        #     StartMenu.setStartState(True)
        
       
            
            
            # enemyattacklist=[90,80,40]
            
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
            # print("run")
            run = True
            Adventure.setAdventureState(True)
            Adventure.setupScreen()
            
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
            

        
     
     
      # cha fuego's attacks       
    if cha == True:
        # img = enemy
        image(enemy, 395, 115, 150, 150)
        img2 = loadImage("charback.png")
        image(img2, 100, 350, 100, 100)
        
         
           # scratch
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            # print("scratch")
            #bulbAttack = bulbHealth - 30
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
        
        
           # slash  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            # print("slash")
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
        
        
        
           # ember
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            # print("ember")
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
    
        
        
           # fire spin
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            # print("fire spin")
            enemyHealth = enemyHealth - 35
            Health-=(enemyattacklist[randint(0,2)])
    
        
           # run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            # print("run")
            run = True
            Adventure.setAdventureState(True)
            Adventure.setupScreen()
          
        # if enemyHealth <= 0:
        #     Adventure.setupScreen()
        #     Adventure.setAdventureState(True)
        
        # if Health <= 0:
        #     StartMenu.setStartState(True)
            
            
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
        # img = enemy
        image(enemy, 395, 115, 150, 150)
        
        
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
   
         
         
         # headbutt
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            # print("headbutt")
            #bulbAttack = bulbHealth - 30
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
       
        
          # tail whip  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            # print("tail whip")
            enemyHealth = enemyHealth - 35
            Health-=(enemyattacklist[randint(0,2)])
        
        
        
        # bubble
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            # print("bubble")
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
    
       
        
          # water gun
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            # print("water gun")
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
        
       
        
          #run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            # print("run")
            run = True
            Adventure.setAdventureState(True)
            Adventure.setupScreen()
            
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
            
