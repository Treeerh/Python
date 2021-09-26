# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных
# классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothers(ABC):
    ext_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothers):
    def __init__(self, size):
        self.size = size
        Coat.ext_count += self.expence

    def __str__(self):
        return f'Размер {self.size}, Ткань {self.expence}, Расход {Coat.ext_count}'

    @property
    def expence(self):
        exp = self.size / 6.5 + .5
        return exp


class Costume(Clothers):
    def __init__(self, height):
        self.height = height
        Coat.ext_count += self.expence

    def __str__(self):
        return f'Рост {self.height}, Ткань {self.expence},Расход {Coat.ext_count}'

    @property
    def expence(self):
        exp = (self.height * 2 + .3) / 100
        return exp

cloth_1 = Coat(65)
print(cloth_1)
cloth_2 = Costume(185)
print(cloth_2)
