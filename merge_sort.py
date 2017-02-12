import sys
import numpy as np

def merge_sort(a,n):
    if n <= 1:
        return a
    mid = n // 2
    b = merge_sort(a[:mid],mid)
    c = merge_sort(a[mid:],n-mid)
    return merge(b,c)

def merge(b,c):
    n1, n2 = len(b), len(c)
    d = np.array([None]*(n1+n2))
    i, j1, j2 = 0, 0, 0
    while i < n1+n2:
        if j1 == n1:
            for j in range(n2-j2):
                d[i] = c[j2+j]
                i += 1
        elif j2 == n2:
            for j in range(n1-j1):
                d[i] = b[j1+j]
                i += 1
        elif b[j1] < c[j2]:
            d[i] = b[j1]
            j1 += 1
            i += 1
        else:
            d[i] = c[j2]
            j2 += 1
            i += 1
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    a = np.array(map(int, input.split()))
    print(merge_sort(a,len(a)))
            
