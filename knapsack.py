# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def dynamic_optimal_weight(W, v):
    # write your code here
    n=len(v)
    v=[0]+v
    value = [[0] * (n+1) for _ in range(W+1)]
    #value[1][1]=1
    #print(value,'\n')
    
    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w][i] =  value[w][i-1]
            #print(value,'\n')
            if v[i] <= w:
                val = value[w-v[i]][i-1]+v[i]
                if val > value[w][i]:
                    value[w][i] = val
            #print(value,'\n')    
    #print(value[w])
    return value[w][n]






if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(dynamic_optimal_weight(W, w))
