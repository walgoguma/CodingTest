N,M = map(int,input().split())
trees = list(map(int,input().split()))

def getTree(cut):
    cnt = 0
    for x in trees:
        if x-cut>0:
            cnt += x-cut
    return cnt

def binarySearch():
    start = 1
    end = max(trees)
    answer = 0
    while start <= end:
        mid = (start+end)//2
        result = getTree(mid)
        if result >= M:
            start = mid + 1
            answer = max(mid,answer)
        else:
            end = mid - 1
    print(answer)

binarySearch()