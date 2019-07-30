import Adventure
import StartMenu
import PokeStats

def setupScreen():
    global bulb, cha, lil
    size(600, 600)
    # img4 = loadImage("giphy.gif")
    # image(
    background(0)
    textSize(36)
    fill(255, 215, 0)
    text("Choose Your Gangsta", 105, 120)

    # BulbaTrap name
    textSize(30)
    fill(32, 178, 170)
    text("BulbaTrap", 25, 450)
    
    # Cha Fuego name
    fill(255, 140, 0)
    text("Cha Fuego", 225, 450)
    
    # Lil Squirt name
    fill(102, 215, 170)
    text("Lil Squirt", 435, 450)
    
    # BulbaTrap img
    fill(32, 178, 170)
    rect(20, 250, 160, 150)
    img = loadImage("1-Bulbasaur.png")
    image(img, 25, 250, 150, 150)
    
    # Cha Fuego img
    fill(255, 140, 0)
    rect(225, 250, 155, 150)
    img2 = loadImage("charmandere3.png")
    image(img2, 230, 250, 150, 150)
    
    # Lil Squirt img
    fill(102, 215, 170)
    rect(431, 250, 155, 150)
    img3 = loadImage("squirtle3.png")
    image(img3, 435, 250, 150, 150)
    
    bulb = False
    cha = False
    lil = False
    
def setSelectionState(state):
    global modeState
    modeState = state
        
def getModeState():
    print("Selection State: " + str(modeState))
    return modeState
    
def drawScreen():
    global bulb, cha, lil
    #  Select BulbaTrap
    if mousePressed and mouseX>20 and mouseX<180 and mouseY>250 and mouseY<400:
        print("bulb")
        bulb = True
        if bulb == True:
            setSelectionState(False)
            Adventure.setAdventureState(True)
            StartMenu.setStartState(False)
        
    
    # Select Cha Fuego
    if mousePressed and mouseX>225 and mouseX<380 and mouseY>250 and mouseY<400:
        print("char")
        if cha == True:
            setSelectionState(False)
            Adventure.setAdventureState(True)
            StartMenu.setStartState(False)
        
    
    
    # Select Lil Squirt
    if mousePressed and mouseX>435 and mouseX<585 and mouseY>250 and mouseY<400:
        print("lil")
        if lil == True:
            setSelectionState(False)
            Adventure.setAdventureState(True)
            StartMenu.setStartState(False)
            
