def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words = set(words)
    ans = []
    memo = {}

    def isTrue(word):
        if word in memo:
            return memo[word]

        for i in range(1, len(word)):
            if word[:i] not in words:
                continue
            right = word[i:]
            if right in words or isTrue(right):
                memo[word] = True
                return True
        memo[word] = False
        return False

    for word in words:
        if isTrue(word):
            ans.append(word)
    return ans


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
