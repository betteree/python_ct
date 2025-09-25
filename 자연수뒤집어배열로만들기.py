def solution(n):
    answer = []
    a = str(n)
    for i in range(len(a)):
        value = int(a[len(a)-1-i])
        answer.append(value)  
    return answer