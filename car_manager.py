from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        super().__init__()
        #self.seth(180)
        self.penup()
        self.goto(300,300)
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            car.penup()
            car.seth(180)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(280, random_y)
            self.all_cars.append(car)

    def moving(self):
        for car in self.all_cars:
            car.fd(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT

    def reset(self):
        self.move_speed = STARTING_MOVE_DISTANCE






