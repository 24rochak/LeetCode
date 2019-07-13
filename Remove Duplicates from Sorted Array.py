def removeDuplicates(nums) -> int:
    print
    i = 0
    j = i + 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1

    print(nums)
    print(i + 1)


removeDuplicates([])
