#   2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
#   реализовать корректную работу
#   с числительными, начинающимися с заглавной буквы — результат тоже
#   должен быть с заглавной. Например:
#       >>> num_translate_adv("One")
#       "Один"
#       >>> num_translate_adv("two")
#       "два"

def num_translate_odv(num):
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
    if num.istitle():
        num = num.lower()
        return numbers.get(num).title()
    else:
        return numbers.get(num)

my_num = input('Введите число: ')
print(num_translate_odv(my_num))
