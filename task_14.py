#Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

max = int(input('Введите максимальное число: '))

i = 1
while i < max:
    print(i, end= ' ')
    i *= 2

print()
