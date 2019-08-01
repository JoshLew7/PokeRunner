time = 0

def startTimer():
    global time
    time = millis()
    
def timeElapse():
    global time
    return millis() - time
