import re
'''
Hidden Word
'''

def checkio(text, word):
    b = text.replace(' ', '')
    c = b.split('\n')
    lw = word.lower()

    for i in range(len(c)):
        if word in c[i]:
            return [i + 1, c[i].index(word) + 1, i + 1, c[i].index(word) + len(word)]

    max_length = max(map(len, c))
    newc = []
    for i in c:
        newi = i.ljust(max_length, '0')
        newc.append(newi)

    num = 0
    f = []
    while num < max_length:
        res = ''
        for i in newc:
            res += i[num]
        f.append(res)
        num += 1

    f2=[]
    for i in f:
        f2.append(i.lower())

    for i in range(len(f)):
        if lw in f2[i]:
            return [f2[i].index(word) + 1, i + 1, f2[i].index(word) + len(word), i + 1]

'''
time convertor 
'''
def time_converter(time):
    min = time.split(':')[1]
    hour = int(time.split(':')[0])
    if hour == 0:
        return '{}:{} a.m.'.format(hour +12, min)
    if hour < 12:
        return '{}:{} a.m.'.format(hour, min)
    if hour == 12:
        return '{}:{} p.m.'.format(hour, min)
    if hour > 12:
        return '{}:{} p.m.'.format(hour - 12, min)

# assert time_converter('12:30') == '12:30 p.m.'
# assert time_converter('09:00') == '9:00 a.m.'
# assert time_converter('23:15') == '11:15 p.m.'

'''
Sum by type
'''
def sum_by_types(items: list):
    numsum = 0
    strsum = ''
    for i in items:
        if type(i) == int:
            numsum += i
        else:
            strsum += i

    return (strsum,numsum)

# assert sum_by_types([]) == ('', 0)
# assert sum_by_types([1, 2, 3]) == ('', 6)
# assert sum_by_types(['1', 2, 3]) == ('1', 5)
# assert sum_by_types(['1', '2', 3]) == ('12', 3)
# assert sum_by_types(['1', '2', '3']) == ('123', 0)
# assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)

'''
Similar Triangles
'''
def similar_triangles(cor1,cor2):
    def dis(c1:tuple,c2:tuple):
        return abs(((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)**0.5)

    c1 = [dis(cor1[0],cor1[1]),dis(cor1[0],cor1[2]),dis(cor1[1],cor1[2]) ]
    c2 = [dis(cor2[0], cor2[1]), dis(cor2[0], cor2[2]), dis(cor2[1], cor2[2])]

    cc1 = sorted(c1)
    cc2 = sorted(c2)
    r1 = cc1[0] / cc2[0]
    r2 = cc1[1] / cc2[1]
    r3 = cc1[2] / cc2[2]
    # if r1 - r2 <= 0.01 and r3-r2 <= 0.01:
    if r1 == r2 and r2 ==r3:
        return True
    else:
        return False

# assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
# assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
# assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
# assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
# assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
# assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'

'''
unix match
'''
import re
def unix_match(filename: str, pattern: str) -> bool:
    re_pattern = pattern.replace('.', '\.')
    re_pattern = re_pattern.replace('*', '.*')
    re_pattern = re_pattern.replace('?', '\S')
    a = re.search(re_pattern, filename)
    if a:
        return True
    else:
        return False

# assert unix_match('somefile.txt', '*') == True
# assert unix_match('other.exe', '*') == True
# assert unix_match('my.exe', '*.txt') == False
# assert unix_match('log1.txt', 'log?.txt') == True
# assert unix_match('log12.txt', 'log?.txt') == False
# assert unix_match('log12.txt', 'log??.txt') == True

'''
unix_match part 2
'''

def unix_match2(filename: str, pattern: str) -> bool:

    if filename == pattern:
        return True
    re_pattern = pattern.replace('!','^')
    print(re_pattern)
    a = re.search(re_pattern,filename)
    if a:
        return True
    else:
        return False

# print(unix_match("nametxt","name[]txt"))
# assert unix_match2('somefile.txt', 'somefile.txt') == True
# assert unix_match2('1name.txt', '[!abc]name.txt') == True
# assert unix_match2('log1.txt', 'log[!0].txt') == True
# assert unix_match2('log1.txt', 'log[1234567890].txt') == True
# assert unix_match2('log1.txt', 'log[!1].txt') == False


'''
Bird Language
'''
def translate(phrase):
    res = ''
    marker = 0
    while marker < len(phrase):
        if phrase[marker] in list('aeiouy'):
            res += phrase[marker]
            marker += 3
        elif phrase[marker] == ' ':
            res += ' '
            marker += 1
        else:
            res += phrase[marker]
            marker += 2
    return res

'''
Caps_lock 
'''
def caps_lock(text: str) -> str:

    def tab(status,i):
        if status == True:
            return i.upper()
        if status == False:
            return i

    tabstatus = False
    res = text[0]
    for i in text[1:]:
        if i.lower() != 'a':
            res += tab(tabstatus,i)
        if i.lower() == 'a':
            if tabstatus == True:
                tabstatus = False
            else:
                tabstatus = True
    return res

'''
Remove Brackets
please review this:
https://py.checkio.org/en/mission/remove-brackets/ 
'''






'''
find quotes
'''
def doit(text):
    '''

    >>> doit('Regex should return "String 1" or "String 2" or "String3" ')
    'String 1,String 2,String3'
    '''
    matches=re.findall(r'\"(.+?)\"',text)
    return ",".join(matches)

