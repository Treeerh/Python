# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.
class Myerror(Exception):
    pass


class Except:
    def __init__(self, divisible, divisor):
        self.res = self.divt(int(divisible), int(divisor))

    def divt(self, a, b):
        if b == 0:
            raise Myerror('Деление на ноль')
        else:
            return a / b

    def __str__(self):
        return f'{self.res}'

while True:
    a = input('Введите делимое : ')
    b = input('Введите делитель : ')
    try:
        d = Except(a, b)
        print(d)
    except Myerror as e:
        print(e)
    except ValueError as e:
        print(e)
        break

