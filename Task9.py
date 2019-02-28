def order(sentence):
  # code here
  dict = {}
  lst = []
  for i in sentence.split():
    for j in range(len(sentence.split()) + 1):
      if str(j) in i:
        dict[j] = i
  for i in range(1,len(sentence.split()) + 1):
    lst.append(dict[i])
  return ' '.join(lst)
  
order("is2 Thi1s T4est 3a")
