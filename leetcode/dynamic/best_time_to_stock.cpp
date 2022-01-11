int maxProfit(vector<int>& prices) {
	int minPrice = prices[0];
	int maxProfit = 0;
	
	for (int p : prices) {
		if (p < minPrice) {
			minPrice = p;
		} else if (p - minPrice > maxProfit) {
			maxProfit = p - minPrice;
		}
	}
	return maxProfit;
}
