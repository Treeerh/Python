#   1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) 
#   файл логов web-сервера nginx_logs.txt
#   (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
#   — получить список кортежей 
#   вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

#   [
#    ...
#    ('141.138.90.60', 'GET', '/downloads/product_2'),
#    ('141.138.90.60', 'GET', '/downloads/product_2'),
#    ('173.255.199.22', 'GET', '/downloads/product_2'),
#    ...
#   ]

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_r, \
        open('log_dz_1.txt', 'w', encoding='utf-8') as file_w:
    temps = []
    for idx in file_r.readlines():
        remote_addr = ''.join(idx.split()[:1])
        request_type = (''.join(idx.split('"')[1:2])[:-8]).split()[0]
        requested_resource = (''.join(idx.split('"')[1:2])[:-8]).split()[1]
        temps.append((remote_addr, request_type, requested_resource))
        file_w.write(f'{remote_addr} {request_type} {requested_resource} \n')

print(temps[:10])