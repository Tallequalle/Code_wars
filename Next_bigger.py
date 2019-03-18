#You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits

import itertools
def next_bigger(n):
    lst = []
    itert = itertools.permutations(str(n))
    for i in itert:
        lst.append(int(''.join(i)))
    lst = sorted(lst)
    for i in range(len(lst)):
        if lst[i] == n:
            try:
                if lst[i + 1] != lst[i]:
                    return lst[i + 1]
            except:
                return -1

next_bigger(2017)
