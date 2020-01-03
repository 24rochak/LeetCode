def removeStones(stones):
    """
    :type stones: List[List[int]]
    :rtype: int
    """
    cols = {}
    rows = {}
    for r, c in stones:
        if r not in rows:
            rows[r] = []
        if c not in cols:
            cols[c] = []
        rows[r].append(c)
        cols[c].append(r)

    ans = 0
    for row in rows:
        cnt = len(rows[row])
        print(cnt)
        if cnt <= 1:
            continue
        else:
            for col in rows[row][1:]:
                cols[col].remove(row)
            rows[row] = [rows[row][0]]
            ans += cnt - 1
        print("rows: ", rows)
        print("cols: ", cols)

    print("ans: ", ans)
    for col in cols:
        cnt = len(cols[col])
        print(cnt)
        if cnt <= 1:
            continue
        else:
            for row in cols[col]:
                rows[row].remove(col)
            cols[col] = cols[col][0]
            ans += cnt - 1
        print("rows: ", rows)
        print("cols: ", cols)
    return ans


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(removeStones(stones))
