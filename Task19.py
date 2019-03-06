#In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.
import itertools
def permutations(string):
    #your code here
    string = [list(i) for i in itertools.permutations(string)]
    lst = []
    for i in range(len(string)):
        element = ''
        for j in range(len(string[i])):
            element = element + str(string[i][j])
        lst.append(element)
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return(lst2)
permutations('aabb')
