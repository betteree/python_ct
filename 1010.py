import math
T= int(input())
result =1
list =[] 
# nCr = n!//((n-r)!*r!  이 공식 쓰기 
def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(T):
    N,M = map(int,input().split(" "))
    
    result = factorial(M) // (factorial(M-N) *factorial(N))
    print(result)
