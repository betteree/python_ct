a = list(input())

flag=1
for i in range(len(a)//2):

    if a[i] == a[-1-i]:
        continue
    else:
        flag =0
        break



print(flag)
