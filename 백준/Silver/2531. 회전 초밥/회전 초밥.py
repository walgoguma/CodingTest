# N: 접시의 수 ,d: 초밥의 가짓수 , k: 연속해서 먹는 접시의 수, c: 쿠폰 번호
N,d,k,c = map(int,input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))

sushi = sushi+sushi[:k-1]

answer = 0
candidated = 0

for i in range(N):
    temp = set(sushi[i:i+k])

    if len(temp) >= answer:
        if list(temp).count(c) == 0:
            candidated = temp
            answer = len(temp)+1
        else:
            candidated = temp
            answer = len(temp)

print(answer)