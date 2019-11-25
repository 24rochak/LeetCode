def removeDuplicates(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    while True:
        new_s = ""
        i, j = 0, 1
        while j < len(s):
            if s[i] != s[j]:
                new_s += s[i]
                i += 1
                j += 1
            else:
                while j < len(s) and s[j] == s[i]:  # and j - i < k:
                    j += 1
                if j - i < k:
                    new_s += s[i:j]
                i = j
                j = i + 1
        if i<len(s):
            new_s+=s[i:]
        if new_s == s:
            break
        s = new_s
    return s
    '''
    cs = set(s)
    while True:
        ns = s
        for c in cs:
            ns = ns.replace(c * k, '')
        if s == ns:
            break
        s = ns
    return s'''


s = "acaaaacc"
k = 3
ans = removeDuplicates(s, k)
print(ans)
