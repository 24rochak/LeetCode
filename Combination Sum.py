def combinationSum(candidates, target):
    def ans(target, l):
        if target < 0:
            return
        elif target == 0:
            if sorted(l) not in answer:
                answer.append(sorted(l))
        for item in candidates:
            if item <= target:
                t = l.copy()
                t.append(item)
                ans(target - item, t)

    answer = []
    candidates = sorted(candidates)
    for item in candidates:
        if target % item == 0:
            answer.append([item] * (target // item))
        if item <= target:
            temp = [item]
            a = ans(target - item, temp)
            if a:
                answer.append(a)
    return answer


candidates = [1, 2]
target = 4
ans = combinationSum(candidates, target)
print(ans)
