N,M = map(int,input().split(" "))
J = int(input())

cnt =0
box = M
left_box = 1
for i in range(J):
    a= int(input())
    can =0
    if a > box:
        can = a-box
        cnt += a-box
        box += can
        left_box +=can

    elif a < left_box:
        can = left_box-a
        cnt += left_box -a
        left_box -= can
        box -= can

print(cnt)
        