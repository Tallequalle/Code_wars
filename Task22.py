#Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.

import base64
def to_base_64(string):
    #your code here
    return base64.b64encode(bytes(string, encoding = 'utf-8')).decode('utf-8')

def from_base_64(string):
    #your code here
    return base64.b64decode(string).decode('utf-8')

to_base_64('this is a string!!')
