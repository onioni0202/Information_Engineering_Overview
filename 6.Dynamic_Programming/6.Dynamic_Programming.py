'''
入力例
6 9
2 3
1 2
3 6
2 1
1 3
5 10

N:ナップサックの個数 W:持てる重さ
w v (w: 重量、v:価値)
'''

N, W = map(int, input().split())
w = [0]*N
v = [0]*N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[0]*(W+1) for i in range(N+1)]

for i in range(N):
    for g in range(W+1):
        if g >= w[i]:
            dp[i+1][g] = max(dp[i][g-w[i]]+v[i], dp[i][g])
        else:
            dp[i+1][g] = dp[i][g]

    for i in range(N+1):
        print(dp[i])
    print(".....")

print(dp[N][W])

'''
出力例
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
.....
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
[0, 2, 3, 5, 5, 5, 5, 5, 5, 5]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
.....
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
[0, 2, 3, 5, 5, 5, 5, 5, 5, 5]
[0, 2, 3, 6, 8, 9, 11, 11, 11, 11]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
.....
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
[0, 2, 3, 5, 5, 5, 5, 5, 5, 5]
[0, 2, 3, 6, 8, 9, 11, 11, 11, 11]
[0, 2, 3, 6, 8, 9, 11, 11, 12, 12]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
.....
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
[0, 2, 3, 5, 5, 5, 5, 5, 5, 5]
[0, 2, 3, 6, 8, 9, 11, 11, 11, 11]
[0, 2, 3, 6, 8, 9, 11, 11, 12, 12]
[0, 3, 5, 6, 9, 11, 12, 14, 14, 15]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
.....
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
[0, 2, 3, 5, 5, 5, 5, 5, 5, 5]
[0, 2, 3, 6, 8, 9, 11, 11, 11, 11]
[0, 2, 3, 6, 8, 9, 11, 11, 12, 12]
[0, 3, 5, 6, 9, 11, 12, 14, 14, 15]
[0, 3, 5, 6, 9, 11, 13, 15, 16, 19]
.....
19
'''