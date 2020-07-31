'''
入力例
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6

N:ノードの数　W:エッジ(辺)の数
x y z (x:始点、y:終点、z:重み)
'''
import heapq
N, W = map(int, input().split())

edge = [[] for i in range(N)]
used = [False]*N
ans = 0
for i in range(W):
    x, y, z = map(int, input().split())
    edge[x].append((z, y))
    edge[y].append((z, x))

edgelist = []
for e in edge[0]:
    heapq.heappush(edgelist, e)
used[0] = True

v = 1
while v < N:
    minedge = heapq.heappop(edgelist)
    if used[minedge[1]]:
        continue
    ans += minedge[0]
    v += 1
    used[minedge[1]] = True
    for e in edge[minedge[1]]:
        if not used[e[1]]:
            heapq.heappush(edgelist, e)
            
print(ans)

'''
出力例
5
'''
