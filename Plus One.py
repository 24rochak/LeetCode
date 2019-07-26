def plusOne(digits: [int]) -> [int]:
    a = "".join(str(i) for i in digits)
    a = str(int(a) + 1)
    return [a[i] for i in range(len(a))]


digits = [1, 2, 0]
ans = plusOne(digits)
print(ans)
