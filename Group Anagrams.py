def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    '''d = {}
    for item in strs:
        t = tuple(sorted(item))
        print(t)
        t = ''.join(sorted(item))
        print(t)
        if t not in d:
            d[t] = [item]
        else:
            d[t].append(item)

    return list(d.values())'''
    a = {}
    for item in strs:
        temp = [0] * 26
        for char in item:
            temp[ord(char) - 97] += 1
        if tuple(temp) not in a:
            a[tuple(temp)] = [item]
        else:
            a[tuple(temp)].append(item)
    return list(a.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = groupAnagrams(strs)
print(ans)
