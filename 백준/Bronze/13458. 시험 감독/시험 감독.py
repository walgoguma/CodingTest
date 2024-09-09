import math

classRoom = int(input())
students = list(map(int, input().split()))
masterManager, assistantManager = map(int, input().split())

answer = 0
for student in students:
    if (student-masterManager) > 0:
        answer += math.ceil((student-masterManager)/assistantManager)+1
    else:
        answer += 1
print(answer)