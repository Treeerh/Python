# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт,
# который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import os, shutil

my_proj = 'my_project'
my_templ = 'templates'
root = os.getcwd()
proj = os.path.join(root, my_proj)
templ = os.path.join(root, my_proj, my_templ)

for src_dir, dirs, files in os.walk(proj):
    dst_dir = src_dir.replace(proj, templ, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)
