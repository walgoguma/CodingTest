N = int(input())

children = []
for _ in range(N):
    children.append(int(input()))

order_children = [children[0]]

for idx, x in enumerate(children[1:],1):
    if x > order_children[-1]:
        order_children.append(x)
    else:
        start = 0
        end = len(order_children)-1
        mid = (end + start) // 2
        while start < end:
             mid = (end + start)//2
             if x > order_children[mid]:
                 start = mid+1
             else:
                 end = mid
        order_children[end] = x

print(N-len(order_children))