def missingNumber(self, nums: List[int]) -> int:
    solution = 0
    for i in range(len(nums)):
        solution ^= i+1
        solution ^= nums[i]
    return solution

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
