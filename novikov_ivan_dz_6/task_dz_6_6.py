#   6. Реализовать простую систему хранения данных о суммах продаж булочной.
#   Должно быть два скрипта с интерфейсом командной строки: для записи данных и для
#   вывода на экран записанных данных. При записи передавать из командной строки
#   значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
#    просто запуск скрипта — выводить все записи;
#    запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому
#    числу, до конца;
#    запуск скрипта с двумя числами — выводить записи, начиная с номера,
#    равного первому числу, по номер, равный второму числу, включительно.
#    Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
#    Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с
#    1. Примеры запуска скриптов:
#
#    python add_sale.py 5978,5
#    python add_sale.py 8914,3
#    python add_sale.py 7879,1
#    python add_sale.py 1573,7
#    python show_sales.py
#    5978,5
#    8914,3
#    7879,1
#    1573,7
#    python show_sales.py 3
#    7879,1
#    1573,7
#    python show_sales.py 1 3
#    5978,5
#    8914,3
#    7879,1
# add_sale.py
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
# shpw_sales.py
import sys

with open('bakery.csv', 'r', encoding='utf-8') as f_summ:
    my_files = f_summ.readlines()


def my_print(b=None, e=None):
    for my_f in my_files[b:e]:
        print(my_f, end='')


if len(sys.argv) == 1:
    my_print()
elif len(sys.argv) == 2:
    b = int(sys.argv[1])
    my_print(b)
elif len(sys.argv) == 3:
    b = int(sys.argv[1])
    e = int(sys.argv[2])
    my_print(b, e)
