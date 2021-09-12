# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

root = os.path.join(os.getcwd(), 'some_data')


def sizes(folder):
    files = os.listdir(folder)
    size_dict = {}
    for idx in (10 ** n for n in range(2, 6)):
        size_list = []
        for file in files:
            f = f'{root}\\{file}'
            fs = os.stat(f).st_size
            if idx - 100 <= fs < idx * 10 - 100:
                size_list.append(fs)
                size_dict[str(idx * 10)] = len(size_list)
    return size_dict


print(sizes(root))


