def romanToInt(str: str) -> int:
    num = 0
    i = 0
    while (i != len(str)):
        if str[i] == "I":
            if i + 1 < len(str) and str[i + 1] == "V":
                num += 4
                i += 2
            elif i + 1 < len(str) and str[i + 1] == "X":
                num += 9
                i += 2
            else:
                num += 1
                i += 1

        elif str[i] == "X":
            if i + 1 < len(str) and str[i + 1] == "L":
                num += 40
                i += 2
            elif i + 1 < len(str) and str[i + 1] == "C":
                num += 90
                i += 2
            else:
                num += 10
                i += 1

        elif str[i] == "C":
            if i + 1 < len(str) and str[i + 1] == "D":
                num += 400
                i += 2
            elif i + 1 < len(str) and str[i + 1] == "M":
                num += 900
                i += 2
            else:
                num += 100
                i += 1
        elif str[i] == "V":
            num += 5
            i += 1
        elif str[i] == "L":
            num += 50
            i += 1
        elif str[i] == "D":
            num += 500
            i += 1
        elif str[i] == "M":
            num += 1000
            i += 1
        print("Num : ", num, "i : ", i)
    return num


print(romanToInt("MCMXCIV"))
