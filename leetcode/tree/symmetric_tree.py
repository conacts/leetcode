def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return self.lol(root.right, root.left)

def lol(self, r, l):
    if not r and not l:
        return True
    elif not r or not l:
        return False
    else:
        return r.val == l.val and self.lol(r.right, l.left) and self.lol(l.right, r.left)
