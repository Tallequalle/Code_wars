#In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def filter_list(l):
  'return a new list with the strings filtered out'
  lst = []
  answer = [lst.append(i) for i in l if type(i) == int]
  return lst

filter_list([1,'a','b',0,15])
