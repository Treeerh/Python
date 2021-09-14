# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} «Запуск отрисовки»')


class Pen(Stationery):
    def draw(self):
        return f'{self.title} «Запуск отрисовки Ручкой»'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} «Запуск отрисовки Карандашем»'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} «Запуск отрисовки Маркером»'

pen = Pen('red')
print(pen.draw())
pencil = Pencil('Grey')
print(pencil.draw())
handle = Handle('Green')
print(handle.draw())