#Given an array, find the int that appears an odd number of times.

def find_it(seq):
    counter2 = 0
    for j in seq:
      counter = 0
      counter2 = j
      for i in seq:
        if counter2 == i:
          counter +=1 
      if counter % 2 == 1:
        break
    return(counter2) 
find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
