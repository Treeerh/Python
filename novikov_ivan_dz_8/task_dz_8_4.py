# 4. Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

from functools import wraps


def val_checker(callback):
    def logger(name_funck):
        @wraps(name_funck)
        def wrapper(*args):
            for arg in args:
                if not callback(arg):
                    raise ValueError(f'{arg}')
            return name_funck(*args)

        return wrapper

    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(4)
print(a)

b = calc_cube(-4)
print(b)
