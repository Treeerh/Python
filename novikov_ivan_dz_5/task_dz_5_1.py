#   1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#   >>> odd_to_15 = odd_nums(15)
#    >>> next(odd_to_15)
#    1
#   >>> next(odd_to_15)
#    3
#    ...
#   >>> next(odd_to_15)
#   15
#   >>> next(odd_to_15)
#   ...StopIteration...

def odd_nums_0(num):
    for idx in range(1,num+1):
        if idx%2 != 0:
            yield idx
odd_to_15 = odd_nums_0(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)


def odd_nums_1(num):
    for idx in range(1,num+1,2):
        yield idx
odd_to_15 = odd_nums_1(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)

nums=15

odd_to_15 =(idx for idx in range(1,nums+1,2))
print(*odd_to_15)

odd_to_15 =(idx for idx in range(1,nums+1) if idx%2 != 0)
print(*odd_to_15)