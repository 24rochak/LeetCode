def minPathSum(grid):
    if not grid:
        return 0
    '''prev = [grid[0][0]]*len(grid[0])
    for i in range(1,len(grid[0])):
        prev[i] = prev[i-1]+grid[0][i]

    for i in range(1,len(grid)):
        temp = [prev[0]+grid[i][0]]*len(grid[0])
        for j in range(1,len(grid[0])):
            temp[j] = min(temp[j-1],prev[j])+grid[i][j]
        prev = temp
    return prev[-1]'''
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i - 1]

    for j in range(1, len(grid)):
        grid[j][0] += grid[j - 1][0]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(minPathSum(grid))
