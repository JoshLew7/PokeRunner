import Adventure
import PokeSelection
import PokeStats
import StartMenu
import Battle_Screen
add_library("sound")

def setup():
    global sf
    size(600,600)
    Adventure.setAdventureState(False)
    StartMenu.setStartState(True)
    PokeSelection.setSelectionState(False)
    Battle_Screen.setBattleState(False)
    sf = SoundFile(this,"pokemusic.mp3")
    StartMenu.setupScreen()

    
def draw():
    if Adventure.getModeState() == True:
        Adventure.drawScreen()  
    elif StartMenu.getModeState() == True:
        StartMenu.drawScreen()
    elif PokeSelection.getModeState() == True:  
        PokeSelection.drawScreen()
    elif Battle_Screen.getModeState() == True:
        Battle_Screen.drawScreen()
    

        
        
