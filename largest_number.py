#Uses python3

import sys

def IsGreaterOrEqual(m,n):
    #a = len(str(m))
    #b = len(str(n))
    #print(int(m) / 10**a)
    #print(int(n) / 10**b)
        
    if int(str(m)+str(n)) > (int(str(n)+str(m))):
        return True
    else:
        return False

def largest_number(a):
    #write your code here
    res = ""
    while len(a)>0:
        maxnum = a[0]
        for number in a:
            #print(number,maxnum)
            if IsGreaterOrEqual(number,maxnum):
                maxnum=number
        res=res+str(maxnum)
        del a[a.index(maxnum)]
        #print(a)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
