descriptions_exceptions = {}
succession_of_exceptions = []
volume_descriptions = int(input())  # n
for n in range(volume_descriptions):
    i = input().split()
    descriptions_exceptions[i[0]] = []
    if len(i) > 1:
        for element in i[2:]:
            descriptions_exceptions[i[0]].append(element)
volume_succession = int(input())  # m
for m in range(volume_succession):
    i = input()
    succession_of_exceptions.append(i)


def recursion_function(input_exception, const_exception):
    global descriptions_exceptions, succession_of_exceptions
    parents = descriptions_exceptions[input_exception]  # родители, от которых наследуется ошибка
    if input_exception in succession_of_exceptions:  # есть ли переданный родитель в итоговом списке
        if succession_of_exceptions.index(input_exception) < succession_of_exceptions.index(const_exception):
            # если родитель стоит левее наследника
            return True
    if parents:  # если есть родители у ошибки
        for parent in parents:  # перебираем всех родителей
            if recursion_function(parent, const_exception):
                return True
            else:  # !такое условие нужно для того, чтобы функция, упёршаяся в стену, не возвращала None!
                continue


for element in succession_of_exceptions[1:]:  # перебираем элементы словаря наследований
    if recursion_function(element, element):  # обрабатываем ошибку
        print(element)
print(descriptions_exceptions)
print(succession_of_exceptions)

""" тесты
10
1 : 2 3 4
2 : 5 3 6 7 8 9
5 : 8
3 : 4 9
10 : 7
4
6 : 3 4
7 : 6
8 : 10 4 6 7
9
10
6
9
4
5
10
1
3
2
8
7
или
6
10
11 : 10
12 : 11
20
13 : 11 20
21 : 20
6
20
13
10
11
21
12
"""
