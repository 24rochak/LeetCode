def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = 0
    l = [0] * len(height)
    r = [0] * len(height)
    for i in range(1, len(height)):
        l[i] = max(l[i - 1], height[i - 1])

    for i in range(len(height) - 2, -1, -1):
        r[i] = max(height[i + 1], r[i + 1])

    for i in range(len(height)):
        ans += max(min(l[i], r[i]) - height[i], 0)
    return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
