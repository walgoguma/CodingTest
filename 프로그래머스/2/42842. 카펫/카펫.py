import math

def solution(brown, yellow):
    answer = []
    
    D = math.sqrt((brown-4)**2-16*yellow)
    x1 = ((brown-4)+D)/4
    y1 = (brown-4)/2-x1
    x2 = ((brown+4)+D)/4
    y2 = (brown-4)/2-x2
    
    print(x1, y1, x2, y2)
    
    if (x1>=1) and (y1>=1) and (x1>=y1):
        answer.append(x1+2)
        answer.append(y1+2)
    else:
        answer.append(x2+2)
        answer.append(y2+2)
        
    return answer