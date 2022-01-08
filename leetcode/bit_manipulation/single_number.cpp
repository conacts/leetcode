int singleNumber(vector<int>& nums) {
	int start = 0;
	for (int i = 0; i < nums.size(); i++) {
		start ^= nums[i];
	}
	return start;
}
