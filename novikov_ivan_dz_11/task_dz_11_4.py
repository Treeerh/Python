# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class Warehouse:  # Склад
    devices_in_warehouse = []

    @classmethod
    def to_warehouse(cls, device):
        cls.devices_in_warehouse.append(device)
        print(device, ' - Принято на склад.')

    def __str__(self):
        string = '\n'.join(map(str, self.devices_in_warehouse))
        return 'Устройства на складе:\n' + string if string else 'На складе нет устройств'


class Office_equipment(ABC):  # Оргтезника
    def __init__(self, maker, model, sireal, year_man, format):
        self.maker = maker  # Производитель (Создатель)
        self.model = model  # Модель
        self.sireal = sireal  # Серийный номер
        self.year_man = year_man  # Год производства
        self.format = format  # Формат

    def __str__(self):
        return f'Произв {self.maker}, Модель {self.model}, СН {self.sireal}, Год {self.year_man}, Формат {self.format}'

    @abstractmethod
    def job(self):
        pass


class Printer(Office_equipment):  # Принтер
    def __init__(self, maker, model, sireal, year_man, format, types, color):
        super().__init__(maker, model, sireal, year_man, format)
        self.types = types
        self.color = color

    def job(self):
        return f'Печатает {self.maker} {self.model}'


class Scaner(Office_equipment):  # Сканер
    def job(self):
        return f'Сканирует {self.maker} {self.model}'


class Replica(Office_equipment):  # Копир
    def __init__(self, maker, model, sireal, year_man, format, types, color):
        super().__init__(maker, model, sireal, year_man, format)
        self.types = types  #
        self.color = color  #

    def job(self):
        return f'Копирует {self.maker} {self.model}'


printer = Printer('Ricoh', 'SP C360DNw', 'SN1212', 2020, 'A4', 'laser', 'black')
scanner = Scaner('HP', 'Pro 4500', 'SN7857', 2019, 'A4')
copier = Replica('Xerox', 'WorkCentre 3025', 'SN1565', 2018, 'A4', 'laser', 'color')
print(printer)
printer.job()
scanner.job()
copier.job()
print(Warehouse())
print('-----')
Warehouse.to_warehouse(printer)
Warehouse.to_warehouse(scanner)
Warehouse.to_warehouse(copier)
print(Warehouse())
