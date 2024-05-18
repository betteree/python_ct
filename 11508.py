N = int(input())
sum1 = 0
a=[]

for i in range(N):
    M = int(input())
    a.append(M)

a.sort(reverse=True)
sum1 =sum(a)

for j in range(N):
    if (j+1)%3 == 0:
        sum1 -= a[j]

print(sum1)