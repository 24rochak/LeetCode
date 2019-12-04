def expand(S):
    """
    :type S: str
    :rtype: List[str]
    """
    res = []

    def expand2(string, start, size, prefix):
        if start == size:
            res.append(prefix)
            return

        if string[start] == "{":
            end = string.find("}", start)
            print("word is: ", string[start:end])
            for letter in string[start + 1: end].split(","):
                print("processing: ", prefix + letter)
                expand2(string, end + 1, size, prefix + letter)
        else:
            expand2(string, start + 1, size, prefix + string[start])

    expand2(S, 0, len(S), "")
    return sorted(res)


def permute(S: str):
    bfs = [""]
    mult = False
    chars = []
    for s in S:
        if s == ',':
            continue
        elif s == '{':
            mult = True
        elif s == '}':
            bfs = [st + c for st in bfs for c in chars]
            chars = []
            mult = False
        elif mult:
            chars.append(s)
        else:
            print("final else")
            bfs = [st + s for st in bfs]
        print("bfs:", bfs)
        print("char:", chars)
    return sorted(bfs)


s = "{a,b}c{d,e}f"
print(permute(s))
