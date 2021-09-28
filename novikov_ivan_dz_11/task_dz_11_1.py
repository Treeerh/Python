# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
#
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, data):
        self.data = self.date_split(data)
        self.validator(self.data)

    @classmethod
    def date_split(cls, date):
        res = date.split('-')
        return res

    @staticmethod
    def validator(data_list):
        day, month, year = map(int, data_list)
        if (1 <= day <= 31) and (1 <= month <= 12):
            return data_list
        else:
            raise ValueError(f'Неверная дата')

    def __str__(self):
        return f'{self.data}'


d1 = Data('21-04-2021')
print(d1)
d2 = Data('11-44-2021')
print(d2)
d3 = Data('13-04-2021')
print(d3)
