# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(name_funck):
    def wrapper(*args):
        print(f'{name_funck.__name__} ', end='')
        cube = name_funck(*args)
        for arg in args:
            print(f'{name_funck(arg)} - {arg} : {type(arg)}, ', end='')
        print('\r')
        return cube

    return wrapper


@type_logger
def calc_cube(*args):
    cubes = []
    for arg in args:
        cubes.append(arg ** 3)
    return cubes


a = calc_cube(4, 8, 9)
print(a)

b = calc_cube(4)
print(b)
