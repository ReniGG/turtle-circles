#Import turtle library
import turtle

#Create a function to draw the concentric circles using a for loop
def draw_circles(turtle_obj, start_radius, count, angle):
    radius = start_radius # Create a new variable called radius that starts with the same value as start_radius to keep the original start_radius' value unchanged
    for _ in range(count): # Use the built-in range function to specify the number of iterations
        turtle_obj.circle(radius) # Invoke the circle method with a specified radius
        radius += 25 # Increase the radius for the next circle
    turtle_obj.left(angle) # Turn the turtle left by the specified angle

# Set up the screen
ws = turtle.Screen() # turtle refers to the Turtle graphics module; Screen() is a method of the turtle module that creates a new screen
ws.bgcolor("powder blue")

# Create turtle
jess = turtle.Turtle() # turtle refers to the Turtle graphics module; Turtle() is a class constructor, it creates a new instance of the Turtle class
jess.shape("turtle")
jess.pensize(5)
jess.color("lightpink")
jess.speed(0)

# Draw the first set of circles
draw_circles(jess, 50, 9, 180)

# Draw the second set of circles
draw_circles(jess, 50, 9, 90)

# Draw the third set of circles
draw_circles(jess, 50, 9, 180)

# Draw the fourth set of circles
draw_circles(jess, 50, 9, 0)

# Change the turtle's color
jess.color("dodger blue")

# Finish the drawing and keep the window open
turtle.done()