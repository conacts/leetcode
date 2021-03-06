def twoSum(self, numbers: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(numbers)):
        t = target - numbers[i]
        if t in d:
            return [1 + d[t], 1 + i]
        d[numbers[i]] = i

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    while l != r:
        t = numbers[r] + numbers[l]
        if t == target:
            return [l+1, r+1]
        elif t > target:
            r -= 1
        elif t < target: 
            l += 1
