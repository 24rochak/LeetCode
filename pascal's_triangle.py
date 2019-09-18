def generate(numRows: int):
    t = None
    for i in range(numRows):
        row = []
        j = 0
        while j <= i:
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(t[j - 1] + t[j])
            j += 1

        t = row
    return t


numRows = 5
ans = generate(numRows)
print(ans)
