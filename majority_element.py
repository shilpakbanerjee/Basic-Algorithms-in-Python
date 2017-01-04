# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here

    mid = left + int((right - left) // 2)
    left_winner = get_majority_element(a, left, mid)
    right_winner = get_majority_element(a, mid, right)
    #print(a[left:right], mid, left_winner, right_winner)
    
    if not (left_winner == -1):
        count = 0
        for item in a[left:right]:
            if item == left_winner:
                count = count + 1
        if count > (right - left) // 2:
            return left_winner
    if not (right_winner == -1):
        count = 0
        for item in a[left:right]:
            if item == right_winner:
                count = count + 1
        if count > (right - left) // 2:
            return right_winner
    return -1
        
    


    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
