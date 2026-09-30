from random import *


# 1 задача
a = [randint(2, 103) for _ in range(10)]
for el in range(len(a)):
    min_i = el
    for k in range(el, len(a)):
        if a[k] < a[min_i]:
            min_i = k
    a[el], a[min_i] = a[min_i], a[el]
print(a)


#2 задача
for el in range(len(a)):
    min_i = el
    for k in range(el, len(a)):
        if a[k] < a[min_i]:
            min_i = k
    a[el], a[min_i] = a[min_i], a[el]
print(a[::-1])


#3 задача
a = []
for _ in range(10):
    s = ""
    for _ in range(3):
        k = str(randint(0, 99))                 # номера делаем
        if len(k) == 1:
            k = "0" + k
        s += k + "-"
    a.append(s[:len(s) - 1])
for el in range(len(a)):
    min_i = el
    for k in range(el, len(a)):
        n1 = a[k].replace("-", "")
        n2 = a[min_i].replace("-", "")              # сортируем телефоны
        if n1 < n2:
            min_i = k
    a[el], a[min_i] = a[min_i], a[el]
print(a)