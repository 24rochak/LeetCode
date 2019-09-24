def replace(nums, i):
    for j in range(0, (len(nums) - i) // 2):
        nums[j + i], nums[-j - 1] = nums[-j - 1], nums[j + i]


def nextPermutation(nums):
    if len(nums) <= 1:
        return nums
    i = len(nums) - 1
    while i >= 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i > 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        print("before: ", nums)
        replace(nums, i)
        print("after:  ", nums)
    else:
        replace(nums, 0)

    return nums


nums = [3, 2, 1]
ans = nextPermutation(nums)
print(ans)
