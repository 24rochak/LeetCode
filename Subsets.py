def subsets(nums):
    print(nums)
    ans = [[]]
    for num in nums:
        ans += [item + [num] for item in ans]
    return ans


nums = [1, 2, 3, 4]
print(subsets(nums))
