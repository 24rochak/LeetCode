def isAnagram(a, b):
    # return sorted(a)==sorted(b)
    counts = {}
    for i in range(len(a)):
        if a[i] not in counts:
            counts[a[i]] = 1
        else:
            counts[a[i]] += 1
    for i in range(len(b)):
        if b[i] not in counts or counts[b[i]] < 0:
            return False
        else:
            counts[b[i]] -= 1
    print(counts)
    for item in counts:
        if counts[item] != 0:
            return False
    return True


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
