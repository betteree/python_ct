M = int(input())
N = int(input())
result = 0
min1 = N
for i in range(M,N+1):
    flag=0
    if i == 1 :
        continue
    for j in range(2,i):
        if i % j == 0 :
            flag = 1
            break
    if flag == 0:
        result += i
        if min1 >= i:
            min1 = i

if result != 0:
    print(result)
    print(min1)
else:
    print(-1)
