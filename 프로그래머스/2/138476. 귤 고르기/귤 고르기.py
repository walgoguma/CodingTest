def solution(k, tangerine):
    answer = 0
    dic = {}
    
    #1. 크기별 개수 dictionary로 저장
    for x in tangerine:
        if dic.get(x):
            dic[x] += 1
        else:
            dic[x] = 1
    
    #2. 개수별로 dictionary 정렬
    sorted_dict = dict(sorted(dic.items(), key= lambda x:x[1], reverse=True))
    
    #3. 개수가 많은 귤은 먼저 택하되 그 개수가 팔려고 하는 개수보다 크거나 같으면 종료
    count = 0
    for x in sorted_dict.values():    
        count += x
        answer += 1
        
        if count >= k:
            break
            
    
    
    return answer