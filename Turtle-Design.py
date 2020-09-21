import turtle
wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.speed(0)

def square(length, angle):
    for i in range(4):
        alex.forward(length)
        alex.right(angle)

for j in range(66):
    if j<= 33:
        new_color = "palegoldenrod"
    else:
        new_color = "gold"

    alex.color(new_color)
    square(100,90)
    alex.right(11)

wn.exitonclick()
