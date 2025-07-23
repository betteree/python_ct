def solution(n):
    answer = 0
    num = []
    for i in range(len(str(n))):
        num.append(n%10)
        n = n // 10
        
    num.sort(reverse = True)
    answer = ''.join(str(n) for n in num)
    
    return int(answer)