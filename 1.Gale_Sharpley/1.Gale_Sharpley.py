'''
入力例
5
3 5 1 4 2
1 2 3 4 5
1 4 3 5 2
2 5 4 1 3
4 1 5 2 3
4 1 3 2 5
5 1 2 3 4
2 3 1 5 4
3 4 2 5 1
3 1 5 2 4 
N: 男性と女性の人数は等しくN人
m: 女性1~Nの中で好きな人の順番の情報をN個入力
l: 男性1~Nの中で好きな人の順番の情報をN個入力
'''

from collections import defaultdict, deque

N = int(input())
M = [deque(map(int, input().split())) for i in range(N)]
L = [deque(map(int, input().split())) for i in range(N)]

Mpair = defaultdict(int) # 0->ペアなし、0以外->パートナーの女性
Lpair = defaultdict(int) # 0->ペアなし、0以外->パートナーの男性
noPairExistence = True

while noPairExistence:
    noPairExistence = False
    for man1 in range(1, N+1):
        if Mpair[man1] == 0: # 男性にペアがいない
            lady = M[man1-1][0] # 今最もペアになりたい対象の女性
            M[man1-1].popleft()
            if Lpair[lady] == 0: # 女性にペアがいない場合
                Mpair[man1] = lady
                Lpair[lady] = man1
            else: #女性にペアがいる場合
                noPairExistence = True
                man2 = Lpair[lady]
                for i in range(N):
                    if L[lady-1][i] == man1: # man1の方が好き
                        Mpair[man1] = lady
                        Mpair[man2] = 0
                        Lpair[lady] = man1
                        break
                    if L[lady-1][i] == man2: # man2の方が好き
                        Mpair[man1] = 0
                        Mpair[man2] = lady
                        Lpair[lady] = man2
                        break

for m,l in Mpair.items():
    print("男性{0}のペアは女性{1}です。".format(m,l))

'''
出力例
男性1のペアは女性3です。
男性2のペアは女性2です。
男性3のペアは女性1です。
男性4のペアは女性5です。
男性5のペアは女性4です。
'''
