#   Склонение слова
#   Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту
#   фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:


percent = 'процент'
for idx in range(0, 101):
    if idx == 0 or idx == 11 or idx == 12 or idx == 13 or idx == 14:
        print(idx, percent + 'ов')
    elif idx % 10 == 1:
        print(idx, percent + '')
    elif idx % 10 == 2 or idx % 10 == 3 or idx % 10 == 4:
        print(idx, percent + 'а')
    else:
        print(idx, percent + 'ов')
