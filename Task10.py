#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.

def binary_array_to_number(arr):
  # your code
  
  return int(''.join([str(i) for i in arr]),2)

binary_array_to_number([0,1,1,0])
