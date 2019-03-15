#The makeLooper() function (make_looper in Python) takes a string (of non-zero length) as an argument. It returns a function. The function it returns will return successive characters of the string on successive invocations. It will start back at the beginning of the string once it reaches the end.

i = 0
def make_looper(string):
    string = list(string)
    length = len(string)
    global i
    if i != length:
        i += 1
        return string[i - 1]
    else:
        i = 1
        return string[i - 1]

make_looper("abc")
