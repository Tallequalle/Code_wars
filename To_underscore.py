#Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.

def to_underscore(string):
    if type(string) == int:
        return str(string)
    string2 = list(string)
    if '_' in string2:
        string = string.split('_')
        string = [word.capitalize() for word in string]
        return ''.join(string)
    elif '_' not in string2:
        counter_b = []
        for element in range(len(string2)):
            if string2[element].isupper() == True:
                counter_b.append(element)
        string2 = [i.lower() for i in string2]
        string_answer = []
        for i in range(len(counter_b)):
            if i != len(counter_b) - 1:
                string_answer.append(string2[counter_b[i]:counter_b[i + 1]])
                string_answer.append('_')
            else:
                string_answer.append(string2[counter_b[i]:])
        string_answer2 = []
        for i in string_answer:
            if type(i) == list:
                for j in i:
                    string_answer2.append(j)
            else:
                string_answer2.append(i)
        return(''.join(string_answer2))

to_underscore('ThisIsBeautifulDay')
