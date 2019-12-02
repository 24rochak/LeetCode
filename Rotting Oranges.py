def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    ans = 0
    while True:
        temp = [row[:] for row in grid]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    continue
                else:
                    if (i - 1) >= 0 and grid[i - 1][j] == 1:
                        count += 1
                        temp[i - 1][j] = 2
                    if (i + 1) < len(grid) and grid[i + 1][j] == 1:
                        count += 1
                        temp[i + 1][j] = 2
                    if (j - 1) >= 0 and grid[i][j - 1] == 1:
                        count += 1
                        temp[i][j - 1] = 2
                    if (j + 1) < len(grid[0]) and grid[i][j + 1] == 1:
                        count += 1
                        temp[i][j + 1] = 2

        if count == 0:
            for row in grid:
                for item in row:
                    if item == 1:
                        return -1
            return ans
        else:
            grid = temp
            ans += 1


grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(orangesRotting(grid))
