def permuteUnique(nums):
    def helper(nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            item = nums.pop(i)
            for j in helper(nums):
                ans.append([item] + j)
            nums.insert(i, item)

        return ans

    nums.sort()
    return helper(nums)


nums = [1, 1, 2]
print(permuteUnique(nums))
