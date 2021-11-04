def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    return self.dfs(root, False)

def dfs(self, node, left_side):
    if not node:
        return 0
    elif not node.left and not node.right:
        if left_side:
            return node.val
        else:
            return 0
    else:
        return self.dfs(node.left, True) + self.dfs(node.right, False)
