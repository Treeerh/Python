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

root = os.getcwd()


def print_dict(v, prefix=''):
    if isinstance(v, dict):
        for k, v2 in v.items():
            p2 = f'{prefix}\\{k}'
            os.makedirs(root + p2)
            print_dict(v2, p2)
    elif isinstance(v, list):
        for i, v2 in enumerate(v):
            p2 = f"{prefix}"
            print_dict(v2, p2)
    else:
        fle = repr(v).replace("'", '')
        f_path = f'{prefix}\\{fle}'
        with open(root + f_path, 'x', encoding='utf-8') as f:
            pass


print(print_dict(conf))
