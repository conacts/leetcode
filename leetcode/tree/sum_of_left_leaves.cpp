int sumOfLeftLeaves(TreeNode* root) {
	return f(root, false);
}
int f(TreeNode* root, bool is_true) {
	if (!root)
		return 0;
	else if (!root->right && !root->left) {
		if (is_true) 
			return root->val;
		else
			return 0;
	}
	else
		return f(root->right, false) + f(root->left, true);
}
