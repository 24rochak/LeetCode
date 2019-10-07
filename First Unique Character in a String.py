def firstUniqChar(s: str) -> int:
    vals = {}
    for i in range(len(s)):
        if s[i] in vals:
            vals[s[i]] = -1
        else:
            vals[s[i]] = i
    print(vals)
    for item in vals:
        if vals[item] != -1:
            return vals[item]
    return -1


s = "loveleetcvtcdode"
print(firstUniqChar(s))
