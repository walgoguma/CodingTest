#N:1~N까지의 자연수, M: 길이
N,M = map(int, input().split())

visit = [0]* (N+1)

def backTracking(temp):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(1,N+1):
        if visit[i] == False:
            visit[i] = True
            backTracking(temp+[i])
            visit[i] = False


backTracking([])