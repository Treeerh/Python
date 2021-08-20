#   3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
#   Эта задача намного серьёзнее, чем может сначала показаться.

air_temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(air_temp)
for idx in air_temp:
    if idx.isdigit():
        i = air_temp.index(idx)
        air_temp.remove(idx)
        air_temp.insert(i,f'"{int(idx):02d}"')
    elif idx.startswith('+') or idx.startswith('-'):
        i = air_temp.index(idx)
        air_temp.remove(idx)
        air_temp.insert(i, f'"{idx[:1]}{int(idx[1:]):02d}"')

print(air_temp)
print(*air_temp)