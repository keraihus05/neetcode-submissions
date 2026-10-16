class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        def get_chars(word):
            s = {}
            for ch in word:
                s[ch] = s.get(ch,0) + 1
            return tuple(sorted(s.items()))

        for word in strs:
            key = get_chars(word)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        
        return list(groups.values())
        

        