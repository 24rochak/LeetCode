def subsets(nums):
    print(nums)
    ans = [[]]
    for num in nums:
        ans += [item + [num] for item in ans]
    return ans


nums = ['m', 'o', 'k', 'k', 'o', 'r', 'i']
print(subsets(nums))
