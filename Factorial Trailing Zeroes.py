def trailingZeroes(n):
    count, i = 0, 5
    while n // i > 1:
        count += n // i
        i *= 5
    return count

print(trailingZeroes(50))
