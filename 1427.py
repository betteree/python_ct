N = int(input())

N_sort =[]
b=0
while(N>0):

    b = N % 10
    N_sort.append(b)
    N=N//10 
       
N_sort.sort(reverse=True)

for i in N_sort:
    print(i,end="")


