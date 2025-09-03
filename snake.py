import turtle
from turtle import Turtle
import random
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance=20

class Snake:
    def __init__(self):
        self.segments=[]
        turtle.colormode(255)
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color(self.random_color())
        new_seg.setpos(position)
        self.segments.append(new_seg)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_coordinates = self.segments[seg - 1].position()
            self.segments[seg].goto(new_coordinates)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def random_color(self):
        r = random.randint(0, 240)
        g = random.randint(0, 240)
        b = random.randint(0, 240)
        return (r, g, b)
    def boundery(self):
        tim = Turtle()
        tim.hideturtle()
        tim.color("red")
        tim.penup()
        tim.goto(-290, -290)
        tim.pendown()
        tim.goto(-290,290)
        tim.goto(290,290)
        tim.goto(290,-290)
        tim.goto(-290,-290)