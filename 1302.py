N =int(input())

dict1 = {}

for i in range(N):
    a = input()
    dict1[a] = dict1.get(a,0) +1

ans = max(dict1.values())

result = []
for book in dict1.items():
    if book[1] == ans:
        result.append(book[0])

result.sort()

print(result[0])
        





    