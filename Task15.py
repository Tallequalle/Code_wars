#A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string

def is_pangram(s):
    s = s.lower()
    alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for i in alphabet:
      if i in s:
        continue
      else:
        return False
    return True

pangram = "The quick, Brown fox jumps over the lazy dog!"
is_pangram(pangram)
