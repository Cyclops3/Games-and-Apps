#!/usr/bin/python  
#finds the period of a^x mod n for given (a, n)

import math

def f(a, x, n):
    return a**x % n

def cont(n, ls):
    x = math.floor(n)
    ls.append(x)
    
    for i in range(1, 10):
        z = n - x
        print '[{0}] = {1}, <{2}> = {3}'.format(n, x, n, z)
        if z == 0:
            break
        n = 1/z
    	x = math.floor(n)
        ls.append(x)
    
    return ls

count = 1
x = 1
a = 2
n = 29

while f(a, x, n) != 1:
	count = count + 1
	x = x+1
    
res = cont(3.245, [])

for i in res:
    print i
    
print '\n{0}'.format(math.floor(1/0.25))
