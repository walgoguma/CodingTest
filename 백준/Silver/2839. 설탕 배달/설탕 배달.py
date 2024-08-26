import sys

#0. 입력
N = int(input())

answer = 0
#1.
if N>=15:
    answer = (N//15)*3
    N %= 15

#2.
while (N<15) and (N > 0):
    if N%3==0:
        answer += N//3
        break
    else:
        N -= 5
        answer += 1

#4. 출력
if answer >=2 and N == -4:
    print(answer)
elif answer >=3 and N== -3:
    print(answer+1)
elif answer >=2 and N== -1:
    print(answer+1)
elif answer >=3 and N== -2:
    print(answer+1)
elif N < 0:
    print(-1)
else:
    print(answer)