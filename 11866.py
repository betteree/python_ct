N,K =map(int,input().split())
list_A=[]
for i in range(N):
    list_A.append(i+1)

print("<",end="")
for i in range(N):
    index =((i+1)*K) % len(list_A) -1
    
    if index<0:
        index += len(list_A)

    a = list_A.pop(index)
    if i < N-1:
        print(a, end=",")
    else:
        print(a,end=">")
