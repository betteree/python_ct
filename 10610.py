n = input()
result =-1
a=0

if '0' in n:
    for i in n:
        a += int(i)

    if a % 3 ==0:
        b = list(n)
        b.sort(reverse=True)
        result =(''.join(b))

   
if int(n) < 30:
    print(-1)

else:
    print(result)



    