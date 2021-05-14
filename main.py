
request_list = []

def ping(t: int) -> int:
    request_list.append(t)
    n = t -3000
    for i in range(len(request_list)):
        if i < n:
            request_list.pop(0)
            print(request_list)
        else:
            break

    return len(request_list)

ping(642)
ping(1869)
ping(4921)
print(request_list)