import turtle
t = turtle.Turtle()

#SQUARE
side = int(input("Length of side: "))
#side=100
for i in range(4):
   t.forward(side)
   t.left(90)
# t.penup()
# t.left(180)
# t.forward(side*2)
# t.pendown()
#TRIANGLE
for i in range(3):
    t.forward(side)
    t.left(120)

t.exitonclick()