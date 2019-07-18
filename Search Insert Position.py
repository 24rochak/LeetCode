def searchInsert(nums, target: int) -> int:
    i = 0
    while (i < len(nums) and target > nums[i]):
        i += 1

    return i


nums = [1, 3, 5, 6]
target = 7
ans = searchInsert(nums, target)
print(ans)
