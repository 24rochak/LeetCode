def fourSum(nums, target: int):
    a = set()
    for i in range(0, len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                for l in range(k + 1, len(nums)):
                    a.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
    print(len(a), a)

    ans = [list(item) for item in a if sum(item) == target]
    print(ans)


nums = [1, 0, -1, 0, -2, 2]
ans = fourSum(nums, 0)
print(ans)
