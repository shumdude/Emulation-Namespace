input_list = [int(i) for i in input().split()]
input_list.sort()
number = None
for j in range(len(input_list)):

    if j == 0:
        continue

    if j == len(input_list)-1:
        if input_list[j]==input_list[j-1]:
            print(input_list[j], end=' ')
            break
        else:
            break

    if (input_list[j+1] != input_list[j]) and (input_list[j-1] == input_list[j]):
        print(input_list[j], end=' ')
        continue