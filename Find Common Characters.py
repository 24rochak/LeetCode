def commonChars(A):
    """
    :type A: List[str]
    :rtype: List[str]
    """
    unique = set(A[0])
    ans = []
    for item in unique:
        temp = []
        for word in A:
            temp.append(word.count(item))
        ans.extend([item] * min(temp))

    return ans


A = ["roller", "bella", "label"]
# A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
ans = commonChars(A)
print(ans)
