def bstToGst(self, root: TreeNode) -> TreeNode:
    # record an ongoing sum to update values accordingly
    self.sum = 0
    self.toGst(root)
    return root
    
def toGst(self, root):
    # null values requested
    if not root:
        return None
    # smallest numbers on right, therefore this must always go before left & sum
    self.toGst(root.right)
    self.sum += root.val
    root.val = self.sum
    self.toGst(root.left)
    # no need to return since we are modifying the tree
    
