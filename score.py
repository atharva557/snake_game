from turtle import Turtle
class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=self.get_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", align="center", font=("Arial", 24, "normal"))
    def inc_score(self):
        self.score+=1
        self.update_score()
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            self.update_highscore(self.high_score)
        self.score=0
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))
    def get_highscore(self):
        with open("data.txt","r")as file:
            return int(file.read())
    def update_highscore(self,new_highscore):
        with open("data.txt","w")as file:
            file.write(str(new_highscore))