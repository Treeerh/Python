import sys


def my_print(b=None, e=None):
    with open('bakery.csv', 'r', encoding='utf-8') as f_summ:
        for my_f in f_summ.readlines()[b:e]:
            print(my_f, end='')


if len(sys.argv) == 1:
    my_print()
elif len(sys.argv) == 2:
    b = int(sys.argv[1])
    my_print(b - 1)
elif len(sys.argv) == 3:
    b = int(sys.argv[1])
    e = int(sys.argv[2])
    my_print(b - 1, e)
