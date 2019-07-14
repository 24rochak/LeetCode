def removeElement(nums, val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    print(nums)
    return len(nums)


arr = [1, 1, 2, 2, 1, 3, 4, 1]
new_len = removeElement(arr, 1)
print(new_len)
