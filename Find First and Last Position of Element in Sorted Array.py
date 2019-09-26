def searchRange(nums, target):
    def search1(i, j):
        while i <= j:
            mid = (i + j) // 2
            if target <= nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return i

    def search2(i, j):
        while i <= j:
            mid = (i + j) // 2
            if target >= nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i

    i, j = search1(0, len(nums) - 1), search2(0, len(nums) - 1)
    print(i, j)
    if i == j:
        i, j = -1, 0
    print(i, j - 1)


nums = [5, 7, 7, 8, 8, 10]
target = 10
searchRange(nums, target)
