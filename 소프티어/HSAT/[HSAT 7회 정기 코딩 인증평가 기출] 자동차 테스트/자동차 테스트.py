import sys
import random
import math
N,Q = map(int, input().split())
cars = list(map(int, input().split()))
cars = sorted (cars)

#tc
# N = 6
# Q = 6
# cars = []
# for _ in range(N):
#     cars.append(random.randint(0,50000))
# cars = sorted (cars)
# print(cars)

def binarySearch(x):
    start = 0
    end = N
    ok = False
    while start <= end:
        mid = (start+end)//2
        if (x == cars[mid]):
            ok = True
            break
        elif (x > cars[mid]):
            start = mid+1
        else:
            end = mid-1
    if ok:
        return mid
    else:
        return -1

for _ in range(Q):
    find = int(input())

# for element in cars:
#     find = element
#     print("find:", find)
    if cars[0]<= find <= cars[-1]:
        x = binarySearch(find)
        if x != -1:
            left = x #x앞에 존재하는 자동차 개수
            right = N-x-1 #뒤에 존재하는 자동차 개수
            print(left*right)
        else:
            print(0)
    else:
        print(0)
