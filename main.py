import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

start = True

def playing():
    global start
    keep_playing = screen.textinput("Play", "Do you want to play? Y or N")
    if keep_playing == "Y" or keep_playing == "y":
        screen.clear()
        start = True
    elif keep_playing == "N" or keep_playing == "n":
        start = False
        screen.bye()

while start:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    #spawn turtle
    player = Player()

    #spawn car manager
    car_manager = CarManager()

    #spawn scoreboard
    score = Scoreboard()

    screen.listen()
    screen.onkey(player.move_forward, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        all_cars = car_manager.all_cars

        new_car = car_manager.new_car()
        car_manager.moving()

        # detect collision with cars
        for car in all_cars:
            if player.distance(car) < 20:
                score.game_over()
                game_is_on = False
                playing()

        #detect collision with wall
        if player.ycor() >= 290:
            score.update_score()
            car_manager.speed_up()
            player.reset()


