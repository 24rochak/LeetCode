def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] == 0:
            _ = nums.pop(i)
            count += 1
            i -= 1
        i += 1
    nums.extend([0] * count)
    print(nums)


nums = [0, 0, 1]
moveZeroes(nums)
