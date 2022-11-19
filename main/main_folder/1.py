objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
k = 0
for i in objects:
    k += 1
    while True:
        loop = []
        for x in objects:
            loop.append(x)
        for j in loop:
            if (i is j):
                objects.remove(j)
        objects.insert(0, 1)
        break
print(k)

# print( len( { id(i) for i in objects } ) )