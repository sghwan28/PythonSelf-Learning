def analyzer(s: str):
    l = len(s)
    c = 1
    res = []
    for i in range(l - 1):
        if s[i] != s[i+1]:
            res.append(c)
            res.append(int(s[i]))
            c = 1
        elif s[i] == s[i + 1]:
            c += 1

    res.append(c)
    res.append(int(s[i]))


    print(res)

    if s[-1] == res[-1]:
        res[-2] += 1
    else:
        res.append(1)
        res.append(int(s[-1]))

    return res


print(analyzer('1122'))