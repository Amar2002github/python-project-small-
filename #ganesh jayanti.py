#ganesh jayanti
import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#FFF3D6")
screen.title("Ganesh Murti - Python Turtle")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def ellipse(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.circle(height / 2, 90)
        t.forward(width)
        t.circle(height / 2, 90)

    t.end_fill()

def circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Decorative halo
circle(0, 170, 150, "#FFD700")
circle(0, 170, 130, "#FFF3D6")

# Body
ellipse(-90, -230, 180, 230, "#F4A261")

# Head
circle(0, 180, 105, "#F4A261")

# Ears
ellipse(-150, 130, 75, 110, "#E99B55")
ellipse(75, 130, 75, 110, "#E99B55")

# Eyes
circle(-38, 200, 12, "black")
circle(38, 200, 12, "black")

# Tilak
t.penup()
t.goto(0, 245)
t.pendown()
t.color("#D62828")
t.width(8)
t.goto(0, 270)

# Trunk
t.penup()
t.goto(0, 170)
t.pendown()
t.color("#F4A261")
t.width(35)
t.setheading(-90)
t.circle(55, 100)

# Tusks
t.color("white")
t.width(8)

t.penup()
t.goto(-25, 145)
t.pendown()
t.goto(-55, 115)

t.penup()
t.goto(25, 145)
t.pendown()
t.goto(55, 115)

# Crown
t.penup()
t.goto(-70, 270)
t.pendown()
t.fillcolor("#E9C46A")
t.color("#B8860B")
t.begin_fill()

t.goto(-45, 330)
t.goto(0, 290)
t.goto(45, 330)
t.goto(70, 270)
t.goto(-70, 270)

t.end_fill()

# Necklace
t.color("#FFD700")
t.width(12)
t.penup()
t.goto(-55, 75)
t.pendown()
t.goto(0, 55)
t.goto(55, 75)

# Arms
t.color("#F4A261")
t.width(25)

t.penup()
t.goto(-70, 20)
t.pendown()
t.goto(-150, -40)

t.penup()
t.goto(70, 20)
t.pendown()
t.goto(150, -40)

# Modak
circle(155, -55, 25, "#D97706")

# Mouse
ellipse(-210, -250, 90, 45, "#555555")
circle(-135, -235, 8, "black")

# Mouse ears
circle(-175, -220, 15, "#666666")
circle(-145, -220, 15, "#666666")

# Text
t.penup()
t.goto(0, -350)
t.color("#D62828")
t.write("॥ श्री गणेशाय नमः ॥",
        align="center",
        font=("Arial", 24, "bold"))

turtle.done()
