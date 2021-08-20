#   Реализовать вывод информации о промежутке времени в зависимости от его
#   продолжительности duration в секундах:
#   до минуты: <s> сек;
#   до часа: <m> мин <s> сек;
#   до суток: <h> час <m> мин <s> сек;
#   * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Ведите промежуток в секундах: '))

second = duration % 60
minute = duration % 3600 // 60
hour = duration % 86400 // 3600
day = duration // 86400     # количество целых днец

if duration < 60 :
    print(second, 'sec')
elif 60 <= duration < 3600:
    print(minute, 'min', second, 'sec')
elif 3600 <= duration < 86400:
    print(hour, 'hou', minute, 'min', second, 'sec')
else:
    print(day, 'day', hour, 'hou', minute, 'min', second, 'sec')