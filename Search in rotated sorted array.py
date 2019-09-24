def search(self, nums, target):
    l, h = 0, len(nums) - 1
    while l <= h:
        m = (l + h) / 2
        if nums[m] == target:
            return m
        if nums[m] < nums[l]:
            if target > nums[h] or target < nums[m]:
                h = m - 1
            else:
                l = m + 1
        else:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                h = m - 1
    return -1
