# NEEDS TO BE OPTIMIZED
def lengthOfLIS(self, nums: List[int]) -> int:
    l = [1] * len(nums)
    for i in range(len(nums)):
        sub = []
        for j in range(i):
            if nums[j] < nums[i]:
                sub.append(l[j])
        l[i] = 1 + max(sub, default=0)
    return max(l, default = 0)
