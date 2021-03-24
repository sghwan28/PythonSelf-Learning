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

if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    assert sort_by_ext(["1.cad", "2.bat", "1.aa", "1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
