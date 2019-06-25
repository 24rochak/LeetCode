import timeit


def threesumclosest(nums, target):
    import sys
    num_locs = {}
    nums.sort()
    n = len(nums)
    for i in range(n):
        num_locs[nums[i]] = i
    i = 0
    minn = sys.maxsize
    out = 0
    while (i < n):
        left = i + 1
        right = n - 1
        while (left < right):
            summ = nums[i] + nums[left] + nums[right]
            diff = abs(summ - target)
            if (diff < minn):
                minn = diff
                out = summ
            if summ > target:
                right = list(num_locs.values())[list(num_locs.keys()).index(nums[right]) - 1]
            elif summ < target:
                left = num_locs[nums[left]] + 1
            else:
                print(summ)
                return

        i = num_locs[nums[i]] + 1

    print(out)


threesumclosest([-10, 0, -2, 3, -8, 1, -10, 8, -8, 6, -7, 0, -7, 2, 2, -5, -8, 1, -4, 6], 18)
