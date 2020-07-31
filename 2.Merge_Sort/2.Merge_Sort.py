'''
入力例
4
4 3 2 1

N: 入力数
A: 配列
'''

from collections import deque

N = int(input())
A = list(map(int, input().split()))


def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = A[left+i]
    for i in range(n2):
        R[i] = A[mid+i]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if right - left > 1:
        mid = (left+right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
        print(A)


mergeSort(A, 0, N)

'''
出力例
[3, 4, 2, 1]
[3, 4, 1, 2]
[1, 2, 3, 4]
'''
