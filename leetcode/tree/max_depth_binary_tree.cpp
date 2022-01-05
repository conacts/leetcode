int maxDepth(TreeNode* root) {
	if (root == NULL) {
		return 0;
	}
	int r = maxDepth(root->right);
	int l = maxDepth(root->left);
	return 1 + max(r, l);
}
