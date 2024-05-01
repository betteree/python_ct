N = int(input())
A = []
input_values1 = input().split()
for value in input_values1:
    A.append(int(value))

M = int(input())
B = []
input_values2 = input().split()
for value in input_values2:
    B.append(int(value))


for i in range(M):  
    found = 0
    for j in range(N):  
        if B[i] == A[j]:
            print(1)
            found = 1
            break
    if not found:
        print(0)
