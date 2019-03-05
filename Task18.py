#How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
def rot13(message):
    #your code here
    #message = message.lower()
    message = list(message)
    lst = ['e','b','g','r','k','n','z','c','y','h','i','s','o','t','x','a','m','p','l','u','v','f']
    lst2 = ['r','o','t','e','x','a','m','p','l','u','v','f','b','g','k','n','z','c','y','h','i','s']
    for i in range(len(lst)):
      element = lst[i].upper()
      lst.append(element)
      element = lst2[i].upper()
      lst2.append(element)
    answer = []
    for i in range(len(message)):
      if message[i] not in lst:
        answer.append(message[i])
      else:
        for j in range(len(lst)):
          if message[i] == lst[j]:
            answer.append(lst2[j])
    return(''.join(answer))
rot13("This is my first ROT13 excercise!")
