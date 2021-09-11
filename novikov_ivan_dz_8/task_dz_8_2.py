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
import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    r_file = f.readlines()
    # print(r_file[:5])
    patt_ip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    patt_datetime = re.compile(r'[\d\w/: \+]')
    # r'(?P<request_type>[a-zA-Z0-9_.+-]+)'
    # r'(?P<requested_resource>[a-zA-Z0-9_.+-]+)'
    # r'(?P<response_code>[a-zA-Z0-9_.+-]+)'
    # r'(?P<response_size>[a-zA-Z0-9_.+-]+)'
    log ={}
    for idx in r_file:
        log['remote_addr'] = patt_ip.findall(idx)
        log['request_datetime'] = patt_datetime.findall(idx)
        print(log)


