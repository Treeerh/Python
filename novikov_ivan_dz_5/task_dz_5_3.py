#   3. Есть два списка:
#   tutors = [
#       'Иван', 'Анастасия', 'Петр', 'Сергей', 
#       'Дмитрий', 'Борис', 'Елена'
#   ]
#   klasses = [
#       '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
#   ]
#   Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#   ('Иван', '9А')
#   ('Анастасия', '7В')
#   ...
#   Количество генерируемых кортежей не должно быть больше длины списка tutors. 
#   Если в списке klasses меньше элементов, чем в списке tutors, 
#   необходимо вывести последние кортежи в виде: (<tutor>, None), например:
#   ('Станислав', None)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Сергей', 'Борис', 'Елена','Сергей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def tu_klass_0(tut,klass):
    if len(tut)-len(klass)>0:
        for i in range(len(tut)-len(klass)):
            klass.append(None)
    for idx in range(0,len(tut)):
        rez = (tut[idx],klass[idx])
        yield rez 

name = tu_klass_0(tutors, klasses)
print(name)
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))

tutors_1 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Сергей', 'Борис', 'Елена','Сергей']
klasses_1 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def tu_klass_1(tut,klass):
    if len(tut)-len(klass)>0:
        for i in range(len(tut)-len(klass)):
            klass.append(None)
    for idx_0, idx_1 in zip(tut,klass):
        yield (idx_0, idx_1) 

name_1 = tu_klass_1(tutors_1, klasses_1)
print(name_1)
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))
print(next(name_1))



