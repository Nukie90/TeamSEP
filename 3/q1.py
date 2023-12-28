import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=20):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.t = turtle.Turtle()
    
    def showdisk(self):
        self.t.penup()
        self.t.setpos(self.dxpos, self.dypos)
        self.t.pendown()
        
        self.t.setheading(0)
        self.t.forward(self.dheight/2)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight/2)
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
        self.t.color("black")