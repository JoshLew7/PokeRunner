import Adventure
import PokeSelection
import PokeStats
import StartMenu

count = 0

def setup():
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

    elif PokeSelection.getModeState() == True:  
        PokeSelection.setupScreen()
        PokeSelection.drawScreen()
        
        
