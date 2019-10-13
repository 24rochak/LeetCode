def fourSumCount(A, B, C, D):
    count, nums = 0, {}
    for i in A:
        for j in B:
            temp = i + j
            if temp in nums:
                nums[i + j] += 1
            else:
                nums[i + j] = 1

    for i in C:
        for j in D:
            temp = -i - j
            if temp in nums:
                count += nums[temp]
    return count


A = [0, 0]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(fourSumCount(A, B, C, D))
