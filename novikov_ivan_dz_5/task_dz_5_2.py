#   2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
#   не используя ключевое слово yield.
num = 15
odd_to_15 = (idx for idx in range(1,num+1) if idx %2 != 0)


print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)

odd_to_15 = (idx for idx in range(1,num+1,2))


print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)