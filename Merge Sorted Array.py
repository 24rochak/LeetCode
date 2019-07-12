def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i = m
    for j in range(len(nums2)):
        nums1[i] = nums2[j]
        i += 1

    nums1.sort()
    return nums1


nums1 = [0]
m = 0

nums2 = [1]
n = 1

nums1 = merge(nums1, m, nums2, n)
print(nums1)
