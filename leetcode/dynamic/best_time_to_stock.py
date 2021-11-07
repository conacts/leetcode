def maxProfit(self, prices: List[int]) -> int:
    # Kadane's Algorithm
    # Same problem as Max Subarray
    maxPrice = 0
    minPrice = prices[0]
    for i in prices:
        if i < minPrice:
            minPrice = i
        elif i - minPrice > maxPrice:
            maxPrice = i - minPrice
    return maxPrice
