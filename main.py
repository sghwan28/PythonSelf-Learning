def compressString(S: str) -> str:
    d = {}
    for i in S:
        d[i] = d.get(i, 0) + 1

    print(d)
    res = ''
    for key, value in d.items():
        res += key
        res += str(value)

    print(res)

    return res if len(res) < len(S) else S

compressString("aabcccccaa")