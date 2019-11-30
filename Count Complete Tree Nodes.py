def countNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    def count(node, left):
        h = 0
        while node:
            h += 1
            if left:
                node = node.left
            else:
                node = node.right
        return h

    # Check left most height and right most height
    lh = count(root, True)
    rh = count(root, False)

    # if same, then all levels are complete
    if lh == rh:
        return (1 << lh) - 1
    # else recurse on left child and right child
    else:
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
