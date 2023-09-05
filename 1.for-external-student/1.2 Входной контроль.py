# 1. Триады
# Ответ 111000101

# 2. Строковый градусник
# x = int(input())
# if x < -25:
#     result = 'жутко холодно'
# elif -26 < x < 0:
#     result = 'холодно'
# elif -1 < x < 10:
#     result = 'прохладно'
# elif 9 < x < 25:
#     result = 'тепло'
# elif 24 < x:
#     result = 'жара'
#
# print(result)


# 3. Любое чётное
# line = input()
# list_substrings = line.split()
# # print(list_substrings)
# for x in list_substrings:
#     if int(x) % 2 == 0:
#         result = x
#         break
#
# print(result)


# 4. Минимальное число
# min_element = 30000
# number_count = input()
# for x in range(int(number_count)):
#     element = input()
#     if int(element) < min_element and element.endswith('3'):
#         min_element = int(element)
#
# print(min_element)


# 5. Чётные против нечётных
# even = 0
# odd = 0
# line = input()
# list_substrings = line.split()
#
# for x in list_substrings:
#     if int(x) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# if even > odd:
#     result = 'even'
# elif even < odd:
#     result = 'odd'
# else:
#     result = 'equal'
#
# print(result)
