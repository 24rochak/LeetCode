def findDuplicate(nums) -> int:
    if not len(nums):
        return -1
    p1 = nums[0]
    p2 = nums[0]
    print(p1, p2)
    while True:
        p1 = nums[p1]
        p2 = nums[nums[p2]]
        print(p1, p2)
        if p1 == p2:
            break

    p1 = nums[0]
    p2 = p2
    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]

    return None


nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
ans = findDuplicate(nums)
print(ans)
