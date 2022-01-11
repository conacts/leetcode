int lengthOfLIS(vector<int>& nums) {
	vector <int> sub = {nums[0]};
	for (int num : nums) {
		if (num > sub[sub.size()-1]) {
			sub.push_back(num);
		} else {
			int i = 0;
			while (sub[i] < num) {
				i += 1;
			}
			sub[i] = num;
		}
	}
	return sub.size();
}
