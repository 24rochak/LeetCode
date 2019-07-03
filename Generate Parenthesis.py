def generateParenthesis(n: int):
    ans = []

    def backtrack(previous, open, close):
        if len(previous) == 2 * n:
            ans.append(previous)
        if open < n:
            backtrack(previous + '(', open + 1, close)
        if close < open:
            backtrack(previous + ')', open, close + 1)

    if n:
        backtrack('', 0, 0)

    return ans


a = generateParenthesis(3)
print(a)
print(len(a))
