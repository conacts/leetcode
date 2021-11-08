def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    d = {}
    for i in range(len(inorder)):
        d[inorder[i]] = i
        
    def build(low, high):
        if low > high:
            return None
        root = TreeNode(postorder.pop())
        mid = d[root.val]
        root.right = build(mid+1, high)
        root.left = build(low, mid-1)
        return root
    
    return f(0, len(inorder)-1)
