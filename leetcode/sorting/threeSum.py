def threeSum(self, nums: List[int]) -> List[List[int]]:
    returnlist = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums)-1
        while l < r:
            ans = nums[i] + nums[l] + nums[r]
            if ans > 0:
                r -= 1
            elif ans < 0:
                l += 1
            else:
                returnlist.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return returnlist
