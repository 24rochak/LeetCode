def firstBadVersion(n, target):
    left = 1
    right = n
    cost = []
    while (left < right):
        mid = left + int(0.7 * (right - left + 1)) - 1
        '''print("left: ",left)
        print("right: ",right)
        print("mid: ",mid)
        print("\n\n")'''
        if mid == target:
            return cost
        elif target < mid:
            cost.append(mid)
            right = mid - 1
        else:
            cost.append(mid)
            left = mid + 1
    # cost.append(left)
    return cost


'''for j in range(100,1,-1):
    max = 0
    id = j
    n = j
    for i in range(n,0,-1):
        ans = firstBadVersion(n,i)
        if ans > max:
            #print(ans)
            max = ans
            id = i
        #print("i:"+str(i)+"cost"+str(max)+" id: "+str(id))
    print("J :"+str(j)+"\tCost :"+str(max)+"\tid :"+str(id))

'''
n = 100
max = 0
for i in range(n, 0, -1):
    ans = firstBadVersion(n, i)
    print(i, ans, sum(ans))
    '''if ans > max:
        max = ans
        id = i
    print("i:"+str(i)+"cost"+str(max)+" id: "+str(id))'''
