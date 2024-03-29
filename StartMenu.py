# add_library('sound')
        
import Adventure
import PokeSelection
import PokeStats
import Battle_Screen

def setupScreen():
    rect(251,326,123,32)
    backgroundImg = loadImage("pokeground.jpg")
    pokehoodText = loadImage("gameText.png")
    startButton = loadImage("startText.png")
    image(backgroundImg,0,0)
    image(pokehoodText,50,10)
    image(startButton,247,320)
    fill(0)
    
def drawScreen():
    if mousePressed:
        if mouseX in range(253,375) and mouseY in range(324,364):
            setStartState(False)
            Adventure.setAdventureState(False)
            PokeSelection.setSelectionState(True)
            Battle_Screen.setBattleState(True)
            PokeSelection.setupScreen()


        
def setStartState(state):
    global modeState
    modeState = state
        
def getModeState():
    return modeState    

    
