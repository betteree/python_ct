import math
N = int(input())
list1 =[]
b=''
for j in range(1,N+1):
    list1.append(j)
    b= b+str(j)
c=''
for k in range(N,0,-1):
    c=c+str(k)


for i in range(int(b),int(c)+1):  
    flag =0
    for j in range(0,N):
        if str(list1[j]) in str(i):
            flag += 1        
            
    if flag == N :
        print(i)
        
        
    
        
        

