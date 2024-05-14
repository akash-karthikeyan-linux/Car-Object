class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_started = True
        print("The engine has started")

    def stop_engine(self):
        self.is_engine_started = False
        print("The engine has stopped")

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
            if self.current_speed >= self.max_speed:
                self.current_speed = self.max_speed
        else:
            print("Car has not started yet")

    def apply_brakes(self):
        self.current_speed -= self.tyre_friction
        if self.current_speed < 0:
            self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")


car = Car("Red", 250, 10, 3)

car.start_engine()
car.accelerate()
car.accelerate()

print(car.current_speed)
car.apply_brakes()
print(car.current_speed)

car.sound_horn()
car.apply_brakes()
car.apply_brakes()
car.apply_brakes()
car.apply_brakes()
print(car.current_speed)
car.stop_engine()
