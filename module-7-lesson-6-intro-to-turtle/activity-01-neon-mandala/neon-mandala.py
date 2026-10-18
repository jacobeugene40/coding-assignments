# PART 1 - Import turtle and set up the screen
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

# PART 2 - Create and configure the pen
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

# PART 3 - Glowing colour spiral
colors = ["red", "orange", "yellow", "lime", "cyan", "magenta"]

for i in range(80):
    board.color(colors[i % 6])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

# PART 4 - Gold filled 5-pointed star at the centre
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()

board.color("gold", "yellow")
board.begin_fill()
for _ in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

# PART 5 - Ring of 36 filled colour petals
board.penup()
board.goto(0, 0)
board.pendown()

petal_colors = ["deeppink", "cyan", "lime", "orange", "violet"]

for i in range(36):
    board.color(petal_colors[i % 5])
    board.begin_fill()
    for _ in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

turtle.done()