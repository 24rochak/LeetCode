def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    ans = []
    for i in range(0, len(nums)):
        item = nums.pop(i)
        for j in permute(nums):
            ans.append([item] + j)
        nums.insert(i, item)

    return ans


nums = [1, 2, 3, 4]
print(len(permute(nums)))
