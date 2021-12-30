def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        root.left = r
        root.right = l
        return root
