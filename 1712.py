A, B, C = map(int, input().split())

if  B<C:
    N = A // (C - B) + 1
    print(int(N))
else:
    print(-1)
