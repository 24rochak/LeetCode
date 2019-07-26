def multiply(num1: str, num2: str) -> str:
    if (len(num1) == 1 and num1[0] == '0') or (len(num2) == 1 and num2[0] == '0'):
        print(type(str(0)))
        return str(0)
    ans = [0] * (len(num1) + len(num2))
    counter = 0
    for i in range(len(num1)):
        carry = 0
        k = len(num2) - 1
        for j in reversed(range(len(ans))):
            a = int(num1[~i])
            b = int(num2[k]) if k >= 0 else 0
            carry, ans[j - counter] = divmod(ans[j - counter] + a * b + carry, 10)
            k -= 1
        counter += 1

    ans = "".join(str(i) for i in ans)
    ans = ans.lstrip('0')
    print(type(ans))
    return str(ans)


num1 = "0"
num2 = "0"
ans = multiply(num1, num2)
print(ans)
