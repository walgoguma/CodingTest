#0. 입력 받기
N = int(input())
_meetingList = []
for _ in range(N):
    _meetingList.append(tuple(map(int, input().split())))

#1. 끝나는 시간 기준으로 정령하기
_meetingList.sort(key=lambda x:(x[1],x[0]))

#2. 값 초기화
answer = 0
prev = (0,0)

#3. 이전 미팅이 끝났다면 그 다음으로 빨리 끝나는 미팅이 바로 진행될 수 있는가?
for element in _meetingList:
    if (element[0] >= prev[1]):
        prev = element
        answer += 1

print(answer)
