#   3. Написать функцию thesaurus(), принимающую в качестве аргументов имена
#   сотрудников и возвращающую словарь,
#   в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
#   начинающиеся с соответствующей буквы. Например:
#   >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
#       {
#           "И": ["Иван", "Илья"],
#           "М": ["Мария"], "П": ["Петр"]
#       }
#   Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
#   если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?


def thesaurus(list_name):
    '''
    The function returns an alphabetically sorted dictionary of names
    :param list_name: incoming list or tuple
    :return: dictionary my_title_tup
    '''
    mys = sorted(list_name)
    my_title = []
    my_title_dict = {}
    for my in mys:
        my_title.append(my[:1])
    my_title = sorted(set(my_title))
    #my_title = set(my_title)
    for my in my_title:
        temp_list = []
        for idx in list_name:
            if my == idx[:1]:
                temp_list.append(idx)
            my_title_dict[my] = temp_list
    #print(type(my_title_dict))
    return my_title_dict


name = ["Анна", "Вася", "Инга", "Матвей", "Дмитрий", "Василиса", "Эдик", "Иван", "Мария", "Петр", "Илья", "Борис"]
print(thesaurus(name))

name_1 = ("Анна", "Вася", "Инга", "Матвей", "Дмитрий", "Эдик", "Иван", "Мария", "Петр", "Илья", "Борис")
print(thesaurus(name_1))
