bool isSymmetric(TreeNode* root) {
	if (f(root->left, root->right))
		return true;
	else
		return false;
}
bool f(TreeNode* l, TreeNode* r) {
	if (!r || !l) 
		return l == r;
	else {
		return r->val == l->val && f(l->left, r->right) && f(l->right, r->left);
	}
}
