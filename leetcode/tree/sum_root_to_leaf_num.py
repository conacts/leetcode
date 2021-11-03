def sumNumbers(self, root) -> int:
    if not root:
        return 0
    elif not root.right and not root.left:
        return root.val
    if root.left: 
        root.left.val = 10 * root.val + root.left.val
    if root.right:
        root.right.val = 10 * root.val + root.right.val
    
    return self.sumNumbers(root.left) + self.sumNumbers(root.right)
