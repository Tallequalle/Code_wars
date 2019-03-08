#Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format
def mixed_fraction(s):
    x, y = s.split('/')[0],s.split('/')[1]
    x, y = int(x),int(y)
    answer = int(x / y)
    if x % y == 0:
        return(str(answer))
    elif (answer == 0):
        d = []
        for i in range(1,max(x, y)):
            if y%i == 0 and x%i == 0:
                d.append(int(i))   
        return ''.join((str(int(x/(max(d))))+'/'+str(int(y/max(d)))))
    else:
        ch = x % (y*answer)
        d = []
        for i in range(1,max(ch,y)):
            if y%i == 0 and ch%i == 0:
                d.append(i)
        if not d:
            return ' '.join((str(answer), str(abs(int(ch)))+'/'+str(abs(int(y)))))
        else:
            return ' '.join((str(answer),str(abs(int(ch/(max(d)))))+'/'+str(int(y/max(d)))))
                
