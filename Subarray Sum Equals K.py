def count(nums, k):
    '''
    cnt = 0
    sums = 0
    d={}
    d[0] = 1
    for i in range(len(nums)):
        sums+=nums[i]
        cnt+=d.get(sums-k,0)
        d[sums] = d.get(sums,0)+1

    return cnt
    '''

    cnt = 0
    sums = [0]
    for i in range(len(nums)):
        sums.append(sums[-1] + nums[i])
    nums = [0] + nums + [0]
    for l in range(0, len(nums) - 2):
        s = sums[l]
        for i in range(1, len(nums) - l - 1):
            s = s - nums[i - 1] + nums[i + l]
            if s == k:
                cnt += 1
    return cnt


nums = [-1, -1, 1]
k = 0
print(count(nums, k))
