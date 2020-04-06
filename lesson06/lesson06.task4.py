class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self):
        print('машина делает поворот налево')

    def show_speed(self):
        print('скорость машины составляет 50 км/ч')


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print('превышение скорости')


town_car = TownCar(80, 'green', 'niva', False)
town_car.show_speed(80)
town_car.stop()
town_car.go()


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print('превышение скорости')


Work_car = WorkCar(50, 'blue', 'lada', False)
Work_car.show_speed(25)
Work_car.turn()


class SportCar(Car):
    pass


Sport_car = SportCar(100, 'red', 'formula1', False)
Sport_car.speed
Sport_car.color
Sport_car.go()


class PoliceCar(Car):
    pass


Police_Car = PoliceCar(65, 'grey', 'uaz', True)
Police_Car.is_police
Police_Car.turn()