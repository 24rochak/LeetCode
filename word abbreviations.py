def findAbbreviations(word):
    abbreviations = []
    for i in range(1, len(word) + 1):
        for j in range(0, len(word) - i + 1):
            abbreviations.append(word[:j] + str(i) + word[j + i:])
    return abbreviations


ans = findAbbreviations("word")
print(ans)
