def largestTimeFromDigits(A: [int]) -> str:
    from itertools import permutations
    ans = -1
    for h1, h2, m1, m2 in permutations(A):
        hours = 10 * h1 + h2
        mins = 10 * m1 + m2
        time = 60 * hours + mins
        if 0 <= hours <= 23 and 0 <= mins <= 59 and time > ans:
            ans = time

    return "%02d:%02d" % (divmod(ans, 60)) if ans >= 0 else ""


A = [4, 0, 0, 0]
ans = largestTimeFromDigits(A)
print(ans)
