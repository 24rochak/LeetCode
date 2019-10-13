def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """

    def findRank(matrix, num):
        n = len(matrix)
        i = 0
        j = n - 1
        count = 0
        while i <= n - 1 and j >= 0:
            if matrix[i][j] <= num:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count

    low = matrix[0][0]
    high = matrix[-1][-1]
    row = 0
    while low < high:
        mid = (low + high) // 2
        rank = findRank(matrix, mid)
        if rank >= k:
            high = mid
        else:
            low = mid + 1

    return low


matrix = [
    [1, 5, 9, 10],
    [10, 11, 14, 16],
    [12, 13, 17, 18],
    [16, 17, 18, 20]
]
k = 5
ans = kthSmallest(matrix, k)
print(ans)
