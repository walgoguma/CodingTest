#L: 암호의 길이, C: 사용가능한 문자 개수
L,C = map(int, input().split())
usage = list(input().split())
usage = sorted(usage)
must = ['a', 'e', 'i', 'o', 'u']

visit = [0]*(C+1)
def backTracking(temp):
    if len(temp) == L:
        cntA = 0
        for x in temp:
            if x in must:
                cntA += 1
        if cntA >= 1 and L - cntA >= 2:
            if (temp == sorted(temp)):
                print(''.join(temp))
        return
    for idx, x in enumerate(usage):
        if visit[idx] == False:
            visit[idx] = True
            if len(temp)==0:
                backTracking(temp + [x])
            elif temp[-1] < x:
                backTracking(temp + [x])
            visit[idx] = False

backTracking([])