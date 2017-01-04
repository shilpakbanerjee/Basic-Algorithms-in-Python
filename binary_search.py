# Uses python3
import sys

def binary_search(a, x, left, right):
    #left, right = 0, len(a)
    # write your code here
    #print(left, right)
    if (left > right - 1):
        return -1
    mid = left + int((right - left) // 2)
    #print(mid)
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, left, mid)
    else:
        return binary_search(a, x, mid + 1, right)
    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #print(a)
    #for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
    #print('\n')
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, n), end = ' ')
    
