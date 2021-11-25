# easier solution ---> 998 ms
def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)


# Optimal solution 616 ms
def maxSubArray(self, nums: List[int]) -> int:
    add = 0
    result = nums[0]
    for i in nums:
        add += i
        if add > result:
            result = add
        if add < 0:
            add = 0
    return result


