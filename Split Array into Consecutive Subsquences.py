def isPossible(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    prev, p1, p2, p3 = None, 0, 0, 0

    i = 0
    while i < len(nums):
        cur = nums[i]

        count = 0
        while i < len(nums) and cur == nums[i]:
            count += 1
            i += 1

        if prev is None or cur != prev + 1:
            if p1 or p2:
                return False
            c1, c2, c3 = count, 0, 0
        else:
            if p1 + p2 > count:
                return False
            c2 = p1
            c3 = p2 + min(p3, count - (p1 + p2))
            c1 = max(count - (p1 + p2 + p3), 0)

        prev, p1, p2, p3 = cur, c1, c2, c3

    return not p1 and not p2


nums = [1, 2, 3, 3, 4, 5]
print(isPossible(nums))
