a, c = [str(i) for i in input().split()], []
for i in a:
    if i not in c and a.count(i) > 1:
        c.append(i)
        print(i, end=' ')