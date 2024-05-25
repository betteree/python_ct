N = int(input())
M = int(input())
list1 =[]
a =input()
list1= a.split(" ")
result =0
list1.sort()
i =0
j= N-1

while i < j :
    sum1 = int(list1[i])+int(list1[j])
    if sum1 < M:
        i += 1     
    elif sum1 > M:
        j -=1
    else:
        result +=1
        i +=1
        j -= 1
        
    


print(result)




