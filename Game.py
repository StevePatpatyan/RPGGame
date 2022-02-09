from graphics import*
win = GraphWin("RPG GAME",1000,500)
start = Rectangle(Point(100,100),Point(300,200))
start.draw(win)
close = Rectangle(Point(400,100),Point(600,200))
close.draw(win)
#Start Screen:
while (True):    
        introButton = win.getMouse()
        if (introButton.getX()>=start.getP1().getX() and introButton.getX()<=start.getP2().getX() and introButton.getY()>=start.getP1().getY() and introButton.getY()<=start.getP2().getY()):
            print("ok!")
        elif (introButton.getX()>=close.getP1().getX() and introButton.getX()<=close.getP2().getX() and introButton.getY()>=close.getP1().getY() and introButton.getY()<=close.getP2().getY()):
            win.close()
            break


