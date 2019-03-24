class Car:
    color = ''
    car_type = ''
    speed = 0
    max_speed = 0
    horse_power = 0
    model = ''
    passengers = 0

    def __init__(self, color, car_type, speed, max_speed,
                 horse_power, model,  passengers):
        self.color = color
        self.car_type = car_type
        self.max_speed = max_speed
        self.horse_power = horse_power
        self.model = model
        self.passengers = passengers
        self.speed = speed

    def __str__(self):
        return 'Type: {}\tmodel {}\tcolor: {}'.format(self.car_type, self.model, self.color)


    def speedup(self):
        self.speed += 10
        print('current speed = ', self.speed)


car1 = Car('red', 'BWM', 0, 300, 1800, 'X6', 5)
print(car1)
car1.speedup()