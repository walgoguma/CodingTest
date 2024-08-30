from itertools import combinations

while True:
    testCase = list(map(int, input().split()))
    N, testCase = testCase[0],testCase[1:]
    if N == 0:
        break

    for case in list(combinations(testCase,6)):
        print(*list(case), end = " \n")

    print("")