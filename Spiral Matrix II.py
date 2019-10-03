def generateMatrix(n: int):
    ans = [[0 for i in range(n)] for j in range(n)]

    row_start, col_start = 0, 0
    row_end, col_end = len(ans) - 1, len(ans[0]) - 1

    count = 1
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            ans[row_start][i] = count
            count += 1
        row_start += 1

        for i in range(row_start, row_end + 1):
            ans[i][col_end] = count
            count += 1
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                ans[row_end][i] = count
                count += 1
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                ans[i][col_start] = count
                count += 1
            col_start += 1

    for row in ans:
        print(row)


n = 4
generateMatrix(n)
