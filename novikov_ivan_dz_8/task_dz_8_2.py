# 2. * (вместо 1) Написать регулярное выражение для
# парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях
# лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
import re,json

with open('nginx_logs.txt', 'r', encoding='utf-8') as f, \
        open('n_logs.txt', 'w', encoding='utf-8') as new_f:
    r_file = f.readlines()
    patt_ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    patt_datetime = re.compile(r'\[([\d\w/: \+]+)\]')
    request_type = re.compile(r'[A-Z]{3}')
    requested_resource = re.compile(r'(\w+/\w+)')
    response_code_size = re.compile(r'\d{1,3} \d{1,3}')
    log = {}
    for idx in r_file:
        log['remote_addr'] = patt_ip.findall(idx)
        log['request_datetime'] = patt_datetime.findall(idx)
        log['request_type'] = request_type.findall(idx)[0]
        log['requested_resource'] = requested_resource.findall(idx)[1]
        log['response_code_size'] = response_code_size.findall(idx)
        new_f.write(f'{log}\r')
