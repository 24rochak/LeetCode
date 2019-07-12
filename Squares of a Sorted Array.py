'''def sortedSquares(A):

    if len(A)==0:
        return []
    min = -10001
    max =  10001
    l = 0
    r = len(A)-1
    for i in range(len(A)):
        if A[i] >= min and A[i] < 0:
            min = A[i]
            l = i
        if A[i] < max and A[i] > 0:
            max = A[i]
            r = i

    ans = [0]*(r-l-1)
    print(l,r)
    while l>=0 and r<len(A):
        if abs(A[l])<abs(A[r]):
            ans.append(A[l]*A[l])
            l-=1
        elif abs(A[l])>abs(A[r]):
            ans.append(A[r] * A[r])
            r += 1
        elif A[l]== A[r]:
            ans.append(A[l] * A[l])
            l -= 1
            r += 1
        else:
            ans.append(A[l] * A[l])
            l -= 1
            ans.append(A[r] * A[r])
            r += 1
    while l>=0:
        ans.append(A[l] * A[l])
        l -= 1

    while r<len(A):
        ans.append(A[r] * A[r])
        r += 1

    return ans'''


def sortedSquares(A):
    ans = [item * item for item in A]
    ans.sort()
    return ans


# A = [2,4,5,7,8,9]
# A = [-9,-8,-5,-4,-1]
# A = [-4,-1,0,3,10]
# A = [-7,-3,2,3,11]
A = [-5, -1, -1, 1, 1, 5]
ans = sortedSquares(A)
print(ans)
