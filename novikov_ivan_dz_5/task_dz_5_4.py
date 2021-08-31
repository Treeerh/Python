#   4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
#   src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#   result = [12, 44, 4, 10, 78, 123]
#   ```

#   Подсказка: использовать возможности python, изученные на уроке.



src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def max_list(input_list):
    for idx in range(1,len(input_list)):
        if input_list[idx]>input_list[idx-1]:
            yield input_list[idx]

print([*max_list(src)])

max_list = [src[idx] for idx in range(1,len(src)) if src[idx]>src[idx-1]]
print(max_list)