import sys
import numpy as np

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(n-i-1):
            if a[min_index] > a[i+j+1]:
                a[min_index], a[i+j+1] = a[i+j+1], a[min_index]
    return a

if __name__=='__main__':
    input = sys.stdin.read()
    a = np.array(map(int, input.split()))
    print(selection_sort(a))
