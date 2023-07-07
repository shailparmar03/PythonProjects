from  turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto_start()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def goto_start(self):
        self.goto(STARTING_POSITION)

