def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for x in tangerine:
        if dic.get(x):
            dic[x] += 1
        else:
            dic[x] = 1
    
    sorted_dict = dict(sorted(dic.items(), key= lambda x:x[1], reverse=True))
    
    count = 0
    for x in sorted_dict.values():    
        count += x
        answer += 1
        
        if count >= k:
            break
            
    
    
    return answer