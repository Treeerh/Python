#   5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
#   чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу
#   со словарём. Проверить работу скрипта для случая,
#   когда все файлы находятся в разных папках.

from itertools import zip_longest as zl
import json, sys

users = sys.argv[1]
hobbys = sys.argv[2]
lfp_hobbys = sys.argv[3]

with open(users, 'r', encoding='utf-8') as f_user, \
        open(hobbys, 'r', encoding='utf-8') as f_hobby:
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

# print(lfp)

with open(lfp_hobbys, 'w', encoding='utf-8') as f_zer:
    lfp_hobby_str = json.dumps(lfp, ensure_ascii=False, indent=4)
    f_zer.writelines(lfp_hobby_str)

with open(lfp_hobbys, 'r', encoding='utf-8') as f:
    result = json.load(f)

# print(result)
