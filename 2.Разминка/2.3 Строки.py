# 1. Уравнение Незнайки
# equation = input() # x+5=7
# parameter_1 = equation[0]
# parameter_2 = equation[2]
# parameter_3 = equation[4]
# sign_plus = equation[1] == '+'
#
# if parameter_1 == 'x':
#     x = int(parameter_3) + (int(parameter_2) * (-1) * (1 if sign_plus else -1))
# elif parameter_2 == 'x':
#     x = (1 if sign_plus else -1) * (int(parameter_3) - int(parameter_1))
# else:
#     x = int(parameter_1) + (int(parameter_2) * (1 if sign_plus else -1))
#
# print(x)


# 2. Шифрование Пилюлькина
code = input()
list_zeroes_count = [len(x) for x in code.split('1')]
print(max(list_zeroes_count))


# 3. Нумерология Кнопочки

