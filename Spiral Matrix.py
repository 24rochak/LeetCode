def spiralOrder(matrix) -> [int]:
    row_start, col_start = 0, 0
    row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1

    ans = []
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            ans.append(matrix[row_start][i])
        row_start += 1

        for i in range(row_start, row_end + 1):
            ans.append(matrix[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                ans.append(matrix[row_end][i])
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                ans.append(matrix[i][col_start])
            col_start += 1

    return ans


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

ans = spiralOrder(mat)
print(ans)
