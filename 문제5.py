N = int(input())
M = int(input())
list1 =[]
a = input()
list1= a.split(" ")
result =0

i= 0
j= 0

while(1):

    if M-int(list1[i]) == int(list1[j+1]):
        result +=1
        list1.pop(j+1)
        i += 1
        j = i
        
    else:
        j += 1
        if list1[-1] == list1[j]:
            break

print(result)




