from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES_Y = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 240, 200, 160, 120]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

cars = []

class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        # it is a random generation of cars, i generates a car for each 5 updates of the screen
        if random.randint(1, 6) == 3:
            car = Turtle()
            car.penup()
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.goto(300, random.choice(LANES_Y))
            cars.append(car)

    def move_cars(self):
        for car in cars:
            if car.xcor() < -320:
                cars.remove(car)
                del car
            else:
                car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10

    def reset_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE

    def check_crash(self, player):
        for car in cars:
            if player.distance(car) < 20 and player.ycor() > car.ycor()-15:
                return True

        return False
