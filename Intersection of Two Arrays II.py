def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    a = {num: nums1.count(num) for num in nums1}
    b = {num: nums2.count(num) for num in nums2}

    c = []
    for item in a:
        c.extend([item] * min(a.get(item, 0), b.get(item, 0)))
    return c


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
ans = intersect(nums1, nums2)
print(ans)
