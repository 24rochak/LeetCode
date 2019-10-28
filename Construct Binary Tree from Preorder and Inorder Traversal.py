class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    def dfs(prestart, instart, inend, preorder, inorder):
        if prestart > len(preorder) - 1 or instart > inend:
            return None
        root = TreeNode(preorder[prestart])
        loc = locs[root.val]
        root.left = dfs(prestart + 1, instart, loc - 1, preorder, inorder)
        root.right = dfs(prestart + loc - instart + 1, loc + 1, inend, preorder, inorder)
        return root

    locs = {val: loc for loc, val in enumerate(inorder)}
    root = dfs(0, 0, len(inorder) - 1, preorder, inorder)
    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
