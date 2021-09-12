# 1. Написать функцию email_parse(<email_address>), которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен из email
# адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
import re, sys


def parser_mail(e_mail):
    # patt = re.compile(r'^(?P<login>\w+)@(?P<domain>\w+\.\w+)$')
    patt = re.compile(r"(?P<login>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    res = patt.match(e_mail)
    if "@" in e_mail:
        return res.groupdict()
    else:
        sys.exit('Not e_mail')


print(parser_mail('ivan-56@bk.ru'))

print(parser_mail('ivan-56bk.ru'))
