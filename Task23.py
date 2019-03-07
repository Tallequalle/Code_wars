#In mathematics, a Diophantine equation is a polynomial equation, usually with two or more unknowns, such that only the integer solutions are sought or studied.

#In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form:
#x2 - 4 * y2 = n

#(where the unknowns are x and y, and n is a given positive number) in decreasing order of the positive xi.

#If there is no solution return [] or "[]" or "". (See "RUN SAMPLE TESTS" for examples of returns).


def sol_equa(n):
    # your code
    lst = []
    for x in range(n,0,-1):
        y = 0
        while x**2 - 4 * (y**2) > 0 :
            answer =  (x - 2*y) * (x + 2*y)
            if answer == n:
                lst.append([x,y])
            y += 1
    return lst
