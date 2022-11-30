# задаём параметры
length, width, mines = (int(i) for i in input().split())

# создаём пустое поле
box = [[0]*width for i in range(length)]

# расставляем мины
for i in range(mines):
    y_mine, x_mine = (int(i) for i in input().split())
    box[y_mine - 1][x_mine - 1] = '*'

# клеточки
for line in range(length):
    for row in range(width):

        # количество мин вокруг клетки
        count = 0

        if box[line][row] == '*':
            continue
        else:
            for i in range(-1, 2):
                if ((line + i) < 0) or ((line + i) > length - 1):
                    continue
                for j in range(-1, 2):
                    if ((row + j) < 0) or ((row + j) > width - 1):
                        continue
                    if box[line + i][row + j] == '*':
                        count += 1

            if count == 0:
                box[line][row] = '_'
            else:
                box[line][row] = count

# рисуем
for i in box:
    print(*i)