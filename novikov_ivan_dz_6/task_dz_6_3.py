#   3. Есть два файла: в одном хранятся ФИО пользователей сайта,
#   а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь,
#   разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
#   формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
#   Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
#   задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
#   При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#   Фрагмент файла с данными о пользователях (users.csv):
#       Иванов,Иван,Иванович
#       Петров,Петр,Петрович
#   Фрагмент файла с данными о хобби (hobby.csv):
#       скалолазание,охота
#       горные лыжи
from itertools import zip_longest as zl
import json, sys

with open('users.csv', 'r', encoding='utf-8') as f_user, \
        open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    rlineusers = f_user.readlines()
    rlinehobbys = f_hobby.readlines()
    lfp_hobby = {}
    lfp = []
    hobby = []
    for rlineuser in rlineusers:
        u = ' '.join(rlineuser.split(',')).replace('\n','')
        lfp.append(u)
    for rlinehobby in rlinehobbys:
        hi = ' '.join(rlinehobby.split()).replace('\n','')
        hobby.append(hi)
    if len(lfp) < len(hobby):
        sys.exit(1)
    else:
        for l, h in zl(lfp, hobby[:len(lfp)], fillvalue=None):  # Вместо None почемуто пишет null
            lfp_hobby[l] = h


with open('lfp_hobby.csv', 'w', encoding='utf-8') as f_zer:
    lfp_hobby_str = json.dumps(lfp_hobby, ensure_ascii=False, indent=4)
    f_zer.writelines(lfp_hobby_str)

with open('lfp_hobby.csv', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(result)
