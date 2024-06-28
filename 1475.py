import math

N = input()
num_list=[]
for char in N:
    num_list.append(int(char))


num_dic = {}

for num in num_list:
    if num == 6 or num == 9:
        num_dic[6] = num_dic.get(6, 0) + 1
    else:
        num_dic[num] = num_dic.get(num, 0) + 1

if num_dic.get(6, 0) != 0:
    num_dic[6] = int(math.ceil(num_dic[6]/2))

print(max(num_dic.values()))