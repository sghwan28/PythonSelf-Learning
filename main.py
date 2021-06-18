from typing import List


a = [0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1]
# foo = lambda x: -1 if x == 0 else 1
# a = [foo(i) for i in a]
# print(a)

presum = [a[0]]
for i in range(1, len(a)):
    presum.append(presum[i-1] + a[i])

presum.insert(0,0)
print(presum)

d = {}
maxd = 0

for i,j in enumerate(presum):
    if j not in d:
        d[j] = i
    else:
        maxd = max(maxd, i - d[j])

# for i in range(len(presum)):
#     if presum[i] not in d.keys():
#         d[presum[i]] = i
#     else:
#         maxd = max(maxd, i - d[presum[i]])

print(maxd)

