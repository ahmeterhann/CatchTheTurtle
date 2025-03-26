import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
font = ("Arial", 30, "normal")
grid_size = 10
x_coordinate = [-20, -10, 0, 10, 20]
y_coordinate = [20, 10, 0, -10]
score = 0
game_over = False

# turtle list
turtle_list = []

# score turtle
score_turtle = turtle.Turtle()

# countdown turtle
countdown_turtle = turtle.Turtle()


def setup_score():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2 * 0.8

    score_turtle.setpos(0, top_height)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=font)


def make_turtle(x, y):
    t = turtle.Turtle()

    def click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=font)

    t.onclick(click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.setpos(x * grid_size, y * grid_size)
    turtle_list.append(t)


def setup_turtle():
    for x in x_coordinate:
        for y in y_coordinate:
            make_turtle(x, y)


def hide_turtle():
    for t in turtle_list:
        t.hideturtle()


# recursive function
def random_show():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(random_show, 800)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2 * 0.8

    countdown_turtle.setpos(0, top_height - 50)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=font)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=font)


turtle.tracer(0)
setup_score()
setup_turtle()
hide_turtle()
random_show()
turtle.tracer(1)
countdown(10)

turtle.mainloop()
