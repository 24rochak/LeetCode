def func(points, k):
    group = {point: i for i, point in enumerate(points)}

    for i in range(len(points) - 1):
        for j in range(1, len(points)):
            if group[points[i]] != group[points[j]]:
                d = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                if d < k:
                    group[points[j]] = group[points[i]]

    groups2 = {k: [] for k in group.values()}
    for item in group:
        groups2[group[item]].append(item)

    for item in groups2:
        print("{}:{}".format(item, groups2[item]))


grid = [(i, j) for j in range(0, 100, 2) for i in range(0, 100, 3)]
size = 4
func(grid, size)
