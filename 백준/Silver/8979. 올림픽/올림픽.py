#N:국가의 수 ,K: 등수를 알고 싶은 국가
N,K = map(int,input().split())

nations = {}
for _ in range(N):
    temp = list(map(int,input().split()))
    nations[temp[0]] = temp[1:]
nations = sorted(nations.items(), key = lambda x:x[1],reverse=True)

score = 0 #현재 등수
prev = [-1,-1,-1] #이전 금은동 개수
cnt = 1 #공동 등수의 개수

for x in nations:
    nation, medal = x

    if medal == prev:
        cnt += 1
    else:
        score += cnt
        cnt = 1

    if nation == K:
        print(score)
        break
    prev = medal