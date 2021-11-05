def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    if not root.right and not root.left:
        return [root.val]
    else:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
