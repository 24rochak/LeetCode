def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    '''l = []
    l.append(1)
    for i in range(1, len(nums)):
        l.append(l[i - 1] * nums[i-1])

    r = [0] * len(nums)
    r[len(nums) - 1] = 1
    for i in range(len(nums) - 2, -1, -1):
        r[i] = r[i + 1] * nums[i+1]
    ans = []
    for i in range(len(nums)):
        ans.append(l[i] * r[i])
    return ans'''
    l = []
    l.append(1)
    for i in range(1, len(nums)):
        l.append(l[i - 1] * nums[i - 1])

    r = 1
    for i in range(len(nums) - 1, -1, -1):
        l[i] = l[i] * r
        r = r * nums[i]

    return l


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
