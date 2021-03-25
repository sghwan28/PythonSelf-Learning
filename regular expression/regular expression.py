import re

'''
Question Source: 
https://www.w3resource.com/python-exercises/re/ 

1. Write a Python program to check that a string contains only 
a certain set of characters (in this case a-z, A-Z and 0-9)

检查一个字符串中是否只有set范围的的字符，若是，return True
'''

def is_allowed(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')   # anything but a-z,A-Z,0-9 and dot
    string = charRe.search(string)
    return not bool(string)     # 反向判断，双重否定等于肯定

# print(is_allowed("ABCDEFabcdef123450"))
# print(is_allowed("*&%@#!}{"))

'''
2. Write a Python program that matches a string that has an 
a followed by zero or more b's

'''
def case2(string):
    a = re.compile(r'ab*')
    s = a.findall(string)
    return s

'''
3. Write a Python program that matches a string that has an a followed by one or more b's
'''
def case3(string):
    a = re.compile(r'ab+')
    s = a.findall(string)
    return s

'''
4. Write a Python program that matches a string that has an a followed by 0 or 1 b'
'''
def case4(string):
    a = re.compile(r'ab?')
    s = a.findall(string)
    return s

'''
5. Write a Python program that matches a string that has an a followed by three 'b'
'''
def case5(string):
    a = re.compile('ab{2,4}')   # 注意：当表达式里有函数运算时，r'string'不可使用， 这里{2，3}指示2或者三个，若为{3}则指示为3个
    s = a.findall(string)
    return s

# assert case5("ab") == []
# assert case5("aabbbbbcabbb") == ['abbbb','abbb']
# assert case5("aabbbbbcabbab") == ['abbbb','abb']


'''
6. Write a Python program to find sequences of lowercase letters joined with a underscore.
'''
def case6(string):
    a = re.compile(r'^[a-z]+_[a-z]+$')
    s = a.findall(string)
    return s

# print(case6('as_2dd_dd'))

'''
7. Write a Python program to find the sequences of one upper case letter followed by lower case letters
'''
def case7(string):
    a = re.compile(r'[A-Z][a-z]+')
    s = a.findall(string)
    return s

# print(case7('dasfdsAAdsdAdsACD'))

'''
8. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
'''
def case8(string):
    a = re.compile(r'a.*?b$')
    s = a.findall(string)
    return s

# print(case8('acbcabb'))


'''
9. 
'''
def case9(string):
    a = re.compile(r'^\w+')
    s = a.findall(string)
    return s

# print(case9(" The quick brown fox jumps over the lazy dog."))

'''
10. Write a Python program that matches a word at the end of string, with optional punctuation
'''
def case10(string):
    a = re.compile(r'\w+\S*$')
    s = a.findall(string)
    return s

# print(case10('The quick brown fox jumps over the lazy dog.'))

'''
11. Write a Python program that matches a word containing 'z'.
'''
def case11(string):
    a = re.compile(r'\w*z\w*')
    s = a.findall(string)
    return s

# print(case11('The quick brown fox jumps over the lazy dog.'))
# print(case11("Python Exercises."))

'''
12.  Write a Python program that matches a word containing 'z', not at the start or end of the word
'''
def case12(string):
    a = re.compile(r'\Bz\B')   # \B: contain z, but not at start, not at end
    s = a.findall(string)
    return s

'''
13. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores
'''
def case13(string):
    a = re.compile(r'^\w*$')
    s = a.findall(string)
    return s

# print(case13('gf gf'))
# print(case13('cs_cs'))

'''
14. Write a Python program to remove leading zeros from an IP address.
'''
def case14():
    ip = '216.08.094.196'
    string = re.sub(r'\.0*','.',ip)
    print(string)

# case14()

'''
15. Write a Python program to check for a number at the end of a string
'''
def case15(string):
    a = re.compile(r'.*[0-9]$')
    if a.match(string):
        return True
    else:
        return False
# print(case15('advd4'))

'''
16. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
'''

def case16(string):
    a = re.compile(r'[0-9]{1,3}')
    s = a.findall(string)
    print(s)

# case16('Exercises number 1, 12, 13, and 345 are important')

'''
17. Write a Python program to search a literals string in a string and 
also find the location within the original string where the pattern occurs
'''
def case17():
    pattern  = 'fox'
    text = 'The quick brown fox jumps over the lazy dog.'
    match = re.search(pattern,text)
    print((match.start(),match.end()))

# case17()

'''
18. Write a Python program to find the occurrence and position of the substrings within a string.
'''
def case18():
    text = 'Python exercises, PHP exercises, C# exercises'
    pattern = 'exercises'
    for match in re.finditer(pattern, text):   # findall 直接返回列表而非match object
        s = match.start()
        e = match.end()
        print('Found "%s" at %d:%d' % (text[s:e], s, e))

'''
19. Write a Python program to extract year, month and date from an url.
'''
def case19():
    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    a = re.compile(r'/(\d{4})/(\d{1,2})/(\d{1,2})/')
    print(a.findall(url))
case19()