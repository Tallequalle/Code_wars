#Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

import itertools
def next_smaller(n):
    lst_min = []
    for i in itertools.permutations(str(n)):
        i = ''.join(i)
        if int(i) < n and int(i[0]) != 0:
            lst_min.append(i)
    if not lst_min:
        return -1
    else:
        return int(max(lst_min))

next_smaller(123456798)
