def setupScreen():
    global playerX,playerY
    global backgroundImg,character,sprite
    global frontFacing,backFacing,leftFacing,rightFacing
    global pokeBLX1,pokeBLY1,pokeBRX1,pokeBRY1,pokeTLX1,pokeTLY1,pokeTRX1,pokeTRY1
    global pokeBLX2,pokeBLY2,pokeBRX2,pokeBRY2,pokeTLX2,pokeTLY2,pokeTRX2,pokeTRY2
    
    playerX = 350
    playerY = 310
    #Bottom Left
    grassBLX = 86
    grassBLY = 461
    pokeBLX1 = int(random(90,235)) #X Location of pokemon in bottomLeft Grass 
    pokeBLY1 = int(random(465,521))#Y Location of pokemon in bottomLeft Grass 
    pokeBLX2 = int(random(90,235)) 
    pokeBLY2 = int(random(465,521))
    #Bottom Right
    grassBRX = 430
    grassBRY = 369
    pokeBRX1 = int(random(430,488))
    pokeBRY1 = int(random(369,521))
    pokeBRX2 = int(random(430,488))
    pokeBRY2 = int(random(369,521))
    #Top Right
    grassTRX = 430
    grassTRY = 187
    pokeTRX1 = int(random(430,488))
    pokeTRY1 = int(random(187,276))
    pokeTRX2 = int(random(430,488))
    pokeTRY2 = int(random(187,276))
    #Top Left 
    grassTLX = 10
    grassTLY = 96
    pokeTLX1 = int(random(10,126))
    pokeTLY1 = int(random(96,153))
    pokeTLX2 = int(random(10,126))
    pokeTLY2 = int(random(96,153))
    
    size(600,600)    
    backgroundImg = loadImage("Pokemap.png")
    frontFacing = loadImage("frontFacing.png")
    backFacing = loadImage("backFacing.png")
    leftFacing = loadImage("leftSideProfile.png")
    rightFacing = loadImage("rightSideProfile.png")
    sprite = frontFacing

    #Bottom Left Grass
    fill(255)
    rect(grassBLX,grassBLY,174,85)
    fill(255,0,0)
    rect(pokeBLX1,pokeBLY1,25,25)
    rect(pokeBLX2,pokeBLY2,25,25)

    
    #Bottom Right Grass
    fill(255)
    rect(grassBRX,grassBRY,83,177)
    fill(255,0,0)
    rect(pokeBRX1,pokeBRY1,25,25)
    rect(pokeBRX2,pokeBRY2,25,25)

    #Top Right Grass
    fill(255)
    rect(grassTRX,grassTRY,83,114)
    fill(255,0,0)
    rect(pokeTRX1,pokeTRY1,25,25)
    rect(pokeTRX2,pokeTRY2,25,25)
    
    #Top Left Grass
    fill(255)
    rect(grassTLX,grassTLY,141,82)
    fill(255,0,0)
    rect(pokeTLX1,pokeTLY1,25,25)
    rect(pokeTLX2,pokeTLY2,25,25)
    
    #Left River
    rect(0,312,328,38)
    
    #Right River
    rect(391,312,150,38)
    
    #Long River Trees
    rect(530,0,70,600)
    
    #Left Trees
    rect(0,312,32,288)

    #Bot Left Trees
    rect(0,550,328,50)
    
    #Bot Right Trees
    rect(398,550,133,50)
    
def setAdventureState(state):
    global modeState
    modeState = state
        
def getModeState():
    print("Adventure State: " + str(modeState))
    return modeState

    
def drawScreen():
    global backgroundImg,sprite
    global playerX,playerY
    global grassBLX,grassBLY,pokeBLX,pokeBLY
    global frontFacing,backFacing,leftFacing,rightFacing
    image(backgroundImg,0,0)
    image(sprite,playerX,playerY,25,25)
    playerMiddleX = playerX + 12
    playerMiddleY = playerY + 12

    if (keyPressed):
        if (key == 'w'):
            sprite = backFacing
            playerY -= 1
        elif(key == 's'):
            sprite = frontFacing
            playerY += 1
        elif(key == 'a'):
            sprite = leftFacing
            playerX -= 1
        elif(key == 'd'):
            sprite = rightFacing
            playerX += 1
    
    if playerX in range(pokeBLX1,pokeBLX1 + 25) and playerY in range(pokeBLY1,pokeBLY1 + 25) or playerX in range(pokeBLX2,pokeBLX2 + 25) and playerY in range(pokeBLY2,pokeBLY2 + 25) :
        print("detect bot left")

    elif playerX in range(pokeBRX1,pokeBRX1 + 25) and playerY in range(pokeBRY1,pokeBRY1 + 25) or playerX in range(pokeBRX2,pokeBRX2 + 25) and playerY in range(pokeBRY2,pokeBRY2 + 25):
        print("detect bot right")

    elif playerX in range(pokeTRX1,pokeTRX1 + 25) and playerY in range(pokeTRY1,pokeTRY1 + 25) or playerX in range(pokeTRX2,pokeTRX2 + 25) and playerY in range(pokeTRY2,pokeTRY2 + 25) :
        print("detect top right")

    elif playerX in range(pokeTLX1,pokeTLX1 + 25) and playerY in range(pokeTLY1,pokeTLY1 + 25) or playerX in range(pokeTLX2,pokeTLX2 + 25) and playerY in range(pokeTLY2,pokeTLY2 + 25) :
        print("detect top left")

        
        
    if playerX in range(0,328) and playerY in range(285,347): #Left River
        if playerY < 325:
            playerY = 284
        else:
            playerY = 348
    elif playerX in range(375,541) and playerY in range(285,347): #Right River
        if playerY < 325:
            playerY = 284
        else:
            playerY = 348
    elif playerX > 507: #Right Trees
        playerX = 506
    elif playerX < 28 and playerY in range(285,600):
        playerX = 29
    elif playerX in range(0,328) and playerY > 527:
        playerY = 526
    elif playerX in range(385,600) and playerY > 527:
        playerY = 526
