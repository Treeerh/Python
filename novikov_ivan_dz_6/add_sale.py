import sys


def add_sale():
    if len(sys.argv) > 1:
        return sys.argv[1] + '\n'
    else:
        sys.exit('No param')


def add_file(my_def):
    with open('bakery.csv', 'a', encoding='utf-8') as f_summ:
        f_summ.writelines(my_def)

add_file(add_sale())
