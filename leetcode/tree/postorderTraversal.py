def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []        
    if not root.left and not root.right:
        return [root.val]
    else:
        l = self.postorderTraversal(root.left)
        r = self.postorderTraversal(root.right)
        return l + r + [root.val]
