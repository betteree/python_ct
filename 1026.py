N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split())) 
A.sort()

result=0

for i in range(N):
    max_B = max(B)
    B.remove(max_B)
    result += (A[i]*max_B)
    
 
print(result)