n = int(input())
count =0

for i in range(n,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))

for j in range(n+1):
    count += 1
    if count>2:
        print(' '*(n-j)+'*'*(2*j-1))