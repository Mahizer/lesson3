# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    min_num = min(arg1, arg2, arg3)
    return arg1 + arg2 + arg3 - min_num


print(my_func(100, 200, 300))
