N = int(input())
have = list(map(int,input().split()))
haveDic = {}
for x in have:
    if x in haveDic :
        haveDic[x] += 1
    else:
        haveDic[x] = 1
have = sorted(list(haveDic.keys()))

M = int(input())
find = list(map(int,input().split()))

def binarySearch(x):
    start = 0
    end = len(have)-1
    while start <= end:
        mid = (start+end)//2
        if x == have[mid]:
            return haveDic[x]
        elif x > have[mid] :
            start = mid + 1
        else:
            end = mid - 1
    return 0

answer = []
for x in find:
    answer.append(binarySearch(x))
print(*answer)