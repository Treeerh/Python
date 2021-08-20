#   Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#   Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#   Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#   Внимание: использовать только арифметические операции!
#   Ккаждому элементу списка добавить 17 и заново вычислить сумму тех чисел
#   из этого списка, сумма цифр которых делится нацело на 7.
#   * Решить задачу под пунктом b, не создавая новый список.
<<<<<<< HEAD:novikov_ivon_dz_1_1/task_dz_1_2.py
#import time
#start_time_0 = time.time()
=======
#   Вариант 1
>>>>>>> 0bfb80ba938428d4b9642a547572b9521c1a9518:novikov_ivon_dz_1/task_dz_1_2.py
clubs_0 = []
sum_0 = 0

for club_0 in range(1, 1000):
    ri = 0
    if club_0 % 2:
        numbs = str(club_0 ** 3)
        for i in numbs:
            ri += int(i)
        if not ri % 7:
            sum_0 += int(numbs)
        clubs_0.append(club_0 ** 3)

print(clubs_0)
print(sum_0)
<<<<<<< HEAD:novikov_ivon_dz_1_1/task_dz_1_2.py
#print("--- %s seconds ---" % (time.time() - start_time_0))
#   Второй вариант
#start_time_1 = time.time()
=======

#   Вариант 2
>>>>>>> 0bfb80ba938428d4b9642a547572b9521c1a9518:novikov_ivon_dz_1/task_dz_1_2.py
clubs_1 = []
sum_1 = 0

for club_1 in range(1, 1000):
    temp = 0
    if club_1 % 2:
        clubs_1.append(club_1 ** 3 + 17)
        qbs = club_1 ** 3 + 17
        while qbs:
            qbs_1 = qbs % 10
            temp += qbs_1
            qbs //= 10
        if not temp % 7:
            sum_1 += club_1 ** 3
print(clubs_1)
print(sum_1)
#print("--- %s seconds ---" % (time.time() - start_time_1))