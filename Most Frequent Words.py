def func(text, banned):
    if not text:
        return []

    banned = set(banned)
    for c in "!?',;.":
        text = text.replace(c, " ")

    final = []
    words = {}
    for word in text.lower().split():
        if word not in words and word not in banned:
            words[word] = 1
        else:
            words[word] += 1
    if not words:
        return []
    maxval = max(words.values())
    for word in words:
        if words[word] == maxval:
            final.append(word)

    return final


text = ""
banned = []
print(func(text, banned))
