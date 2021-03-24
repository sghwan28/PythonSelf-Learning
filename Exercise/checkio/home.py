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









