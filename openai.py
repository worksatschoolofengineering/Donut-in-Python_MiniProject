import turtle

# create a turtle
t = turtle.Turtle()

# create a circle
t.circle(50)

# lift the pen
t.penup()

# move the turtle to the center of the circle
t.goto(0, 50)

# set the turtle's heading to 0 (pointing to the right)
t.setheading(0)

# draw another circle
t.pendown()
t.circle(25)

# create a spinning animation
while True:
    t.right(1)