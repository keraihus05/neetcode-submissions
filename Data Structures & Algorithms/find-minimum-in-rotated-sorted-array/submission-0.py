class Solution:
    def findMin(self, nums: List[int]) -> int:
        numbers = set(nums)
        return min(numbers)