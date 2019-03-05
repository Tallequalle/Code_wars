#You need to write regex that will validate a password to make sure it meets the following criteria:

   # At least six characters long
   # contains a lowercase letter
   # contains an uppercase letter
   # contains a number

def search(regex, stroka):
  if len(stroka) < 6:
    return False 
  check = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
  check2 = ['!','.',';',' ']
  for i in check2:
    if i in stroka:
      return False
  for j in range(2):
    counter1 = 0
    for i in check:
      if i in stroka:
        counter1 += 1
      else:
        continue 
    if counter1 == 0:
      return False
    else:
      pass
    counter1 = 0
    check = [i.upper() for i in ''.join(check)]
  counter1 = 0
  for i in range(10):
    if str(i) in stroka:
      counter1 += 1
    else:
      continue
  if counter1 == 0:
    return False
  else:
    return True
regex = ''
search(regex, 'fjd3IR9')
