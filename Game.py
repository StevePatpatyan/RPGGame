from graphics import*
def contains(self,p):
    leftBound = self.point.x;
    rightBound = self.point.x + 15;
    upBound = self.point.y - 21;
    lowBound = self.point.y + 15;
    if(p.x >= leftBound and p.x <= rightBound and p.y >= upBound and p.y <= lowBound):
        return True;
    else:
        return False;
        
win = GraphWin("RPG GAME",1000,500)
start = Rectangle(Point(100,100),Point(200,200))
start.draw(win)
while (True):    
        introButton = win.getMouse()
        if (start.contains(introButton)):
            print("yurr")
