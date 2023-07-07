from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  Highest Score : {self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER! ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt") as f:
            return int(f.read())

    def write_high_score(self,high_sore):
        with open("data.txt", mode="w") as f:
            f.write(str(high_sore))
