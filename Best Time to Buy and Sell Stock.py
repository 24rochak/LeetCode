def maxProfit(prices: [int]) -> int:
    import sys
    profit = 0
    minprice = sys.maxsize
    for i in range(0, len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > profit:
            profit = prices[i] - minprice

    return profit


l = [3, 2, 6, 5, 0, 3]
ans = maxProfit(l)
print(ans)
