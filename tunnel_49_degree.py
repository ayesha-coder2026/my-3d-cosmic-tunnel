import colorsys
import turtle 

# screen ki setting or canvas open karna kaliya
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Cosmeic 3D Tunnel Project By Ayesha")

#turtle character setting
t = turtle.Turtle()
t.speed(0)
t.width(1)

for i in range(230):
    color = colorsys.hsv_to_rgb(i/120, 1.0, 1.0)
    t.pencolor(color)
    t.forward(i * 1.5)
    t.left(49)
    t.circle(i, 40)
    t.left(360)

turtle.done()
