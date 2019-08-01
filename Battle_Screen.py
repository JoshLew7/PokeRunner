from random import  randint
import PokeSelection
import Adventure
import StartMenu

def setupScreen():    
    global growl, tackle, vinewhip, toxic
    global scratch, slash, ember, firespin
    global headbutt, tailwhip, bubble, watergun    
    
    global enemyHealth, Health
    global bulb, cha, lil
    global enemypicturelist, enemy
    
     # Background
    img = loadImage("BattleScreen.jpg")
    image(img, 0, 0, 600, 600)    
    
    enemypicturelist = [ 
    loadImage("1-Bulbasaur.png"), 
    loadImage("squirtle3.png"), 
    loadImage("charmandere3.png"), 
    loadImage("pika7.png")]

    enemyHealth = 500
    Health = 500 
    
    enemy = (enemypicturelist[randint(0,3)])
            
    # Characters
    if PokeSelection.pokemon == "bulbasaur":
        bulb = True
        Attack1 = "Tackle"
        Attack2 = "Vine Whip"
        Attack3 = "Growl"
        Attack4 = "Toxic"
        tackle = 40
        vinewhip = 40
        toxic = 50 
        growl = 25

    else:
        bulb = False        
    if PokeSelection.pokemon == "charmander":
        cha = True
        Attack1 = "Scratch"
        Attack2 = "Fire Spin"
        Attack3 = "Slash"
        Attack4 = "Ember"
        scratch = 40
        slash = 70
        ember = 40
        firespin = 35

    else:
        cha = False        
    if PokeSelection.pokemon == "squirtle":
        lil = True
        Attack1 = "Head Butt"
        Attack2 = "Water Gun"
        Attack3 = "Tail Whip"
        Attack4 = "Bubble"
        headbutt = 10
        tailwhip = 35
        bubble = 40
        watergun = 70

    else:
        lil = False

    #Attack and run setup
    fill(255)
    rect(30, 450, 150, 50)
    fill(0)
    textSize(25)
    text(Attack1, 40, 490)

    fill(255)
    rect(205, 450, 150, 50)
    fill(0)
    textSize(25)
    text(Attack2, 208, 487)
    
    fill(255)
    rect(205, 510, 150, 50)
    fill(0)
    textSize(25)
    text(Attack4, 225, 550)
    
    fill(255)
    rect(30, 510, 150, 50)
    fill(0)
    textSize(25)
    text(Attack3, 45, 550)
    
    fill(255)
    rect(410, 480, 140, 52)
    fill(0)
    textSize(30)
    text("Run", 435, 525) 

def setBattleState(state):
    global modeState
    modeState = state
        
def getModeState():
    return modeState 
    
def drawScreen():
    global enemyHealth, Health, enemyattacklist,enemypicturelist, enemy 
    global run    
               
    enemyattacklist=[70,60,10]
        
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
        
    if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
        run = True
        Adventure.setAdventureState(True)
        Adventure.setupScreen()
    
    
    # bulbaTrap's attacks
    if bulb == True:
        img2 = loadImage("gold-silver-back.png")
        image(img2, 95, 325, 120, 120)
        image(enemy, 395, 115, 150, 150)
    
        # growl
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            enemyHealth = enemyHealth - 25
            Health-=(enemyattacklist[randint(0,2)])

        #tackle  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            enemyHealth = enemyHealth - 30
            Health-=(enemyattacklist[randint(0,2)])
           
        # vine whip
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
       
        # toxic
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            enemyHealth = enemyHealth - 50
            Health-=(enemyattacklist[randint(0,2)])
     
      # cha fuego's attacks       
    if cha == True:
        image(enemy, 395, 115, 150, 150)
        img2 = loadImage("charback.png")
        image(img2, 100, 350, 100, 100)
         
           # scratch
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])

           # slash  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])

           # ember
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])

           # fire spin
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            enemyHealth = enemyHealth - 35
            Health-=(enemyattacklist[randint(0,2)])
     
    # lil squirt attacks       
    if lil == True:
        img2 = loadImage("squback.png")
        image(img2, 100, 310, 160, 160)
        image(enemy, 395, 115, 150, 150)
         
        # headbutt
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            enemyHealth = enemyHealth - 70
            Health-=(enemyattacklist[randint(0,2)])
       
        # tail whip  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            enemyHealth = enemyHealth - 35
            Health-=(enemyattacklist[randint(0,2)])
            
        # bubble
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])

        # water gun
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            enemyHealth = enemyHealth - 40
            Health-=(enemyattacklist[randint(0,2)])
   
#Update Health     
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
        
