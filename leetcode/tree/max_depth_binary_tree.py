def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    else:
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if r > l:
            return 1 + r
        else:
            return 1 + l
