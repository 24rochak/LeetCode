def isPerfectSquare(num: int) -> bool:
    def sqrt(A):
        x_k = 0.5
        x_k1 = 0.5 * (x_k + (A / x_k))
        error = 0.01
        while (abs(x_k1 - x_k) > error):
            x_k = x_k1
            x_k1 = 0.5 * (x_k + (A / x_k))
        return x_k1

    ans = sqrt(num)
    print(ans)
    if ans - int(ans) < 0.00001:
        return True
    else:
        return False


num = 5
ans = isPerfectSquare(num)
print(ans)
