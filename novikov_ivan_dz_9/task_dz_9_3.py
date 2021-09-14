# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage,'bonus':bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя соьрудника : {self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'



ivan = Position ('Ivan','Ivanov','PR',3500,3000)
print(ivan.get_full_name())
print(ivan.get_total_income())

petro = Position ('Petr','Petrov','QA',3500,3000)
print(petro.get_full_name())
print(petro.get_total_income())
