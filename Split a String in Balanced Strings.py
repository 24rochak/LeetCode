def balancedStringSplit(s: str) -> int:
    l = r = count = 0
    for item in s:
        if item == 'L':
            l += 1
        else:
            r += 1
        if l == r:
            count += 1
            l = r = 0
    return count


s = "RLRRRLLRLL"
print(balancedStringSplit(s))
