import math

# 1. Свой-Чужой
# import math
#
# n = input()
# if n > 0:
#     result = sum(range(1, n + 1))
# else:
#     result = sum(range(1, n - 1, -1))
# print(result)


# 2. Прямоугольники
# count = 0
# rect_square = int(input())
# max_side = int(math.sqrt(rect_square))
# for x in range(1, max_side+1):
#     if rect_square % x == 0:
#         count += 1
#
# print(count)


# 3. Результаты охоты
# result = ''
# animals_info = input()
# for x in range(1, 10):
#     count_digit = animals_info.count(str(x))
#     if count_digit>0:
#         result = ''.join([result, str(count_digit), str(x)])
#
# print(result)


# 4. Тот-кого-нельзя-называть
# salaries = input()
# salaries_int = list(map(int, salaries.split()))
# print(round(min(salaries_int)/max(salaries_int)*100))


# 5. Шаги
left_foot, right_foot = 0, 0
number_zones = input()
for x in range(int(number_zones)):
    steps_info = input()
    steps_info_lst = list(map(int, steps_info.split()))
    left_foot += steps_info_lst[0] * steps_info_lst[2]
    right_foot += steps_info_lst[1] * steps_info_lst[2]

print(int(abs(left_foot/100-right_foot/100)))
