def addBinary(a: str, b: str) -> str:
    print(bin(int(a, 2) + int(b, 2))[2:])

    ans = ""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    while i >= 0 and j >= 0:
        temp = int(a[i]) + int(b[j]) + carry
        if temp == 0:
            ans += "0"
            carry = 0
        elif temp == 1:
            ans += "1"
            carry = 0
        elif temp == 2:
            ans += "0"
            carry = 1
        else:
            ans += "1"
            carry = 1
        i -= 1
        j -= 1

    while i >= 0:
        temp = int(a[i]) + carry
        if temp == 0:
            ans += "0"
            carry = 0
        elif temp == 1:
            ans += "1"
            carry = 0
        elif temp == 2:
            ans += "0"
            carry = 1
        else:
            ans += "1"
            carry = 1
        i -= 1

    while j >= 0:
        temp = int(b[j]) + carry
        if temp == 0:
            ans += "0"
            carry = 0
        elif temp == 1:
            ans += "1"
            carry = 0
        elif temp == 2:
            ans += "0"
            carry = 1
        else:
            ans += "1"
            carry = 1
        j -= 1
    if carry == 1:
        return (ans + str(carry))[::-1]
    else:
        return ans[::-1]


a = "11"
b = "1"
ans = addBinary(a, b)
print(ans)
