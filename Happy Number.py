def isHappy(n: int) -> bool:
    s = set()
    while n != 1:
        if n in s:
            return False
        s.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return True


n = 1111111
ans = isHappy(n)
print(ans)
