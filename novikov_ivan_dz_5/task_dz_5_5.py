#   5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
#   Представлен список чисел. Определить элементы списка, не имеющие повторений. 
#   Сформировать из этих элементов список с сохранением порядка их 
#   следования в исходном списке, например:
#    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#   result = [23, 1, 3, 10, 4, 11]
#   Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def my_list(job_list):
    temp = {}
    for idx in job_list:
        if idx in temp:
            temp[idx] += 1
        else:
            temp[idx] = 1
    for idx in job_list:
        if temp[idx] == 1:
            yield idx
        
my = my_list(src)
print(*my)

def mylist(job_list):
    for idx in job_list:
        if job_list.count(idx) == 1:
            yield idx

my = mylist(src)
print(*my)

my = [idx for idx in src if src.count(idx) == 1]
print(my)


