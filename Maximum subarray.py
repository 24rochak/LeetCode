def maxSubArray(nums: [int]) -> int:
    tot = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1], 0) + nums[i]
        if nums[i] > tot:
            tot = nums[i]

    return tot


l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

ans = maxSubArray(l)
print(ans)
