import math
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(90000)

#Drawing Axis 
t.penup()
# Draw X-axis
t.goto(-360, 0)
t.pendown()
t.goto(360, 0)
t.penup()
# Draw Y-axis
t.goto(0, -150)
t.pendown()
t.goto(0, 150)
t.penup()
# Actually plotting or graph
for i in range(-360, 361):
    x = i
    # Edit your mathematical function here
    y = (x**2 + 2*x + 1) / 100
    
    # Go to position and start drawing
    t.goto(x, y)
    t.pendown()
    
    # Derivative/gradient for x^2 + 2x + 1 scaled down by 100: (2x + 2) / 100
    gradient = (2 * x + 2) / 100
    print(f"X: {x:.2f}, Y: {y:.2f}, gradient: {gradient:.3f}")

    if gradient == 0:
        print("Gradient is zero at x =", x)

screen.mainloop()
