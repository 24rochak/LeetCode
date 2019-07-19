def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    nums = [1]
    count = 1
    while (count < n):
        stack = []
        i = 0
        j = 1
        while (True):
            if j == len(nums):
                stack.extend([j - i, nums[i]])
                break
            elif nums[i] == nums[j]:
                j += 1
            else:
                stack.extend([j - i, nums[i]])
                i = j
                j = i + 1
        # print("stack : ",stack)
        nums = stack
        count += 1

    ans = ''.join(str(i) for i in nums)
    return ans


n = 2
for i in range(n):
    ans = countAndSay(i)
    print(i, ans)
