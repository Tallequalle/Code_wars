#Your task is to write a function that takes a string and return a new string with all vowels removed.
def disemvowel(string):
  newstr = ""
  vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
  anti_vowels = ''.join([l for l in string if l not in vowels])
  return(''.join([l for l in string if l not in vowels]))
disemvowel("This website is for losers LOL!")
