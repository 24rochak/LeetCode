def ncans(vals, quant1, quant2):
    i, j = 0, len(vals) - 1
    ans = 0
    q1 = 0
    q2 = 0
    while i <= j:
        if i < j:
            if vals[i] > q1:
                ans += 1
                q1 = quant1
            q1 = q1 - vals[i]
            if vals[j] > q2:
                ans += 1
                q2 = quant2
            q2 = q2 - vals[j]
        elif i == j:
            if vals[i] > q1 + q2:
                ans += 1
        i += 1
        j -= 1
    return ans


vals = [5]
q1 = 5
q2 = 7
print(ncans(vals, q1, q2))
