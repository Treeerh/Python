#5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
from utils import currency_rates as cr
from sys import argv


if argv[1:]:
    print(cr(argv[1]))
else:
    chcd = input('Введите валюту :')
    print(cr(chcd))
