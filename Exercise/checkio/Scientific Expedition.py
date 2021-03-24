'''
Hidden Word
'''

def checkio(text, word):
    return [1, 1, 1, 4]

# assert checkio(
# """
# DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?
# """, "ten") == [2, 14, 2, 16]

# assert checkio(
# """
# He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!
# """, "noir") == [4, 16, 7, 16]
# print("Coding complete? Click 'Check' to earn cool rewards!")

a = '''
DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?
'''
target = 'ten'
b = a.replace(' ','')
c = b.split('\n')[1:-1]
print(c)
row = 0
for i in range(len(c)):
    if target in i:
        row = i
        pass
