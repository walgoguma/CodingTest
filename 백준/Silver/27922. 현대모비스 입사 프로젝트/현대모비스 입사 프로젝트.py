N,K = map(int, input().split())
candidate = [[],[],[]]
for _ in range(N):
    x,y,z = map(int, input().split())
    candidate[0].append(x+y)
    candidate[1].append(y+z)
    candidate[2].append(z+x)

answer = 0
for x in candidate:
    x = sorted(x,reverse=True)
    answer = max(answer, sum(x[:K]))
print(answer)
