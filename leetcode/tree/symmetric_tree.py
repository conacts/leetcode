def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return self.f(root.left, root.right)

def f(self, l, r):
    if not l or not r:
        return l == r
    else:
        return l.val == r.val and self.f(l.right, r.left) and self.f(l.left, r.right)
