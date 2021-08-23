#   4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве
#   аргументов строки в
#       формате «Имя Фамилия» и возвращающую словарь, в котором
#       ключи — первые буквы фамилий,
#       а значения — словари, реализованные по схеме предыдущего задания и
#       содержащие записи,
#       в которых фамилия начинается с соответствующей буквы. Например:
#   >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
#   "Анна Савельева")
#       {
#       "А": {
#            "П": ["Петр Алексеев"]
#             },
#        "С": {
#            "И": ["Иван Сергеев", "Инна Серова"],
#            "А": ["Анна Савельева"]
#             }
#       }
#   Как поступить, если потребуется сортировка по ключам?
def thesaurus(list_name):
    '''
    The function returns an alphabetically sorted dictionary of names
    :param list_name: incoming list or tuple
    :return: dictionary my_title_tup
    '''
    my_title = []
    my_title_dict = {}
    for my in list_name:
        my_title.append(my[:1])
    my_title = sorted(set(my_title))
    for my in my_title:
        temp_list = []
        for idx in list_name:
            if my == idx[:1]:
                temp_list.append(idx)
            my_title_dict[my] = temp_list
    return my_title_dict

def thesaurus_odv(list_name):
    my_title = []
    my_title_dict = {}
    for my in list_name:
        my_title.append(my.split(' ')[1:][0][:1])
    my_title = set(my_title)
    for my in my_title:
        temp_list = []
        for idx in list_name:
            if my == idx.split(' ')[1:][0][:1]:
                temp_list.append(idx)
            my_title_dict[my] = thesaurus(temp_list)
    return my_title_dict

name = ("Иван Сергеев", "Алина Жабова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(thesaurus_odv(name))
print('--------------------------------')
for key, val in thesaurus_odv(name).items():
    print('{',f'{key} : {val}','}')
