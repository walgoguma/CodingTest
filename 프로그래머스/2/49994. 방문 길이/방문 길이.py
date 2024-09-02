def solution(dirs):
    answer = 0
    
    currntPath = set()
    
    x,y = (0,0)
    
    for dirc in list(dirs):
        
        if dirc == 'L':
            newX = x -1
            newY = y
        elif dirc == 'R':
            newX = x +1
            newY = y
        elif dirc == 'U':
            newX = x
            newY = y +1
        elif dirc == 'D':
            newX = x 
            newY = y -1
        
        if (-5<=newX<=5) and (-5<=newY<=5):
            if x!=newX:
                if x < newX:
                    currntPath.add((x,y,newX,newY))
                else:
                    currntPath.add((newX,newY,x,y))
            else: 
                if y < newY:
                    currntPath.add((x,y,newX,newY))
                else:
                    currntPath.add((newX,newY,x,y))
            
            
            x = newX
            y = newY

    return len(currntPath)