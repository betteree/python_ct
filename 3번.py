#입력 216 출력 198
N = int(input())
result=0
for i in range(N+1):
    
    a = i 
    result = i

    for j in range(len(str(i))):
        result += a % 10
        a //= 10
        
    if result == N:
        print(i)
        break

    if i == N :
        print("0")



