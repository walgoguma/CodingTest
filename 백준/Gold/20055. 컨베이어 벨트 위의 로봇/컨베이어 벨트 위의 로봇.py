#N:내리는 위치, K:내구도 제한
N, K = map(int,input().split())
temp = list(map(int,input().split()))
temp = [[temp[x],0] for x in range(2*N)]
convBelt = [temp[:N],temp[N:][::-1]]

def rotate(belt):
    a,b = belt[0][-1], belt[1][0]
    belt[0] = [b]+belt[0][:N-1]
    belt[1] = belt[1][1:] + [a]

    return belt


answer = 0

while True:
    answer += 1
    #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    convBelt = rotate(convBelt)
    convBelt[0][-1][1] = 0

    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    #로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(N-2,-1,-1):
        if convBelt[0][i][1] == 1: #만약 로봇이 존재하고
            if convBelt[0][i+1][0] > 0 and convBelt[0][i+1][1] ==0 : # 내구도가 0보다 크면 이동가능
                convBelt[0][i+1][0] -= 1
                convBelt[0][i][1] = 0
                convBelt[0][i+1][1] = 1
    convBelt[0][-1][1] = 0

    #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.

    if convBelt[0][0][0] > 0:
        convBelt[0][0][0] -= 1
        convBelt[0][0][1] = 1

    #4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    durable = 0
    for i in range(N):
        if convBelt[0][i][0] == 0:
            durable += 1
        if convBelt[1][i][0] == 0:
            durable += 1

    if durable >= K:
        print(answer)
        break