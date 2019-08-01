from random import  randint
import PokeSelection
import Adventure
import StartMenu
import timer

def setupScreen():    
    global growl, tackle, vinewhip, toxic
    global scratch, slash, ember, firespin
    global headbutt, tailwhip, bubble, watergun    
    global HealthBoxY,HealthBoxB,health
    
    global enemyHealth, Health
    global bulb, cha, lil
    global enemypicturelist, enemy, playersTurn
    
     # Background
    img = loadImage("BattleScreen.jpg")
    image(img, 0, 0, 600, 600)    
    battleBox = loadImage("battleBox.png")
    run = loadImage("Run.png")
    HealthBoxB = loadImage("HealthBoxB.png")
    HealthBoxY = loadImage("HealthBoxY.png")
    health = loadImage("HealthW.png")
        
    enemypicturelist = [ 
    loadImage("1-Bulbasaur.png"), 
    loadImage("squirtle3.png"), 
    loadImage("charmandere3.png"), 
    loadImage("pika7.png")]

    enemyHealth = 500
    Health = 500 
    
    playersTurn = True
    
    enemy = (enemypicturelist[randint(0,3)])
            
    # Characters
    if PokeSelection.pokemon == "bulbasaur":
        bulb = True
        Attack1 = loadImage("TackleMove.png")
        Attack2 = loadImage("Vine-Whip.png")
        Attack3 = loadImage("Growl.png")
        Attack4 = loadImage("Toxic.png")
        tackle = 40
        vinewhip = 40
        toxic = 50 
        growl = 25

    else:
        bulb = False        
    if PokeSelection.pokemon == "charmander":
        cha = True
        Attack1 = loadImage("Scratch.png")
        Attack2 = loadImage("Fire-Spin.png")
        Attack3 = loadImage("Slash.png")
        Attack4 = loadImage("Ember.png")
        scratch = 40
        slash = 70
        ember = 40
        firespin = 35

    else:
        cha = False        
    if PokeSelection.pokemon == "squirtle":
        lil = True
        Attack1 = loadImage("Head-Butt.png")
        Attack2 = loadImage("Water-Gun.png")
        Attack3 = loadImage("Tail-Whip.png")
        Attack4 = loadImage("Bubble.png")
        headbutt = 10
        tailwhip = 35
        bubble = 40
        watergun = 70

    else:
        lil = False

    #Attack and run setup
    image(battleBox,30,450,150,50)
    image(Attack1,45,453)

    image(battleBox,205,450,150,50)
    image(Attack2,220,453)

    fill(255)
    # rect(205, 510, 150, 50)
    image(battleBox,205,510,150,50)
    image(Attack4,225,512)
    
    fill(255)
    image(battleBox,30,510,150,50)
    image(Attack3,45,512)

    
    fill(255)
    # rect(410, 480, 140, 52)
    image(battleBox,410,480,150,50)
    image(run,435,481)

def setBattleState(state):
    global modeState
    modeState = state
        
def getModeState():
    return modeState 
    
def drawScreen():
    global HealthBoxY,HealthBoxB,health
    global enemyHealth, Health, enemyattacklist,enemypicturelist, enemy 
    global run, playersTurn   
               
    enemyattacklist=[70,60,10]
    
    if timer.timeElapse() > 950:
        playersTurn = True
        
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
        if mousePressed and playersTurn == True and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            enemyHealth = enemyHealth - 25
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])

        #tackle  
        if mousePressed and playersTurn == True and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            enemyHealth = enemyHealth - 30
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
           
        # vine whip
        if mousePressed and playersTurn == True and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            enemyHealth = enemyHealth - 70
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
       
        # toxic
        if mousePressed and playersTurn == True and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            enemyHealth = enemyHealth - 50
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
     
      # cha fuego's attacks       
    if cha == True:
        image(enemy, 395, 115, 150, 150)
        img2 = loadImage("charback.png")
        image(img2, 100, 350, 100, 100)
         
           # scratch
        if mousePressed and playersTurn == True and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            enemyHealth = enemyHealth - 40
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])

           # slash  
        if mousePressed and playersTurn == True and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            enemyHealth = enemyHealth - 70
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])

           # ember
        if mousePressed and playersTurn == True and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            enemyHealth = enemyHealth - 40
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])

           # fire spin
        if mousePressed and playersTurn == True and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            enemyHealth = enemyHealth - 35
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
     
    # lil squirt attacks       
    if lil == True:
        img2 = loadImage("squback.png")
        image(img2, 100, 310, 160, 160)
        image(enemy, 395, 115, 150, 150)
         
        # headbutt
        if mousePressed and playersTurn == True and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            enemyHealth = enemyHealth - 70
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
       
        # tail whip  
        if mousePressed and playersTurn == True and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            enemyHealth = enemyHealth - 35
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
            
        # bubble
        if mousePressed and playersTurn == True and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            enemyHealth = enemyHealth - 40
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])

        # water gun
        if mousePressed and playersTurn == True and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            enemyHealth = enemyHealth - 40
            playersTurn = False
            
            timer.startTimer()
            Health-=(enemyattacklist[randint(0,2)])
   
#Update Health     
    # fill(255)
    # rect(10, 15, 205, 50)
    # textSize(36) 
    # fill(0)
    textSize(20)
    image(HealthBoxY,10,25,205,50)
    image(health,25,35)
    stroke(0)
    fill(0)
    text(enemyHealth, 110, 56)
    
    image(HealthBoxY,380,305,205,50)
    image(health,395,315)
    text(Health, 480, 335)
        
