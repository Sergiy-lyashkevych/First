#Спільні елементи зі спільним індексом
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in range(len(a)):
    if a[i] == b[i]:
        c.append(a[i])
print(c)'''

#Прохід циклом вайл
'''a = [1,2,3,4,5]
i = 0
while len(a) > i:
    t = a[i]
    i = i + 1
    print(t)'''

#Все що менше 5 в окремий список відпрацювання continue
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i > 5:
        continue
    b.append(i)
print(b)'''

# Числа від 1 до 100 кратні 7
'''i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1'''

#факторіал числа більшого 4 та меншого 16
'''n = int(input('Vvedit chuslo bilshe 4 ta menshe 16'))
if 4 < n and n < 16 :
    res = 1
    while n > 0:
        res = res * n
        n = n - 1

    print(res)
else:
    print('you are out of range')'''
#таблиця множення на 5
'''m = 1
res = 0
while m <= 9:
    res = 5 * m
    print('5','X',m,'=',res)
    m = m + 1'''
#Прямокутник з зірочок

'''s = int(input('Vvedit shuruny'))
v = int(input('Vvedit vusotu'))
for i in range(v):
    print(end = '\n')
    
    for i in range(s):
        print('@',end =' ')'''
#Трикутник одним циклом
'''h = int(input('Vvedit vusoty'))
i = 1
while i <= h:
    print('*' * i, sep = ' ')
    print(end = '\n')
    if i == h:
        i = i - 1
        h = h - 1
        if i == 0:
            break
    else:
        i = i + 1'''
#Пісочний годинник
'''s = int(input('Vvedit shuruny'))
p = s
i = 1
while s >= 1:
    print(' ' * i, end ='')
    print('*' * s, end = '\n')
    if s == 1:
        break
    i += 1
    s = s - 2
while s <= p:
    print(' ' * i, end ='')
    print('*' * s, end = '\n')
    i -= 1
    s = s + 2'''
#Создайте список случайных чисел (размером 4 элемента).
#Создайте второй список в два раза больше первого, где первые 4 элемента должны быть равны элементам первого списка,
#а остальные элементы заполните удвоенными значением начальных. Например, Было →  [1,4,7,2] Стало → [1,4,7,2,2,8,14,4]
'''import random
a = []
b = []
c = []
for i in range(4):
    a.append(random.randint(1,100))
print(a)
for i in a:
    b.append(i * 2)
print(b)
c = a + b
print(c)'''
#4)Представьте в виде списка списков матрицу
#[  1,  2 ,   3,   4]
#[  5,  6 ,   7,   8]
#[  9,10, 11, 12]
#[13,14, 15, 16]
'''a = []
p = 1
for i in range(4):
    b = []
    for z in range(4):
        b.append(p)
        p = p + 1
    a.append(b)
print(a)'''
#Розвернути матрицю на 90 градусів
M = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
Mrotated = []
for i in range(6):
    for k in range(6):
        Mrotated.append(M[k][i])
print(Mrotated)
    





