def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    worddic = set(wordList)
    alphabeta = "abcdefghijklmnopqrstuvwxyz"
    if endWord not in worddic:
        return 0

    count = 1
    forward = {beginWord}
    backward = {endWord}
    while forward and backward:
        count += 1
        next = set()

        if len(forward) > len(backward):
            forward, backward = backward, forward

        for word in forward:
            for i in range(len(word)):
                first = word[:i]
                last = word[i + 1:]
                for c in alphabeta:
                    new_word = first + c + last
                    if new_word in backward:
                        return count

                    if new_word in worddic:
                        next.add(new_word)
                        worddic.remove(new_word)

        forward = next

    return 0


beginWord = "leet"
endWord = "code"
wordList = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
print(ladderLength(beginWord, endWord, wordList))
