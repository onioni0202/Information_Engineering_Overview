'''
入力例
7 9
0 1 1
1 2 2
1 3 3
2 5 10
1 4 7
3 4 1
3 6 5
4 6 8
5 4 5

N:ノードの数　W:エッジ(辺)の数
x y z (x:始点、y:終点、z:重み)
'''

import heapq


def dijkstra_heap(s):
    d = [float("inf")] * N
    used = [False] * N  # True:確定済み
    d[s] = 0
    used[s] = True
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist, e)
    v = 1
    while v < N:
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        d[minedge[1]] = minedge[0]
        used[minedge[1]] = True
        v += 1
        for e in edge[minedge[1]]:
            if not used[e[1]]:
                heapq.heappush(edgelist, (e[0] + minedge[0], e[1]))
        print(d)
    return d


N, W = map(int, input().split()) 

edge = [[] for i in range(N)]
for i in range(W):
    x, y, z = map(int, input().split())
    edge[x].append((z, y))
    edge[y].append((z, x))

print(dijkstra_heap(0))

'''
出力例
[0, 1, inf, inf, inf, inf, inf]
[0, 1, 3, inf, inf, inf, inf]
[0, 1, 3, 4, inf, inf, inf]
[0, 1, 3, 4, 5, inf, inf]
[0, 1, 3, 4, 5, inf, 9]
[0, 1, 3, 4, 5, 10, 9]
[0, 1, 3, 4, 5, 10, 9]
'''