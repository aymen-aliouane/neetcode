class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(numbers, start=1):
            search = target - val
            if search in d:
                return [d[search], i]
            d[val] = i
