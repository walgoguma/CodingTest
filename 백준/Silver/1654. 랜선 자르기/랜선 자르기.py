N,K = map(int, input().split())
cables= []
for _ in range(N):
    cables.append(int(input()))

def countCable(cut):
    cnt = 0
    for x in cables:
       cnt += x//cut
    return cnt

def binarySearch():
    start = 1
    end = max(cables)
    find = 0
    while start <= end:
        mid = (start + end) // 2
        result = countCable(mid)

        # if result == K:
        #     find = mid
        if result >= K:
            start = mid +1
            find = max(find, mid)
        else:
            end = mid - 1
    print(find)

binarySearch()