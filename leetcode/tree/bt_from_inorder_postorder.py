# Optimal Solution
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    d = {}
    for i in range(len(inorder)):
        d[inorder[i]] = i
        
    def build(low, high):
        if low > high:
            return None
        root = TreeNode(postorder.pop())
        mid = d[root.val]
        # Strange occurance where if root.left is before root.right it doesn't run 
        # it is because you pop() postorder
        root.right = build(mid+1, high)
        root.left = build(low, mid-1)
        return root
    
    return build(0, len(inorder)-1)


# Not Optimal Solution
def buildTree(self, inorder, postorder):
    if not inorder or not postorder:
        return None

    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val) # Line A

    root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
    root.left = self.buildTree(inorder[:inorderIndex], postorder) 

    return root
