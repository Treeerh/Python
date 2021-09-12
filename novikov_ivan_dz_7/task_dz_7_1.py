    #    1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#    |--my_project
#       |--settings
#       |--mainapp
#       |--adminapp
#       |--authapp
#   Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
#   как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
#   папок под конкретный проект; можно ли будет при этом расширять конфигурацию и
#   хранить данные о вложенных папках и файлах (добавлять детали)?

# Влоб
import os, sys
import yaml

my_strucs = {'my_project':['settings','mainapp','adminapp','authapp']}

path = os.getcwd() #текущий каталог

for key, valls in my_strucs.items():
    if os.path.isdir(f'{path}\\{key}'):
        sys.exit('Пака существует')
    else:
        os.mkdir(f'{path}\\{key}')
        print(f'Созданна папка {key}')
    for idx in valls:
        if os.path.isdir(f'{path}\\{key}\\{idx}'):
            sys.exit('Пака существует')
        else:
            os.mkdir(f'{path}\\{key}\\{idx}')
            print(f'В папке {key} cозданна папка {idx}')

