#Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
def likes(names):
    #your code here
    standart = 'like this'
    if len(names) == 0:
        return('no one likes this')
    elif (len(names) == 1):
        return(str(names[0])+' '+'likes this')
    elif (len(names) == 2):
        return(names[0]+' '+'and'+' '+names[1]+' '+standart)
    elif (len(names) == 3):
        return(names[0]+','+' '+names[1] +' '+ 'and'+' '+names[2]+' '+standart)
    elif (len(names) >3):
        return(names[0]+','+' '+names[1] +' '+ 'and'+' '+(str(int(len(names))-2))+' '+'others'+' '+standart)
    else:
        return('Error')
likes([])
likes(['Alex', 'Jacob', 'Mark', 'Max'])
