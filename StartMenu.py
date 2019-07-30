import Adventure
import PokeSelection

def setupScreen():
    background(0)
    # img=loadImage("lucario.jpeg")#bottom  right
    # image(img,300,300,300,300)
    loadPixels()
    updatePixels()
    
    img=loadImage("charzard.jpg")
    image(img,1,200,400,500)
    img=loadImage("fire2.jpg")
    image(img,240,260,111,111)
    loadPixels()
    updatePixels()

    textSize(90)
    fill(0,0,255)
    stroke(255)
    text ("POKEY'",20,100)
    
    fill(255,0,0)
    text ("HOOD",320,100)
    
    fill(255,0,0)
    rect(130,170,156,50)#white rectanglke around the story mode
    
    fill(0,0,255)
    textSize(25)
    text ("Story Mode",140,200)
    
    rect(330,170,160,50)#blue rect around battle mode
    fill(255,0,0)
    text ("Battle Mode", 340,201)
    
def setStartState(state):
    global modeState
    modeState = state
        
def getModeState():
    print("Start State: " + str(modeState))
    return modeState    

def drawScreen():
    if mousePressed and mouseX>130 and mouseX<290 and mouseY>170 and mouseY<220:
        print("pressed")
        setStartState(False)
        Adventure.setAdventureState(False)
        PokeSelection.setSelectionState(True)
        
    if mousePressed and mouseX>330 and mouseX<490 and mouseY>170 and mouseY<220:
        print("pressed")
        setStartState(False)
        Adventure.setAdventureState(False)
        PokeSelection.setSelectionState(True)
