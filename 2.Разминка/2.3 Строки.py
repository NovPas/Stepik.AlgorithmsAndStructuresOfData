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
# code = input()
# list_zeroes_count = [len(x) for x in code.split('1')]
# print(max(list_zeroes_count))


# 3. Нумерология Кнопочки
# sign = False
# dic = {}
# count = int(input())
# for i in range(count):
#     num_fio = input()
#     num, fio = num_fio.split()
#     dic[int(num)] = fio
#
# dic = dict(sorted(dic.items()))
#
# for key in dic:
#     tup = tuple(x for x in range(1, key + 1) if not key % x)
#     if sum(tup) % 2:
#         print(key, dic[key])
#         sign = True
#
# if not sign:
#     print('empty')


# 4. Палиндромы
# def palindrome(s):
#     s = ''.join(filter(lambda x: x.isdigit() or x.isalpha(), s))
#     s = s.upper()
#     r_iter = int(len(s)/2)
#     for x in range(r_iter):
#         if s[x] != s[-x-1]:
#             return 'NO'
#     return 'YES'
#
# s = input()
# print(palindrome(s))


# 5. Код Пифии
# res = ''
# code_s = input()
# for x in range(0, len(code_s), 2):
#     letter = code_s[x:x+2]
#     res += str(chr(int(letter, 16)))
# print(res)


# 5. Код пифии - 2
# res = ''
# code_s = input()
# for x in code_s:
#     code = ord(x)
#     res += hex(code)[2:].upper()
#
# print(res)


# Точное время
# time_input = input()
# time_add = int(input())
#
# # sec
# time_ss = int(time_input[6:])
# time_ss += time_add
# res_ss = time_ss % 60
# rest_mm = time_ss // 60
#
# # min
# time_mm = int(time_input[3:5])
# time_mm += rest_mm
# res_mm = time_mm % 60
# rest_hh = time_mm // 60
#
# # hours
# time_hh = int(time_input[0:2])
# res_hh = time_hh + rest_hh
#
# if res_hh >= 24:
#     print('23:59:59')
# else:
#     print("%s:%s:%s" % (str(res_hh).zfill(2), str(res_mm).zfill(2), str(res_ss).zfill(2)))


# Точное время - 2
# time_input = input()
# time_add = int(input())
#
# # sec
# time_ss = int(time_input[6:])
# time_ss += time_add
# res_ss = time_ss % 60
# rest_mm = time_ss // 60
#
# # min
# time_mm = int(time_input[3:5])
# time_mm += rest_mm
# res_mm = time_mm % 60
# rest_hh = time_mm // 60
#
# # hours
# time_hh = int(time_input[0:2])
# time_hh += rest_hh
# res_hh = time_hh % 24
#
# print("%s:%s:%s" % (str(res_hh).zfill(2), str(res_mm).zfill(2), str(res_ss).zfill(2)))


# Лекции Незнайки
correct_list = []
wrong_list = []
res_list = []

n = int(input())
for x in range(n):
    name = input()
    correct_list.append(name)

n = int(input())
for x in range(n):
    name = input()
    wrong_list.append(name)

for str1 in correct_list:
    summa = 0
    for str2 in wrong_list:
        if len(str1) != len(str2):
            continue
        elif tuple(str1[x] == str2[x] for x in range(len(str1))).count(False) == 1:
            summa += 1

    res_list.append(summa)

print(' '.join(map(str, res_list)))
