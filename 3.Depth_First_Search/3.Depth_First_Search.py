'''
入力例
8 7
1 2
2 4
2 5
8 6
6 7
1 3
3 8

N:ノード数 M:エッジの数
x y: エッジの始点と終点
'''

from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for i in range(M):
    x, y = map(int, input().split())
    d[x].append(y)
    d[y].append(x)

nodes = [False]*N
stack = []

s = 1  # スタート
stack.append(s)
nodes[s-1] = True

while len(stack)!=0:
    print(nodes)
    From = stack.pop()
    for To in d[From]:
        if nodes[To-1] == False:
            stack.append(To)
            nodes[To-1] = True

'''
出力例
[True, False, False, False, False, False, False, False]
[True, True, True, False, False, False, False, False]
[True, True, True, False, False, False, False, True]
[True, True, True, False, False, True, False, True]
[True, True, True, False, False, True, True, True]
[True, True, True, False, False, True, True, True]
[True, True, True, True, True, True, True, True]
[True, True, True, True, True, True, True, True]
'''