class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        ans = nums[0]

        while low <= high:
            mid = (low + high)//2
            if nums[mid] < nums[high]:
                high = mid - 1
                ans = min(ans, nums[mid])
            else:
                low = mid + 1
                ans = min(ans, nums[mid])
        return ans   