import re

'''
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