from graphics import*
from Person import*
from random import*
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
        p1WeaponName = "WoodenSword.png"
        p2WeaponName = "WoodenSword1.png"
        p1Weapon = Image(Point(441,427),p1WeaponName)
        p1Weapon.draw(win)
        p2Weapon = Image(Point(559,427),p2WeaponName)
        p2Weapon.draw(win)
        player = ["Player 1","Player 2"]
        hp1 = 100
        hp2 = 100
        speed1 = 0
        speed2 = 0
        #coin flip to determine who gets priority:
        coin = ["heads","tails"]
        coinText = Text(Point(500,50),"Pick a side.")
        coinText.draw(win)
        heads = Rectangle(Point(200,100),Point(400,200))
        heads.draw(win)
        headsText = Text(Point(300,150),"HEADS")
        headsText.draw(win)
        tails = Rectangle(Point(600,100),Point(800,200))
        tails.draw(win)
        tailsText = Text(Point(700,150),"TAILS")
        tailsText.draw(win)
        while (True):
                coinButton = win.getMouse()
                if (coinButton.getX()>=heads.getP1().getX() and coinButton.getX()<=heads.getP2().getX() and coinButton.getY()>=heads.getP1().getY() and coinButton.getY()<=heads.getP2().getY()):
                        pVal = 0
                        break
                elif (coinButton.getX()>=tails.getP1().getX() and coinButton.getX()<=tails.getP2().getX() and coinButton.getY()>=tails.getP1().getY() and coinButton.getY()<=tails.getP2().getY()):
                      pVal = 1
                      break
        coinText.undraw()
        heads.undraw()
        tails.undraw()
        headsText.undraw()
        tailsText.undraw()
        prediction = coin[pVal]
        resultCoin = coin[randint(0,1)]
        if (prediction==resultCoin):
                speed1 = speed1+10
                playerTextVal = 0
        elif(prediction!=resultCoin):
                speed2 = speed2+10
                playerTextVal = 1
        resultText = Text(Point(500,50),"The result is "+resultCoin+"! "+player[playerTextVal]+" gets +10 speed.")
        resultText.draw(win)
        win.getMouse()
        resultText.undraw()
        status = ["fight","defend"]
        p1wVal = 0
        p2wVal = 0
        p1WMulti = 1
        p2WMulti = 1
        p1WeaponName = ["WoodenSword.png","StoneSword.png","IronSword.png","DiamondSword.png","Trident.png"]
        p2WeaponName = ["WoodenSword1.png","StoneSword1.png","IronSword1.png","DiamondSword1.png","Trident1.png"]
        #Players choose their move:
        while (hp1>0 and hp2>0):
                defDet1 = randint(0,1)
                defDet2 = randint(0,1)
                turn = None
                if (p1WeaponName[p1wVal] == "WoodenSword.png"):
                        p1WeaponDMG = 5
                elif (p1WeaponName[p1wVal] == "StoneSword.png"):
                        p1WeaponDMG = 10
                elif (p1WeaponName[p1wVal] == "IronSword.png"):
                        p1WeaponDMG = 20
                elif (p1WeaponName[p1wVal] == "DiamondSword.png"):
                        p1WeaponDMG = 40
                elif (p1WeaponName[p1wVal] == "Trident.png"):
                        p1WeaponDMG = 80
                p1Weapon.undraw()
                p2Weapon.undraw()
                p1Weapon.draw(win)
                p2Weapon.draw(win)
                p1Fight = Rectangle(Point(100,100),Point(300,150))
                p1Fight.draw(win)
                p1FightText = Text(Point(200,125),"Attack")
                p1FightText.draw(win)
                p1Defend = Rectangle(Point(100,160),Point(300,210))
                p1Defend.draw(win)
                p1DefendText = Text(Point(200,185),"Deflect?")
                p1DefendText.draw(win)
                while (True):
                        p1Button = win.getMouse()
                        if (p1Button.getX()>=p1Fight.getP1().getX() and p1Button.getX()<=p1Fight.getP2().getX() and p1Button.getY()>=p1Fight.getP1().getY() and p1Button.getY()<=p1Fight.getP2().getY()):
                                p1sVal = 0
                                break
                        elif (p1Button.getX()>=p1Defend.getP1().getX() and p1Button.getX()<=p1Defend.getP2().getX() and p1Button.getY()>=p1Defend.getP1().getY() and p1Button.getY()<=p1Defend.getP2().getY()):
                                p1sVal = 1
                                break
                p1Fight.undraw()
                p1FightText.undraw()
                p1Defend.undraw()
                p1DefendText.undraw()
                if (p2WeaponName[p2wVal] == "WoodenSword1.png"):
                        p2WeaponDMG = 5
                elif (p2WeaponName[p2wVal] == "StoneSword1.png"):
                        p2WeaponDMG = 10
                elif (p2WeaponName[p2wVal] == "IronSword1.png"):
                        p2WeaponDMG = 20
                elif (p2WeaponName[p2wVal] == "DiamondSword1.png"):
                        p2WeaponDMG = 40
                elif (p2WeaponName[p2wVal] == "Trident1.png"):
                        p2WeaponDMG = 80
                p2Fight = Rectangle(Point(700,100),Point(900,150))
                p2Fight.draw(win)
                p2FightText = Text(Point(800,125),"Attack")
                p2FightText.draw(win)
                p2Defend = Rectangle(Point(700,160),Point(900,210))
                p2Defend.draw(win)
                p2DefendText = Text(Point(800,185),"Deflect?")
                p2DefendText.draw(win)
                while (True):
                        p2Button = win.getMouse()
                        if (p2Button.getX()>=p2Fight.getP1().getX() and p2Button.getX()<=p2Fight.getP2().getX() and p2Button.getY()>=p2Fight.getP1().getY() and p2Button.getY()<=p2Fight.getP2().getY()):
                                p2sVal = 0
                                break
                        elif (p2Button.getX()>=p2Defend.getP1().getX() and p2Button.getX()<=p2Defend.getP2().getX() and p2Button.getY()>=p2Defend.getP1().getY() and p2Button.getY()<=p2Defend.getP2().getY()):
                                p2sVal = 1
                                break
                p2Fight.undraw()
                p2FightText.undraw()
                p2Defend.undraw()
                p2DefendText.undraw()
                
                #Moves begin:
                if (speed1>speed2):
                        if (status[p1sVal]=="fight"):
                                if (status[p2sVal]=="defend" and defDet2==0):
                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                elif (status[p2sVal]=="defend" and defDet2==1):
                                        #fail text.....
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                else:
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                elif (speed2>speed1):
                        if (status[p2sVal]=="fight"):
                                if (status[p1sVal]=="defend" and defDet1==0):
                                        hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                elif (status[p1sVal]=="defend" and defDet1==1):
                                        #fail text.....
                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                else:
                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                elif (speed1==speed2):
                        randomTurn = randint(0,1)
                        turn = player[randomTurn]
                        if (turn=="Player 1"):
                                if (status[p1sVal]=="fight"):
                                        if (status[p2sVal]=="defend" and defDet2==0):
                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                elif (status[p2sVal]=="defend" and defDet2==1):
                                        #fail text.....
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                else:
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                        elif (turn=="Player 2"):
                                if (status[p2sVal]=="fight"):
                                        if (status[p1sVal]=="defend" and defDet1==0):
                                        hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                elif (status[p1sVal]=="defend" and defDet1==1):
                                        #fail text.....
                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                else:
                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                if (speed1<speed2):
                        if (status[p1sVal]=="fight"):
                                if (status[p2sVal]=="defend" and defDet2==0):
                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                elif (status[p2sVal]=="defend" and defDet2==1):
                                        #fail text.....
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                else:
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                elif (speed2<speed1):
                        if (status[p2sVal]=="fight"):
                                if (status[p1sVal]=="defend" and defDet1==0):
                                        hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                elif (status[p1sVal]=="defend" and defDet1==1):
                                        #fail text.....
                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                else:
                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                elif (turn=="Player 2"):
                        if (status[p1sVal]=="fight"):
                                if (status[p2sVal]=="defend" and defDet2==0):
                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                elif (status[p2sVal]=="defend" and defDet2==1):
                                        #fail text.....
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                else:
                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                elif (turn=="Player 1"):
                        if (status[p2sVal]=="fight"):
                                if (status[p1sVal]=="defend" and defDet1==0):
                                        hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                elif (status[p1sVal]=="defend" and defDet1==1):
                                        #fail text.....
                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                else:
                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
