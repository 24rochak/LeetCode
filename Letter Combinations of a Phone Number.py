def letterCombinations(digits: str):
    conv = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            ans.append(combination)
        else:
            for alpha in conv[next_digits[0]]:
                backtrack(combination + alpha, next_digits[1:])

    ans = []
    if digits:
        backtrack("", digits)
    return ans


digits = "245"
c = letterCombinations(digits)
print(c)
print(len(c))
