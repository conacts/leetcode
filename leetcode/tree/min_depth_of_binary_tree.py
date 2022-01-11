def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    r = self.minDepth(root.right)
    l = self.minDepth(root.left)
    
    if not root.right or not root.left:
        return 1 + max(r, l)
    
    return 1 + min(r, l)
