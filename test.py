prices = [2, 5, 7, 8, 9, 18, 2, 2]
budget = 47
prices = [0] + prices + [0]
#  0  1  2  3  4  5  6   7  8  9
# [0, 2, 5, 7, 8, 9, 18, 2, 2, 0]

for L in range(len(prices) - 2, 0, -1):
    S = sum(prices[1:L + 1])
    for i in range(1, len(prices) - L):
        S = S - prices[i - 1] + prices[i + L]
        if S == budget:
            print(L + 1, i - 1, prices[i:i + L + 1])
