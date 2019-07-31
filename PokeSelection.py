import Adventure
import StartMenu
import PokeStats

cha = False
bulb = False
lil = False


def setupScreen():
    global sf
    backgroundImg = loadImage("starter.jpg")
    image(backgroundImg,0,0,600,600)
    
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
            
