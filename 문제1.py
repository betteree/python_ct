n = int(input())

if n == 1 or n == 3:
    print(-1)
else:
    a = n//5
    b = n % 5
    c = b // 2
    d = b % 2
    if d != 0:
        a -= 1
        c = (b+5) //2   
    print(a+c)



