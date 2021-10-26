def twoSum(self, numbers: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(numbers)):
        t = target - numbers[i]
        if t in d:
            return [1 + d[t], 1 + i]
        d[numbers[i]] = i
