def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    # print(citations)
    left = 0
    n = len(citations)
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if citations[mid] == (n - mid):
            return n - mid
        elif citations[mid] < (n - mid):
            left = mid + 1
        else:
            right = mid - 1
    return n - left


citations = []
ans = hIndex(citations)
print(ans)
