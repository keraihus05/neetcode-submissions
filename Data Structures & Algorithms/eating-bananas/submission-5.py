from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = max(piles)
        while low <= high:
            mid = (high + low)//2
            k = mid
            if sum(ceil(pile / k)for pile in piles) <= h:
                high = mid - 1
                ans = min(k, ans)
            else:
                low = mid + 1
        return ans






        
        