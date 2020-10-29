# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def num_sum():
    user_input = input('Введите числа через пробел: ').split()
    s = 0
    while user_input[0].upper() != 'Q':
        my_list = []
        for i in user_input:
            if i != 'Q':
                my_list.append(int(i))
            else:
                s += sum(my_list)
                return f'Сумма введенных чисел = {s}'
        s += sum(my_list)
        print(s)
        user_input = input('Введите числа через пробел: ').split()
    else:
        return f'Сумма введенных чисел = {s}'

print('Для выхода введите - Q')
print(num_sum())


