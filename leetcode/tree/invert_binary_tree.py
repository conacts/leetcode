def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    elif not root.left and not root.right:
        return root
    else:
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left = r
        root.right = l
        return root
        
