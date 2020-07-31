"""
入力例
8 8
4 1
3 1
3 2
1 5
4 6
1 6
6 7
7 8

N:=ノード数 M:=辺数
x y: エッジの始点と終点
"""

from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)
V = defaultdict(int)

for i in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    V[y] += 1

q = deque(v for v in range(1, N) if V[v] == 0)

ans = []
while q:
    From = q.popleft()
    ans.append(From)
    for to in G[From]:
        V[to] -= 1
        if V[to] == 0:
            q.append(to)
    print(ans)

'''
出力例
[3]
[3, 4]
[3, 4, 2]
[3, 4, 2, 1]
[3, 4, 2, 1, 5]
[3, 4, 2, 1, 5, 6]
[3, 4, 2, 1, 5, 6, 7]
[3, 4, 2, 1, 5, 6, 7, 8]
'''
