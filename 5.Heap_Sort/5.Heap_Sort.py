'''
入力例
6
4 2 5 3 1 6

N: 入力数
A: 配列
'''

N = int(input())
A = list(map(int, input().split()))


def Heapify(A, i, n):
    child1 = i*2 + 1
    child2 = i*2 + 2
    if child1 >= n:
        return
    if child2 < n and A[child2] > A[child1]:
        child1 = child2
    if A[child1] <= A[i]:
        return
    A[i], A[child1] = A[child1], A[i]
    Heapify(A, child1, n)


def HeapSort(A):
    # 最後尾から順番にヒープ
    for i in range(N//2)[::-1]:
        Heapify(A, i, N)

    for i in range(N)[::-1]:
        A[0], A[i] = A[i], A[0]  # 最大値はAの先頭にある
        Heapify(A, 0, i)
        print(A)

HeapSort(A)

'''
出力例
[5, 3, 4, 2, 1, 6]
[4, 3, 1, 2, 5, 6]
[3, 2, 1, 4, 5, 6]
[2, 1, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
'''