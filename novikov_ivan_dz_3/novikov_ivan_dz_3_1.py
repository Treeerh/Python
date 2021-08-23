#   1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#       >>> num_translate("one")
#       "один"
#       >>> num_translate("eight")
#       "восемь"
#   Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
#   необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.\

def num_translate(num):
    '''
    the function returns the dictionary value by the key
    :param num: key value
    :return: value
    '''
    numbers = {'один':'one', 'два':'two',
               'три':'three', 'четыре':'four',
               'пять':'five', 'шесть':'six',
               'семь':'seven', 'восемь':'eight',
               'девять':'nine', 'десять':'ten'}
    return numbers.get(num)

my_num = input('Введите число: ')
print(num_translate(my_num))


