<<<<<<< HEAD
import turtle as t
=======
import turtle
>>>>>>> 3dd6f8760a5f4b002f65c3d2696654804344f9b5

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=20):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
<<<<<<< HEAD
        self.t = t.Turtle()
=======
        self.t = turtle.Turtle()
>>>>>>> 3dd6f8760a5f4b002f65c3d2696654804344f9b5
    
    def showdisk(self):
        self.t.penup()
        self.t.setpos(self.dxpos, self.dypos)
        self.t.pendown()
        
        self.t.setheading(0)
<<<<<<< HEAD
        self.t.forward(self.dwidth/2)
        self.t.left(90)
        self.t.forward(self.dheight)
=======
        self.t.forward(self.dheight/2)
>>>>>>> 3dd6f8760a5f4b002f65c3d2696654804344f9b5
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
<<<<<<< HEAD
        self.t.forward(self.dwidth/2)
=======
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight/2)
>>>>>>> 3dd6f8760a5f4b002f65c3d2696654804344f9b5
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
<<<<<<< HEAD
        

=======
        self.t.color("black")
>>>>>>> 3dd6f8760a5f4b002f65c3d2696654804344f9b5
