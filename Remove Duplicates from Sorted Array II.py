def removeDuplicates(nums: [int]) -> int:
    i = 0
    while i < len(nums):
        current = nums[i]
        # print("current:{%d}" % (current))
        j = i + 1
        count = 0
        while j < len(nums) and nums[j] == current:
            # print("\t {%d} count:{%d}" % (nums[j], count))
            if count < 1:
                j += 1
                count += 1
            elif count == 1:
                nums.pop(j)
                # j += 1
        i = j
    return len(nums)


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
ans = removeDuplicates(nums)
print(ans)
