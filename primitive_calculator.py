# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamic_optimal_sequence(n):
    op = [[n+10,0],[0,1]]
    for i in range(2,n+1):
        temp = [0,0,0]
        
        if i % 2 == 0:
            temp[0] = i // 2
        else:
            temp[0] = 0
            
        if i % 3 == 0:
            temp[1] = i // 3
        else:
            temp[1] = 0
            
        temp[2] = i-1

        op_temp = [op[temp[0]][0], op[temp[1]][0], op[temp[2]][0]]
        prev_number = temp[op_temp.index(min(op_temp))]
        
        
        op.append([op[prev_number][0]+1]+op[prev_number][1:]+[i])
        #print(op)
        
    return op[n][1:]





input = sys.stdin.read()
n = int(input)
sequence = list(dynamic_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
