from graphics import*
win = GraphWin("RPG GAME",1000,500)

while (True):
    while (True):    
        introButton = win.checkMouse()
        if (introButton!=None):
            break
