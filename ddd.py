def solution(players, callings):

    dict1 = {}
    for i in range(len(players)):
        dict1[players[i]] = i
        
    for i in callings:
        a= dict1[i]
        re = players[a-1]   
        b= dict1[re]
        
        dict1[i] = b
        dict1[players[a-1]] = a
        
         
    sorted(dict1.items(), key= lambda item:item[1])  
        
    for j in dict1.keys:
        result.append(j)
        
    return players

players =["mumu", "soe", "poe", "kai", "mine"]
callings =["kai", "kai", "mine", "mine"]
print(solution(players,callings))