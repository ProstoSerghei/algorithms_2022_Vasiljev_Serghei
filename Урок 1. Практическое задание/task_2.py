"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


# O(n^2)
def my_min(arr):
    res = 0
    for i in range(len(arr)):
        cheker = True
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                cheker = False
        if cheker:
            res = arr[i]
    return res


# O(n)
def my_min2(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < res:
            res = arr[i]
    return res


temp = [2, 5, 6, 4, 9, 7, 8]

print(f'O(n^2) - квадратичная: {my_min(temp)}')
print(f'O(n) - линейная: {my_min2(temp)}')
