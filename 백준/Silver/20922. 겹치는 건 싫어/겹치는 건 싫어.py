N,K = map(int, input().split())
sequence = list(map(int, input().split()))

point = 0
count = {}
temp = 0
answer = 0
while point <= N-1:
    if count.get(sequence[point],-1) != -1:
        count[sequence[point]][0] += 1
        count[sequence[point]][1].append(point)
    else:
        count[sequence[point]] = [1,[point]]

    if count[sequence[point]][0] > K:
        point = count[sequence[point]][1][0]+1
        count = {}
        answer = max(answer,temp)
        temp = 0
    else:
        temp += 1
        point += 1
answer = max(answer,temp)
print(answer)