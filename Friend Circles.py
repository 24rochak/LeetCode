def findCircleNum(M) -> int:
    '''Using SCC => slow
    def dfs(i):
        visited[i] = True
        for j in range(len(M[i])):
            if M[i][j] and not visited[j]:
                dfs(j)
        topo.append(i)

    topo = []
    visited = [False] * len(M)
    for i in range(len(M)):
        if not visited[i]:
            dfs(i)

    for i in range(len(M)):
        for j in range(0, i):
            M[i][j], M[j][i] = M[j][i], M[i][j]

    ans = 0
    visited = [False] * len(M)
    for i in topo:
        if not visited[i]:
            dfs(i)
            ans += 1
    return ans'''

    # Using plain DFS => Fast
    seen = set()

    def dfs(node):
        for adj, direct in enumerate(M[node]):
            if direct and adj not in seen:
                seen.add(adj)
                dfs(adj)

    ans = 0
    for i in range(len(M)):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)

    return ans


M = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]

print(findCircleNum(M))
