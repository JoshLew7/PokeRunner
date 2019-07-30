import PokeStats

def setup():
    # BulbaTrap's Attacks
    global growl, tackle, vinewhip, toxic
    
    # Cha Fuego's Attacks
    global scratch, slash, ember, firespin
    
    # Lil Squirt's Attacks
    global headbutt, tailwhip, bubble, watergun
    
    # health bars
    global bulbHealth, chaHealth, squHealth
    
    # starter health
    global bulbNum, chaNum, sqNum
    
    global bulb, cha, lil
    
    # Characters
    bulb = False
    cha = True
    lil = False
   
     # Background
    size(600, 600)
    img = loadImage("battleScreen.png")
    image(img, 0, 0, 600, 600)
    
    
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
        
    
def draw():
    
      # BulbaTrap's Attacks
    global growl, tackle, vinewhip, toxic
    
    # Cha Fuego's Attacks
    global scratch, slash, ember, firespin
    
     # Lil Squirt's Attacks
    global headbutt, tailwhip, bubble, watergun
    
    # health bars
    global bulbHealth, chaHealth, squHealth
    
    global bulbNum, chaNum, sqNum
    
    # characters
    global bulb, cha, lil
   
    # text(enemyHealth, 
    
    # bulbaTrap's attacks
    if bulb == True:
        
        # growl
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            print("growl")
            
        
       
        
          # tackle  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            print("tackle")
        
       
        
          # vine whip
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            print("vine whip")
    
        
        
        # toxic
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            print("toxic")
        
        
        
        #run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            print("run")
     
     
    # cha fuego's attacks       
    if cha == True:
        
         
        # scratch
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            print("scratch")
            #bulbAttack = bulbHealth - 30
        
        
        # slash  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            print("slash")
        
        
        
        # ember
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            print("ember")
    
        
        
        # fire spin
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            print("fire spin")
        
       
        
          #run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            print("run")
     
     
    # lil squirt attacks       
    if lil == True:
         
         
         # headbutt
        if mousePressed and mouseX <= 190 and mouseX >= 40  and mouseY <= 540 and mouseY >= 490:
            print("headbutt")
            #bulbAttack = bulbHealth - 30
       
        
          # tail whip  
        if mousePressed and mouseX >= 30 and mouseX <= 180  and mouseY <= 490 and mouseY >= 50:
            print("tail whip")
        
        
        
        # bubble
        if mousePressed and mouseX <= 355 and mouseX >= 205 and mouseY >= 450 and mouseY <= 500:
            print("bubble")
    
       
        
          # water gun
        if mousePressed and mouseX >= 205 and mouseX <= 355 and mouseY >= 510 and mouseY <= 560:
            print("water gun")
        
       
        
          #run
        if mousePressed and mouseX >= 410 and mouseX <= 550 and mouseY >= 480 and mouseY <= 532:
            print("run")
        
    



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
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
