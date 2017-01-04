# Uses python3
import sys




def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if (right - left < 1):
        return [], 0
    if (right - left == 1):
        return [a[left]], 0
    elif (right - left == 2) and (a[left] > a[right-1]):
        return [a[right-1],a[left]], 1
    elif (right - left == 2) and (a[left] <= a[right-1]):
        return [a[left],a[right-1]], 0
    ave = (left + right) // 2
    
    A, i = get_number_of_inversions(a, left, ave)
    number_of_inversions += i
    B, i = get_number_of_inversions(a, ave, right)
    number_of_inversions += i

    
    #print(number_of_inversions)
    
    #write your code here
    #print(A,B)
    #print(A[0],B[0])
    D = []
    count = 0
    #for i in A:
    #    for j in B:
    #        if i > j:
    #            count += 1
    while (len(A)>0) and (len(B)>0):
        m, n = A[0], B[0]
        #print(m,n)
        if m <= n:
            D.append(m)
            del A[0]
        else:
            D.append(n)
            del B[0]
            count += len(A)
        #print(D)
        #print(count)
    D = D + A
    D = D + B
     
    number_of_inversions += count
    #print(D)
    return D, number_of_inversions
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    D, number_of_inversions = get_number_of_inversions(a, 0, len(a))
    print(number_of_inversions)
