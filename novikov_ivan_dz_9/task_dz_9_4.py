# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.

class Car:
    is_police = False
    speed = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self):
        self.speed += 10
        return f'Поехали {self.name} speed: {self.speed}'

    def stop(self):
        self.speed = 0
        return f'Остановились {self.name} speed: {self.speed}'

    def turn(self, direction):
        self.speed -= 5
        return f'{self.name} повернул: {"<-<" if direction == 0 else ">->"}'

    def show_speed(self):
        return f'{self.name} speed = {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} преввысил скорость {self.speed}')
            self.speed = 60
            return f'{self.speed} сброшена'
        else:
            print(f'{self.name} есть куда стремиться {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} преввысил скорость {self.speed}')
            self.speed = 40
            return f'{self.speed} сброшена'
        else:
            print(f'{self.name} есть куда стремиться {self.speed}')


class PoliceCar(Car):
    is_police = True


lada = Car('LADA', 'Red')
lada.go()
lada.go()
print(lada.show_speed())

daca = TownCar('DACA', 'Black')
print(daca.stop())
print(daca.go())
print(daca.go())
print(daca.go())
print(daca.go())
print(daca.go())
print(daca.go())
print(daca.go())
print(daca.go())
print(daca.show_speed())
print(daca.show_speed())