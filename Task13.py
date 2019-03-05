#The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
#In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
def gap(g, m, n):
    # your code
    lst = []
    lst2 = []
    for i in range(m,n):
        k = 0
        for j in range(2,i):
            if i % j == 0:
                k += 1
        if k == 0:
            lst.append(i)
    for i in range(0,len(lst)-1):
        if (lst[i + 1]-lst[i] == g):
            lst2.append(lst[i])
            lst2.append(lst[i + 1])
            return(lst2)
gap(2,100,110)
