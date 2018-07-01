import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    while True:
        draw_square(some_turtle)
        some_turtle.right(11)

def draw_circle_of_squares():
    # Creates the window
    window = turtle.Screen()
    window.bgcolor("white")

    # Create the turtle Arrow
    arrow = turtle.Turtle()
    arrow.shape("arrow")
    arrow.color("black")
    arrow.speed(0)

    # Draw a circle of squares
    draw_circle(arrow)

    # Exits with a click anywhere in the window
    window.exitonclick()

draw_circle_of_squares()