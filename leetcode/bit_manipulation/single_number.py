def singleNumber(self, nums: List[int]) -> int:
    solution = 0
    for num in nums:
        # operation for XOR in python
        solution ^= num
    return solution
