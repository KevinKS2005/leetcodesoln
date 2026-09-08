class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            a = target - n
            if a in seen:
                return [seen[a], i]
            seen[n] = i