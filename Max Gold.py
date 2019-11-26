def getMaximumGold(grid):
    row_bound = len(grid)
    col_bound = len(grid[0])
    max_gold = 0

    def dfs(row, col, gold):
        if grid[row][col] <= 0:
            return gold
        tmp = grid[row][col]
        gold += tmp
        tmp_max = gold

        # up
        if row > 0 and grid[row - 1][col]:
            grid[row][col] = 0
            tmp_max = max(tmp_max, dfs(row - 1, col, gold))
            grid[row][col] = tmp

        # left
        if col > 0 and grid[row][col - 1]:
            grid[row][col] = 0
            tmp_max = max(tmp_max, dfs(row, col - 1, gold))
            grid[row][col] = tmp

        # down
        if row + 1 < row_bound and grid[row + 1][col]:
            grid[row][col] = 0
            tmp_max = max(tmp_max, dfs(row + 1, col, gold))
            grid[row][col] = tmp

        # right
        if col + 1 < col_bound and grid[row][col + 1]:
            grid[row][col] = 0
            tmp_max = max(tmp_max, dfs(row, col + 1, gold))
            grid[row][col] = tmp

        return tmp_max

    # print dfs(4,4,0)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                max_gold = max(dfs(row, col, 0), max_gold)
    return max_gold


grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]

print(getMaximumGold(grid))
