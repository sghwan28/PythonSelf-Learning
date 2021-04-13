# import textwrap

# assert textwrap.wrap('abc',1) == ['a','b','c']
# assert textwrap.wrap('abc',2) == ['ab','c']

# print(textwrap.fill('abcd',2))  #相当于在wrap的基础上加上了换行符

# print(textwrap.shorten('Hello  World!',11,placeholder='...'))
# def turn(l: list):
#     for i in range(len(l)):
#         if l[i] == 0:
#             l[i] = 1
#         elif l[i] == 1:
#             l[i] = 0

def flipAndInvertImage(image) :
    image = [reversed(k) for k in image]
    image = [list(map(lambda a: int(not a), i)) for i in image]
    return image

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
