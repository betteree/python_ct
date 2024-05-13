#입력 216 출력 198

N = int(input())
result = 0
a= 0
cnt=1

while(True):
    a = cnt     
    result = cnt
    a_len= len(str(a))

    for i in range(a_len):
        result += (a % 10)
        a //= 10 

    if result == N:
        break

    cnt += 1


print(cnt)


