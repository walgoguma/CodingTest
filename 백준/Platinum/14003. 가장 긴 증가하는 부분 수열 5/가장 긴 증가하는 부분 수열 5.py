N = int(input())
setList = list(map(int, input().split()))

maxNum = 1
subSetList = [setList[0]]
temp = [0]
currentIdx = 0

if len(setList) > 1:
    for idx, x in enumerate(setList[1:], 1):
        if x > subSetList[-1]:
            subSetList.append(x)
            temp.append(len(subSetList)-1)
        else:
            start = 0
            end = len(subSetList) - 1

            while start < end:
                mid = (start + end) // 2
                if subSetList[mid] >= x:
                    end = mid
                else:
                    start = mid + 1
            temp.append(end)
            subSetList[end] = x
            currentIdx = end
        maxNum = max(maxNum, len(subSetList))

find = maxNum-1 #찾으러는 값의 인덱스
answer  = [0]*maxNum
for i in range(N-1,-1,-1):
    if temp[i] == find:
        answer[find] = setList[i]
        find -= 1

print(maxNum)
print(*answer)