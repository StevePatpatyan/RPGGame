from graphics import*
from Person import*
#Start Screen:
win = GraphWin("RPG GAME",1000,500)
while (True):
        start = Rectangle(Point(100,100),Point(300,200))
        start.draw(win)
        startText = Text(Point(200,150),"START")
        startText.draw(win)
        close = Rectangle(Point(400,100),Point(600,200))
        close.draw(win)
        closeText = Text(Point(500,150),"EXIT")
        closeText.draw(win)
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
        #woodenSword = Image(Point(441,427),"WoodenSword.png")
        #woodenSword.draw(win)
        #woodenSword1 = Image(Point(559,427),"WoodenSword1.png")
        #woodenSword1.draw(win)
        hp1 = 100
        hp2 = 100
        turn = None
        #coin flip to determine who gets priority:
        coin = ["heads","tails"]
        coinText = Text(Point(500,50),"Pick a side.")
        coinText.draw(win)
        heads = Rectangle(Point(200,100),Point(400,200))
        heads.draw(win)
        tails = Rectangle(Point(600,100),Point(800,200))
        tails.draw(win)
        while (True):
                coinButton = win.getMouse()
                if (coinButton.getX()>=heads.getP1().getX() and coinButton.getX()<=heads.getP2().getX() and coinButton.getY()>=heads.getP1().getY() and coinButton.getY()<=heads.getP2().getY()):
                        pVal = 0
                        break
                elif (coinButton.getX()>=tails.getP1().getX() and coinButton.getX()<=tails.getP2().getX() and coinButton.getY()>=tails.getP1().getY() and coinButton.getY()<=tails.getP2().getY()):
                      pVal = 1
                      break
        prediction = coin[pVal]
        coinText.undraw()
        heads.undraw()
        tails.undraw()
        #Players choose their move:
        p1Fight = Rectangle(Point(100,100),Point(300,150))
        p1Fight.draw(win)
        p1FightText = Text(Point(200,125),"Attack")
        p1FightText.draw(win)
        p1Defend = Rectangle(Point(100,150),Point(300,200))
        p1Defend.draw(win)
        p1DefendText = Text(Point(200,175),"Deflect?")
        p1DefendText.draw(win)
        p1Status = ["fight","defend"]
        while (True):
                p1Button = win.getMouse()
                if (p1Button.getX()>=p1Fight.getP1().getX() and p1Button.getX()<=p1Fight.getP2().getX() and p1Button.getY()>=p1Fight.getP1().getY() and p1Button.getY()<=p1Fight.getP2().getY()):
                        p1sVal = 0
                        break
                elif (p1Button.getX()>=p1Defend.getP1().getX() and p1Button.getX()<=p1Defend.getP2().getX() and p1Button.getY()>=p1Defend.getP1().getY() and p1Button.getY()<=p1Defend.getP2().getY()):
                        p1sVal = 1
                        break
        p1FightDefend = p1Status[p1sVal]
        p2FightDefend = p2Status[p2SVal]
        p2Fight = Rectangle(Point(700,100),Point(900,150))
        p2Fight.draw(win)
        p2Defend = Rectangle(Point(700,150),Point(900,200))
        p2Defend.draw(win)
                
                
