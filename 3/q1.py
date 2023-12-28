import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, width=20, height=20):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.t = t.Turtle()
    
    def showdisk(self):
        self.t.color("black")
        self.t.penup()
        self.t.setpos(self.dxpos, self.dypos)
        self.t.pendown()
        
        self.t.setheading(0)
        self.t.forward(self.dwidth/2)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth/2)
        self.t.setheading(0)
    
    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
        self.t.penup()
        self.t.setpos(self.dxpos, self.dypos)
        self.t.pendown()
        
    def cleardisk(self):
        self.t.penup()
        self.t.setpos(self.dxpos, self.dypos)
        self.t.pendown()
        self.t.color("white")
        self.t.setheading(0)
        self.t.forward(self.dwidth/2)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth/2)
        self.t.setheading(0)

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick = 10, length = 100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        
    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        t.setheading(0)
        t.forward(self.pthick/2)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick/2)
        t.penup()
        t.goto(self.pxpos, self.pypos + self.plength)
        t.write(self.pname)
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        
    def pushdisk(self, disk):
        disk.newpos(self.pxpos, self.toppos + self.pypos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += disk.dheight
    def popdisk(self):
        disk = self.stack.pop()
        disk.cleardisk()
        self.toppos -= disk.dheight
        return disk
    