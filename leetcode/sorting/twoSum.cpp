//#include <vector>
//using hashmap
vector<int> twoSum(vector<int>& nums, int target) {
	map <int, int> d;
	vector <int> ans;
	for (int i = 0; i < nums.size(); i++) {
		int look = target - nums[i];
		if (d.count(look)) {
			ans.push_back(d.find(look)->second);
			ans.push_back(i);
		}
	d.insert(pair<int, int>(nums[i], i));
	}
	return ans;
}
