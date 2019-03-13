#The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

def fib(n):
    if n == 0:
        return 0
    elif n in (1,2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def perimeter(n):
    sum = 0
    for i in range(n + 2):
        sum += fib(i)
    return 4 * sum

perimeter(30)
