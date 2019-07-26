def addStrings(num1: str, num2: str) -> str:
    ans = ""
    carry = 0
    length = len(num1) if len(num1) > len(num2) else len(num2)
    for i in range(length):
        a = int(num1[~i]) if i < len(num1) else 0
        b = int(num2[~i]) if i < len(num2) else 0
        carry, sum = divmod(a + b + carry, 10)
        ans += str(sum)

    if carry:
        ans += str(carry)

    return ans[::-1]


num1 = "13"
num2 = "1"
ans = addStrings(num1, num2)
print(ans)
