TreeNode* invertTree(TreeNode* root) {
	if (root) {
		auto r = invertTree(root->right);
		auto l = invertTree(root->left);
		root->right = l;
		root->left = r;
	}
	return root;
}
