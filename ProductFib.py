
#The Fibonacci numbers are the numbers in the following integer sequence (Fn):

def rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec(n - 1) + rec(n - 2)
    
def productFib(prod):
    n = 0
    while rec(n) < prod:
        n += 1
        if rec(n) * rec(n - 1) == prod:
            return [rec(n - 1), rec(n) , True]
        elif (rec(n) * rec(n - 1) > prod):
            return [rec(n - 1), rec(n), False]
        else:
            continue
    

productFib(5895)
