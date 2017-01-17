# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
 
# bring in the packages of functions we need
import random
import turtle
import time
 
# -------- functions start here ----------------

# code that reates a trinagle with random sides  
def regular_triangle(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        # This will allow the code to run until all 3 sides are drawn 
        while side_count < 3:
                myTurtle.forward(side)
                myTurtle.right(120)
                side_count = side_count + 1
 # code that creates a square with random sides 
def regular_square(myTurtle, x, y, side):
        myTurtle.penup() 
        myTurtle.goto(x,y)
        myTurtle.pendown() 
        side_count = 0
        # This will allow code to run until shape has all 4 sides 
        while side_count < 4: 
            myTurtle.forward(side) 
            myTurtle.right(90) 
            side_count = side_count + 1 
 # code that creates a pentagon with different side lengths 
def regular_pentagon(myTurtle, x, y, side):
        myTurtle.penup() 
        myTurtle.goto(x,y) 
        myTurtle.pendown()
        side_count = 0 
        # code will run until the shape has all 5 sides 
        while side_count < 5:
            myTurtle.forward(side) 
            myTurtle.left(72)
            side_count = side_count + 1 
 # code that creates a hexagon with different side lengths 
def regular_hexagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y) 
        myTurtle.pendown() 
        side_count = 0 
        # code will run until the shape has all 6 sides 
        while side_count < 6: 
            myTurtle.forward(side)
            myTurtle.right(60) 
            side_count = side_count + 1 
# code that creates an octagon with different side lengths  
def regular_octagon(myTurtle, x, y, side):
        myTurtle.penup() 
        myTurtle.goto(x,y) 
        myTurtle.pendown() 
        side_count = 0 
        # code will run until the shape has all 8 sides 
        while side_count < 8: 
            myTurtle.forward(side) 
            myTurtle.right(45) 
            side_count = side_count + 1 
 # code that creates a random sized circle 
def circle(myTurtle, x, y, radius):
        myTurtle.penup() 
        myTurtle.goto(x,y) 
        myTurtle.pendown() 
        side_count = 0 
        # This will allow the circle to look like one by having a lot of sides all together 
        while side_count < 150: 
            myTurtle.forward(radius/45) 
            myTurtle.right(2.4) 
            side_count = side_count + 1 
            
            
        
 
# -------- execution starts here ----------------
 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
 
squirt = turtle.Turtle()

# write a message to the screen
# the arguments after the string set where & how it's written
squirt.write("Enter a shape!\nWhen you're done, enter 'exit'.", False, "center", ("Arial", 12,"normal"))
squirt.backward(1)

# wait a moment for the user to read
time.sleep(300)

 
shape = ""
while shape != "exit":
        shape = raw_input()
 
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
 
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        elif shape == 'hexagon':
                regular_hexagon(squirt, randx, randy, randside)
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)
