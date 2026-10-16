class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        zeros = {0:0}
        prod = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zeros[0] += 1
        if zeros[0] > 1:
            for i in range(len(nums)):
                ans.append(0)
            return ans
        elif zeros[0] == 1:    
            for i in range(len(nums)):
                if nums[i]==0:
                    ans.append(prod)
                else:
                    ans.append(0)
            return ans
        else:
            for i in range(len(nums)):
                product = int(prod / nums[i])
                ans.append(product)
            return ans

        # if product = 0, locate location of 0 and compute the product. if more than 1 0, all of the answers will be zero, could use a hashmap to locate zeros