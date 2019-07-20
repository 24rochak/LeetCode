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
        print(left, mid, right)
        if citations[mid] == (n - mid):
            return n - mid
        elif citations[mid] < (n - mid): # can fulfill current criteria,check if more citations can be accommodated
            left = mid + 1
        else:
            right = mid - 1 # can't fulfill current criteria, check if less length can fulfill
    return n - left


citations = [0]
ans = hIndex(citations)
print(ans)