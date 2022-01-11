bool isBalanced(TreeNode* root) {
	return f(root) != -1;
}

int f(TreeNode* root) {
	if (!root)
		return 0;
	int r = f(root->right);
	int l = f(root->left);
	
	if (r == -1 || l == -1) 
		return -1;
	if (abs(r - l) > 1)
		return -1;
	return max(r, l) + 1;
}
