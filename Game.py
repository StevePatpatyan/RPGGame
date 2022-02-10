from graphics import*
from Person import*
#Start Screen:
win = GraphWin("RPG GAME",1000,500)
start = Rectangle(Point(100,100),Point(300,200))
start.draw(win)
startText = Text(Point(200,150),"START")
startText.draw(win)
close = Rectangle(Point(400,100),Point(600,200))
close.draw(win)
closeText = Text(Point(500,150),"EXIT")
closeText.draw(win)
while (True):
        while (True):
                introButton = win.getMouse()
                if (introButton.getX()>=start.getP1().getX() and introButton.getX()<=start.getP2().getX() and introButton.getY()>=start.getP1().getY() and introButton.getY()<=start.getP2().getY()):
                        start.undraw()
                        close.undraw()
                        startText.undraw()
                        closeText.undraw()
                        break
                elif (introButton.getX()>=close.getP1().getX() and introButton.getX()<=close.getP2().getX() and introButton.getY()>=close.getP1().getY() and introButton.getY()<=close.getP2().getY()):
                        win.close()
                        break
        p1 = Person(400,400,20,50,25,25,":|","|")
        p1.draw(win)
        p2 = Person(600,400,20,50,25,25,":|","/")
        p2.draw(win)
        woodenSword = Image(Point(441,427),"WoodenSword.png")
        woodenSword.draw(win)
        woodenSword1 = Image(Point(559,427),"WoodenSword1.png")
        woodenSword1.draw(win)
        hp1 = 100
        hp2 = 100
        turn = None
        coin = ["heads","tails"]
        coinText = Text(Point(500,100),"Pick a side.")
        #heads = Rectangle
        p1Fight = Rectangle(Point(100,100),Point(300,150))
        p1Fight.draw(win)
        p1Defend = Rectangle(Point(100,150),Point(300,200))
        p1Defend.draw(win)
        p2Fight = Rectangle(Point(700,100),Point(900,150))
        p2Fight.draw(win)
        p2Defend = Rectangle(Point(700,150),Point(900,200))
        p2Defend.draw(win)
                
                
