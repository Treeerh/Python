#   ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

#   Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку
#   до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
#   ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

#   Сформировать из обработанного списка строку:
#   в "05" часов "17" минут температура воздуха была "+05" градусов

#   Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
#   Как модифицировать это условие для чисел со знаком?
#   Примечание: если обособление чисел кавычками не будет получаться - можете вернуться
#   к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

air_temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(air_temp)

air_temp_1=[]
my_string = ''
for idx in air_temp:
    if idx.isdigit():
        air_temp_1.append('"')
        air_temp_1.append(f'{int(idx):02d}')
        air_temp_1.append('"')
        my_string += '"'+f'{int(idx):02d}'+'" '
    elif idx.startswith('+') or idx.startswith('-'):
        air_temp_1.append('"')
        air_temp_1.append(f'{idx[:1]}{int(idx[1:]):02d}')
        air_temp_1.append('"')
        my_string += '"'+f'{idx[:1]}{int(idx[1:]):02d}'+'" '
    else:
        air_temp_1.append(idx)
        my_string = my_string + idx + ' '

print(air_temp_1)
print(type(air_temp_1))

print(my_string)
print(type(my_string))


