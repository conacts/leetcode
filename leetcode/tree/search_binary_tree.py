def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    elif root.val == val:
        return root
    else:
        return self.searchBST(root.right, val) or self.searchBST(root.left, val)

# Faster
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val > val:
        return self.searchBST(root.left, val)
    elif root.val < val:
        return self.searchBST(root.right, val)
    else:
        return root
