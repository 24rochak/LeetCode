def oddCells(n, m, indices):
    mat = [[0] * m for _ in range(n)]
    for item in indices:
        mat[item[0]] = [x + 1 for x in mat[item[0]]]
        for i in range(len(mat)):
            mat[i][item[1]] += 1
        for row in mat:
            print(row)
        print("-------")
    count = 0
    for row in mat:
        for item in row:
            if item % 2 == 1:
                count += 1
    return count


n = 2
m = 3
indices = [[0, 1], [1, 1]]
print(oddCells(n, m, indices=indices))
