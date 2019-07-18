def isBadVersion(i):
    state = [0, False, False, False, True, True]
    return state[i]


def firstBadVersion(n):
    left = 1
    right = n
    while (left < right):
        mid = int((left + right) / 2)
        if not isBadVersion(mid):
            left = mid + 1
        elif isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        else:
            right = mid - 1

    return right


n = 5
ans = firstBadVersion(n)
print(ans)
