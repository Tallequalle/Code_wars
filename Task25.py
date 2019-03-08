#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    if not s:
        return False
    elif(len(s) > 140):
        return False
    else:
        s = s.split(' ')
        s = [i.capitalize() for i in s]
        s = str('#'+''.join(s))
        return s

generate_hashtag('codewars  is  nice')
