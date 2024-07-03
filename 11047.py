N, K = map(int, input().split())
list1 = []

for i in range(N):
    a = int(input())
    list1.append(a)

count = 0

for j in range(N-1, -1, -1):
    count += K // list1[j]
    K = K % list1[j]

print(count)
