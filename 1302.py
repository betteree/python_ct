N =int(input())

dict1 = {}

for i in range(N):
    a = input()
    dict1[a] = dict1.get(a,0) +1

n1= dict(sorted(dict1.items()))

print(next(iter(n1.keys())))

        





    