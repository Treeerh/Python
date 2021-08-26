#   3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
#       которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь
#       дату из ответа, какой тип данных лучше использовать в ответе функции?
from requests import get
from sys import argv
from decimal import Decimal as dec
import datetime

def currency_rates(char_c):
    global days
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  #получили страницу
    content = response.content.decode(encoding=response.encoding)       #декодировали ее
    charcode = []
    value = []
    rez = {}
    char_c = char_c.upper()
    for el in content.split('Date="'):
        days = ''.join(el.split('"')[:1]).replace('.','/')
    days = datetime.datetime.strptime(days, '%d/%m/%Y')
    print(type(days))
    for el in content.split('<CharCode>'):
        charcode.append(''.join(el.split('</CharCode>')[:-1]))
    for el in content.split('<Value>'):
        value.append((''.join(el.split('</Value>')[:-1])).replace(',', '.'))
    for i in range(len(charcode)):
        rez[charcode[i]] = value[i]
    if char_c in rez:
        return f'Курс {char_c} на {days} составляет {dec(rez[char_c])} рублей'


if __name__ == '__main__':
    if argv[1:]:
        print(currency_rates(argv[1]))
    else:
        chcd = input('Введите валюту :')
        print(currency_rates(chcd))