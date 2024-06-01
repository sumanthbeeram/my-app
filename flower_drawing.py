import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
flower = turtle.Turtle()

# Customize the turtle's shape and color
flower.shape("turtle")
flower.color("red")
flower.speed(10)  # Set the drawing speed

# Draw the stem of the flower
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.forward(200)

# Function to draw a petal
def draw_petal():
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Draw the petals
for _ in range(6):
    draw_petal()
    flower.left(60)

# Close the drawing window when clicked
screen.exitonclick()
