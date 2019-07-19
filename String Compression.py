def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    i = 0
    j = 1
    n = len(chars)
    while True:
        if j == len(chars):
            del chars[i + 1:j]
            if j - i != 1:
                count = j - i
                for d in str(count):
                    chars.insert(i + 1, str(d))
                    i += 1
                i = i + 1
            else:
                i += 1
            j = i + 1
            break
        elif chars[i] == chars[j]:
            j += 1
        else:
            del chars[i + 1:j]
            if j - i != 1:
                count = j - i
                for d in str(count):
                    chars.insert(i + 1, str(d))
                    i += 1
                i = i + 1
            else:
                i = i + 1
            j = i + 1
        print(i, j)

    print(chars)
    return len(chars)


inp = ["a"]
ans = compress(inp)
print(ans)
