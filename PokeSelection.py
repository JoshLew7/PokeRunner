import Adventure
import StartMenu
import PokeStats
import Battle_Screen

def setupScreen():
    global sf
    rect(55,232,112,132)
    rect(241,244,121,100)
    rect(426,227,138,134)

    background(0)
    fill(255)
    ellipse(300,300,200,200)
    noFill()
    backgroundImg = loadImage("pokeball.png")
    image(backgroundImg,0,0,600,600)
    starterText = loadImage("starterText.png")
    image(starterText,125,0)
    
    #Squirtle
    water = loadImage("squirtle3.png")
    image(water,25,200,150,200)
    lilS = loadImage("LilS.png")
    image(lilS,45,375)
    global Lil
    Lil = False
    
    #Bulbasuar
    blub = loadImage("bulb.png")
    image(blub,175,200,200,150)
    blubT = loadImage("BulbaT.png")
    image(blubT,238,365)
    global Bul
    Bul = False
    
    #Charmander
    fire = loadImage("char.png")
    image(fire,425,225,150,150)
    chaF = loadImage("ChaF.png")
    image(chaF,425,375)
    global Cha
    Cha = False
    
    
def setSelectionState(state):
    global modeState
    modeState = state
        
def getModeState():
    return modeState
    
def drawScreen():
    global pokemon
    if mousePressed:
        if mouseX in range(55,167) and mouseY in range(232,364):
            pokemon = "squirtle"
            Battle_Screen.lil = True
            setSelectionState(False)
            Adventure.setAdventureState(True)
            StartMenu.setStartState(False)
            Battle_Screen.setBattleState(False)
            Adventure.setupScreen()
            Lil = True

        if mouseX in range(241,362) and mouseY in range(244,344):
            pokemon = "bulbasaur"
            Battle_Screen.blub = True
            setSelectionState(False)
            Adventure.setAdventureState(True)
            StartMenu.setStartState(False)
            Battle_Screen.setBattleState(False)
            Adventure.setupScreen()
            Bul = True

        if mouseX in range(426,564) and mouseY in range(227,361):
            pokemon = "charmander"
            Battle_Screen.cha = True
            setSelectionState(False)
            Adventure.setAdventureState(True)
            StartMenu.setStartState(False)
            Battle_Screen.setBattleState(False)
            Adventure.setupScreen()
            Cha = True
            
