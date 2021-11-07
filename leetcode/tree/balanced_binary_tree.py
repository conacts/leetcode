def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self.f(root) != -1

def f(self, root):
    if not root:
        return 0
    
    l = self.f(root.left)
    r = self.f(root.right)
    
    if l == -1 or r == -1:
        return -1
    if abs(l - r) > 1:
        return -1
    return 1 + max(l, r)
