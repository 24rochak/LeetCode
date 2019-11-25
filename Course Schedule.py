def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses

    for course, pre in prerequisites:
        graph[course].append(pre)

    def dfs(i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True

        visited[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visited[i] = 1
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


numCourses = 2
prerequisites = [[1, 0]]
# 0 is a prerequisite of 1
print(canFinish(numCourses, prerequisites))
