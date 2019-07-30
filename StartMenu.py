add_library('sound')
add_library("sound")
        
import Adventure 
import PokeSelection

def setupScreen():
    global music
    size(600,600)
    backgroundImg = loadImage("pokeground.jpg")
    pokehoodText = loadImage("gameText.png")
    startButton = loadImage("startText.png")
    image(backgroundImg,0,0)
    image(pokehoodText,50,10)
    image(startButton,247,320)


    
def drawScreen():
    if mousePressed:
        setStartState(False)
        Adventure.setAdventureState(False)
        PokeSelection.setSelectionState(True)
        
def setStartState(state):
    global modeState
    modeState = state
        
def getModeState():
    print("Start State: " + str(modeState))
    return modeState    
