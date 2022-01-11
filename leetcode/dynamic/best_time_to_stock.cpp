int maxProfit(vector<int>& prices) {
	int maxp = 0;
	int minp = prices[0];
	for (int i : prices) {
		if (i < minp) {
			minp = i;
		} else if (maxp < i - minp) {
			maxp = i - minp;
		}
	}
	return maxp;
}
