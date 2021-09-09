# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в
# любом текстовом редакторе «руками» (не программно); предусмотреть возможные
# исключительные ситуации, библиотеки использовать нельзя.
import os, yaml
from yaml.loader import SafeLoader

with open('temp/config.yaml', 'r', encoding='UTF-8') as f_r:
    conf = yaml.load(f_r, Loader=SafeLoader)  # Список словарей
    #print(conf)
def print_dict(v, prefix=''):
    if isinstance(v, dict):
        for k, v2 in v.items():
            p2 = f'{prefix}\\{k}'
            print_dict(v2, p2)
    elif isinstance(v, list):
        for i, v2 in enumerate(v):
            p2 = f"{prefix}"
            print_dict(v2, p2)
    else:
        os.makedirs(f'{prefix}\\{repr(v)}')
print(print_dict(conf))