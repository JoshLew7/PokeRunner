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
    StartMenu.setupScreen()
    sf = SoundFile(this,"pokemusic.mp3")


def playMusic(bool):
    if bool == True:
        sf.play()
    elif bool == False:
        sf.stop()
        sf.pause()
    else:
        pass

    
def draw():
    if Adventure.getModeState() == True:
        Adventure.drawScreen()  
        # playMusic(False)
    elif StartMenu.getModeState() == True:
        StartMenu.drawScreen()
        # playMusic(False)
    elif PokeSelection.getModeState() == True:  
        PokeSelection.drawScreen()
        # playMusic(False)
    elif Battle_Screen.getModeState() == True:
        Battle_Screen.drawScreen()
        # playMusic(False)

        
    

        
        
