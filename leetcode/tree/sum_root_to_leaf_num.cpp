int sumNumbers(TreeNode* root) {
	if (!root)
		return 0;
	else if (root->right == NULL && root->left == NULL)
		return root->val;
	if (root->left)
		root->left->val = 10 * root->val + root->left->val;
	if (root->right)
		root->right->val = 10 * root->val + root->right->val;
	return sumNumbers(root->right) + sumNumbers(root->left);
}
