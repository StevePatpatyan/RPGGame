from graphics import*
from Person import*
from random import*
#import playsound
#Start Screen:
win = GraphWin("RPG GAME",1000,500)
win.setBackground("black")
while (True):
        win.setBackground("gray")
        start = Rectangle(Point(200,100),Point(400,200))
        start.setFill("light green")
        start.draw(win)
        startText = Text(Point(300,150),"START")
        startText.draw(win)
        close = Rectangle(Point(500,100),Point(700,200))
        close.setFill("red")
        close.draw(win)
        closeText = Text(Point(600,150),"EXIT")
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
        #Sign in/log in
        signIn = Rectangle(Point(400,100),Point(600,200))
        signInText = Text(Point(500,150),"Register Username")
        logIn = Rectangle(Point(400,225),Point(600,325))
        logInText = Text(Point(500,275),"Log In As Existing User")
        signIn.draw(win)
        signInText.draw(win)
        logIn.draw(win)
        logInText.draw(win)
        while (True):
                logButton = win.getMouse()
                if (logButton.getX()>=signIn.getP1().getX() and logButton.getX()<=signIn.getP2().getX() and logButton.getY()>=signIn.getP1().getY() and logButton.getY()<=signIn.getP2().getY()):
                        logVal = 0
                        break
                elif (logButton.getX()>=logIn.getP1().getX() and logButton.getX()<=logIn.getP2().getX() and logButton.getY()>=logIn.getP1().getY() and logButton.getY()<=logIn.getP2().getY()):
                        logVal = 1
                        break
        signIn.undraw()
        signInText.undraw()
        logIn.undraw()
        logInText.undraw()
        logTextStatus = ["Register As A New Player:","Log In As Existing User:"]
        logText = Text(Point(500,50),logTextStatus[logVal])
        userEnter = Entry(Point(500,200),50)
        userEnterText = Text(Point(500,175),"Username:")
        passEnter = Entry(Point(500,300),50)
        passEnterText = Text(Point(500,275),"Password:")
        logText.draw(win)
        userEnter.draw(win)
        userEnterText.draw(win)
        passEnter.draw(win)
        passEnterText.draw(win)
        while (True):
                userButton = win.getMouse()
        p1 = Person(400,400,20,50,25,25,":|","|")
        p1.draw(win)
        p2 = Person(600,400,20,50,25,25,":|","/")
        p2.draw(win)
        p1WeaponName = "WoodenSword.png"
        p2WeaponName = "WoodenSword1.png"
        #p1ArmorName = "Leather.png"
        p1Weapon = Image(Point(441,427),p1WeaponName)
        p1Weapon.draw(win)
        #p1Armor = Image(Point(420,427),p1ArmorName)
        #p1Armor.draw(win)
        p2Weapon = Image(Point(559,427),p2WeaponName)
        p2Weapon.draw(win)
        player = ["Player 1","Player 2"]
        hp1 = float(100)
        hp2 = float(100)
        hp1Full = hp1
        hp2Full = hp2
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
        status = ["fight","defend","speed","weapon","armor"]
        p1wVal = 0
        p2wVal = 0
        p1aVal = 0
        p2aVal = 0
        p1WMulti = 1
        p2WMulti = 1
        p1wCharge = 0
        p2wCharge = 0
        p1aCharge = 0
        p2aCharge = 0
        #Players choose abilities:
        powerStatus = ["hp","attack","deflect"]
        powerText = Text(Point(500,50),"Player 1, choose your power.")
        hpPower = Rectangle(Point(400,75),Point(600,125))
        attkPower = Rectangle(Point(400,150),Point(600,200))
        deflPower = Rectangle(Point(400,225),Point(600,275))
        hpPowerText = Text(Point(500,100),"HP Boost + 50")
        attkPowerText = Text(Point(500,175),"Power Boost x1.5")
        deflPowerText = Text(Point(500,250),"Deflect Chance Up")
        powerText.draw(win)
        hpPower.draw(win)
        attkPower.draw(win)
        deflPower.draw(win)
        hpPowerText.draw(win)
        attkPowerText.draw(win)
        deflPowerText.draw(win)
        while (True):
                p1Button = win.getMouse()
                if (p1Button.getX()>=hpPower.getP1().getX() and p1Button.getX()<=hpPower.getP2().getX() and p1Button.getY()>=hpPower.getP1().getY() and p1Button.getY()<=hpPower.getP2().getY()):
                        p1aVal = 0
                        break
                elif (p1Button.getX()>=attkPower.getP1().getX() and p1Button.getX()<=attkPower.getP2().getX() and p1Button.getY()>=attkPower.getP1().getY() and p1Button.getY()<=attkPower.getP2().getY()):
                        p1aVal = 1
                        break
                elif (p1Button.getX()>=deflPower.getP1().getX() and p1Button.getX()<=deflPower.getP2().getX() and p1Button.getY()>=deflPower.getP1().getY() and p1Button.getY()<=deflPower.getP2().getY()):
                        p1aVal = 2
                        break
        powerText.undraw()
        hpPower.undraw()
        attkPower.undraw()
        deflPower.undraw()
        hpPowerText.undraw()
        attkPowerText.undraw()
        deflPowerText.undraw()
        time.sleep(0.5)
        powerText = powerText = Text(Point(500,50),"Player 2, choose your power.")
        powerText.draw(win)
        hpPower.draw(win)
        attkPower.draw(win)
        deflPower.draw(win)
        hpPowerText.draw(win)
        attkPowerText.draw(win)
        deflPowerText.draw(win)
        while (True):
                p2Button = win.getMouse()
                if (p2Button.getX()>=hpPower.getP1().getX() and p2Button.getX()<=hpPower.getP2().getX() and p2Button.getY()>=hpPower.getP1().getY() and p2Button.getY()<=hpPower.getP2().getY()):
                        p2aVal = 0
                        break
                elif (p2Button.getX()>=attkPower.getP1().getX() and p2Button.getX()<=attkPower.getP2().getX() and p2Button.getY()>=attkPower.getP1().getY() and p2Button.getY()<=attkPower.getP2().getY()):
                        p2aVal = 1
                        break
                elif (p2Button.getX()>=deflPower.getP1().getX() and p2Button.getX()<=deflPower.getP2().getX() and p2Button.getY()>=deflPower.getP1().getY() and p2Button.getY()<=deflPower.getP2().getY()):
                        p2aVal = 2
                        break
        powerText.undraw()
        hpPower.undraw()
        attkPower.undraw()
        deflPower.undraw()
        hpPowerText.undraw()
        attkPowerText.undraw()
        deflPowerText.undraw()
        if (powerStatus[p1aVal] == "hp"):
                hp1 = float(150)
                hp1Full = hp1
        elif (powerStatus[p1aVal] == "attack"):
                p1WMulti = 1.5
        if (powerStatus[p2aVal] == "hp"):
                hp2 = float(150)
                hp2Full = hp2
        elif (powerStatus[p2aVal] == "attack"):
                p2WMulti = 1.5
        p1WeaponName = ["WoodenSword.png","StoneSword.png","IronSword.png","DiamondSword.png","Trident.png"]
        p2WeaponName = ["WoodenSword1.png","StoneSword1.png","IronSword1.png","DiamondSword1.png","Trident1.png"]
        #p1ArmorName = ["Leather.png"]
        hp1Text = Text(Point(50,425),"HP: "+str(hp1))
        if (hp1<=0):
                hp1BarFilled = Rectangle(Point(5,450),Point(5,475))
        else:
                hp1BarFilled = Rectangle(Point(5,450),Point(5+(50*(hp1/hp1Full)),475))
        if (hp1/hp1Full<=0.2):
                hp1BarFilled.setFill("red")
        else:
                hp1BarFilled.setFill("light green")
        hp1BarEmpty = Rectangle(Point(5,450),Point(55,475))
        hp2Text = Text(Point(950,425),"HP: "+str(hp2))
        if (hp2<=0):
                hp2BarFilled = Rectangle(Point(945,450),Point(945,475))
        else:
                hp2BarFilled = Rectangle(Point(945,450),Point(945+(50*(hp2/hp2Full)),475))
        if (hp2/hp2Full<=0.2):
                hp2BarFilled.setFill("red")
        else:
                hp2BarFilled.setFill("light green")
        hp2BarEmpty = Rectangle(Point(945,450),Point(995,475))
        hp1Text.draw(win)
        hp1BarFilled.draw(win)
        hp1BarEmpty.draw(win)
        hp2Text.draw(win)
        hp2BarFilled.draw(win)
        hp2BarEmpty.draw(win)
        #Players choose their move:
        while (hp1>0 and hp2>0):
                if (powerStatus[p1aVal]=="deflect"):
                        defDet1 = randint(0,2)
                else:
                        defDet1 = randint(0,1)
                if (powerStatus[p2aVal]=="deflect"):
                        defDet2 = randint(0,2)
                else:
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
                p1SpeedUp = Rectangle(Point(100,220),Point(300,270))
                p1SpeedUp.draw(win)
                p1SpeedUpText = Text(Point(200,245),"Speed Up")
                p1SpeedUpText.draw(win)
                p1WeaponUp = Rectangle(Point(100,280),Point(300,330))
                p1WeaponUp.draw(win)
                p1WeaponUpText = Text(Point(200,305),"Upgrade Weapon")
                p1WeaponUpText.draw(win)
                while (p1wCharge==0):
                        p1Button = win.getMouse()
                        if (p1Button.getX()>=p1Fight.getP1().getX() and p1Button.getX()<=p1Fight.getP2().getX() and p1Button.getY()>=p1Fight.getP1().getY() and p1Button.getY()<=p1Fight.getP2().getY()):
                                p1sVal = 0
                                break
                        elif (p1Button.getX()>=p1Defend.getP1().getX() and p1Button.getX()<=p1Defend.getP2().getX() and p1Button.getY()>=p1Defend.getP1().getY() and p1Button.getY()<=p1Defend.getP2().getY()):
                                p1sVal = 1
                                break
                        elif (p1Button.getX()>=p1SpeedUp.getP1().getX() and p1Button.getX()<=p1SpeedUp.getP2().getX() and p1Button.getY()>=p1SpeedUp.getP1().getY() and p1Button.getY()<=p1SpeedUp.getP2().getY()):
                                p1sVal = 2
                                break
                        elif (p1Button.getX()>=p1WeaponUp.getP1().getX() and p1Button.getX()<=p1WeaponUp.getP2().getX() and p1Button.getY()>=p1WeaponUp.getP1().getY() and p1Button.getY()<=p1WeaponUp.getP2().getY()):
                                p1sVal = 3
                                break
                p1Fight.undraw()
                p1FightText.undraw()
                p1Defend.undraw()
                p1DefendText.undraw()
                p1SpeedUp.undraw()
                p1SpeedUpText.undraw()
                p1WeaponUp.undraw()
                p1WeaponUpText.undraw()
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
                p2SpeedUp = Rectangle(Point(700,220),Point(900,270))
                p2SpeedUp.draw(win)
                p2SpeedUpText = Text(Point(800,245),"Speed Up")
                p2SpeedUpText.draw(win)
                p2WeaponUp = Rectangle(Point(700,280),Point(900,330))
                p2WeaponUp.draw(win)
                p2WeaponUpText = Text(Point(800,305),"Upgrade Weapon")
                p2WeaponUpText.draw(win)
                while (p2wCharge==0):
                        p2Button = win.getMouse()
                        if (p2Button.getX()>=p2Fight.getP1().getX() and p2Button.getX()<=p2Fight.getP2().getX() and p2Button.getY()>=p2Fight.getP1().getY() and p2Button.getY()<=p2Fight.getP2().getY()):
                                p2sVal = 0
                                break
                        elif (p2Button.getX()>=p2Defend.getP1().getX() and p2Button.getX()<=p2Defend.getP2().getX() and p2Button.getY()>=p2Defend.getP1().getY() and p2Button.getY()<=p2Defend.getP2().getY()):
                                p2sVal = 1
                                break
                        elif (p2Button.getX()>=p2SpeedUp.getP1().getX() and p2Button.getX()<=p2SpeedUp.getP2().getX() and p2Button.getY()>=p2SpeedUp.getP1().getY() and p2Button.getY()<=p2SpeedUp.getP2().getY()):
                                p2sVal = 2
                                break
                        elif (p2Button.getX()>=p2WeaponUp.getP1().getX() and p2Button.getX()<=p2WeaponUp.getP2().getX() and p2Button.getY()>=p2WeaponUp.getP1().getY() and p2Button.getY()<=p2WeaponUp.getP2().getY()):
                                p2sVal = 3
                                break
                p2Fight.undraw()
                p2FightText.undraw()
                p2Defend.undraw()
                p2DefendText.undraw()
                p2SpeedUp.undraw()
                p2SpeedUpText.undraw()
                p2WeaponUp.undraw()
                p2WeaponUpText.undraw()
                #Moves begin:
                if (speed1>speed2):
                        if (p1wCharge==0):
                                if (status[p1sVal]=="fight"):
                                        if (status[p2sVal]=="defend" and defDet2==0 or status[p2sVal]=="defend" and defDet2==2):
                                                moveText = Text(Point(500,50),"Player 1's attack was deflected back!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                        elif (status[p2sVal]=="defend" and defDet2==1):
                                                failText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                failText.draw(win)
                                                win.getMouse()
                                                failText.undraw()
                                                moveText = Text(Point(500,50),"Player 1 attacked!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                        else:
                                                moveText = Text(Point(500,50),"Player 1 attacked!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                elif (status[p1sVal]=="defend"):
                                        if (status[p2sVal]=="speed" or status[p1sVal]=="weapon"):
                                                moveText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"...")
                                                moveText.draw(win)  
                                elif (status[p1sVal]=="speed"):
                                        moveText = Text(Point(500,50),"Player 1 increased their speed by 5!")
                                        moveText.draw(win)
                                        speed1 = speed1+5
                                elif(status[p1sVal]=="weapon"):
                                        if (p1wVal==4):
                                                moveText = Text(Point(500,50),"Player 1 is already max power!")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"Player 1 started charging their weapon!")
                                                moveText.draw(win)
                                                p1wCharge = 1
                        else:
                                moveText = Text(Point(500,50),"Player 1 is charging their weapon...")
                                moveText.draw(win)
                elif (speed2>speed1):
                        if (p2wCharge==0):
                                if (status[p2sVal]=="fight"):
                                        if (status[p1sVal]=="defend" and defDet1==0 or status[p2sVal]=="defend" and defDet1==2):
                                                 moveText = Text(Point(500,50),"Player 2's attack was deflected back!")
                                                 moveText.draw(win)
                                                 hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                        elif (status[p1sVal]=="defend" and defDet1==1):
                                                failText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                failText.draw(win)
                                                win.getMouse()
                                                failText.undraw()
                                                moveText = Text(Point(500,50),"Player 2 attacked!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                        else:
                                                moveText = Text(Point(500,50),"Player 2 attacked!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                elif (status[p2sVal]=="defend"):
                                        if (status[p1sVal]=="speed" or status[p1sVal]=="weapon"):
                                                moveText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"...")
                                                moveText.draw(win)
                                elif (status[p2sVal]=="speed"):
                                        moveText = Text(Point(500,50),"Player 2 increased their speed by 5!")
                                        moveText.draw(win)
                                        speed2 = speed2+5
                                elif(status[p2sVal]=="weapon"):
                                        if (p2wVal==4):
                                                moveText = Text(Point(500,50),"Player 2 is already max power!")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"Player 2 started charging their weapon!")
                                                moveText.draw(win)
                                                p2wCharge = 1
                        else:
                                moveText = Text(Point(500,50),"Player 2 is charging their weapon...")
                                moveText.draw(win)
                elif (speed1==speed2):
                        randomTurn = randint(0,1)
                        turn = player[randomTurn]
                        if (turn=="Player 1"):
                                if (p1wCharge==0):
                                        if (status[p1sVal]=="fight"):
                                                if (status[p2sVal]=="defend" and defDet2==0 or status[p2sVal]=="defend" and defDet2==2):
                                                        moveText = Text(Point(500,50),"Player 1's attack was deflected back!")
                                                        moveText.draw(win)
                                                        hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                                elif (status[p2sVal]=="defend" and defDet2==1):
                                                        failText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                        failText.draw(win)
                                                        win.getMouse()
                                                        moveText = Text(Point(500,50),"Player 1 attacked!")
                                                        moveText.draw(win)
                                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                                else:
                                                        moveText = Text(Point(500,50),"Player 1 attacked!")
                                                        moveText.draw(win)
                                                        hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                        elif (status[p1sVal]=="defend"):
                                                if (status[p2sVal]=="speed" or status[p2sVal]=="weapon"):
                                                        moveText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"...")
                                                        moveText.draw(win)
                                        elif (status[p1sVal]=="speed"):
                                                moveText = Text(Point(500,50),"Player 1 increased their speed by 5!")
                                                moveText.draw(win)
                                                speed1 = speed1+5
                                        elif(status[p1sVal]=="weapon"):
                                                if (p1wVal==4):
                                                        moveText = Text(Point(500,50),"Player 1 is already max power!")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"Player 1 started charging their weapon!")
                                                        moveText.draw(win)
                                                        p1wCharge = 1
                                else:
                                        moveText = Text(Point(500,50),"Player 1 is charging their weapon...")
                                        moveText.draw(win)
                        elif (turn=="Player 2"):
                                if (p2wCharge==0):
                                        if (status[p2sVal]=="fight"):
                                                if (status[p1sVal]=="defend" and defDet1==0 or status[p1sVal]=="defend" and defDet1==2):
                                                        moveText = Text(Point(500,50),"Player 2's attack was deflected back!")
                                                        moveText.draw(win)
                                                        hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                                elif (status[p1sVal]=="defend" and defDet1==1):
                                                        failText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                        failText.draw(win)
                                                        win.getMouse()
                                                        failText.undraw()
                                                        moveText = Text(Point(500,50),"Player 2 attacked!")
                                                        moveText.draw(win)
                                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                                else:
                                                        moveText = Text(Point(500,50),"Player 2 attacked!")
                                                        moveText.draw(win)
                                                        hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                        elif (status[p2sVal]=="defend"):
                                                if (status[p1sVal]=="speed" or status[p1sVal]=="weapon"):
                                                        moveText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"...")
                                                        moveText.draw(win)
                                        elif (status[p2sVal]=="speed"):
                                                moveText = Text(Point(500,50),"Player 2 increased their speed by 5!")
                                                moveText.draw(win)
                                                speed2 = speed2+5
                                        elif(status[p2sVal]=="weapon"):
                                                if (p2wVal==4):
                                                        moveText = Text(Point(500,50),"Player 2 is already max power!")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"Player 2 started charging their weapon!")
                                                        moveText.draw(win)
                                                        p2wCharge = 1
                                else:
                                        moveText = Text(Point(500,50),"Player 2 is charging their weapon...")
                                        moveText.draw(win)
                hp1Text.undraw()
                hp1BarFilled.undraw()
                hp2Text.undraw()
                hp2BarFilled.undraw()
                if (hp1<=0):
                        hp1=0
                if (hp2<=0):
                    hp2=0
                hp1Text = Text(Point(50,425),"HP: "+str(hp1))
                if (hp1<=0):
                        hp1BarFilled = Rectangle(Point(5,450),Point(5,475))
                else:
                        hp1BarFilled = Rectangle(Point(5,450),Point(5+(50*(hp1/hp1Full)),475))
                if (hp1/hp1Full<=0.2):
                        hp1BarFilled.setFill("red")
                else:
                        hp1BarFilled.setFill("light green")
                hp2Text = Text(Point(950,425),"HP: "+str(hp2))
                if (hp2<=0):
                        hp2BarFilled = Rectangle(Point(945,450),Point(945,475))
                else:
                        hp2BarFilled = Rectangle(Point(945,450),Point(945+(50*(hp2/hp2Full)),475))
                if (hp2/hp2Full<=0.2):
                        hp2BarFilled.setFill("red")
                else:
                        hp2BarFilled.setFill("light green")
                hp1Text.draw(win)
                hp1BarFilled.draw(win)
                hp2Text.draw(win)
                hp2BarFilled.draw(win)
                win.getMouse()
                moveText.undraw()
                if (hp2<=0 and hp1<=0):
                        winnerText=Text(Point(500,50),"Both of the homies dead. Damn...")
                        winnerText.draw(win)
                        p1.undraw()
                        p1 = Person(400,400,20,50,25,25,"x","|")
                        p1.draw(win)
                        p2.undraw()
                        p2 = Person(600,400,20,50,25,25,"x","/")
                        p2.draw(win)
                        break
                elif (hp2<=0):
                        winnerText=Text(Point(500,50),"Player 2 has been defeated. Player 1 wins!")
                        winnerText.draw(win)
                        p2.undraw()
                        p2 = Person(600,400,20,50,25,25,"x","/")
                        p2.draw(win)
                        break
                elif (hp1<=0):
                        winnerText=Text(Point(500,50),"Player 1 has been defeated. Player 2 wins!")
                        winnerText.draw(win)
                        p1.undraw()
                        p1 = Person(400,400,20,50,25,25,"x","|")
                        p1.draw(win)
                        break
                if (speed1<speed2):
                        if (p1wCharge==0):
                                if (status[p1sVal]=="fight"):
                                        if (status[p2sVal]=="defend" and status[p2sVal]=="defend" and defDet2==0):
                                                moveText = Text(Point(500,50),"Player 1's attack was deflected back!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                        elif (status[p2sVal]=="defend" and defDet2==1):
                                                failText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                failText.draw(win)
                                                win.getMouse()
                                                failText.undraw()
                                                moveText = Text(Point(500,50),"Player 1 attacked!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                        else:
                                                moveText = Text(Point(500,50),"Player 1 attacked!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                elif (status[p1sVal]=="defend" and status[p2sVal]=="fight"):
                                                moveText = Text(Point(500,50),"...")
                                                moveText.draw(win)
                                elif (status[p1sVal]=="defend"):
                                                if (status[p2sVal]=="speed" or status[p2sVal]=="weapon"):
                                                        moveText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"...")
                                                        moveText.draw(win)
                                                        moveText.undraw()
                                elif (status[p1sVal]=="speed"):
                                        moveText = Text(Point(500,50),"Player 1 increased their speed by 5!")
                                        moveText.draw(win)
                                        speed1 = speed1+5
                                elif(status[p1sVal]=="weapon"):
                                        if (p1wVal==4):
                                                moveText = Text(Point(500,50),"Player 1 is already max power!")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"Player 1 started charging their weapon!")
                                                moveText.draw(win)
                                                p1wCharge = 1
                                
                        else:
                                moveText = Text(Point(500,50),"Player 1 is charging their weapon...")
                                moveText.draw(win)
                elif (speed2<speed1):
                        if (p2wCharge==0):
                                if (status[p2sVal]=="fight"):
                                        if (status[p1sVal]=="defend" and defDet1==0 or status[p1sVal]=="defend" and defDet1==2):
                                                moveText = Text(Point(500,50),"Player 2's attack was deflected back!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                        elif (status[p1sVal]=="defend" and defDet1==1):
                                                failText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                failText.draw(win)
                                                win.getMouse()
                                                failText.undraw()
                                                moveText = Text(Point(500,50),"Player 2 attacked!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                        else:
                                                moveText = Text(Point(500,50),"Player 2 attacked!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                elif (status[p2sVal]=="defend" and status[p1sVal]=="fight"):
                                                moveText = Text(Point(500,50),"...")
                                                moveText.draw(win)
                                elif (status[p2sVal]=="defend"):
                                                if (status[p1sVal]=="speed" or status[p1sVal]=="weapon"):
                                                        moveText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"...")
                                                        moveText.draw(win)
                                                        moveText.undraw()
                                elif (status[p2sVal]=="speed"):
                                        moveText = Text(Point(500,50),"Player 2 increased their speed by 5!")
                                        moveText.draw(win)
                                        speed2 = speed2+5
                                elif(status[p2sVal]=="weapon"):
                                        if (p2wVal==4):
                                                moveText = Text(Point(500,50),"Player 2 is already max power!")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"Player 2 started charging their weapon!")
                                                moveText.draw(win)
                                                p2wCharge = 1
                        else:
                                moveText = Text(Point(500,50),"Player 2 is charging their weapon...")
                                moveText.draw(win)
                elif (turn=="Player 2"):
                        if (p1wCharge==0):
                                if (status[p1sVal]=="fight"):
                                        if (status[p2sVal]=="defend" and defDet2==0 or status[p2sVal]=="defend" and defDet2==2):
                                                moveText = Text(Point(500,50),"Player 1's attack was deflected back!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p1WeaponDMG*p1WMulti)
                                        elif (status[p2sVal]=="defend" and defDet2==1):
                                                failText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                failText.draw(win)
                                                win.getMouse()
                                                failText.undraw()
                                                moveText = Text(Point(500,50),"Player 1 attacked!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                        else:
                                                moveText = Text(Point(500,50),"Player 1 attacked!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p1WeaponDMG*p1WMulti)
                                elif (status[p1sVal]=="defend" and status[p2sVal]=="fight"):
                                                moveText = Text(Point(500,50),"...")
                                                moveText.draw(win)
                                elif (status[p1sVal]=="defend"):
                                                if (status[p2sVal]=="speed" or status[p2sVal]=="weapon"):
                                                        moveText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"...")
                                                        moveText.draw(win)
                                                        moveText.undraw()
                                elif (status[p1sVal]=="speed"):
                                        moveText = Text(Point(500,50),"Player 1 increased their speed by 5!")
                                        moveText.draw(win)
                                        speed1 = speed1+5
                                elif(status[p1sVal]=="weapon"):
                                        if (p1wVal==4):
                                                moveText = Text(Point(500,50),"Player 1 is already max power!")
                                                moveText.draw(win)
                                        else:
                                                moveText = Text(Point(500,50),"Player 1 started charging their weapon!")
                                                moveText.draw(win)
                                                p1wCharge = 1
                        else:
                                moveText = Text(Point(500,50),"Player 1 is charging their weapon...")
                                moveText.draw(win)
                elif (turn=="Player 1"):
                        if (p2wCharge==0):
                                if (status[p2sVal]=="fight"):
                                        if (status[p1sVal]=="defend" and defDet1==0 or status[p1sVal]=="defend" and defDet1==2):
                                                moveText = Text(Point(500,50),"Player 2's attack was deflected back!")
                                                moveText.draw(win)
                                                hp2 = hp2-(p2WeaponDMG*p2WMulti)
                                        elif (status[p1sVal]=="defend" and defDet1==1):
                                                failText = Text(Point(500,50),"Player 1 tried to block the attack, but it failed...")
                                                failText.draw(win)
                                                win.getMouse()
                                                failText.undraw()
                                                moveText = Text(Point(500,50),"Player 2 attacked!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                        else:
                                                moveText = Text(Point(500,50),"Player 2 attacked!")
                                                moveText.draw(win)
                                                hp1 = hp1-(p2WeaponDMG*p2WMulti)
                                elif (status[p2sVal]=="defend" and status[p1sVal]=="fight"):
                                                moveText = Text(Point(500,50),"...")
                                                moveText.draw(win)
                                elif (status[p2sVal]=="defend"):
                                                if (status[p1sVal]=="speed" or status[p1sVal]=="weapon"):
                                                        moveText = Text(Point(500,50),"Player 2 tried to block the attack, but it failed...")
                                                        moveText.draw(win)
                                                else:
                                                        moveText = Text(Point(500,50),"...")
                                                        moveText.draw(win)
                                                        moveText.undraw()
                                elif (status[p2sVal]=="speed"):
                                        moveText = Text(Point(500,50),"Player 2 increased their speed by 5!")
                                        moveText.draw(win)
                                        speed2 = speed2+5
                                elif(status[p2sVal]=="weapon"):
                                        moveText = Text(Point(500,50),"Player 2 started charging their weapon!")
                                        moveText.draw(win)
                                        p2wCharge = 1
                        else:
                                moveText = Text(Point(500,50),"Player 2 is charging their weapon...")
                                moveText.draw(win)
                if (status[p1sVal]=="defend" and status[p2sVal]=="defend"):
                        moveText = Text(Point(500,50),"Both failed to block...")
                        moveText.draw(win)
                hp1Text.undraw()
                hp1BarFilled.undraw()
                hp2Text.undraw()
                hp2BarFilled.undraw()
                if (hp1<=0):
                        hp1=0
                if (hp2<=0):
                    hp2=0
                hp1Text = Text(Point(50,425),"HP: "+str(hp1))
                if (hp1<=0):
                        hp1BarFilled = Rectangle(Point(5,450),Point(5,475))
                else:
                        hp1BarFilled = Rectangle(Point(5,450),Point(5+(50*(hp1/hp1Full)),475))
                if (hp1/hp1Full<=0.2):
                        hp1BarFilled.setFill("red")
                else:
                        hp1BarFilled.setFill("light green")
                hp2Text = Text(Point(950,425),"HP: "+str(hp2))
                if (hp2<=0):
                        hp2BarFilled = Rectangle(Point(945,450),Point(945,475))
                else:
                        hp2BarFilled = Rectangle(Point(945,450),Point(945+(50*(hp2/hp2Full)),475))
                if (hp2/hp2Full<=0.2):
                        hp2BarFilled.setFill("red")
                else:
                        hp2BarFilled.setFill("light green")
                hp1Text.draw(win)
                hp1BarFilled.draw(win)
                hp2Text.draw(win)
                hp2BarFilled.draw(win)
                win.getMouse()
                moveText.undraw()
                if (hp2<=0 and hp1<=0):
                        winnerText=Text(Point(500,50),"Both of the homies dead. Damn...")
                        winnerText.draw(win)
                        p1.undraw()
                        p1 = Person(400,400,20,50,25,25,"x","|")
                        p1.draw(win)
                        p2.undraw()
                        p2 = Person(600,400,20,50,25,25,"x","/")
                        p2.draw(win)
                        break
                elif (hp2<=0):
                        winnerText=Text(Point(500,50),"Player 2 has been defeated. Player 1 wins!")
                        winnerText.draw(win)
                        p2.undraw()
                        p2 = Person(600,400,20,50,25,25,"x","/")
                        p2.draw(win)
                        break
                elif (hp1<=0):
                        winnerText=Text(Point(500,50),"Player 1 has been defeated. Player 2 wins!")
                        winnerText.draw(win)
                        p1.undraw()
                        p1 = Person(400,400,20,50,25,25,"x","|")
                        p1.draw(win)
                        break
                if (p1wCharge!=0):
                        p1wCharge = p1wCharge+1
                if (p1wCharge==3):
                        successText = Text(Point(500,50),"Player 1 successfully upgraded their weapon!!")
                        successText.draw(win)
                        p1wCharge = 0
                        p1wVal = p1wVal+1
                        p1Weapon.undraw()
                        p1Weapon = Image(Point(441,427),p1WeaponName[p1wVal])
                        p1Weapon.draw(win)
                        win.getMouse()
                        successText.undraw()
                if (p2wCharge!=0):
                        p2wCharge = p2wCharge+1
                if (p2wCharge==3):
                        successText = Text(Point(500,50),"Player 2 successfully upgraded their weapon!!")
                        successText.draw(win)
                        p2wCharge = 0
                        p2wVal = p2wVal+1
                        p2Weapon.undraw()
                        p2Weapon = Image(Point(559,427),p2WeaponName[p2wVal])
                        p2Weapon.draw(win)
                        win.getMouse()
                        successText.undraw()
        #winner/loser/draw
        win.getMouse()
        hp1Text.undraw()
        hp1BarFilled.undraw()
        hp1BarEmpty.undraw()
        hp2Text.undraw()
        hp2BarFilled.undraw()
        hp2BarEmpty.undraw()
        winnerText.undraw()
        p1Weapon.undraw()
        p2Weapon.undraw()
        p1.undraw()
        p2.undraw()
        
