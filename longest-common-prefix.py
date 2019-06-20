def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        lens = [len(item) for item in strs]
        lenmax = min(lens)
        if lenmax == 0:
            return ""
        it = 0
        while it < lenmax:
            chars = [item[it] for item in strs]
            if len(set(chars)) == 1:
                it += 1
            else:
                break
        return strs[0][:it]


prefix = longestCommonPrefix(["c", "c"])
print(prefix)
