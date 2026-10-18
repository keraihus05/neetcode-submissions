class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_height = min(height[l], height[r])
        vol = 0
        while l<r:
            if height[l]<=height[r]:
                max_height = max(max_height, height[l])
                vol += max_height - height[l]
                l += 1
            else:
                max_height = max(max_height, height[r])
                vol += max_height - height[r]
                r -= 1
            


        return vol
