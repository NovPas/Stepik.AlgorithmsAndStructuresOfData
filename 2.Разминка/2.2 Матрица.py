# 1. Дороги
# trails_sum = 0
# n = int(input())
# for x in range(n):
#     str_matrix = input()
#     str_list_int = list(map(int, str_matrix.split()))
#     trails_sum += sum(str_list_int[x+1:])
#
# print(trails_sum)


# 2. Шамбала
# def draw_x(matrix, start_point, side):
#     finish_point = start_point + side
#     for i in range(start_point, finish_point):
#         for j in range(start_point, finish_point):
#             if i == finish_point-1 or i == start_point or j == finish_point-1 or j == start_point:
#                 matrix[i][j] = 'X'
#
#
# n = int(input())
# n = 2 * n - 1
# start_point = 0
# matrix = [[' '] * n for x in range(n)]
# for side in range(n, 0, -4):
#     draw_x(matrix, start_point, side)
#     start_point += 2
#
# for x in matrix:
#     print(''.join(map(str, x)))


# 3. Ход конём
# pos = input()
# x1 = ord(pos[0])-64
# y1 = int(pos[1])
# x2 = ord(pos[3])-64
# y2 = int(pos[4])
# if (abs(x2-x1) == 2 and abs(y2-y1) == 1) or (abs(x2-x1) == 1 and abs(y2-y1) == 2):
#     print('YES')
# else:
#     print('NO')


# 4. Равнобедренные треугольники

def createstring(symbols):
    str_res = ' ' * symbols
    str_res = '*' + str_res[1:-1] + ('*' if len(str_res)>1 else '')
    return str_res


n = int(input())
numbers_strings = 2 * n - 1
for x in range(0, n):
    print(createstring(x+1))
for x in range(n-1, 0, -1):
    print(createstring(x))
