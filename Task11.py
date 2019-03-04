#Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

#Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
def iq_test(numbers):
    #your code here
    counter1,counter2 = 0,0
    numbers = [int(i) for i in numbers.split()]
    for i in numbers:
      if i % 2 == 0: 
        counter1+=1
      else:
        counter2+=1
    if counter1 > counter2:
      for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
          return i + 1
        else:
          continue
    else:
      for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
          return i + 1
        else:
          continue
iq_test("2 4 7 8 10")
