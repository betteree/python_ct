def solution(n):
    answer = n+1
    num = bin(n).count("1")
    
    while 1: 
        if n < answer and num == bin(answer).count("1"):
        
            break
        
        answer += 1
    
    return answer



print(solution(78))