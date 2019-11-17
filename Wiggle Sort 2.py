def wiggleSort(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    nums[::2], nums[1::2] = reversed(nums[:(len(nums) + 1) // 2]), reversed(nums[(len(nums) + 1) // 2:])
    return nums


nums = [1, 5, 1, 1, 6, 4]
print(wiggleSort(nums))
