'''
入力例
5 7
0 4
0 1 10
0 2 2
1 2 6
1 3 6
3 2 3
2 4 5
3 4 8

N:ノードの数　W:エッジ(辺)の数
S:スタート G:ゴール
fr y z (x:始点、y:終点、z:重み)をW個入力
'''

from collections import defaultdict, deque

N, W = map(int, input().split())
S, G = map(int, input().split())

cap = [[0]*N for i in range(N)] # capacity 流すことができる量
flowPassed = [[0]*N for i in range(N)] # 逆辺を考慮してcapから引かれる量
gragh = defaultdict(list) # パスの情報
for i in range(W):
    fr, to, c = map(int, input().split())
    cap[fr][to] = c
    gragh[fr].append(to)
    gragh[to].append(fr)
parantsList = [-1] * N # bfsの経路を保存
cntPathCap = [0] * N # currentPathCapacity 


def bfs(start, goal):
    global parantsList
    global cntPathCap
    parantsList = [-1] * N
    cntPathCap = [0] * N
    q = deque()
    q.append(start)
    parantsList[start] = -2 # startの親は存在しない
    cntPathCap[start] = 10**9 # とりあえずいっぱい流してみる
    while len(q) != 0:
        cnt = q.popleft()
        for to in gragh[cnt]:
            if parantsList[to] == -1 and cap[cnt][to] - flowPassed[cnt][to] > 0:
                parantsList[to] = cnt 
                # 現在流れてきた量をどれぐらい次に流せるかを考慮
                cntPathCap[to] = min(cntPathCap[cnt], cap[cnt][to] - flowPassed[cnt][to]) 
                if to == goal:
                    return cntPathCap[goal]
                q.append(to)
    return 0


def edmondsKarp(start, goal):
    maxFlow = 0
    while True:
        flow = bfs(start, goal)
        if flow == 0:
            break
        maxFlow += flow
        cnt = goal # 経路をgoalからstartにたどる
        while (cnt != start):
            pre = parantsList[cnt]
            flowPassed[pre][cnt] += flow 
            flowPassed[cnt][pre] -= flow 
            cnt = pre
    return maxFlow


maxFlow = edmondsKarp(S, G)
print(maxFlow)

'''
出力例
11
'''