#   4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
#   (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
#   Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
#   и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
#   Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
#   В словаре должны храниться данные, полученные в результате парсинга.


from itertools import zip_longest as zl
import json, sys

with open('users.csv', 'r', encoding='utf-8') as f_user, \
        open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    rlineusers = f_user.readlines()
    rlinehobbys = f_hobby.readlines()
    lfp = []
    if len(rlineusers) < len(rlinehobbys):
        sys.exit(1)
    else:
        for rlineuser, rlinehobby in zl(rlineusers, rlinehobbys[:len(rlineusers)]):
            full_name = {}
            temp_str = rlineuser.split(',')
            if not rlinehobby:
                temp_hobby = None
            else:
                temp_hobby = ''.join(rlinehobby.replace('\n', ''))
            full_name['surname'] = temp_str[0]
            full_name['name'] = temp_str[1]
            full_name['patronymic'] = temp_str[2][:-1]
            full_name['hobby'] = temp_hobby
            lfp.append(full_name)

print(lfp)

with open('lfp_hobby_4.csv', 'w', encoding='utf-8') as f_zer:
    lfp_hobby_str = json.dumps(lfp, ensure_ascii=False, indent=4)
    f_zer.writelines(lfp_hobby_str)

with open('lfp_hobby_4.csv', 'r', encoding='utf-8') as f:
    result = json.load(f)

print(result)
