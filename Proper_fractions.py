#For example, let's assume that d is 15: you can build a total of 8 different proper fractions between 0 and 1 with it: 1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.

def proper_fractions(n):
    if n == 1:
        return 0
    lst = []
    lst2 = []
    for i in range(1,n):
        lst.append(i)
    for i in lst:
        for j in range(2,n):
            if i % j == 0 and n % j == 0:
                lst2.append(i)
    for element in lst2:
        for i in lst:
            if element == i:
                lst.remove(i)
    return(len(lst))

proper_fractions(25)
