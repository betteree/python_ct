N,M =map(int,input().split())

a=[]
b=[]

for i in range(M):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)

if min(a) < 6*min(b):
    if min(a) < (N%6)*min(b):
        print((N//6)*min(a) + min(a))
    else:
        print((N//6)*min(a)+(N%6)*min(b))

else:
    print(N*min(b))

