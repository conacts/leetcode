def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        look = target - nums[i]
        if look in d:
            return [i, d[look]]
        d[nums[i]] = i
