'''
split list
'''
def split_list(items: list) -> list:
    n = len(items)
    if n == 0:
        return [[],[]]
    if n%2 == 0:
        return [items[:n//2],items[n//2:]]
    else:
        return [items[:(n//2) + 1],items[n//2 + 1:]]

# if __name__ == '__main__':
#     print("Example:")
#     print(split_list([1, 2, 3, 4, 5, 6]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
#     assert split_list([1, 2, 3]) == [[1, 2], [3]]
#     assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
#     assert split_list([1]) == [[1], []]
#     assert split_list([]) == [[], []]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

'''
all the same
'''


def all_the_same(elements:list) -> bool:
    if len(elements) == 0:
        return True
    marker = elements[0]
    flag = True
    for i in elements:
        if i != marker:
            flag = False
    return flag

# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert all_the_same([1, 1, 1]) == True
#     assert all_the_same([1, 2, 1]) == False
#     assert all_the_same(['a', 'a', 'a']) == True
#     assert all_the_same([]) == True
#     assert all_the_same([1]) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")


'''
Date and time converter
'''
def date_time(time: str) -> str:
    def cday(day: str):
        if day[0] == '0':
            return day[1]
        else:
            return day

    def cmon(mon: str):
        return d1[int(mon)]

    def chour(hour:str):
        if int(hour) == 1:
            return '{} hour'.format(cday(hour))
        else:
            return '{} hours'.format(cday(hour))

    def cmin(min:str):
        if int(min) == 1:
            return '{} minute'.format(cday(min))
        else:
            return '{} minutes'.format(cday(min))


    l1 = time.split()[0]  # day, month and year
    l2 = time.split()[1]  # hour and minute
    day = l1.split('.')[0]
    month = l1.split('.')[1]
    year = l1.split('.')[-1]
    hour = l2.split(':')[0]
    min = l2.split(':')[-1]
    mon_num = [i for i in range(1, 13)]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    d1 = dict(zip(mon_num, months))
    return '{} {} {} year {} {}'.format(cday(day),cmon(month),year,chour(hour),cmin(min))

# if __name__ == '__main__':
#     print("Example:")
#     print(date_time('01.01.2000 00:00'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
#     assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
#     assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

'''
Morse Decoder
'''
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    words = code.split('   ')
    len1 = len(words)
    s = 0
    res =[]
    while s < len1:
        for i in words:
            b = i.split(' ')
            c = [MORSE[i] for i in b]
            res.append(''.join(c))
            s += 1
    f = ' '.join(res)
    if f[0].islower():
        f = f[0].upper() + f[1:]
    return f


# if __name__ == '__main__':
#     print("Example:")
#     print(morse_decoder('... --- ...'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
#     assert morse_decoder("..--- ----- .---- ---..") == "2018"
#     assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
#     print("Coding complete? Click 'Check' to earn cool rewards!")



'''
Pawn Brotherhood 
'''
l1 = list('abcdefgh')
l2 = [1,2,3,4,5,6,7,8]
d1 = dict(zip(l1,l2))

def safe_pawns(pawns: set) -> int:

    def foo(s):
        char = s[0]
        return (d1[char], int(s[1]))

    newlist = list(map(foo, pawns))
    safe = 0
    for i in pawns:
        cor = foo(i)
        if (cor[0]-1,cor[1]-1) in newlist or (cor[0]+1,cor[1]-1) in newlist:
            safe += 1
    return safe


# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


'''
sun angle
'''

from datetime import datetime

def sun_angle(time):
    s1 = '06:00'
    s2 = time
    s3 = '18:00'
    FMT = '%H:%M'


    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    res = tdelta.seconds / 240
    if res <0 or res >180:
        return "I don't see the sun!"
    else:
        return res

# if __name__ == '__main__':
#     print("Example:")
#     print(sun_angle("07:00"))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert sun_angle("07:00") == 15
#     assert sun_angle("01:23") == "I don't see the sun!"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

