import math
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(90000)

# Drawing Axis
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

#Plotting the Sin wave
for i in range(-360, 361):
    x = i
    y = math.sin(math.radians(x)) * 100
    
    # Go to position and start drawing
    t.goto(x, y)
    t.pendown()
    
    # Corrected gradient calculation (dy/dx) for scaled sine wave
    gradient = math.cos(math.radians(x)) * (math.pi / 180) * 100
    print(f"X: {x:.2f}, Y: {y:.2f}, gradient: {gradient:.3f}")

    # Check for turning points (gradient near zero due to float precision)
    if abs(gradient) < 0.001:
        print("Gradient is zero at x =", x)

screen.mainloop()
