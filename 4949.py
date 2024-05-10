

while(True):
    
    a = input()
    list =[]
    re = 1

    if a ==".":
        break

    for i in a:
        if i == "(" or i=="[":
            list.append(i)
        elif i == ")":
            if len(list) != 0 and list[-1] =="(" :
                list.pop()
                re=1
            else:
                re=0
                break

        elif i== "]":
            if len(list) !=0 and list[-1] == "[":
                list.pop()
                re = 1
            else:
                re = 0
                break

    if len(list)==0 and re:
        print('yes')
    else:
        print("no")


    

    

