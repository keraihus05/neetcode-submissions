class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        num_hash = {}
        longest = 0
        for num in nums:
            num_set.add(num)

        for num in num_set:
            if num-1 not in num_set:
                num_hash[num] = 0

        for num in num_hash:
            i = 0
            while True:
                if num+i in num_set:
                    num_hash[num] += 1
                    i+=1
                else:
                    break
            if num_hash[num] > longest:
                longest = num_hash[num]
        return longest
            
        
        



                
            
                
        
            
            