def solution(brown, yellow):
    answer = []
    i = 1
    while(True):
        if (yellow % i == 0 ):
            if (brown  == i*2 + (yellow// i *2) + 4):
                answer.append(yellow// i +2)
                answer.append(i+2)
                
                break
                
        i += 1
    return answer