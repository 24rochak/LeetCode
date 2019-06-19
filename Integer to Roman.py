def intToRoman(self, num: int) -> str:
    roman = ""
    m = int(num / 1000)
    roman += "M" * m
    num -= 1000 * m

    if num >= 900:
        roman += "CM"
        num -= 900
    elif 900 > num >= 500:
        roman += "D"
        num -= 500
    elif num >= 400:
        roman += "CD"
        num -= 400

    c = int(num / 100)
    roman += "C" * c
    num -= 100 * c

    if num >= 90:
        roman += "XC"
        num -= 90
    elif 90 > num >= 50:
        roman += "L"
        num -= 50
    elif num >= 40:
        roman += "XL"
        num -= 40

    x = int(num / 10)
    roman += "X" * x
    num -= 10 * x

    if num >= 9:
        roman += "IX"
        num -= 9
    elif 9 > num >= 5:
        roman += "V"
        num -= 5
    elif num >= 4:
        roman += "IV"
        num -= 4

    i = int(num / 1)
    roman += "I" * i
    num -= 1 * i

    return roman
