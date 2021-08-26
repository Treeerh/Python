#   2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты 
#       (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. 
#       Использовать библиотеку requests. В качестве API можно использовать 
#       http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API 
#       в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, 
#       решить поставленную задачу? Функция должна возвращать результат числового типа, например float. 
#       Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? 
#       Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, 
#       которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от 
#       того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
from requests import get
from sys import argv
from decimal import Decimal as dec
import datetime

def currency_rates(char_c):
    response_0 = get('http://www.cbr.ru/scripts/XML_daily.asp')  #получили страницу 
    content = response_0.content.decode(encoding=response_0.encoding)       #декодировали ее
    charcode = []
    value = []
    rez = {}
    char_c = char_c.upper()
    for el in content.split('Date="'):
        dates = ''.join(el.split('"')[:1])
    for el in content.split('<CharCode>'):
        charcode.append(''.join(el.split('</CharCode>')[:-1]))
    for el in content.split('<Value>'):
        value.append( (''.join(el.split('</Value>')[:-1])).replace(',', '.') )
    for i in range(len(charcode)):
        rez[charcode[i]] = value[i]
   
    if char_c in rez:
       return f'Курс {char_c} на {dates} составляет {dec(rez[char_c])} рублей'

if __name__ == '__main__':
    if argv[1:]:
        print(currency_rates(argv[1]))
    else:
        chcd = input('Введите валюту :')
        print(currency_rates(chcd))
    
    
    
