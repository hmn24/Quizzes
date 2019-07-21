### Quiz 1
import sys

# For memoisation purposes
val = {}

# Function to define recursion which utilises memoisation
def getUmbrellas(n, p):
    if n == 0: return 0
    if n in val.keys(): return val[n]
    res = sys.maxsize
    for j in p:
        if j <= n:
            op = getUmbrellas(n - j, p) 
            if (op != sys.maxsize) and (op + 1) < res:
                res = op + 1            
    val[n] = res
    return res

# Question to quiz
# getUmbrellas(8, [3,5])


### Quiz 2
n = 6
r = 3
ar = [1, 3, 9, 9, 27, 81]

from collections import defaultdict

def count_quadlets(ar,r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    v4 = defaultdict(int)
    count = 0
    for k in ar:
        count += v4[k]
        v4[k*r] += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
    return count

def count_triplets(ar,r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in ar:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
    return count