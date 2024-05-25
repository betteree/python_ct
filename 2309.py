a=[]
sum_re =0
for i in range(9):
    N = int(input())
    a.append(N)
    sum_re += N

j=0
k=1
a.sort()
while(1):
    sum_re -= a[j]
    if sum_re > 100:
        sum_re -= a[k]
        if sum_re == 100:
            break
        else :
            sum_re += a[k]
            sum_re += a[j]
            k += 1
            if k == 9:
                j += 1
                k = j+1
            continue
    elif sum_re < 100:
        sum_re += a[j]
        j += 1
        k += j+1
        continue




for i in range(len(a)):
    if i != j and i != k:
        print(a[i])

