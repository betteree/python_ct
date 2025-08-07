def solution(want, number, discount):
    answer = 0
    dic1 = {}
    
    #정현이가 원하는 제품별 수량
    for i in range(len(number)):
        dic1[want[i]] = number[i]
       
    #10일간 할인하는 제품별 수량
    for i in range(0, len(discount)-9):
        dic2 = {}
        
        for j in range(i, i+10):
            if discount[j] in dic2:
                dic2[discount[j]] += 1
            else:
                dic2[discount[j]] = 1
                
        if dic1 == dic2:
            answer += 1
            
    return answer
