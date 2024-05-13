T  = int(input())
result =[]

for i in range(T):
    a=[]
    b = input()
    for j in b:
        if j == "(":
            a.append(b)
        elif j ==")":
            if len(a) != 0:
                a.pop()
            else:
                result.append("NO")
                break
    else:
        if len(a) == 0:
            result.append("YES")
        else:
            result.append("NO")


for i in result:
    print(i)