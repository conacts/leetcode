# NEEDS TO BE OPTIMIZED >> 2600ms
def lengthOfLIS(self, nums: List[int]) -> int:
    l = [1] * len(nums)
    for i in range(len(nums)):
        sub = []
        for j in range(i):
            if nums[j] < nums[i]:
                sub.append(l[j])
        l[i] = 1 + max(sub, default=0)
    return max(l, default = 0)

# Optimized >> 96ms >> better than 80%
def lengthOfLIS(self, nums: List[int]) -> int:
    sub = [nums[0]]
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            i = 0
            while num > sub[i]:
                i += 1
            sub[i] = num
    return len(sub)
