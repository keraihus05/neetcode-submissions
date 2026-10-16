class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)
        sorted_items = sorted(num_freq.items(), key = lambda item: item[1], reverse = True )
        sorted_list = {key: value for key, value in sorted_items}
        k_freq = list(sorted_list.keys())[:k]
        return k_freq