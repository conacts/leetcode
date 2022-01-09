vector<int> twoSum(vector<int>& nums, int target) {
	vector<int> res;
	int i = 0; 
	int j = nums.size()-1;
	int sum = 0;
	while(i < j) {
		sum = nums[i] + nums[j];
		if (sum == target) {
			return {i+1,j+1};
		}
		if(sum > target) {
			j--;
		}
		else {
			i++;
		}
	}
	// empty vector
	return {};
}
