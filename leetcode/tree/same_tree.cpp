bool isSameTree(TreeNode* p, TreeNode* q) {
	if (p == NULL || q == NULL) {
		return p == q;
	}
	bool r = isSameTree(p->right, q->right);
	bool l = isSameTree(p->left, q->left);
	return r && l && p->val == q->val;
}
