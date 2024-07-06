n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))

list1.sort(reverse=True)
result =0

for i in range(n):
    
    result0 = list1[i] *(i+1)
    result = max(result,result0)
    
print(result)

