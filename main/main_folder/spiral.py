n = int(input())

box = [[0] * n for i in range(n)]
start = 1
step_y = 1
step_x = 1
line = 0
row = 0
for i in range(0, n):
    box[line][i] = start
    start += 1
# print(*box)

while True:
    for y in range(n-4, n, 1):
        box[y][n-1] = start
        start += 1

    for x in range(n-2, -1, -1):
        box[n-1][x] = start
        start += 1

    for y in range(n-2, n-5, -1):
        box[y][n-n] = start
        start += 1

    for x in range(n-4, n-1, 1):
        box[n-4][x] = start
        start += 1
