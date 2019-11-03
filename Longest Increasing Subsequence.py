def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
        print(i, j, tails)
    return size
    '''dp = [0]*len(nums)
    maxans = 1
    for i in range(1,len(nums)):
        maxval = 0
        for j in range(0,i):
            if nums[i]>nums[j]:
                maxval = max(maxval,dp[j])
        dp[i] = maxval+1
        maxans = max(maxans,dp[i])

    return maxans'''


nums = []
print(lengthOfLIS(nums))
