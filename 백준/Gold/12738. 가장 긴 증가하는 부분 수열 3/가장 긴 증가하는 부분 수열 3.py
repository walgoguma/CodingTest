N = int(input())
setList = list(map(int, input().split()))

maxNum = 1
subSetList = [setList[0]]

if len(setList) > 1:
    for idx, x in enumerate(setList[1:], 1):
        if x > subSetList[-1]:
            subSetList.append(x)
        else:
            start = 0
            end = len(subSetList) - 1

            while start < end:
                mid = (start + end) // 2
                if subSetList[mid] >= x:
                    end = mid
                else:
                    start = mid + 1

            subSetList[end] = x

        maxNum = max(maxNum, len(subSetList))

print(maxNum)