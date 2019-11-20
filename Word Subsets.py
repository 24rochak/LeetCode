def wordSubsets(A, B):
    """
    :type A: List[str]
    :type B: List[str]
    :rtype: List[str]
    """
    '''b = [0] * 26
    for i in range(len(B)):
        t1 = [0]*26
        for j in B[i]:
            t1[ord(j) - ord('a')] += 1

        for i in range(len(t1)):
            b[i] = max(b[i],t1[i])


    ans = set()
    for a in A:
        t1 = [0] * 26
        for i in a:
            t1[ord(i) - ord('a')] += 1

        t1 = [t1[i]-b[i] for i in range(len(t1))]

        if min(t1)>=0:
            ans.add(a)
    return list(ans)'''

    b = {}
    for word in set(B):
        temp = {}
        for char in word:
            if char not in temp:
                temp[char] = 1
            else:
                temp[char] += 1

        for char, count in temp.items():
            if char in b:
                b[char] = max(count, b[char])
            else:
                b[char] = count
    ans = []
    for word in A:
        flag = True
        for char, count in b.items():
            if word.count(char) < count:
                flag = False
                break
        if flag:
            ans.append(word)
    return ans


A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["ec", "oo", "ceo"]
print(wordSubsets(A, B))
