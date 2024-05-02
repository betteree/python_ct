N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

i = 0

while i < len(B):
    low = 0
    high = len(A) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < B[i]:
            low = mid + 1  
        elif A[mid] > B[i]:
            high = mid - 1  
        else:
            found = True
            break

    if found:
        print(1)
    else:
        print(0)

    i += 1
