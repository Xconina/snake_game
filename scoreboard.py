from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.sety(278)
        self.display_score()
        

    def display_score(self):
        self.write(f"Score = {self.score}", align="center", font= ("courier", 15, "bold"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= ("courier", 26, "bold"))

    # def restart(self):
    #     self.clear()
    #     self.score(0)
    #     self.display_score()

    # def start_again(self):
    #     self.goto(0,-25)
    #     self.write(f"Press SPACE to play again", align="center", font= ("courier", 18, "bold"))