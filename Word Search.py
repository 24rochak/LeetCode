def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]
    board[i][j] = "#"
    res = dfs(board, i + 1, j, word[1:]) or \
          dfs(board, i - 1, j, word[1:]) or \
          dfs(board, i, j + 1, word[1:]) or \
          dfs(board, i, j - 1, word[1:])
    board[i][j] = tmp
    return res


def exist(board, word):
    db = {}
    for r in board:
        for c in r:
            if c not in db:
                db[c] = 1
            else:
                db[c] += 1

    dw = {}
    for c in word:
        if c not in dw:
            dw[c] = 1
        else:
            dw[c] += 1
        if c not in db or dw[c] > db[c]:
            return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False


board = [["a", "a"]]
word = "aaa"
print(exist(board, word))
