# Recursive
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


# Optimal
def sumNumbers(self, root) -> int:
    self.total = 0

    def dfs(node, num):
        num = num * 10 + node.val
        if not (node.left or node.right):
            self.total += num
            return
        
        if node.left:
            dfs(node.left, num)
        if node.right:
            dfs(node.right, num)

    dfs(root, 0)
    return self.total
