#Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible
#ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

import itertools

def choose_best_sum(t, k, ls):
    # your codes)
    lst = itertools.combinations(ls, k)
    summary = 0
    for i in lst:
        if sum(i) <= t and summary < sum(i):
            summary = sum(i)
    if summary == 0:
        return None
    return summary

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(230, 4, xs)
