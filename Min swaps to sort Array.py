def minSwaps(nums):
    n = len(nums)
    arrpos = [*enumerate(nums)]
    arrpos.sort(key=lambda x: x[1])
    visited = {i: False for i in range(n)}
    count = 0
    for i in range(n):
        if visited[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size:
            count += cycle_size - 1

    return count


arr = [4, 5, 2, 1, 5]
print(minSwaps(arr))
