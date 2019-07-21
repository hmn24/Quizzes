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