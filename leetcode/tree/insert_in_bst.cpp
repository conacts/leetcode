// not totally efficient, stack is most efficinet
TreeNode* insertIntoBST(TreeNode* root, int val) {
	if (!root)
	{
		TreeNode* newNode = new TreeNode(val);
		return newNode;
	}
	if (root->val < val)
		root->right = insertIntoBST(root->right, val);
	else
		root->left = insertIntoBST(root->left, val);
	return root;
}
