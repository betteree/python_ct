def solution(s):
    
    
    words = s.split(" ")
    result = []
    
    for i in words:
        
        if i:
            word = i[0].upper() + i[1:].lower()
        else:
            word = ''
        
        result.append(word)
        
    return ' '.join(result)