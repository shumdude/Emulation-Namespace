input_list = [int(x) for x in input().split()]
output_list1 = []
output_list2 = []
output_list = []
l = len(input_list)
for i in range(-l+1, 1):
    output_list1.append(input_list[i])
for j in range(-1, l-1):
    output_list2.append(input_list[j])
for z in range(l):
    output_list.append(output_list1[z]+output_list2[z])
print(output_list)