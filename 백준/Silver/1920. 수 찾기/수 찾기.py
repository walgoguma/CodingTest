import sys

N = int(input())
A = list(map(int,input().split()))
A = sorted(A)

M = int(input())
nums = list(map(int,input().split()))

def binarySearch(x):
    start = 0
    end = N-1
    find  = False

    while start <= end:
        mid = (end+start)//2
        if x == A[mid]:
            find = True
            break

        if x > A[mid]:
            start = mid +1
        else:
            end = mid - 1

    if find == True:
        print(1)
    else:
        print(0)

for num in nums:
    binarySearch(num)