def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    elif not root.left and not root.right:
        return [root.val]
    elif not root.left and root.right:
        return [root.val] + self.inorderTraversal(root.right)
    elif not root.right and root.left:
        return self.inorderTraversal(root.left) + [root.val]
    else:
        l = self.inorderTraversal(root.left)
        r = self.inorderTraversal(root.right)
        return l + [root.val] + r
