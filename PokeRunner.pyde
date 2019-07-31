import Adventure
import PokeSelection
import PokeStats
import StartMenu
add_library("sound")


count = 0

def playMusic(bool):
    if bool == True:    
        sf.play()
    elif bool == False:
        sf.stop()
    else:
        pass
            

def setup():
    global sf
    size(600,600)
    Adventure.setAdventureState(False)
    StartMenu.setStartState(True)
    PokeSelection.setSelectionState(False)
    sf = SoundFile(this,"pokemusic.mp3")


def draw():
    global count
    if Adventure.getModeState() == True:
        while count < 1:
            count = 0    
            Adventure.setupScreen()
            count += 1
        Adventure.drawScreen()   
        playMusic(False)
    elif StartMenu.getModeState() == True:
        StartMenu.setupScreen()
        StartMenu.drawScreen()
        playMusic(False)

    elif PokeSelection.getModeState() == True:  
        PokeSelection.setupScreen()
        PokeSelection.drawScreen()
        playMusic(False)
    print("fish")


        
        
