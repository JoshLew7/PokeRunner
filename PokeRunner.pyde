import Adventure
import PokeSelection
import PokeStats
import StartMenu
add_library("sound")


count = 0

def playMusic():
        sf = SoundFile(this,"pokemusic.mp3")
        sf.play()    

def setup():
    global sf
    size(600,600)
    Adventure.setAdventureState(False)
    StartMenu.setStartState(True)
    PokeSelection.setSelectionState(False)

def draw():
    global count
    if Adventure.getModeState() == True:
        while count < 1:
            count = 0    
            Adventure.setupScreen()
            count += 1
        Adventure.drawScreen()    
    elif StartMenu.getModeState() == True:
        StartMenu.setupScreen()
        StartMenu.drawScreen()
        playMusic()

    elif PokeSelection.getModeState() == True:  
        PokeSelection.setupScreen()
        PokeSelection.drawScreen()

        
        
