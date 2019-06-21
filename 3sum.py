def threeSum(nums: [int]):
    two_sums = []
    indices = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            two_sums.append(nums[i] + nums[j])
            indices.append((i, j))

    ans = []

    for i in range(len(nums)):
        for j in range(len(two_sums)):
            if -nums[i] == two_sums[j]:
                index = j
                if i != indices[index][0] and i != indices[index][1]:
                    ans.append([nums[i], nums[indices[index][0]], nums[indices[index][1]]])

    print(set(tuple(sorted(l)) for l in ans))


threeSum(
    [4, -2, -9, 9, 7, 9, 10, -15, 4, -9, -9, 8, -6, 7, -7, -2, 4, -9, -7, -11, 13, 9, 5, -8, 10, 8, -6, -1, -2, -6, 6,
     -12, 7, 4, 4, -9, -1, -1, -8, 10, 5, -10, -5, 7, 12, 4, 12, -6, 10, -10, -2, 8, 7, 10, 7, 2, -5, 9, -14, 9, -12,
     -1, 4, 2, 11, -15, 9, -13, -1, -14, 4, 12, -9, -15, -4, 10, 4, -7, -11, -9, -1, -6, 14, -9, -10, -1, 0, -8, -7, -6,
     8, -12, 0, -3, 5, -4, -11, -1, -10, 4, -8, 10, -7, -10, 2, 4, -14])
