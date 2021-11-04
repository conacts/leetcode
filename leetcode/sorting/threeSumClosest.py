def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    closest = sum(nums[:3])
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            ans = nums[i] + nums[l] + nums[r]
            if ans == target:
                return ans
            if abs(ans - target) < abs(closest - target):
                closest = ans
            if ans < target:
                l += 1
            elif ans > target:
                r -= 1
    return closest
