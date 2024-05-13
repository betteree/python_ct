T  = int(input())
a = []
result =[]
cnt1=0
cnt2=0

for i in range(T):
    while(1):
        b =input()
        if b == 13:
            break
        
        if b == "("or b == ")":
            a.append(b)
        if b== "(":
            if len(a) != 0 and a[-1] == ")":
                a.pop()
                result.append("YES")
            else:
                result.append("NO")

        elif b ==")":
            if len(a) !=0 and a[0] =="(":
                a.pop()
                result.append("YES")
            else: 
                result.append("NO")


for k in range(T):
    print(result[k])
