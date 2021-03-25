'''
frequency sorting
'''

def frequency_sorting(numbers):
    a = sorted(numbers,key= lambda s: (numbers.count(s),-s),reverse= True)
    return a

# assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
# assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
# assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"

'''
reverse every ascending
'''
def reverse_ascending(items):
    s = 0
    res =[]
    while s < len(items) - 1:
        a = [items[s]]
        for i in range(s,len(items) - 1):
            if items[i] < items[i+1]:
                a.append(items[i+1])
                s += 1
            else:
                res.append(a)
                s += 1
                break

    res.append(a)
    f = []
    for i in res:
        f += i[::-1]

    return f




assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
# assert list(reverse_ascending([])) == []
# assert list(reverse_ascending([1])) == [1]
# assert list(reverse_ascending([1, 1])) == [1, 1]
# assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
