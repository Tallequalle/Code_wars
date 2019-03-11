#Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.
#If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        pass;

    def encode(self, str):
        stroka = []
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        str = str.lower()
        str = [i for i in str]
        for letter in str:
            for i in range(len(alphabet)):
                if letter == alphabet[i] and letter in alphabet:
                    try:
                        stroka.append(alphabet[i + self.shift].uppper())
                    except:
                        stroka.append(alphabet[self.shift - (len(alphabet) - i)].upper())
                    break
                elif (letter not in alphabet):
                    stroka.append(letter)
                    break
        return ''.join(stroka)

    def decode(self, str):
        stroka = []
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        str = str.lower()
        str = [i for i in str]
        for letter in str:
            for i in range(len(alphabet)):
                if letter == alphabet[i] and letter in alphabet:
                    try:
                        stroka.append(alphabet[i - self.shift].upper())
                    except:
                        stroka.append(alphabet[len(alphabet) - (self.shift - i)].upper())
                    break
                elif (letter not in alphabet):
                    stroka.append(letter)
                    break
        return ''.join(stroka)


c = CaesarCipher(5);
c.encode('Codewars')  #'HTIJBFWX'
