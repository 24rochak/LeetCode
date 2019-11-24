def uniquePathsWithObstacles(matrix):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if matrix[0][0] == 1 or matrix[-1][-1] == 1:
        return 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif i == 0 and j == 0:
                matrix[i][j] = 1
            elif i == 0 and j > 0:
                matrix[i][j] = matrix[i][j - 1]
            elif j == 0 and i > 0:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    return matrix[-1][-1]


grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(uniquePathsWithObstacles(grid))
