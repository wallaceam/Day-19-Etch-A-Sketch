from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(5)


def counter_clockwise():
    tim.left(5)


def reset():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset)

screen.title("Push 'W' to move forward, 'S' to move backward, 'A' to turn left, 'D' to turn right, or 'C' to reset.")

screen.exitonclick()
