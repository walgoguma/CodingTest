def solution(players, callings):
    #등수 리스트
    rank = dict(zip(players,range(len(players))))
    
    for call in callings:
        idx = rank[call]
        rank[call] -= 1
        rank[players[idx-1]] += 1
        
        players[idx-1],players[idx] = players[idx], players[idx-1]
    
    return players