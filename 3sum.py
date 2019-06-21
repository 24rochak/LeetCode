def threeSum(nums: [int]):
    n = len(nums)
    nums.sort()
    num_locs = {}
    for i in range(n):
        num_locs[nums[i]] = i

    ans = []
    i = 0

    while i < n:
        first_num = nums[i]
        j = i + 1
        while j < n:
            second_num = nums[j]
            third_num = 0 - (first_num + second_num)
            if third_num in num_locs and num_locs[third_num] > j:
                ans.append([first_num, second_num, third_num])
            j = num_locs[second_num] + 1
        i = num_locs[first_num] + 1

    print(ans)


threeSum([8, -6, 7, -7, -2, 4, -9, -7, -6, -1, -2, -6, 6, -9])
