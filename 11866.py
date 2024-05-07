N,K =map(int,input().split())
list_A=[]

for i in range(N):
    list_A.append(i+1)
result=[]
index=0

for i in range(N):
    index =(index+K-1) % len(list_A)
    
    a = list_A.pop(index)
    result.append(a)

    if len(list_A) > 0:
        index %= len(list_A)

print("<" + ", ".join(map(str, result)) + ">")