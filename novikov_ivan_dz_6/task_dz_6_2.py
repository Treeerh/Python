#   2. * (вместо 1) Найти IP адрес спамера и количество отправленных им
#   запросов по данным файла логов из предыдущего задания.
#   Примечания: спамер — это клиент, отправивший больше всех запросов;
#   код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


with open('nginx_logs.txt', 'r', encoding='utf-8') as file_r, \
        open('log_dz_2.txt', 'w', encoding='utf-8') as file_w:
    temps = []
    scores = {}
    for idx in file_r.readlines():
        remote_addr = ''.join(idx.split()[:1])
        request_type = (''.join(idx.split('"')[1:2])[:-8]).split()[0]
        requested_resource = (''.join(idx.split('"')[1:2])[:-8]).split()[1]
        if remote_addr in scores:
            scores[remote_addr] += 1
            file_w.write(f'{remote_addr} {request_type} {requested_resource} {scores[remote_addr]} \n')
            temps.append((remote_addr, request_type, requested_resource, scores[remote_addr]))
        else:
            scores[remote_addr] = 1
            file_w.write(f'{remote_addr} {request_type} {requested_resource} {scores[remote_addr]} \n')
            temps.append((remote_addr, request_type, requested_resource, scores[remote_addr]))

print(max(temps, key=lambda item: item[3]))
print(sorted(temps, key=lambda x: x[3], reverse=True)[:10])
