'''

Sort by extension

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".
'''

def isnoextension(s:str) -> bool:
    '''
    >>> isnoextension('config.')
    True
    >>> isnoextension('.config')
    True
    >>> isnoextension('config.a')
    False
    >>> isnoextension('a.config')
    False
    >>> isnoextension('config.a.aa')
    False
    '''
    if '.' not in s:
        return True
    if s.count('.') == 1:
        if s[0] == '.':
            return True
        elif s[-1] == '.':
            return True
    return False

def sort_by_ext(files:list):
    files_withex = files[::]
    files_noex = []
    for i in files:
        if isnoextension(i):
            files_withex.remove(i)
            files_noex.append(i)

    res1 = sorted(files_noex)
    res2 = sorted(files_withex,key=lambda s:(s.split('.')[-1],s.split('.')[0]))  # sort by two keys, using tuple.
    return res1 + res2

#     assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
#     assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
#     assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
#     assert sort_by_ext(["1.cad", "2.bat", "1.aa", "1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"]

'''
Digital Multiplication 
'''

def checkio(number: int) -> int:
    res = [i for i in str(number) if i != '0']
    ini = 1
    for i in res:
        ini *= int(i)
    return ini

# assert checkio(123405) == 120
# assert checkio(999) == 729
# assert checkio(1000) == 1
# assert checkio(1111) == 1


'''
words order
'''

def words_order(text: str, words: list) -> bool:
    if len(set(words)) != len(words):
        return False
    text_list =text.split(' ')
    for i in words:
        if i not in text_list:
            return False
    for i in range(len(words)-1):
        if text_list.index(words[i]) > text_list.index(words[i+1]):
            return False
    return True

# assert words_order('hi world im here', ['world', 'here']) == True
# assert words_order('hi world im here', ['here', 'world']) == False
# assert words_order('hi world im here', ['world']) == True
# assert words_order('hi world im here', ['world', 'here', 'hi']) == False
# assert words_order('hi world im here', ['world', 'im', 'here']) == True
# assert words_order('hi world im here', ['world', 'hi', 'here']) == False
# assert words_order('hi world im here', ['world', 'world']) == False
# assert words_order('hi world im here', ['country', 'world']) == False
# assert words_order('hi world im here', ['wo', 'rld']) == False
# assert words_order('', ['world', 'here']) == False


'''

Surjection Strings

'''
def isometric_strings(str1: str, str2: str) -> bool:
    d ={}
    for i in range(len(str1)):
        d[str1[i]] = d.get(str1[i],[]) + [str2[i]]

    for i,j in d.items():
        if len(set(j)) > 1:
            return False
    return True


assert isometric_strings('add', 'egg') == True
assert isometric_strings('foo', 'bar') == False
assert isometric_strings('', '') == True
assert isometric_strings('all', 'all') == True


