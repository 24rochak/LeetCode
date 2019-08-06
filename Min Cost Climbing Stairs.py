def minCostClimbingStairs(cost: [int]) -> int:
    # f1 = min if we select current element
    # f2 = min if we don't select current element
    f1 = f2 = 0
    for x in reversed(cost):
        f1, f2 = x + min(f1, f2), f1
        print("x:{%d} f1:{%d} f2:{%d}" % (x, f1, f2))
    return min(f1, f2)


cost = [10, 15, 20]
ans = minCostClimbingStairs(cost)
print(ans)
